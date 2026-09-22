"""Read-only Silo V3 factory event enumeration boundary.

Enumerates NewSilo events from externally supplied factory configuration.
Event order is never treated as a SiloFactory ID. Runtime verification of
each discovered market is a separate downstream boundary.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .registry import RegistryError
from .rpc_transport import RpcTransport
from .runtime_freshness import FreshnessPolicy, parse_hex_block, validate_block_numbers

BLOCK_METHOD = "eth_blockNumber"
GET_LOGS_METHOD = "eth_getLogs"

@dataclass(frozen=True)
class SiloFactoryEvent:
    network_id: str
    factory: str
    implementation: str
    token0: str
    token1: str
    silo0: str
    silo1: str
    silo_config: str
    block_number: int
    transaction_hash: str
    log_index: int

@dataclass(frozen=True)
class SiloFactoryCompleteness:
    network_id: str
    factory: str
    start_block: int
    end_block: int
    post_scan_block: int
    event_count: int
    unique_market_count: int
    provider_id: str
    current_complete: bool

@dataclass(frozen=True)
class SiloFactoryObservation:
    events: tuple[SiloFactoryEvent, ...]
    completeness: SiloFactoryCompleteness

def _address_topic(value: Any) -> str:
    if not isinstance(value, str) or not value.startswith("0x") or len(value) != 66:
        raise RegistryError("invalid indexed address topic")
    return "0x" + value[-40:]

def _data_address(data: Any, index: int) -> str:
    if not isinstance(data, str) or not data.startswith("0x"):
        raise RegistryError("invalid event data")
    raw = data[2:]
    start = index * 64
    if len(raw) < start + 64:
        raise RegistryError("NewSilo event data is truncated")
    return "0x" + raw[start + 24:start + 64]

def _hex_int(value: Any, label: str) -> int:
    if not isinstance(value, str) or not value.startswith("0x"):
        raise RegistryError(label + " must be hexadecimal")
    try:
        return int(value, 16)
    except ValueError as exc:
        raise RegistryError(label + " invalid") from exc

def _valid_address(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("0x") and len(value) == 42

class SiloV3FactoryEnumerator:
    def __init__(
        self,
        transport: RpcTransport,
        freshness: FreshnessPolicy,
        *,
        event_topic0: str,
        chunk_size: int = 100_000,
        strict_current: bool = True,
    ) -> None:
        if not isinstance(event_topic0, str) or not event_topic0.startswith("0x") or len(event_topic0) != 66:
            raise RegistryError("NewSilo event topic0 is required")
        if chunk_size <= 0:
            raise RegistryError("chunk_size must be positive")
        self.transport = transport
        self.freshness = freshness
        self.event_topic0 = event_topic0.lower()
        self.chunk_size = chunk_size
        self.strict_current = strict_current
        self.last_observation: SiloFactoryObservation | None = None

    def enumerate(
        self,
        network_id: str,
        factory: str,
        *,
        from_block: int,
        to_block: int | None = None,
    ) -> SiloFactoryObservation:
        if not _valid_address(factory):
            raise RegistryError("invalid SiloFactory address")
        if from_block < 0:
            raise RegistryError("from_block cannot be negative")

        before = self.transport.call(network_id, BLOCK_METHOD)
        latest_before = parse_hex_block(before.result)
        end_block = latest_before if to_block is None else to_block
        if end_block < from_block:
            raise RegistryError("invalid block range")
        if end_block > latest_before:
            raise RegistryError("to_block is ahead of observed latest block")

        events: list[SiloFactoryEvent] = []
        cursor = from_block
        while cursor <= end_block:
            chunk_end = min(cursor + self.chunk_size - 1, end_block)
            obs = self.transport.call(
                network_id,
                GET_LOGS_METHOD,
                [{
                    "address": factory,
                    "fromBlock": "0x" + format(cursor, "x"),
                    "toBlock": "0x" + format(chunk_end, "x"),
                    "topics": [self.event_topic0],
                }],
            )
            if obs.provider_id != before.provider_id:
                raise RegistryError("provider changed during Silo factory enumeration")
            if not isinstance(obs.result, list):
                raise RegistryError("eth_getLogs must return a list")
            for raw in obs.result:
                events.append(self._parse_event(network_id, factory, raw))
            cursor = chunk_end + 1

        after = self.transport.call(network_id, BLOCK_METHOD)
        if after.provider_id != before.provider_id:
            raise RegistryError("provider changed during Silo factory enumeration")
        post_scan_block = parse_hex_block(after.result)
        validate_block_numbers(end_block, post_scan_block, self.freshness)

        identities: set[tuple[str, str, str]] = set()
        for event in events:
            identity = (event.silo_config.lower(), event.silo0.lower(), event.silo1.lower())
            if identity in identities:
                raise RegistryError("duplicate Silo market event identity")
            identities.add(identity)

        current_complete = post_scan_block == end_block
        if self.strict_current and not current_complete:
            raise RegistryError("snapshot advanced during strict-current enumeration")

        result = SiloFactoryObservation(
            events=tuple(events),
            completeness=SiloFactoryCompleteness(
                network_id=network_id,
                factory=factory,
                start_block=from_block,
                end_block=end_block,
                post_scan_block=post_scan_block,
                event_count=len(events),
                unique_market_count=len(identities),
                provider_id=before.provider_id,
                current_complete=current_complete,
            ),
        )
        self.last_observation = result
        return result

    def _parse_event(self, network_id: str, factory: str, raw: Any) -> SiloFactoryEvent:
        if not isinstance(raw, dict):
            raise RegistryError("invalid NewSilo log")
        topics = raw.get("topics")
        if not isinstance(topics, list) or len(topics) != 4:
            raise RegistryError("NewSilo must contain four topics")
        if str(topics[0]).lower() != self.event_topic0:
            raise RegistryError("unexpected NewSilo topic0")
        tx_hash = raw.get("transactionHash")
        if not isinstance(tx_hash, str) or not tx_hash.startswith("0x"):
            raise RegistryError("transaction hash required")
        return SiloFactoryEvent(
            network_id=network_id,
            factory=factory,
            implementation=_address_topic(topics[1]),
            token0=_address_topic(topics[2]),
            token1=_address_topic(topics[3]),
            silo0=_data_address(raw.get("data"), 0),
            silo1=_data_address(raw.get("data"), 1),
            silo_config=_data_address(raw.get("data"), 2),
            block_number=_hex_int(raw.get("blockNumber"), "log blockNumber"),
            transaction_hash=tx_hash,
            log_index=_hex_int(raw.get("logIndex"), "log index"),
        )
