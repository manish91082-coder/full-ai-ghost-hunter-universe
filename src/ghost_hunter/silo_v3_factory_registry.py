"""Canonical SiloFactory identity registry and explicit scan-plan boundary.

The registry is an evidence-backed identity denominator. It never invents
historical start blocks and never promotes a factory into execution authority.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Mapping

from .registry import RegistryError

EXPECTED_SCHEMA = "g02.silo.factory.registry.v1"
EXPECTED_EVENT_TOPIC0 = "0x3d6b896c73b628ec6ba0bdfe3cdee1356ea2af31af2a97bbd6b532ca6fa00acb"
EXPECTED_EVENT_SIGNATURE = (
    "NewSilo(address indexed implementation,address indexed token0,"
    "address indexed token1,address silo0,address silo1,address siloConfig)"
)

def _valid_address(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("0x") and len(value) == 42

def _valid_network_id(value: Any) -> bool:
    if not isinstance(value, str) or not value.startswith("eip155:"):
        return False
    try:
        return int(value.split(":", 1)[1]) >= 0
    except ValueError:
        return False

@dataclass(frozen=True)
class SiloFactoryRecord:
    id: str
    protocol: str
    network_name: str
    chain_id: int
    network_id: str
    factory: str
    source_order: int
    currentness_state: str
    historical_range_state: str
    runtime_observation_state: str
    market_denominator_state: str

@dataclass(frozen=True)
class SiloFactoryScanTarget:
    record_id: str
    network_id: str
    factory: str
    start_block: int
    event_topic0: str

@dataclass(frozen=True)
class SiloFactoryRegistry:
    schema_version: str
    source_url: str
    source_commit: str
    network_count: int
    factory_count: int
    event_signature: str
    event_topic0: str
    records: tuple[SiloFactoryRecord, ...]

    @classmethod
    def from_json(cls, path: str | Path) -> "SiloFactoryRegistry":
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        if payload.get("schema_version") != EXPECTED_SCHEMA:
            raise RegistryError("unsupported SiloFactory registry schema")
        if str(payload.get("event_topic0", "")).lower() != EXPECTED_EVENT_TOPIC0:
            raise RegistryError("unexpected NewSilo topic0")
        if payload.get("event_signature") != EXPECTED_EVENT_SIGNATURE:
            raise RegistryError("unexpected NewSilo signature")
        records_raw = payload.get("records")
        if not isinstance(records_raw, list):
            raise RegistryError("records must be a list")

        records = []
        ids = set()
        identities = set()
        network_orders = {}
        for raw in records_raw:
            if not isinstance(raw, dict):
                raise RegistryError("invalid factory record")
            record = SiloFactoryRecord(
                id=raw.get("id", ""),
                protocol=raw.get("protocol", ""),
                network_name=raw.get("network_name", ""),
                chain_id=raw.get("chain_id", -1),
                network_id=raw.get("network_id", ""),
                factory=raw.get("factory", ""),
                source_order=raw.get("source_order", 0),
                currentness_state=raw.get("currentness_state", ""),
                historical_range_state=raw.get("historical_range_state", ""),
                runtime_observation_state=raw.get("runtime_observation_state", ""),
                market_denominator_state=raw.get("market_denominator_state", ""),
            )
            if not record.id or record.id in ids:
                raise RegistryError("duplicate SiloFactory record id")
            if not _valid_address(record.factory):
                raise RegistryError("invalid SiloFactory address")
            if not _valid_network_id(record.network_id):
                raise RegistryError("invalid SiloFactory network identity")
            if record.chain_id != int(record.network_id.split(":", 1)[1]):
                raise RegistryError("chain_id/network_id mismatch")
            identity = (record.network_id, record.factory.lower())
            if identity in identities:
                raise RegistryError("duplicate network/factory identity")
            if record.source_order <= 0:
                raise RegistryError("source_order must be positive")
            ids.add(record.id)
            identities.add(identity)
            network_orders.setdefault(record.network_id, []).append(record.source_order)
            records.append(record)

        if payload.get("factory_count") != len(records):
            raise RegistryError("factory_count mismatch")
        if payload.get("network_count") != len(network_orders):
            raise RegistryError("network_count mismatch")
        for orders in network_orders.values():
            if sorted(orders) != list(range(1, len(orders) + 1)):
                raise RegistryError("source_order must be contiguous per network")

        return cls(
            schema_version=payload["schema_version"],
            source_url=payload["source_url"],
            source_commit=payload["source_commit"],
            network_count=payload["network_count"],
            factory_count=payload["factory_count"],
            event_signature=payload["event_signature"],
            event_topic0=payload["event_topic0"].lower(),
            records=tuple(records),
        )

    def build_scan_plan(self, start_blocks: Mapping[str, int]) -> tuple[SiloFactoryScanTarget, ...]:
        required = {record.id for record in self.records}
        supplied = set(start_blocks)
        missing = sorted(required - supplied)
        extra = sorted(supplied - required)
        if missing:
            raise RegistryError("missing explicit start blocks: " + ",".join(missing))
        if extra:
            raise RegistryError("unexpected start-block record ids: " + ",".join(extra))
        plan = []
        for record in self.records:
            start_block = start_blocks[record.id]
            if isinstance(start_block, bool) or not isinstance(start_block, int) or start_block < 0:
                raise RegistryError("invalid historical start block for " + record.id)
            plan.append(SiloFactoryScanTarget(
                record_id=record.id,
                network_id=record.network_id,
                factory=record.factory,
                start_block=start_block,
                event_topic0=self.event_topic0,
            ))
        return tuple(plan)
