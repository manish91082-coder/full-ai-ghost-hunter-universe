import json

import pytest

from ghost_hunter.registry import RegistryError
from ghost_hunter.provider_registry import ProviderEndpoint
from ghost_hunter.provider_pool import ProviderPool
from ghost_hunter.rpc_transport import RpcTransport


class Response:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return json.dumps(self.payload).encode()


def pool():
    return ProviderPool.from_providers([
        ProviderEndpoint("p1", "net:1", "https://runtime.invalid/1", 1),
        ProviderEndpoint("p2", "net:1", "https://runtime.invalid/2", 2),
    ])


def opener_factory(results):
    def opener(request, timeout):
        return Response(results[request.full_url])
    return opener


def test_read_only_call_returns_observation_and_records_success():
    p = pool()
    opener = opener_factory({
        "https://runtime.invalid/1": {"jsonrpc": "2.0", "id": 1, "result": "0x10"}
    })
    obs = RpcTransport(p, opener=opener).call("net:1", "eth_blockNumber")
    assert obs.result == "0x10"
    assert obs.provider_id == "p1"


def test_failure_rotates_provider():
    p = pool()
    calls = []
    def opener(request, timeout):
        calls.append(request.full_url)
        if request.full_url.endswith("/1"):
            raise OSError("timeout")
        return Response({"jsonrpc": "2.0", "id": 1, "result": "0x11"})
    transport = RpcTransport(p, opener=opener)
    observation = transport.call("net:1", "eth_blockNumber")
    assert observation.provider_id == "p2"
    assert observation.result == "0x11"
    assert calls == ["https://runtime.invalid/1", "https://runtime.invalid/2"]


def test_quorum_disagreement_fails_closed():
    p = pool()
    def opener(request, timeout):
        result = "0x10" if request.full_url.endswith("/1") else "0x11"
        return Response({"jsonrpc": "2.0", "id": 1, "result": result})
    with pytest.raises(RegistryError):
        RpcTransport(p, opener=opener).quorum_call("net:1", "eth_blockNumber", quorum=2)


def test_call_retries_within_same_request_after_provider_failure():
    p = pool()
    calls = []
    def opener(request, timeout):
        calls.append(request.full_url)
        if request.full_url.endswith("/1"):
            raise OSError("timeout")
        return Response({"jsonrpc": "2.0", "id": 1, "result": "0x12"})
    obs = RpcTransport(p, opener=opener).call("net:1", "eth_blockNumber")
    assert obs.provider_id == "p2"
    assert calls == ["https://runtime.invalid/1", "https://runtime.invalid/2"]


def test_quorum_fails_closed_when_provider_capacity_is_insufficient_after_failure():
    p = pool()
    def opener(request, timeout):
        if request.full_url.endswith("/1"):
            raise OSError("timeout")
        return Response({"jsonrpc": "2.0", "id": 1, "result": "0x20"})
    with pytest.raises(RegistryError):
        RpcTransport(p, opener=opener).quorum_call("net:1", "eth_blockNumber", quorum=2)


def test_v2_pair_enumerator_requires_provider_consistency_and_records_completeness():
    from ghost_hunter.v2_pair_enumerator import V2PairEnumerator
    from ghost_hunter.runtime_freshness import FreshnessPolicy

    p = pool()

    def opener(request, timeout):
        body = request.data.decode()
        if "574f2ba3" in body:
            result = "0x" + "1".zfill(64)
        elif "1e3dd18b" in body:
            result = "0x" + "0"*24 + "1234567890abcdef1234567890abcdef12345678"
        elif "eth_blockNumber" in body:
            result = "0x20"
        else:
            result = "0x" + "0"*24 + "1111111111111111111111111111111111111111"
        return Response({"jsonrpc": "2.0", "id": 1, "result": result})

    enumerator = V2PairEnumerator(RpcTransport(p, opener=opener), FreshnessPolicy())
    pairs = enumerator.enumerate_pairs("net:1", "0x" + "1"*40, max_pairs=10)

    assert pairs[0].pair_address.lower() == "0x1234567890abcdef1234567890abcdef12345678"
    assert enumerator.last_completeness is not None
    assert enumerator.last_completeness.factory_reported_count == 1
    assert enumerator.last_completeness.enumerated_count == 1
    assert enumerator.last_completeness.start_block == 32
    assert enumerator.last_completeness.end_block == 32
    assert enumerator.last_completeness.provider_id == "p1"


def test_v2_pair_state_observes_code_and_records_digest():
    from ghost_hunter.v2_pair_enumerator import V2PairEnumerator
    from ghost_hunter.runtime_freshness import FreshnessPolicy

    p = pool()

    def opener(request, timeout):
        body = request.data.decode()
        if "eth_blockNumber" in body:
            result = "0x20"
        elif "eth_getCode" in body:
            result = "0x60016000"
        elif "0dfe1681" in body:
            result = "0x" + "0"*24 + "1"*40
        elif "d21220a7" in body:
            result = "0x" + "0"*24 + "2"*40
        elif "0902f1ac" in body:
            result = "0x" + "1".zfill(64) + "0".zfill(64) + "0".zfill(64)
        else:
            result = "0x"
        return Response({"jsonrpc": "2.0", "id": 1, "result": result})

    state = V2PairEnumerator(RpcTransport(p, opener=opener), FreshnessPolicy()).read_pair_state(
        "net:1", "0x" + "3"*40
    )

    assert state.token0.lower() == "0x" + "1"*40
    assert state.token1.lower() == "0x" + "2"*40
    assert state.reserve0 == 1
    assert state.reserve1 == 0
    assert len(state.bytecode_sha256) == 64


def test_v2_pair_state_fails_closed_on_provider_switch():
    from ghost_hunter.v2_pair_enumerator import V2PairEnumerator
    from ghost_hunter.runtime_freshness import FreshnessPolicy

    p = pool()
    calls = {"count": 0}

    def opener(request, timeout):
        calls["count"] += 1
        body = request.data.decode()
        if calls["count"] == 1:
            result = "0x20"
            return Response({"jsonrpc": "2.0", "id": 1, "result": result})
        if request.full_url.endswith("/1"):
            raise OSError("provider failure")
        return Response({"jsonrpc": "2.0", "id": 1, "result": "0x20"})

    with pytest.raises(RegistryError):
        V2PairEnumerator(
            RpcTransport(p, opener=opener), FreshnessPolicy()
        ).read_pair_state("net:1", "0x" + "3"*40)


def test_v2_pair_enumerator_fails_closed_on_duplicate_factory_pair_identity():
    from ghost_hunter.v2_pair_enumerator import V2PairEnumerator
    from ghost_hunter.runtime_freshness import FreshnessPolicy

    p = pool()

    def opener(request, timeout):
        body = request.data.decode()
        if "574f2ba3" in body:
            result = "0x" + "2".zfill(64)
        elif "1e3dd18b" in body:
            result = "0x" + "0"*24 + "1234567890abcdef1234567890abcdef12345678"
        elif "eth_blockNumber" in body:
            result = "0x20"
        else:
            result = "0x" + "0"*24 + "1111111111111111111111111111111111111111"
        return Response({"jsonrpc": "2.0", "id": 1, "result": result})

    with pytest.raises(RegistryError):
        V2PairEnumerator(
            RpcTransport(p, opener=opener), FreshnessPolicy()
        ).enumerate_pairs("net:1", "0x" + "1"*40, max_pairs=10)


def test_silo_market_discovery_is_deduplicated_and_requires_provenance():
    from ghost_hunter.silo_market_discovery import parse_market_candidates

    payload = {
        "markets": {
            "items": [
                {"id": "market-1", "siloId": "0x" + "1"*40, "chainId": 1},
                {"id": "market-2", "siloId": "0x" + "2"*40, "chainId": 42161},
            ]
        }
    }
    result = parse_market_candidates(payload, provenance="https://api-v3.silo.finance")
    assert len(result) == 2
    assert result[0].source == "SILO_V3_PUBLIC_API_DISCOVERY"


def test_silo_market_discovery_fails_closed_on_duplicate_identity():
    from ghost_hunter.silo_market_discovery import parse_market_candidates

    payload = {
        "markets": [
            {"id": "market-1", "siloId": "0x" + "1"*40, "chainId": 1},
            {"id": "market-1b", "siloId": "0x" + "1"*40, "chainId": 1},
        ]
    }
    with pytest.raises(RegistryError):
        parse_market_candidates(payload, provenance="https://api-v3.silo.finance")
