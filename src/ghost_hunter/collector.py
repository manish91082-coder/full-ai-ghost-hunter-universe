"""Deterministic collector and provider-pool primitives. No network or wallet side effects."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Iterable, Optional
from .state_store import AppendOnlyStateStore, StateRecord, make_envelope

@dataclass(frozen=True)
class ProviderHealth:
    name: str
    healthy: bool
    latency_ms: Optional[float] = None
    error_rate: float = 0.0
    last_success_at: Optional[str] = None
    rate_limited: bool = False

class ProviderPool:
    def __init__(self, providers: Iterable[str]) -> None:
        names = tuple(dict.fromkeys(providers))
        if not names: raise ValueError("provider pool cannot be empty")
        self._health = {n: ProviderHealth(name=n, healthy=True) for n in names}
    def ordered(self):
        return tuple(h for h in self._health.values() if h.healthy and not h.rate_limited)
    def mark(self, name: str, *, healthy: bool, latency_ms: Optional[float] = None, error_rate: Optional[float] = None, rate_limited: Optional[bool] = None) -> None:
        old = self._health[name]
        self._health[name] = ProviderHealth(name, healthy, latency_ms if latency_ms is not None else old.latency_ms, error_rate if error_rate is not None else old.error_rate, old.last_success_at, rate_limited if rate_limited is not None else old.rate_limited)
    def health(self) -> Dict[str, ProviderHealth]:
        return dict(self._health)

@dataclass(frozen=True)
class CollectionResult:
    accepted: bool
    canonical_id: str
    reason: Optional[str] = None

class Collector:
    def __init__(self, store: AppendOnlyStateStore, providers: ProviderPool) -> None:
        self.store, self.providers = store, providers
    def ingest(self, *, object_type: str, canonical_id: str, network_id: str, source: str, payload: Dict[str, Any], observed_block: Optional[int], freshness_deadline: str, evidence_ref: str, verification_state: str = "NORMALIZED", confidence: float = 0.5) -> CollectionResult:
        digest = self.store.capture_raw(evidence_ref, payload)
        envelope = make_envelope(object_type=object_type, canonical_id=canonical_id, network_id=network_id, source=source, payload=payload, observed_block=observed_block, freshness_deadline=freshness_deadline, evidence_ref=evidence_ref, verification_state=verification_state, confidence=confidence)
        if envelope.raw_payload_hash != digest:
            self.store.reject(canonical_id, "CONFLICT", "raw hash mismatch")
            return CollectionResult(False, canonical_id, "CONFLICT")
        try:
            self.store.put(StateRecord(envelope, dict(payload)))
        except ValueError as exc:
            self.store.reject(canonical_id, "REJECTED", str(exc))
            return CollectionResult(False, canonical_id, "REJECTED")
        return CollectionResult(True, canonical_id)
