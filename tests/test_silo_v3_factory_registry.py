import json
from pathlib import Path

import pytest

from ghost_hunter.registry import RegistryError
from ghost_hunter.silo_v3_factory_registry import (
    EXPECTED_EVENT_TOPIC0,
    SiloFactoryRegistry,
)

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "02_FLASH_LOAN_UNIVERSE" / "data" / "G02_SILO_FACTORY_REGISTRY_v001.json"

def test_silo_factory_registry_has_37_identities_across_13_networks():
    registry = SiloFactoryRegistry.from_json(REGISTRY_PATH)
    assert registry.factory_count == 37
    assert registry.network_count == 13
    assert len(registry.records) == 37
    assert len({(r.network_id, r.factory.lower()) for r in registry.records}) == 37
    assert registry.event_topic0 == EXPECTED_EVENT_TOPIC0

def test_registry_rejects_duplicate_factory_identity(tmp_path):
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    data["records"].append(dict(data["records"][0], id="SILOFACT-9999"))
    data["factory_count"] = 38
    candidate = tmp_path / "duplicate.json"
    candidate.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(RegistryError):
        SiloFactoryRegistry.from_json(candidate)

def test_registry_requires_every_factory_to_have_explicit_start_block():
    registry = SiloFactoryRegistry.from_json(REGISTRY_PATH)
    starts = {record.id: 100 for record in registry.records[:-1]}
    with pytest.raises(RegistryError, match="missing explicit start blocks"):
        registry.build_scan_plan(starts)

def test_registry_rejects_extra_start_block():
    registry = SiloFactoryRegistry.from_json(REGISTRY_PATH)
    starts = {record.id: 100 for record in registry.records}
    starts["NOT-A-FACTORY"] = 100
    with pytest.raises(RegistryError, match="unexpected start-block"):
        registry.build_scan_plan(starts)

def test_registry_builds_explicit_scan_plan_without_inference():
    registry = SiloFactoryRegistry.from_json(REGISTRY_PATH)
    starts = {record.id: index * 100 for index, record in enumerate(registry.records)}
    plan = registry.build_scan_plan(starts)
    assert len(plan) == 37
    assert plan[0].start_block == 0
    assert plan[-1].start_block == 3600
    assert all(item.event_topic0 == EXPECTED_EVENT_TOPIC0 for item in plan)
