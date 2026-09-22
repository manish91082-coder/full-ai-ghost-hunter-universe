"""Materialize read-only Silo V3 factory observations from external RPC runtime.

Evidence-only: never signs/submits transactions and never promotes partial output
to a complete denominator.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Any, Iterable

from .registry import RegistryError
from .silo_v3_factory_enumerator import SiloV3FactoryEnumerator, SiloFactoryObservation
from .silo_v3_market_binding import SiloV3MarketBinder

# keccak256("NewSilo(address,address,address,address,address,address)")
# Derived from the pinned ISiloFactory event declaration.
NEWSILO_TOPIC0 = "0x3d6b896c73b628ec6ba0bdfe3cdee1356ea2af31af2a97bbd6b532ca6fa00acb"


@dataclass(frozen=True)
class FactoryMaterialization:
    factory_id: str
    network_id: str
    factory: str
    start_block: int
    status: str
    event_count: int
    verified_market_count: int
    provider_id: str | None
    current_complete: bool
    events: tuple[dict[str, Any], ...] = ()
    markets: tuple[dict[str, Any], ...] = ()
    error: str | None = None


def _event_dict(event: Any) -> dict[str, Any]:
    return {
        "network_id": event.network_id, "factory": event.factory,
        "implementation": event.implementation, "token0": event.token0,
        "token1": event.token1, "silo0": event.silo0, "silo1": event.silo1,
        "silo_config": event.silo_config, "block_number": event.block_number,
        "transaction_hash": event.transaction_hash, "log_index": event.log_index,
    }


def _market_dict(market: Any) -> dict[str, Any]:
    return {"event": _event_dict(market.event),
            "silo0": asdict(market.silo0_state),
            "silo1": asdict(market.silo1_state)}


def materialize_factories(records: Iterable[dict[str, Any]],
                          enumerator: SiloV3FactoryEnumerator,
                          *, binder: SiloV3MarketBinder | None = None,
                          stop_on_error: bool = False) -> tuple[FactoryMaterialization, ...]:
    results: list[FactoryMaterialization] = []
    for record in records:
        factory_id = str(record.get("factory_id", ""))
        network_id = str(record.get("network_id", ""))
        factory = str(record.get("factory", ""))
        start = record.get("scan_start_block_inclusive")
        try:
            if not factory_id or not network_id or not factory:
                raise RegistryError("factory scan record identity is incomplete")
            if not isinstance(start, int) or start < 0:
                raise RegistryError("scan_start_block_inclusive must be a non-negative integer")
            observation: SiloFactoryObservation = enumerator.enumerate(
                network_id, factory, from_block=start)
            markets: tuple[dict[str, Any], ...] = ()
            verified_count = 0
            status = "ENUMERATED_READ_ONLY"
            if binder is not None:
                bound = binder.verify(observation)
                markets = tuple(_market_dict(m) for m in bound.markets)
                verified_count = bound.verified_market_count
                status = "RUNTIME_VERIFIED_READ_ONLY"
            results.append(FactoryMaterialization(
                factory_id, network_id, factory, start, status,
                observation.completeness.event_count, verified_count,
                observation.completeness.provider_id,
                observation.completeness.current_complete,
                tuple(_event_dict(e) for e in observation.events), markets))
        except Exception as exc:
            results.append(FactoryMaterialization(
                factory_id, network_id, factory,
                start if isinstance(start, int) and start >= 0 else -1,
                "FAILED_CLOSED", 0, 0, None, False, error=str(exc)))
            if stop_on_error:
                break
    return tuple(results)


def materialization_document(results: Iterable[FactoryMaterialization],
                             *, expected_factory_count: int,
                             scan_plan_path: str,
                             provider_env: str = "GH_PROVIDER_RUNTIME") -> dict[str, Any]:
    rows = tuple(results)
    complete = (len(rows) == expected_factory_count and expected_factory_count > 0
                and all(r.status != "FAILED_CLOSED" and r.current_complete for r in rows))
    return {
        "schema_version": "g02.silo.factory.runtime.observation.v1",
        "canonical_role": "CURRENT_RUNTIME_OBSERVATION_EVIDENCE",
        "execution_authority": "NONE", "live_trading": "STOP",
        "scan_plan": scan_plan_path, "provider_env": provider_env,
        "expected_factory_count": expected_factory_count,
        "materialized_factory_count": len(rows),
        "overall_status": "COMPLETE" if complete else "INCOMPLETE",
        "records": [asdict(r) for r in rows],
        "completion_rule": "COMPLETE requires every bounded scan-plan identity to have a strict-current observation; failed or partial output is never a complete denominator.",
    }
