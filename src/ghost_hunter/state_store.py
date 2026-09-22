"""Append-only normalized state store primitives."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib, json
from typing import Any, Dict, List, Optional, Tuple

VERIFICATION_STATES = {"DISCOVERED","FETCHED","VALIDATED","NORMALIZED","FRESH","VERIFIED","REJECTED","STALE","CONFLICT","UNAVAILABLE"}

@dataclass(frozen=True)
class StateEnvelope:
    object_type: str
    canonical_id: str
    network_id: str
    source: str
    observed_block: Optional[int]
    observed_at: str
    collector_version: str
    schema_version: str
    freshness_deadline: str
    evidence_ref: str
    verification_state: str
    confidence: float
    raw_payload_hash: str
    def validate(self) -> None:
        if not self.object_type or not self.canonical_id or not self.network_id or not self.source:
            raise ValueError("missing canonical identity/source")
        if self.verification_state not in VERIFICATION_STATES:
            raise ValueError("invalid verification_state")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be within [0,1]")
        if len(self.raw_payload_hash) != 64:
            raise ValueError("raw_payload_hash must be SHA-256 hex")

@dataclass(frozen=True)
class StateRecord:
    envelope: StateEnvelope
    payload: Dict[str, Any]
    @property
    def identity(self) -> str:
        return self.envelope.canonical_id

class AppendOnlyStateStore:
    def __init__(self) -> None:
        self._raw: Dict[str, Dict[str, Any]] = {}
        self._current: Dict[str, StateRecord] = {}
        self._history: List[StateRecord] = []
        self._rejections: List[Dict[str, Any]] = []
        self._coverage: Dict[str, int] = {"discovered":0,"accepted":0,"rejected":0,"stale":0,"conflict":0,"unavailable":0}
    @staticmethod
    def hash_payload(payload: Dict[str, Any]) -> str:
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
        return hashlib.sha256(raw).hexdigest()
    def capture_raw(self, evidence_ref: str, payload: Dict[str, Any]) -> str:
        digest = self.hash_payload(payload)
        self._raw[evidence_ref] = {"hash": digest, "payload": payload}
        return digest
    def put(self, record: StateRecord) -> None:
        record.envelope.validate()
        key = record.identity
        previous = self._current.get(key)
        self._history.append(record)
        self._current[key] = record
        if previous is None:
            self._coverage["discovered"] += 1
        self._coverage["accepted"] += 1
    def reject(self, canonical_id: str, reason: str, details: Optional[str] = None) -> None:
        if reason not in {"REJECTED","STALE","CONFLICT","UNAVAILABLE"}:
            raise ValueError("invalid rejection reason")
        self._rejections.append({"canonical_id":canonical_id,"reason":reason,"details":details,"recorded_at":datetime.now(timezone.utc).isoformat()})
        self._coverage["rejected"] += 1
        self._coverage[reason.lower()] += 1
    def current(self, canonical_id: str) -> Optional[StateRecord]:
        return self._current.get(canonical_id)
    def history(self, canonical_id: Optional[str] = None) -> Tuple[StateRecord, ...]:
        if canonical_id is None:
            return tuple(self._history)
        return tuple(r for r in self._history if r.identity == canonical_id)
    def coverage(self) -> Dict[str, int]:
        return dict(self._coverage)
    def raw(self, evidence_ref: str) -> Optional[Dict[str, Any]]:
        return self._raw.get(evidence_ref)

def make_envelope(*, object_type: str, canonical_id: str, network_id: str, source: str, payload: Dict[str, Any], observed_block: Optional[int], freshness_deadline: str, evidence_ref: str, verification_state: str = "NORMALIZED", confidence: float = 0.5, collector_version: str = "collector-0.1.0", schema_version: str = "state-1.0") -> StateEnvelope:
    return StateEnvelope(object_type, canonical_id, network_id, source, observed_block, datetime.now(timezone.utc).isoformat(), collector_version, schema_version, freshness_deadline, evidence_ref, verification_state, confidence, AppendOnlyStateStore.hash_payload(payload))
