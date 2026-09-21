"""Generic read-only V2-style factory pair enumeration.

This boundary is observation-only. Runtime factory/network/provider data must
arrive from external configuration. No transaction construction, signing, or
submission is performed here.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass

from .registry import RegistryError
from .rpc_transport import RpcObservation, RpcTransport
from .runtime_freshness import FreshnessPolicy, parse_hex_block, validate_block_numbers

ALL_PAIRS_LENGTH_SELECTOR = "0x574f2ba3"
ALL_PAIRS_SELECTOR = "0x1e3dd18b"
GET_RESERVES_SELECTOR = "0x0902f1ac"
TOKEN0_SELECTOR = "0x0dfe1681"
TOKEN1_SELECTOR = "0xd21220a7"
GET_CODE_METHOD = "eth_getCode"
BLOCK_METHOD = "eth_blockNumber"
CALL_METHOD = "eth_call"

@dataclass(frozen=True)
class PairDiscovery:
    network_id: str
    factory: str
    pair_index: int
    pair_address: str
    provider_id: str
    observed_block: int

@dataclass(frozen=True)
class PairState:
    pair_address: str
    token0: str
    token1: str
    reserve0: int
    reserve1: int
    observed_block: int
    provider_id: str
    bytecode_sha256: str

@dataclass(frozen=True)
class EnumerationCompleteness:
    network_id: str
    factory: str
    factory_reported_count: int
    enumerated_count: int
    start_block: int
    end_block: int
    provider_id: str

def _word(value: str) -> str:
    if not isinstance(value, str) or not value.startswith("0x"):
        raise RegistryError("RPC hex result required")
    raw = value[2:]
    if not raw or len(raw) % 64:
        raise RegistryError("invalid ABI word encoding")
    return raw

def _uint(value: str) -> int:
    return int(_word(value)[-64:], 16)

def _address(value: str) -> str:
    raw = _word(value)
    return "0x" + raw[-40:]

def _index_calldata(selector: str, index: int) -> str:
    if index < 0:
        raise RegistryError("pair index cannot be negative")
    return selector + format(index, "064x")

def _bytecode_sha256(value: str) -> str:
    if not isinstance(value, str) or not value.startswith("0x"):
        raise RegistryError("RPC bytecode hex result required")
    raw = value[2:]
    if len(raw) % 2:
        raise RegistryError("invalid bytecode hex encoding")
    if not raw:
        raise RegistryError("pair address has no runtime bytecode")
    try:
        payload = bytes.fromhex(raw)
    except ValueError as exc:
        raise RegistryError("invalid bytecode hex encoding") from exc
    return hashlib.sha256(payload).hexdigest()

class V2PairEnumerator:
    def __init__(self, transport: RpcTransport, freshness: FreshnessPolicy) -> None:
        self.transport = transport
        self.freshness = freshness
        self._last_completeness: EnumerationCompleteness | None = None

    @property
    def last_completeness(self) -> EnumerationCompleteness | None:
        return self._last_completeness

    def pair_count(self, network_id: str, factory: str, *, block_tag: str = "latest") -> RpcObservation:
        if not factory.startswith("0x") or len(factory) != 42:
            raise RegistryError("invalid factory address")
        return self.transport.call(
            network_id, CALL_METHOD,
            [{"to": factory, "data": ALL_PAIRS_LENGTH_SELECTOR}, block_tag],
        )

    def enumerate_pairs(self, network_id: str, factory: str, *, max_pairs: int) -> list[PairDiscovery]:
        if max_pairs < 0:
            raise RegistryError("max_pairs must be non-negative")
        start = self.transport.call(network_id, BLOCK_METHOD)
        start_block = parse_hex_block(start.result)
        block_tag = "0x" + format(start_block, "x")
        count_obs = self.transport.call(
            network_id, CALL_METHOD,
            [{"to": factory, "data": ALL_PAIRS_LENGTH_SELECTOR}, block_tag],
        )
        count = _uint(count_obs.result)
        if count > max_pairs:
            raise RegistryError("pair universe exceeds configured safety bound")
        if count_obs.provider_id != start.provider_id:
            raise RegistryError("provider changed during enumeration preflight")
        result: list[PairDiscovery] = []
        seen: set[str] = set()
        for i in range(count):
            obs = self.transport.call(
                network_id, CALL_METHOD,
                [{"to": factory, "data": _index_calldata(ALL_PAIRS_SELECTOR, i)}, block_tag],
            )
            if obs.provider_id != start.provider_id:
                raise RegistryError("provider changed during pair enumeration")
            pair_address = _address(obs.result)
            key = pair_address.lower()
            if key in seen:
                raise RegistryError("duplicate pair identity returned by factory")
            seen.add(key)
            result.append(PairDiscovery(
                network_id, factory, i, pair_address,
                obs.provider_id, start_block,
            ))

        end = self.transport.call(network_id, BLOCK_METHOD)
        if end.provider_id != start.provider_id:
            raise RegistryError("provider changed during enumeration postflight")
        end_block = parse_hex_block(end.result)
        if len(result) != count:
            raise RegistryError("pair enumeration count mismatch")
        validate_block_numbers(start_block, end_block, self.freshness)

        self._last_completeness = EnumerationCompleteness(
            network_id, factory, count, len(result),
            start_block, end_block, start.provider_id,
        )
        return result

    def read_pair_state(self, network_id: str, pair: str) -> PairState:
        if not pair.startswith("0x") or len(pair) != 42:
            raise RegistryError("invalid pair address")
        before = self.transport.call(network_id, BLOCK_METHOD)
        before_block = parse_hex_block(before.result)
        block_tag = "0x" + format(before_block, "x")
        code = self.transport.call(network_id, GET_CODE_METHOD, [pair, block_tag])
        t0 = self.transport.call(
            network_id, CALL_METHOD, [{"to": pair, "data": TOKEN0_SELECTOR}, block_tag]
        )
        t1 = self.transport.call(
            network_id, CALL_METHOD, [{"to": pair, "data": TOKEN1_SELECTOR}, block_tag]
        )
        reserves = self.transport.call(
            network_id, CALL_METHOD, [{"to": pair, "data": GET_RESERVES_SELECTOR}, block_tag]
        )
        after = self.transport.call(network_id, BLOCK_METHOD)

        observations = (code, t0, t1, reserves, after)
        if any(obs.provider_id != before.provider_id for obs in observations):
            raise RegistryError("provider changed during pair-state observation")

        after_block = parse_hex_block(after.result)
        if after_block < before_block:
            raise RegistryError("block number moved backwards")
        validate_block_numbers(before_block, after_block, self.freshness)

        words = _word(reserves.result)
        if len(words) < 128:
            raise RegistryError("invalid getReserves ABI result")

        return PairState(
            pair, _address(t0.result), _address(t1.result),
            int(words[:64], 16), int(words[64:128], 16),
            after_block, before.provider_id, _bytecode_sha256(code.result),
        )
