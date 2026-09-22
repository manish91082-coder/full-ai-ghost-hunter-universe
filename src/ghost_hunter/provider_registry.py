"""Runtime provider registry contract.

Provider endpoints are supplied only by external runtime configuration. No
endpoint, credential, network or provider name is authoritative in source.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Iterable

from .registry import RegistryError


@dataclass(frozen=True)
class ProviderEndpoint:
    provider_id: str
    network_id: str
    endpoint: str
    priority: int = 100
    enabled: bool = True

    def validate(self) -> None:
        if not self.provider_id.strip() or not self.network_id.strip():
            raise RegistryError("provider identity missing")
        if not self.endpoint.strip():
            raise RegistryError("provider endpoint missing")
        if self.priority < 0:
            raise RegistryError("provider priority must be non-negative")


def load_provider_endpoints(env_name: str) -> tuple[ProviderEndpoint, ...]:
    raw = os.getenv(env_name, "")
    if not raw.strip():
        raise RegistryError("provider configuration is missing")
    rows = []
    for item in raw.split(","):
        parts = item.strip().split("|")
        if len(parts) != 4:
            raise RegistryError("provider record must be id|network|endpoint|priority")
        row = ProviderEndpoint(parts[0], parts[1], parts[2], int(parts[3]))
        row.validate()
        if row.enabled:
            rows.append(row)
    if not rows:
        raise RegistryError("no enabled providers")
    return tuple(sorted(rows, key=lambda x: x.priority))


def choose_provider(providers: Iterable[ProviderEndpoint], network_id: str) -> ProviderEndpoint:
    candidates = [p for p in providers if p.enabled and p.network_id == network_id]
    if not candidates:
        raise RegistryError("no provider available for requested network")
    return min(candidates, key=lambda p: p.priority)
