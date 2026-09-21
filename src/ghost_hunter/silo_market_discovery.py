"""Silo V3 market discovery boundary.

Consumes externally collected Silo V3 API records as discovery evidence.
It does not treat API output as execution authority or as final on-chain truth.
Every market must later be verified against runtime deployment/code/state.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .registry import RegistryError


@dataclass(frozen=True)
class SiloMarketCandidate:
    market_id: str
    chain_id: int
    silo_id: str
    source: str
    provenance: str


def parse_market_candidates(payload: Any, *, provenance: str) -> tuple[SiloMarketCandidate, ...]:
    if not isinstance(provenance, str) or not provenance.strip():
        raise RegistryError("Silo discovery provenance is required")
    if not isinstance(payload, dict):
        raise RegistryError("Silo discovery payload must be an object")

    markets = payload.get("markets")
    if isinstance(markets, dict):
        markets = markets.get("items")
    if not isinstance(markets, list):
        raise RegistryError("Silo discovery payload has no market list")

    result: list[SiloMarketCandidate] = []
    seen: set[tuple[int, str]] = set()

    for item in markets:
        if not isinstance(item, dict):
            raise RegistryError("invalid Silo market record")
        market_id = item.get("id")
        silo_id = item.get("siloId")
        chain_id = item.get("chainId")
        if not isinstance(market_id, str) or not market_id:
            raise RegistryError("Silo market id is required")
        if not isinstance(silo_id, str) or not silo_id:
            raise RegistryError("Silo siloId is required")
        if not isinstance(chain_id, int) or chain_id < 0:
            raise RegistryError("Silo chainId must be a non-negative integer")

        identity = (chain_id, silo_id.lower())
        if identity in seen:
            raise RegistryError("duplicate Silo market identity")
        seen.add(identity)

        result.append(SiloMarketCandidate(
            market_id=market_id,
            chain_id=chain_id,
            silo_id=silo_id,
            source="SILO_V3_PUBLIC_API_DISCOVERY",
            provenance=provenance,
        ))

    return tuple(result)
