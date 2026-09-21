import hashlib
import json

import pytest

from src.ghost_hunter.registry import RegistryError
from src.ghost_hunter.runtime_registry import load_snapshot_file, snapshot_to_runtime_projection
from src.ghost_hunter.provider_registry import load_provider_endpoints, choose_provider


def write_snapshot(tmp_path, canonical_id):
    payload = {
        "registry_type": "fixture",
        "version": "v1",
        "manifest_hash": "1" * 64,
        "entries": [{
            "registry_type": "fixture",
            "canonical_id": canonical_id,
            "network_id": "fixture:1",
            "version": "v1",
            "source_ref": "fixture://source",
            "observed_at": "2099-01-01T00:00:00Z",
            "payload_hash": "2" * 64,
            "status": "ACTIVE",
        }],
    }
    raw = json.dumps(payload, sort_keys=True).encode()
    path = tmp_path / "snapshot.json"
    path.write_bytes(raw)
    return path, hashlib.sha256(raw).hexdigest()


def test_runtime_snapshot_substitution_changes_projection(tmp_path):
    a, ah = write_snapshot(tmp_path, "market:A")
    b, bh = write_snapshot(tmp_path, "market:B")
    pa = snapshot_to_runtime_projection(load_snapshot_file(a, expected_sha256=ah, allowed_versions={"v1"}))
    pb = snapshot_to_runtime_projection(load_snapshot_file(b, expected_sha256=bh, allowed_versions={"v1"}))
    assert pa["active_entries"][0]["canonical_id"] == "market:A"
    assert pb["active_entries"][0]["canonical_id"] == "market:B"
    assert pa != pb


def test_snapshot_hash_mismatch_fails_closed(tmp_path):
    path, _ = write_snapshot(tmp_path, "market:A")
    with pytest.raises(RegistryError):
        load_snapshot_file(path, expected_sha256="0" * 64, allowed_versions={"v1"})


def test_provider_selection_is_runtime_only(monkeypatch):
    monkeypatch.setenv(
        "GH_PROVIDER_FIXTURE",
        "p2|fixture:1|endpoint-two|20,p1|fixture:1|endpoint-one|10",
    )
    providers = load_provider_endpoints("GH_PROVIDER_FIXTURE")
    assert choose_provider(providers, "fixture:1").provider_id == "p1"


def test_missing_provider_configuration_fails_closed(monkeypatch):
    monkeypatch.delenv("GH_PROVIDER_MISSING", raising=False)
    with pytest.raises(RegistryError):
        load_provider_endpoints("GH_PROVIDER_MISSING")


def test_provider_source_has_no_embedded_endpoint():
    source = open("src/ghost_hunter/provider_registry.py", encoding="utf-8").read()
    assert "https://" not in source
    assert "0x" not in source
