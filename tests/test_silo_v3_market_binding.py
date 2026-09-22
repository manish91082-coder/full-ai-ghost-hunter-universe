from dataclasses import replace
import pytest

from ghost_hunter.registry import RegistryError
from ghost_hunter.silo_v3_factory_enumerator import (
    SiloFactoryCompleteness,
    SiloFactoryEvent,
    SiloFactoryObservation,
)
from ghost_hunter.silo_v3_market_binding import SiloV3MarketBinder
from ghost_hunter.silo_v3_runtime import SiloRuntimeState


def _state(network, silo, config, provider="p1"):
    return SiloRuntimeState(
        network_id=network,
        silo=silo,
        config=config,
        silo0="0x" + "3" * 40,
        silo1="0x" + "4" * 40,
        asset="0x" + "5" * 40,
        liquidity=100,
        max_flash_loan=90,
        flash_fee_probe_amount=1,
        flash_fee=1,
        factory="0x" + "6" * 40,
        observed_block=100,
        provider_id=provider,
        silo_bytecode_sha256="a" * 64,
        config_bytecode_sha256="b" * 64,
    )


def _observation():
    network = "eip155:1"
    factory = "0x" + "8" * 40
    config = "0x" + "5" * 40
    silo0 = "0x" + "3" * 40
    silo1 = "0x" + "4" * 40
    event = SiloFactoryEvent(
        network_id=network,
        factory=factory,
        implementation="0x" + "1" * 40,
        token0="0x" + "2" * 40,
        token1="0x" + "7" * 40,
        silo0=silo0,
        silo1=silo1,
        silo_config=config,
        block_number=100,
        transaction_hash="0x" + "b" * 64,
        log_index=0,
    )
    return SiloFactoryObservation(
        events=(event,),
        completeness=SiloFactoryCompleteness(
            network_id=network,
            factory=factory,
            start_block=100,
            end_block=100,
            post_scan_block=100,
            event_count=1,
            unique_market_count=1,
            provider_id="p1",
            current_complete=True,
        ),
    )


class FakeVerifier:
    def __init__(self, mismatch=False, provider="p1"):
        self.mismatch = mismatch
        self.provider = provider
        self.calls = []

    def verify(self, network_id, silo, *, flash_fee_probe_amount=1):
        self.calls.append((network_id, silo, flash_fee_probe_amount))
        config = "0x" + ("9" if self.mismatch else "5") * 40
        return _state(network_id, silo, config, self.provider)


def test_binder_verifies_both_vaults_and_preserves_completeness():
    verifier = FakeVerifier()
    result = SiloV3MarketBinder(verifier).verify(_observation(), flash_fee_probe_amount=123)

    assert result.enumerated_market_count == 1
    assert result.verified_market_count == 1
    assert len(result.markets) == 1
    assert len(verifier.calls) == 2
    assert all(call[2] == 123 for call in verifier.calls)


def test_binder_rejects_runtime_config_mismatch():
    with pytest.raises(RegistryError):
        SiloV3MarketBinder(FakeVerifier(mismatch=True)).verify(_observation())


def test_binder_rejects_incomplete_snapshot():
    observation = _observation()
    observation = replace(
        observation,
        completeness=replace(observation.completeness, current_complete=False),
    )
    with pytest.raises(RegistryError):
        SiloV3MarketBinder(FakeVerifier()).verify(observation)


def test_binder_rejects_provider_switch():
    with pytest.raises(RegistryError):
        SiloV3MarketBinder(FakeVerifier(provider="p2")).verify(_observation())
