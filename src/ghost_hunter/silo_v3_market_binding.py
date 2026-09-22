"""Bind enumerated SiloFactory markets to read-only runtime verification.

Every discovered market must pass runtime verification for both vaults before
the market is considered runtime-observed. No execution authority is created.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .registry import RegistryError
from .silo_v3_factory_enumerator import SiloFactoryEvent, SiloFactoryObservation
from .silo_v3_runtime import SiloRuntimeState


class RuntimeVerifier(Protocol):
    def verify(self, network_id: str, silo: str, *, flash_fee_probe_amount: int = 1) -> SiloRuntimeState:
        ...


@dataclass(frozen=True)
class SiloMarketVerification:
    event: SiloFactoryEvent
    silo0_state: SiloRuntimeState
    silo1_state: SiloRuntimeState


@dataclass(frozen=True)
class SiloMarketVerificationBatch:
    markets: tuple[SiloMarketVerification, ...]
    enumerated_market_count: int
    verified_market_count: int
    provider_id: str
    current_complete: bool


class SiloV3MarketBinder:
    """Fail-closed binding from NewSilo discoveries to runtime market state."""

    def __init__(self, verifier: RuntimeVerifier) -> None:
        self.verifier = verifier

    def verify(
        self,
        observation: SiloFactoryObservation,
        *,
        flash_fee_probe_amount: int = 1,
    ) -> SiloMarketVerificationBatch:
        if flash_fee_probe_amount < 0:
            raise RegistryError("probe amount must be non-negative")
        if observation.completeness.event_count != len(observation.events):
            raise RegistryError("event completeness count mismatch")
        if observation.completeness.unique_market_count != len(observation.events):
            raise RegistryError("duplicate market identity already present")
        if not observation.completeness.current_complete:
            raise RegistryError("cannot bind an incomplete factory snapshot")

        verified: list[SiloMarketVerification] = []
        for event in observation.events:
            silo0 = self.verifier.verify(
                observation.completeness.network_id,
                event.silo0,
                flash_fee_probe_amount=flash_fee_probe_amount,
            )
            silo1 = self.verifier.verify(
                observation.completeness.network_id,
                event.silo1,
                flash_fee_probe_amount=flash_fee_probe_amount,
            )
            if silo0.config.lower() != event.silo_config.lower() or silo1.config.lower() != event.silo_config.lower():
                raise RegistryError("runtime SiloConfig disagrees with factory event")
            if {silo0.silo.lower(), silo1.silo.lower()} != {event.silo0.lower(), event.silo1.lower()}:
                raise RegistryError("runtime vault identities disagree with factory event")
            if silo0.provider_id != silo1.provider_id or silo0.provider_id != observation.completeness.provider_id:
                raise RegistryError("provider changed across market verification")
            if silo0.network_id != observation.completeness.network_id or silo1.network_id != observation.completeness.network_id:
                raise RegistryError("runtime verification network mismatch")
            verified.append(SiloMarketVerification(event, silo0, silo1))

        return SiloMarketVerificationBatch(
            markets=tuple(verified),
            enumerated_market_count=observation.completeness.unique_market_count,
            verified_market_count=len(verified),
            provider_id=observation.completeness.provider_id,
            current_complete=True,
        )
