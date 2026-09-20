"""Dynamic runtime configuration boundary.

Critical execution values are never embedded in source code. Values must be supplied
by environment/configuration at runtime. This module is intentionally non-trading.
"""
from __future__ import annotations
import os
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

class ConfigurationError(ValueError):
    pass

def required(name: str) -> str:
    value=os.getenv(name)
    if value is None or not value.strip():
        raise ConfigurationError(f"required runtime configuration missing: {name}")
    return value.strip()

def optional_decimal(name: str) -> Optional[Decimal]:
    value=os.getenv(name)
    return Decimal(value) if value and value.strip() else None

@dataclass(frozen=True)
class RuntimeConfig:
    environment: str
    state_store_uri: str
    provider_config_uri: str
    universe_registry_uri: str
    strategy_registry_uri: str
    economic_gate_usd: Decimal
    max_hops: int
    max_candidates_per_cycle: int

    @classmethod
    def from_env(cls) -> "RuntimeConfig":
        gate=optional_decimal("GH_MIN_NET_PROFIT_USD")
        if gate is None:
            raise ConfigurationError("GH_MIN_NET_PROFIT_USD is required")
        return cls(
            environment=required("GH_ENVIRONMENT"),
            state_store_uri=required("GH_STATE_STORE_URI"),
            provider_config_uri=required("GH_PROVIDER_CONFIG_URI"),
            universe_registry_uri=required("GH_UNIVERSE_REGISTRY_URI"),
            strategy_registry_uri=required("GH_STRATEGY_REGISTRY_URI"),
            economic_gate_usd=gate,
            max_hops=int(required("GH_MAX_HOPS")),
            max_candidates_per_cycle=int(required("GH_MAX_CANDIDATES_PER_CYCLE")),
        )
