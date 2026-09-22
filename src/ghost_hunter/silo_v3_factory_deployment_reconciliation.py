from __future__ import annotations
import json
from pathlib import Path
from .registry import RegistryError
EXPECTED_SCHEMA="g02.silo.factory.deployment.reconciliation.v1"
def load(path: str|Path):
 p=json.loads(Path(path).read_text(encoding="utf-8"))
 if p.get("schema_version")!=EXPECTED_SCHEMA: raise RegistryError("unsupported deployment reconciliation schema")
 records=p.get("records",[])
 if len(records)!=p.get("network_count"): raise RegistryError("network count mismatch")
 cand=[r for r in records if not r.get("matches_pinned_factory_list_newest")]
 if len(cand)!=p.get("current_deployment_candidate_count"): raise RegistryError("candidate count mismatch")
 if p.get("reconciled_scan_identity_upper_bound")!=p.get("known_created_factory_count")+len(cand): raise RegistryError("upper bound mismatch")
 for r in records:
  if r.get("source_ref")!="master" or not isinstance(r.get("address"),str) or len(r["address"])!=42: raise RegistryError("invalid deployment evidence")
 return p
