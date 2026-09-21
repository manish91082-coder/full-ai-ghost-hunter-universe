import pytest
from src.ghost_hunter.registry import RegistryEntry, RegistrySnapshot, RegistryError, validate_snapshot, require_fresh_snapshot

def entry(cid="network:1"):
    return RegistryEntry("universe", cid, "1", "v1", "fixture://evidence", "2099-01-01T00:00:00Z", "0"*64)

def test_snapshot_validates_and_is_dynamic():
    s=RegistrySnapshot("universe","v1",(entry("network:1"),), "1"*64)
    assert validate_snapshot(s) is s
    assert s.entries[0].canonical_id=="network:1"

def test_duplicate_identity_fails_closed():
    e=entry()
    s=RegistrySnapshot("universe","v1",(e,e), "1"*64)
    with pytest.raises(RegistryError):
        s.validate()

def test_unauthorized_version_fails_closed():
    s=RegistrySnapshot("universe","v9",(entry(),), "1"*64)
    with pytest.raises(RegistryError):
        require_fresh_snapshot(s, allowed_versions={"v1"})

def test_registry_contains_no_execution_universe_constants():
    source=open("src/ghost_hunter/registry.py", encoding="utf-8").read()
    forbidden=("0x","http://","https://","chain_id=1","Ethereum","Uniswap","Aave","Morpho")
    assert not any(x in source for x in forbidden)
