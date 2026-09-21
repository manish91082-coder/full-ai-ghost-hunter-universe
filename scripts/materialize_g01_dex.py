"""Materialize the current public DeFiLlama /protocols discovery payload.

This is a research/evidence utility only. It never authorizes trading and never
embeds an authoritative chain, venue, address, token, pool, pair, strategy or
execution universe. Raw payloads are written to the supplied output directory
for hashing and CI artifact retention. The current canonical G01 registry is
read-only and is used only for a conservative name-level join report.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SOURCE_URL = "https://api.llama.fi/protocols"
SOURCE_ID = "defillama-free-protocols"
DEX_CATEGORIES = {"dex", "dexes", "dexs", "exchange", "amm", "orderbook"}


def fetch(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "ghost-hunter-g01-materializer/1.0"},
    )
    with urllib.request.urlopen(request, timeout=120, context=ssl.create_default_context()) as response:
        return response.read()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_registry(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    obj = json.loads(path.read_text(encoding="utf-8"))
    return obj.get("records", []) if isinstance(obj, dict) else []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--registry",
        default="01_BLOCKCHAIN_UNIVERSE/data/G01_SOURCE_UNION_REGISTRY_v001.json",
    )
    parser.add_argument("--url", default=SOURCE_URL)
    args = parser.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    retrieved_at = datetime.now(timezone.utc).isoformat()
    raw = fetch(args.url)
    payload_hash = sha256(raw)
    (out / "defillama_protocols_raw.json").write_bytes(raw)

    payload = json.loads(raw)
    if not isinstance(payload, list):
        raise ValueError("DeFiLlama /protocols payload is not a JSON array")

    dex_rows = [
        row for row in payload
        if isinstance(row, dict)
        and str(row.get("category") or "").strip().lower() in DEX_CATEGORIES
    ]

    relationships: list[dict[str, Any]] = []
    chain_names: set[str] = set()
    for row in dex_rows:
        name = row.get("name")
        if not isinstance(name, str) or not name.strip():
            continue
        slug = row.get("slug")
        slug = slug.strip() if isinstance(slug, str) and slug.strip() else None
        for chain in row.get("chains") or []:
            if not isinstance(chain, str) or not chain.strip():
                continue
            chain_name = chain.strip()
            chain_names.add(chain_name)
            relationships.append({
                "schema_version": "g01.dex_protocol_chain_observation.v1",
                "source_id": SOURCE_ID,
                "evidence_ref": args.url,
                "retrieved_at": retrieved_at,
                "protocol_name": name.strip(),
                "protocol_slug": slug,
                "chain_name": chain_name,
                "source_chain_id": None,
                "authority": "discovery_only",
            })

    unique: dict[tuple[str, str | None, str], dict[str, Any]] = {}
    for row in relationships:
        key = (
            row["protocol_slug"] or row["protocol_name"].casefold(),
            row["chain_name"].casefold(),
            row["source_chain_id"],
        )
        unique.setdefault(key, row)

    canonical = load_registry(Path(args.registry))
    canonical_names = {
        str(r.get("normalized_name") or r.get("input_name") or "").strip().casefold()
        for r in canonical
        if isinstance(r, dict)
    }
    overlap = sorted(
        name for name in chain_names if name.casefold() in canonical_names
    )
    new_name_candidates = sorted(
        name for name in chain_names if name.casefold() not in canonical_names
    )

    (out / "dex_protocol_chain_observations.jsonl").write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in unique.values()),
        encoding="utf-8",
    )

    summary = {
        "schema_version": "g01.dex_materialization_run.v1",
        "source_id": SOURCE_ID,
        "source_url": args.url,
        "retrieved_at": retrieved_at,
        "raw_payload_sha256": payload_hash,
        "raw_payload_bytes": len(raw),
        "source_protocol_rows": len(payload),
        "dex_category_rows": len(dex_rows),
        "unique_protocol_chain_observations": len(unique),
        "unique_chain_labels_observed": len(chain_names),
        "name_level_overlap_with_current_g01_registry": len(overlap),
        "name_level_unmatched_candidates": len(new_name_candidates),
        "overlap_names": overlap,
        "unmatched_candidate_names": new_name_candidates,
        "identity_resolution": "PENDING_PRIMARY_VERIFICATION",
        "lifecycle_resolution": "PENDING_PRIMARY_VERIFICATION",
        "authority": "DISCOVERY_ONLY",
        "live_execution_authorized": False,
    }
    (out / "materialization_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
