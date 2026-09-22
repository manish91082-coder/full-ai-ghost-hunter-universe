import json
from pathlib import Path
import pytest
from ghost_hunter.registry import RegistryError
from ghost_hunter.silo_v3_factory_scan_plan import load
P=Path(__file__).resolve().parents[1]/"02_FLASH_LOAN_UNIVERSE/data/G02_SILO_FACTORY_SCAN_PLAN_v001.json"
def test_scan_plan_has_38_identities_9_receipt_and_29_genesis_fallbacks():
 p=load(P); assert len(p["records"])==38; assert sum(r["start_block_status"]=="DEPLOYMENT_RECEIPT_VERIFIED" for r in p["records"])==9; assert sum(r["start_block_status"]=="GENESIS_FULL_CHAIN_REQUIRED" for r in p["records"])==29

def test_genesis_fallback_is_not_a_deployment_claim():
 p=load(P); r=next(x for x in p["records"] if x["start_block_status"]=="GENESIS_FULL_CHAIN_REQUIRED"); assert r["scan_start_block_inclusive"]==0; assert r["start_block_evidence"]["deployment_transaction"] is None

def test_genesis_fallback_cannot_use_nonzero_block(tmp_path):
 p=json.loads(P.read_text()); r=next(x for x in p["records"] if x["start_block_status"]=="GENESIS_FULL_CHAIN_REQUIRED"); r["scan_start_block_inclusive"]=1; q=tmp_path/"bad.json"; q.write_text(json.dumps(p));
 with pytest.raises(RegistryError): load(q)

def test_duplicate_identity_fails_closed(tmp_path):
 p=json.loads(P.read_text()); p["records"].append(dict(p["records"][0])); p["total_scan_identities"]=39; q=tmp_path/"bad.json"; q.write_text(json.dumps(p));
 with pytest.raises(RegistryError): load(q)
