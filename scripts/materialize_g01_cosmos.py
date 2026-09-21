#!/usr/bin/env python3
"""Materialize the current Cosmos Chain Registry production subset.

Discovery-only. Never authorizes execution and never mutates the canonical G01
registry. Uses the pinned Git tree SHA supplied at runtime for reproducibility.
"""
import hashlib, json, os, sys
from datetime import datetime, timezone
from urllib.request import Request, urlopen

API_ROOT = "https://api.github.com"
RAW_ROOT = "https://raw.githubusercontent.com/cosmos/chain-registry"
REPO = "cosmos/chain-registry"
TREE_SHA = os.environ.get("COSMOS_TREE_SHA", "810b0b68e4591078295ccce76205e970b3c002e5")
OUT = "artifacts/g01_cosmos"

def get(url):
    req = Request(url, headers={"User-Agent": "ghost-hunter-g01-materializer/1.0", "Accept": "application/vnd.github+json"})
    with urlopen(req, timeout=30) as r:
        return r.read()

def main():
    os.makedirs(OUT, exist_ok=True)
    tree_bytes = get(f"{API_ROOT}/repos/{REPO}/git/trees/{TREE_SHA}?recursive=1")
    tree = json.loads(tree_bytes)
    chain_paths = sorted(
        x["path"] for x in tree.get("tree", [])
        if x.get("type") == "blob" and x["path"].endswith("/chain.json")
        and not x["path"].startswith(("_", "."))
    )
    observations = []
    errors = []
    for path in chain_paths:
        try:
            payload = get(f"{RAW_ROOT}/{TREE_SHA}/{path}")
            obj = json.loads(payload)
            observations.append({
                "source_path": path,
                "source_tree_sha": TREE_SHA,
                "payload_sha256": hashlib.sha256(payload).hexdigest(),
                "chain_name": obj.get("chain_name"),
                "chain_id": obj.get("chain_id"),
                "status": obj.get("status"),
                "network_type": obj.get("network_type"),
                "chain_type": obj.get("chain_type"),
                "bech32_prefix": obj.get("bech32_prefix"),
                "raw_observation": obj,
            })
        except Exception as exc:
            errors.append({"source_path": path, "error": str(exc)})
    prod = [x for x in observations if x["status"] == "live" and x["network_type"] == "mainnet"]
    excluded = [x for x in observations if x["status"] != "live" or x["network_type"] != "mainnet"]
    now = datetime.now(timezone.utc).isoformat()
    with open(f"{OUT}/chain_registry_production.jsonl", "w", encoding="utf-8") as f:
        for x in prod:
            f.write(json.dumps(x, sort_keys=True, ensure_ascii=False) + "\n")
    summary = {
        "artifact": "G01_COSMOS_CHAIN_REGISTRY_PRODUCTION_MATERIALIZATION",
        "retrieved_at": now,
        "source_repo": REPO,
        "source_tree_sha": TREE_SHA,
        "chain_json_paths": len(chain_paths),
        "observations_loaded": len(observations),
        "production_records": len(prod),
        "excluded_nonproduction_records": len(excluded),
        "fetch_errors": len(errors),
        "raw_tree_sha256": hashlib.sha256(tree_bytes).hexdigest(),
        "production_jsonl_sha256": hashlib.sha256(open(f"{OUT}/chain_registry_production.jsonl","rb").read()).hexdigest(),
        "authority": "discovery/reconciliation input only; not execution authorization",
        "filter": "status == live AND network_type == mainnet",
    }
    with open(f"{OUT}/materialization_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, sort_keys=True)
    with open(f"{OUT}/fetch_errors.json", "w", encoding="utf-8") as f:
        json.dump(errors, f, indent=2, sort_keys=True)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if not errors else 2

if __name__ == "__main__":
    sys.exit(main())
