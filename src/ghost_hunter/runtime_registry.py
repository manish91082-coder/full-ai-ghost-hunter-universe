"""Fail-closed runtime registry loader.

Authoritative registry data is external. This module verifies bytes and projects
validated snapshots; it contains no chain, RPC, address, token, pool or strategy
constants.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from pathlib import Path
from typing import Iterable, Mapping

from .registry import RegistryEntry, RegistrySnapshot, RegistryError, require_fresh_snapshot


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_snapshot_file(path: str | Path, *, expected_sha256: str,
                       allowed_versions: Iterable[str]) -> RegistrySnapshot:
    raw = Path(path).read_bytes()
    actual = sha256_bytes(raw)
    if actual != expected_sha256:
        raise RegistryError("snapshot SHA-256 mismatch")
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RegistryError("invalid snapshot JSON") from exc

    entries = tuple(
        RegistryEntry(
            registry_type=str(x["registry_type"]),
            canonical_id=str(x["canonical_id"]),
            network_id=str(x["network_id"]),
            version=str(x["version"]),
            source_ref=str(x["source_ref"]),
            observed_at=str(x["observed_at"]),
            payload_hash=str(x["payload_hash"]),
            status=str(x.get("status", "ACTIVE")),
        )
        for x in payload.get("entries", [])
    )
    snapshot = RegistrySnapshot(
        registry_type=str(payload["registry_type"]),
        version=str(payload["version"]),
        entries=entries,
        manifest_hash=str(payload["manifest_hash"]),
        signature_ref=payload.get("signature_ref"),
    )
    return require_fresh_snapshot(snapshot, allowed_versions=allowed_versions)


def snapshot_to_runtime_projection(snapshot: RegistrySnapshot) -> Mapping[str, object]:
    snapshot.validate()
    return {
        "registry_type": snapshot.registry_type,
        "version": snapshot.version,
        "manifest_hash": snapshot.manifest_hash,
        "entry_count": len(snapshot.entries),
        "active_entries": [asdict(e) for e in snapshot.entries if e.status == "ACTIVE"],
    }
