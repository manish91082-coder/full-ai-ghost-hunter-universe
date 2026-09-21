"""Generic read-only V2-style factory pair enumeration.

The enumerator contains interface selectors only. Runtime factory addresses,
networks and provider endpoints are supplied externally. It never submits
transactions and never treats discovery as execution authorization.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .registry import RegistryError
from .rpc_transport import RpcObservation, RpcTransport
from .runtime_freshness import parse_hex_block, validate_block_numbers, FreshnessPolicy


ALL_PAIRS_LENGTH_SELECTOR = "0x574f2ba3"
ALL_PAIRS_SELECTOR = "0x1e3dd18b"
GET_RESERVES_SELECTOR = "0x0902f1ac"
TOKEN0_SELECTOR = "0x0dfe1681"
TOKEN1_SELECTOR = "0xd21220a7"


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


def _word(value: str) -> str:
    if not isinstance(value, str) or not value.startswith("0x"):
        raise RegistryError("RPC hex result required")
    raw = value[2:]
    if len(raw) % 64 != 0 or not raw:
        raise RegistryError("invalid ABI word encoding")
    return raw


def _uint(value: str) -> int:
    raw = _word(value)
    return int(raw[-64:], 16)


def _address(value: str) -> str:
    raw = _word(value)
    return "0x" + raw[-40:]


def _index_calldata(selector: str, index: int) -> str:
    if index < 0:
        raise RegistryError("pair index cannot be negative")
    return selector + format(index, "064x")


class V2PairEnumerator:
    def __init__(self, transport: RpcTransport, freshness: FreshnessPolicy) -> None:
        self.transport = transport
        self.freshness = freshness

    def pair_count(self, network_id: str, factory: str) -> RpcObservation:
        if not factory.startswith("0x") or len(factory) != 42:
            raise RegistryError("invalid factory address")
        return self.transport.call(
            network_id, "eth_call",
            [{"to": factory, "data": ALL_PAIRS_LENGTH_SELECTOR}, "latest"],
        )

    def enumerate_pairs(self, network_id: str, factory: str,
                        *, max_pairs: int) -> list[PairDiscovery]:
        if max_pairs < 0:
            raise RegistryError("max_pairs must be non-negative")
        count_obs = self.pair_count(network_id, factory)
        count = _uint(count_obs.result)
        if count > max_pairs:
            raise RegistryError("pair universe exceeds configured safety bound")
        result: list[PairDiscovery] = []
        for i in range(count):
            obs = self.transport.call(
                network_id, "eth_call",
                [{"to": factory, "data": _index_calldata(ALL_PAIRS_SELECTOR, i)}, "latest"],
            )
            result.append(PairDiscovery(
                network_id, factory, i, _address(obs.result),
                obs.provider_id, count_obs.result if False else 0,
            ))
        return result

    def read_pair_state(self, network_id: str, pair: str) -> PairState:
        if not pair.startswith("0x") or len(pair) != 42:
            raise RegistryError("invalid pair address")
        t0 = self.transport.call(network_id, "eth_call",
            [{"to": pair, "data": TOKEN0_SELECTOR}, "latest"])
        t1 = self.transport.call(network_id, "eth_call",
            [{"to": pair, "data": TOKEN1_SELECTOR}, "latest"])
        reserves = self.transport.call(network_id, "eth_call",
            [{"to": pair, "data": GET_RESERVES_SELECTOR}, "latest"])
        words = _word(reserves.result)
        if len(words) < 128:
            raise RegistryError("invalid getReserves ABI result")
        reserve0 = int(words[0:64], 16)
        reserve1 = int(words[64:128], 16)
        block = parse_hex_block(reserves.result[130:]) if False else None
        if not isinstance(block, int):
            raise RegistryError("live block metadata required for pair state")
        validate_block_numbers(block, block, self.freshness)
        return PairState(pair, _address(t0.result), _address(t1.result),
                         reserve0, reserve1, block, reserves.provider_id)
