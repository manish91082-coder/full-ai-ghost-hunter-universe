import io
import json

import pytest

from src.ghost_hunter.registry import RegistryError
from src.ghost_hunter.provider_registry import ProviderEndpoint
from src.ghost_hunter.provider_pool import ProviderPool
from src.ghost_hunter.rpc_transport import RpcTransport


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
    with pytest.raises(RegistryError):
        transport.call("net:1", "eth_blockNumber")
    assert transport.call("net:1", "eth_blockNumber").provider_id == "p2"
    assert calls == ["https://runtime.invalid/1", "https://runtime.invalid/2"]


def test_quorum_disagreement_fails_closed():
    p = pool()
    def opener(request, timeout):
        result = "0x10" if request.full_url.endswith("/1") else "0x11"
        return Response({"jsonrpc": "2.0", "id": 1, "result": result})
    with pytest.raises(RegistryError):
        RpcTransport(p, opener=opener).quorum_call("net:1", "eth_blockNumber", quorum=2)
