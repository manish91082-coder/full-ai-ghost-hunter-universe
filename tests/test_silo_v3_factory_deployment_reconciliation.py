import json
from pathlib import Path
import pytest
from ghost_hunter.registry import RegistryError
from ghost_hunter.silo_v3_factory_deployment_reconciliation import load
P=Path(__file__).resolve().parents[1]/"02_FLASH_LOAN_UNIVERSE/data/G02_SILO_FACTORY_DEPLOYMENT_RECONCILIATION_v001.json"
def test_reconciles_13_networks_and_one_current_only_candidate():
 p=load(P); assert p["network_count"]==13; assert p["matched_network_count"]==12; assert p["current_deployment_candidate_count"]==1; assert p["reconciled_scan_identity_upper_bound"]==38; assert p["candidates"][0]["network_id"]=="eip155:10"
def test_tampered_upper_bound_fails_closed(tmp_path):
 d=json.loads(P.read_text()); d["reconciled_scan_identity_upper_bound"]=37; q=tmp_path/"bad.json"; q.write_text(json.dumps(d))
 with pytest.raises(RegistryError): load(q)
