"""Fail-closed validation for the SiloFactory historical scan plan."""
from __future__ import annotations
import json
from pathlib import Path
from .registry import RegistryError
EXPECTED_SCHEMA="g02.silo.factory.scan.plan.v2"
REQUIRED_STATUSES={"DEPLOYMENT_RECEIPT_VERIFIED","GENESIS_FULL_CHAIN_REQUIRED"}
def load(path: str|Path):
 p=json.loads(Path(path).read_text(encoding="utf-8"))
 if p.get("schema_version")!=EXPECTED_SCHEMA: raise RegistryError("unsupported SiloFactory scan-plan schema")
 records=p.get("records")
 if not isinstance(records,list) or len(records)!=p.get("total_scan_identities"): raise RegistryError("scan identity count mismatch")
 identities={(r.get("network_id"),str(r.get("factory","")).lower()) for r in records}
 if len(identities)!=len(records): raise RegistryError("duplicate scan identity")
 if p.get("known_created_factory_count")!=37 or p.get("current_deployment_candidate_count")!=1: raise RegistryError("unexpected denominator counts")
 for r in records:
  status=r.get("start_block_status"); start=r.get("scan_start_block_inclusive")
  if status not in REQUIRED_STATUSES: raise RegistryError("invalid start-block status")
  if status=="DEPLOYMENT_RECEIPT_VERIFIED":
   if not isinstance(start,int) or start<0: raise RegistryError("verified start block missing")
   ev=r.get("start_block_evidence",{})
   if ev.get("evidence_type")!="FOUNDRY_RECEIPT_CREATE_BLOCK" or not ev.get("deployment_transaction"): raise RegistryError("verified start block lacks receipt evidence")
  else:
   if start!=0: raise RegistryError("genesis fallback must start at block 0")
   ev=r.get("start_block_evidence",{})
   if ev.get("evidence_type")!="GENESIS_LOWER_BOUND_NO_DEPLOYMENT_INFERENCE": raise RegistryError("invalid genesis fallback evidence")
   if ev.get("deployment_transaction") is not None: raise RegistryError("genesis fallback cannot contain deployment tx")
   if r.get("range_authority")!="GENESIS_TO_CURRENT": raise RegistryError("genesis range authority required")
 return p
