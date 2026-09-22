"""G01 external source extraction and normalization primitives.

This module is intentionally data-driven. Authoritative discovery inputs are supplied
by an external manifest and payloads. No chain, RPC, contract, token, pool, pair or
strategy universe is embedded in source code.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping


@dataclass(frozen=True)
class Candidate:
    source_id: str
    source_key: str
    name: str
    chain_type: str | None
    chain_id: str | None
    network_type: str | None
    status: str | None
    state: str
    evidence_ref: str


def _get(obj: Mapping[str, Any], path: str, default: Any = None) -> Any:
    value: Any = obj
    for part in path.split("."):
        if not isinstance(value, Mapping) or part not in value:
            return default
        value = value[part]
    return value


def extract_cosmos_tree_records(
    tree_payload: Mapping[str, Any],
    chain_payloads: Mapping[str, Mapping[str, Any]],
    source_id: str,
    evidence_ref: str,
) -> list[Candidate]:
    candidates: list[Candidate] = []
    for item in tree_payload.get("tree", []):
        path = item.get("path", "")
        if not path.endswith("/chain.json"):
            continue
        record = chain_payloads.get(path)
        if record is None:
            candidates.append(
                Candidate(source_id, path, path.rsplit("/", 2)[-2], None, None, None,
                          None, "UNKNOWN", evidence_ref)
            )
            continue
        status = record.get("status")
        network_type = record.get("network_type")
        state = "VERIFIED_CANDIDATE" if status == "live" and network_type == "mainnet" else "EXCLUDED_NONPRODUCTION"
        candidates.append(
            Candidate(
                source_id=source_id,
                source_key=path,
                name=str(record.get("pretty_name") or record.get("chain_name") or path),
                chain_type=record.get("chain_type"),
                chain_id=str(record["chain_id"]) if record.get("chain_id") is not None else None,
                network_type=network_type,
                status=status,
                state=state,
                evidence_ref=evidence_ref,
            )
        )
    return candidates


def extract_defillama_chain_records(
    payload: Iterable[Mapping[str, Any]],
    source_id: str,
    evidence_ref: str,
) -> list[Candidate]:
    out: list[Candidate] = []
    for row in payload:
        name = row.get("name")
        if not name:
            continue
        chain_id = row.get("chainId")
        key = f"{name}|{chain_id}" if chain_id is not None else str(name)
        out.append(Candidate(source_id, key, str(name), None,
                             str(chain_id) if chain_id is not None else None,
                             None, None, "DISCOVERY_ONLY", evidence_ref))
    return out


def extract_dex_protocol_chains(
    payload: Iterable[Mapping[str, Any]],
    source_id: str,
    evidence_ref: str,
) -> list[Candidate]:
    out: list[Candidate] = []
    dex_categories = {"dex", "dexes", "exchange", "amm", "orderbook"}
    for row in payload:
        category = str(row.get("category") or "").strip().lower()
        if category not in dex_categories:
            continue
        for chain in row.get("chains") or []:
            if not chain:
                continue
            out.append(
                Candidate(source_id, f"{row.get('name','unknown')}|{chain}",
                          str(chain), None, None, None, None,
                          "DEX_DISCOVERY_ONLY", evidence_ref)
            )
    return out


def deduplicate_candidates(candidates: Iterable[Candidate]) -> list[Candidate]:
    seen: set[tuple[str, str | None, str | None]] = set()
    result: list[Candidate] = []
    for candidate in candidates:
        key = (candidate.name.strip().lower(), candidate.chain_type, candidate.chain_id)
        if key in seen:
            continue
        seen.add(key)
        result.append(candidate)
    return result
