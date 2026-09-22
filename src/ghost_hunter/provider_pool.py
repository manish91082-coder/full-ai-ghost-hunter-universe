"""Fail-closed provider pool with health-aware rotation.

Provider endpoints remain runtime configuration. This module defines selection,
failure accounting and cooldown semantics only. It performs no network I/O.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from .registry import RegistryError
from .provider_registry import ProviderEndpoint


@dataclass
class ProviderHealth:
    failures: int = 0
    successes: int = 0
    cooldown_until: int = 0
    last_error: str | None = None


@dataclass
class ProviderPool:
    providers: tuple[ProviderEndpoint, ...]
    health: dict[tuple[str, str], ProviderHealth] = field(default_factory=dict)

    @classmethod
    def from_providers(cls, providers: Iterable[ProviderEndpoint]) -> "ProviderPool":
        rows = tuple(p for p in providers if p.enabled)
        if not rows:
            raise RegistryError("provider pool is empty")
        if len({(p.provider_id, p.network_id) for p in rows}) != len(rows):
            raise RegistryError("duplicate provider identity")
        return cls(rows, {(p.provider_id, p.network_id): ProviderHealth() for p in rows})

    def available(self, network_id: str, now_tick: int = 0) -> tuple[ProviderEndpoint, ...]:
        rows = [
            p for p in self.providers
            if p.network_id == network_id and p.enabled
            and self.health[(p.provider_id, p.network_id)].cooldown_until <= now_tick
        ]
        return tuple(sorted(rows, key=lambda p: (self.health[(p.provider_id, p.network_id)].failures, p.priority)))

    def select(self, network_id: str, now_tick: int = 0) -> ProviderEndpoint:
        rows = self.available(network_id, now_tick)
        if not rows:
            raise RegistryError("all providers unavailable for network")
        return rows[0]

    def record_success(self, provider_id: str, network_id: str) -> None:
        h = self._health(provider_id, network_id)
        h.successes += 1
        h.failures = 0
        h.cooldown_until = 0
        h.last_error = None

    def record_failure(self, provider_id: str, network_id: str, *, now_tick: int, cooldown_ticks: int = 1,
                       error: str | None = None) -> None:
        if cooldown_ticks < 1:
            raise RegistryError("cooldown_ticks must be positive")
        h = self._health(provider_id, network_id)
        h.failures += 1
        h.cooldown_until = now_tick + cooldown_ticks
        h.last_error = error

    def _health(self, provider_id: str, network_id: str) -> ProviderHealth:
        key = (provider_id, network_id)
        if key not in self.health:
            raise RegistryError("unknown provider identity")
        return self.health[key]
