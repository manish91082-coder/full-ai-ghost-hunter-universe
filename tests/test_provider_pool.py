import pytest

from ghost_hunter.registry import RegistryError
from ghost_hunter.provider_registry import ProviderEndpoint
from ghost_hunter.provider_pool import ProviderPool


def providers():
    return [
        ProviderEndpoint("slow", "fixture:1", "endpoint-slow", 20),
        ProviderEndpoint("fast", "fixture:1", "endpoint-fast", 10),
        ProviderEndpoint("other", "fixture:2", "endpoint-other", 1),
    ]


def test_select_prefers_lowest_priority_when_healthy():
    pool = ProviderPool.from_providers(providers())
    assert pool.select("fixture:1").provider_id == "fast"


def test_failure_cools_provider_and_rotates():
    pool = ProviderPool.from_providers(providers())
    pool.record_failure("fast", "fixture:1", now_tick=10, cooldown_ticks=3, error="timeout")
    assert pool.select("fixture:1", now_tick=10).provider_id == "slow"
    assert [p.provider_id for p in pool.available("fixture:1", now_tick=13)] == ["slow", "fast"]


def test_all_failed_fails_closed():
    pool = ProviderPool.from_providers(providers())
    pool.record_failure("fast", "fixture:1", now_tick=10, cooldown_ticks=5)
    pool.record_failure("slow", "fixture:1", now_tick=10, cooldown_ticks=5)
    with pytest.raises(RegistryError):
        pool.select("fixture:1", now_tick=12)


def test_duplicate_provider_identity_fails_closed():
    rows = [ProviderEndpoint("x", "fixture:1", "a"), ProviderEndpoint("x", "fixture:1", "b")]
    with pytest.raises(RegistryError):
        ProviderPool.from_providers(rows)


def test_unknown_provider_cannot_mutate_health():
    pool = ProviderPool.from_providers(providers())
    with pytest.raises(RegistryError):
        pool.record_failure("unknown", "fixture:1", now_tick=1)


def test_same_provider_id_on_two_networks_has_independent_health():
    rows = [
        ProviderEndpoint("shared", "fixture:1", "endpoint-1", 1),
        ProviderEndpoint("shared", "fixture:2", "endpoint-2", 1),
    ]
    pool = ProviderPool.from_providers(rows)
    pool.record_failure("shared", "fixture:1", now_tick=10, cooldown_ticks=5)
    with pytest.raises(RegistryError):
        pool.select("fixture:1", now_tick=10)
    assert pool.select("fixture:2", now_tick=10).provider_id == "shared"
