import json
from pathlib import Path
from ghost_hunter.silo_factory_deployment_block_evidence import validate_deployment_block_evidence

def load():
    return json.loads(Path("02_FLASH_LOAN_UNIVERSE/data/G02_SILO_FACTORY_DEPLOYMENT_BLOCK_EVIDENCE_v001.json").read_text())

def test_current_deployment_evidence_is_9_plus_4_blocked():
    out=validate_deployment_block_evidence(load())
    assert out == {"valid":True,"evidenced_count":9,"blocked_count":4,"identity_count":13}

def test_optimism_current_factory_has_exact_create_block():
    r=next(x for x in load()["records"] if x["network_id"]=="eip155:10")
    assert r["factory"].lower()=="0x8ab5d81d342f14e594c65a6b33582b57e78e4a9d"
    assert r["deployment_block"]==148172013

def test_missing_broadcasts_remain_fail_closed():
    assert {x["network_id"] for x in load()["blocked"]}=={"eip155:5000","eip155:57073","eip155:4326","eip155:50"}
