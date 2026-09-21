"""Build a deterministic G01 DEX-label reconciliation queue.

Input: materialization_summary.json from the external research artifact.
Input: current canonical G01 source-union registry.
Output: unresolved DEX labels with conservative classification candidates.

This tool never promotes a label to canonical identity.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ALIAS_HINTS = {
    "near": "NEAR Protocol",
    "fuel": "Fuel Ignition",
    "plume mainnet": "Plume",
    "gravity": "Gravity L1",
    "rise": "Rise",
}

def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()

def classify(label: str, canonical_names: set[str]) -> tuple[str, str | None]:
    n = norm(label)
    if n in canonical_names:
        return "EXACT_NAME_MATCH", None
    if n in ALIAS_HINTS:
        return "LIKELY_ALIAS_CANDIDATE", ALIAS_HINTS[n]
    if "evm" in n or "zk" in n or "mainnet" in n or "network" in n:
        return "EXECUTION_PLANE_VARIANT_CANDIDATE", None
    if n in {"bitcoin", "ethereum", "solana", "cardano", "tron", "near", "sui"}:
        return "POSSIBLE_NETWORK_CANDIDATE", None
    return "UNKNOWN", None

def build(summary_path: Path, registry_path: Path, output_path: Path) -> None:
    summary = json.loads(summary_path.read_text())
    registry = json.loads(registry_path.read_text())
    canonical_names = {norm(r["normalized_name"]) for r in registry.get("records", []) if r.get("normalized_name")}
    rows = []
    for label in summary.get("unmatched_candidate_names", []):
        state, suggested = classify(label, canonical_names)
        rows.append({
            "observation_label": label,
            "classification": state,
            "suggested_canonical_name": suggested,
            "identity_state": "PENDING_PRIMARY_VERIFICATION",
            "lifecycle_state": "PENDING_PRIMARY_VERIFICATION",
            "source_id": summary.get("source_id"),
            "evidence_ref": summary.get("source_url"),
            "authority": "DISCOVERY_ONLY",
            "canonical_promotion": False,
        })
    output = {
        "schema_version": "g01.dex_label_reconciliation_queue.v1",
        "gate": "G01",
        "status": "UNRESOLVED_QUEUE",
        "input_observed_labels": summary.get("unique_chain_labels_observed"),
        "input_unmatched_labels": len(rows),
        "rows": rows,
        "classification_is_non_authoritative": True,
        "identity_requires_primary_evidence": True,
        "canonical_promotion_allowed": False,
    }
    output_path.write_text(json.dumps(output, indent=2) + "\n")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--summary", required=True)
    p.add_argument("--registry", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    build(Path(a.summary), Path(a.registry), Path(a.output))
