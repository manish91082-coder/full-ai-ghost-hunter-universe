import json
from pathlib import Path
import pytest
from ghost_hunter.registry import RegistryError
from ghost_hunter.silo_v3_factory_scan_plan import load
P=Path(__file__).resolve().parents[1]/"02_FLASH_LOAN_UNIVERSE/data/G02_SILO_FACTORY_SCAN_PLAN_v001.json"
def test_scan_plan_has_38_identities_and_9_verified_start_blocks():
 p=load(P); assert len(p["records"])==38; assert sum(r["start_block_status"]=="DEPLOYMENT_RECEIPT_VERIFIED" for r in p["records"])==9; assert sum(r["start_block_status"]=="BLOCKED_MISSING_START_BLOCK" for r in p["records"])==29
def test_network_scoped_identity_does_not_cross_apply_blocks():
 p=load(P); x=next(r for r in p["records"] if r["factory"].lower()=="0xf81d90df1b63d48536e78564d24d5dd8f2be58ad" and r["network_id"]=="eip155:50"); assert x["start_block_status"]=="BLOCKED_MISSING_START_BLOCK"
def test_blocked_record_cannot_carry_guessed_start_block(tmp_path):
 p=json.loads(P.read_text()); blocked=next(r for r in p["records"] if r["start_block_status"]=="BLOCKED_MISSING_START_BLOCK"); blocked["scan_start_block_inclusive"]=1; q=tmp_path/"bad.json"; q.write_text(json.dumps(p));
 with pytest.raises(RegistryError): load(q)
def test_duplicate_network_factory_identity_fails_closed(tmp_path):
 p=json.loads(P.read_text()); p["records"].append(dict(p["records"][0])); p["total_scan_identities"]=39; q=tmp_path/"bad.json"; q.write_text(json.dumps(p));
 with pytest.raises(RegistryError): load(q)
