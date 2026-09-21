"""G01 machine-readable DEX/network relationship extraction.

Consumes external DeFiLlama-style payloads. No authoritative chain, venue,
address, token, pool, pair, RPC, strategy, or execution universe is embedded.
Protocol-to-chain observations are discovery evidence only.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Mapping


@dataclass(frozen=True)
class DexChainRelationship:
    source_id: str
    evidence_ref: str
    protocol_name: str
    protocol_slug: str | None
    chain_name: str
    source_chain_id: str | None


@dataclass(frozen=True)
class DexChainObservation:
    source_id: str
    evidence_ref: str
    chain_name: str
    source_chain_id: str | None


def _is_dex_category(value: Any) -> bool:
    return str(value or "").strip().lower() in {"dex", "dexes", "dexs", "exchange", "amm", "orderbook"}


def extract_defillama_dex_protocol_relationships(
    payload: Iterable[Mapping[str, Any]],
    source_id: str,
    evidence_ref: str,
) -> list[DexChainRelationship]:
    out: list[DexChainRelationship] = []
    for row in payload:
        if not _is_dex_category(row.get("category")):
            continue
        name = row.get("name")
        if not isinstance(name, str) or not name.strip():
            continue
        slug = row.get("slug")
        slug = slug.strip() if isinstance(slug, str) and slug.strip() else None
        for chain in row.get("chains") or []:
            if not isinstance(chain, str) or not chain.strip():
                continue
            out.append(
                DexChainRelationship(
                    source_id=source_id,
                    evidence_ref=evidence_ref,
                    protocol_name=name.strip(),
                    protocol_slug=slug,
                    chain_name=chain.strip(),
                    source_chain_id=None,
                )
            )
    return out


def extract_defillama_dex_chain_surface(
    payload: Iterable[Mapping[str, Any]],
    source_id: str,
    evidence_ref: str,
) -> list[DexChainObservation]:
    out: list[DexChainObservation] = []
    for row in payload:
        name = row.get("name")
        if not isinstance(name, str) or not name.strip():
            continue
        chain_id = row.get("chainId")
        out.append(
            DexChainObservation(
                source_id=source_id,
                evidence_ref=evidence_ref,
                chain_name=name.strip(),
                source_chain_id=str(chain_id) if chain_id is not None else None,
            )
        )
    return out


def deduplicate_relationships(
    rows: Iterable[DexChainRelationship],
) -> list[DexChainRelationship]:
    seen: set[tuple[str, str, str | None, str]] = set()
    out: list[DexChainRelationship] = []
    for row in rows:
        key = (
            row.source_id,
            row.protocol_slug or row.protocol_name.casefold(),
            row.source_chain_id,
            row.chain_name.casefold(),
        )
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out
