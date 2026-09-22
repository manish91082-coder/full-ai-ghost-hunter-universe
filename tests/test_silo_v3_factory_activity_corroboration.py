import json
from pathlib import Path
from ghost_hunter.silo_v3_factory_activity_corroboration import validate_activity_corroboration

def load_payload():
    return json.loads(Path("02_FLASH_LOAN_UNIVERSE/data/G02_SILO_FACTORY_ACTIVITY_CORROBORATION_v001.json").read_text())

def test_activity_corroboration_has_38_exact_identities():
    result = validate_activity_corroboration(load_payload())
    assert result["valid"] is True
    assert result["record_count"] == 38
    assert result["identity_count"] == 38

def test_same_address_cross_network_is_not_duplicate():
    payload = load_payload()
    matches = [r for r in payload["records"] if r["factory"].lower() == "0xf81d90df1b63d48536e78564d24d5dd8f2be58ad"]
    assert {r["network_id"] for r in matches} == {"eip155:146", "eip155:50"}

def test_start_silo_id_is_not_scan_block():
    assert all("scan_start_block_inclusive" not in r for r in load_payload()["records"])
