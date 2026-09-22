"""Dynamic registry interfaces and immutable snapshot validation.

Runtime authority is external. This module contains schemas/validation only.
It never embeds chains, RPC endpoints, addresses, tokens, pools or strategies.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Tuple

class RegistryError(ValueError):
    pass

@dataclass(frozen=True)
class RegistryEntry:
    registry_type: str
    canonical_id: str
    network_id: str
    version: str
    source_ref: str
    observed_at: str
    payload_hash: str
    status: str = "ACTIVE"

    def validate(self) -> None:
        required = {
            "registry_type": self.registry_type,
            "canonical_id": self.canonical_id,
            "network_id": self.network_id,
            "version": self.version,
            "source_ref": self.source_ref,
            "observed_at": self.observed_at,
            "payload_hash": self.payload_hash,
        }
        if any(not str(v).strip() for v in required.values()):
            raise RegistryError("registry entry has missing identity/provenance")
        if self.status not in {"ACTIVE", "RETIRED", "QUARANTINED"}:
            raise RegistryError("invalid registry status")
        if len(self.payload_hash) != 64:
            raise RegistryError("payload_hash must be SHA-256 hex")

@dataclass(frozen=True)
class RegistrySnapshot:
    registry_type: str
    version: str
    entries: Tuple[RegistryEntry, ...]
    manifest_hash: str
    signature_ref: str | None = None

    def validate(self) -> None:
        if not self.registry_type or not self.version or len(self.manifest_hash) != 64:
            raise RegistryError("invalid registry snapshot identity")
        seen: set[tuple[str, str]] = set()
        for entry in self.entries:
            entry.validate()
            if entry.registry_type != self.registry_type:
                raise RegistryError("entry registry type mismatch")
            key = (entry.network_id, entry.canonical_id)
            if key in seen:
                raise RegistryError("duplicate canonical registry identity")
            seen.add(key)

class RegistrySource:
    """Interface implemented by runtime-backed registry adapters."""
    def load(self) -> RegistrySnapshot:
        raise NotImplementedError

def validate_snapshot(snapshot: RegistrySnapshot) -> RegistrySnapshot:
    snapshot.validate()
    return snapshot

def require_fresh_snapshot(snapshot: RegistrySnapshot, *, allowed_versions: Iterable[str]) -> RegistrySnapshot:
    snapshot.validate()
    allowed = set(allowed_versions)
    if snapshot.version not in allowed:
        raise RegistryError("registry version is not authorized")
    return snapshot

def project_runtime_value(snapshot: RegistrySnapshot, canonical_id: str) -> Mapping[str, Any]:
    for entry in snapshot.entries:
        if entry.canonical_id == canonical_id:
            return {
                "registry_type": entry.registry_type,
                "network_id": entry.network_id,
                "version": entry.version,
                "source_ref": entry.source_ref,
                "status": entry.status,
            }
    raise RegistryError("canonical_id absent from authoritative snapshot")
