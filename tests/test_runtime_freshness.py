import pytest

from src.ghost_hunter.registry import RegistryError
from src.ghost_hunter.rpc_transport import RpcObservation
from src.ghost_hunter.runtime_freshness import (
    FreshnessPolicy,
    parse_hex_block,
    require_revalidated,
    validate_block_numbers,
)


def test_freshness_accepts_small_lag():
    result = validate_block_numbers(100, 102, FreshnessPolicy(max_block_lag=2))
    assert result.lag == 2


def test_stale_observation_fails_closed():
    with pytest.raises(RegistryError):
        validate_block_numbers(100, 103, FreshnessPolicy(max_block_lag=2))


def test_revalidation_requires_same_state():
    previous = RpcObservation("p1", "net:1", "eth_getBalance", "0x10")
    current = RpcObservation("p2", "net:1", "eth_getBalance", "0x10")
    require_revalidated(previous, current)


def test_revalidation_disagreement_fails_closed():
    previous = RpcObservation("p1", "net:1", "eth_getBalance", "0x10")
    current = RpcObservation("p2", "net:1", "eth_getBalance", "0x11")
    with pytest.raises(RegistryError):
        require_revalidated(previous, current)


def test_hex_block_parser():
    assert parse_hex_block("0x2a") == 42
    with pytest.raises(RegistryError):
        parse_hex_block("42")
