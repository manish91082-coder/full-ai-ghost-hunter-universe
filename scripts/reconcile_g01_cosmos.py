#!/usr/bin/env python3
"""Build a conservative semantic reconciliation queue from Cosmos production observations.

This tool never promotes identities. It only classifies observations for review.
"""
import json, os, re
from collections import Counter
from pathlib import Path

INPUT = Path(os.environ.get("COSMOS_PRODUCTION_JSONL","artifacts/g01_cosmos/chain_registry_production.jsonl"))
REGISTRY = Path("01_BLOCKCHAIN_UNIVERSE/data/G01_SOURCE_UNION_REGISTRY_v001.json")
OUT = Path("artifacts/g01_cosmos")
OUT.mkdir(parents=True, exist_ok=True)

def norm(s):
    if not s: return ""
    s=s.lower().strip()
    s=re.sub(r"[^a-z0-9]+"," ",s)
    return re.sub(r"\s+"," ",s).strip()

def classify(obs, existing):
    n=norm(obs.get("chain_name"))
    exact=existing.get(n, [])
    if exact:
        return "EXACT_OR_CANONICAL_NAME_OVERLAP", exact
    name=(obs.get("chain_name") or "").lower()
    if any(x in name for x in ("test","dev","staging","sandbox","local")):
        return "NONPRODUCTION_LABEL_REVIEW", []
    if any(x in name for x in ("evm","cosmos","wasm","solana","move")):
        return "EXECUTION_PLANE_REVIEW", []
    if any(x in name for x in ("bridge","ibc","gravity","wormchain","gateway")):
        return "PROTOCOL_OR_EXECUTION_RELATION_REVIEW", []
    return "PRIMARY_IDENTITY_REVIEW", []

def main():
    registry=json.loads(REGISTRY.read_text(encoding="utf-8"))
    existing={}
    for r in registry.get("records",[]):
        for value in (r.get("input_name"),r.get("normalized_name"),r.get("canonical_record_key")):
            k=norm(value)
            if k: existing.setdefault(k,[]).append(r.get("canonical_record_key"))
    rows=[json.loads(x) for x in INPUT.read_text(encoding="utf-8").splitlines() if x.strip()]
    queue=[]
    counts=Counter()
    for o in rows:
        cls,refs=classify(o,existing)
        item={
            "queue_id":"cosmos:"+str(len(queue)+1).zfill(4),
            "source_path":o.get("source_path"),
            "chain_name":o.get("chain_name"),
            "native_chain_id":o.get("chain_id"),
            "chain_type":o.get("chain_type"),
            "status":o.get("status"),
            "network_type":o.get("network_type"),
            "classification":cls,
            "possible_existing_canonical_keys":sorted(set(refs)),
            "identity_promotion":"PROHIBITED_PENDING_PRIMARY_RECONCILIATION",
            "evidence_payload_sha256":o.get("payload_sha256"),
        }
        queue.append(item); counts[cls]+=1
    queue.sort(key=lambda x:(x["classification"],norm(x["chain_name"]),x["native_chain_id"] or ""))
    Path(OUT/"semantic_reconciliation_queue.jsonl").write_text(
        "".join(json.dumps(x,sort_keys=True,ensure_ascii=False)+"\n" for x in queue),encoding="utf-8")
    summary={
        "artifact":"G01_COSMOS_SEMANTIC_RECONCILIATION_QUEUE",
        "input_records":len(rows),
        "queue_records":len(queue),
        "classification_counts":dict(sorted(counts.items())),
        "canonical_registry_records":len(registry.get("records",[])),
        "identity_promotion":"PROHIBITED",
        "authority":"review queue only; no execution authorization"
    }
    Path(OUT/"semantic_queue_summary.json").write_text(json.dumps(summary,indent=2,sort_keys=True),encoding="utf-8")
    print(json.dumps(summary,indent=2,sort_keys=True))
if __name__=="__main__": main()
