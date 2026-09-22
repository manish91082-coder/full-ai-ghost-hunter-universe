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


def _pool():
    return ProviderPool.from_providers([
        ProviderEndpoint("p1", "net:1", "https://runtime.invalid/1", 1),
        ProviderEndpoint("p2", "net:1", "https://runtime.invalid/2", 2),
    ])


def _word(address):
    return "0" * 24 + address[2:]


def test_silo_factory_enumerator_decodes_event_and_requires_current_snapshot():
    from ghost_hunter.silo_v3_factory_enumerator import SiloV3FactoryEnumerator
    from ghost_hunter.runtime_freshness import FreshnessPolicy

    factory = "0x" + "8" * 40
    silo0 = "0x" + "3" * 40
    silo1 = "0x" + "4" * 40
    config = "0x" + "5" * 40
    topic0 = "0x" + "a" * 64

    def opener(request, timeout):
        body = request.data.decode()
        if "eth_blockNumber" in body:
            result = "0x20"
        elif "eth_getLogs" in body:
            result = [{
                "topics": [topic0, _word(factory), _word("0x" + "1" * 40), _word("0x" + "2" * 40)],
                "data": "0x" + _word(silo0) + _word(silo1) + _word(config),
                "blockNumber": "0x20",
                "transactionHash": "0x" + "b" * 64,
                "logIndex": "0x0",
            }]
        else:
            raise AssertionError(body)
        return Response({"jsonrpc": "2.0", "id": 1, "result": result})

    result = SiloV3FactoryEnumerator(
        RpcTransport(_pool(), opener=opener),
        FreshnessPolicy(),
        event_topic0=topic0,
        strict_current=True,
    ).enumerate("net:1", factory, from_block=32, to_block=32)

    assert len(result.events) == 1
    assert result.events[0].silo0.lower() == silo0
    assert result.events[0].silo1.lower() == silo1
    assert result.events[0].silo_config.lower() == config
    assert result.completeness.current_complete is True


def test_silo_factory_enumerator_rejects_duplicate_market_identity():
    from ghost_hunter.silo_v3_factory_enumerator import SiloV3FactoryEnumerator
    from ghost_hunter.runtime_freshness import FreshnessPolicy

    topic0 = "0x" + "a" * 64
    factory = "0x" + "8" * 40
    event = {
        "topics": [topic0, _word("0x" + "1" * 40), _word("0x" + "2" * 40), _word("0x" + "3" * 40)],
        "data": "0x" + _word("0x" + "4" * 40) + _word("0x" + "5" * 40) + _word("0x" + "6" * 40),
        "blockNumber": "0x20",
        "transactionHash": "0x" + "b" * 64,
        "logIndex": "0x0",
    }

    def opener(request, timeout):
        body = request.data.decode()
        if "eth_blockNumber" in body:
            return Response({"jsonrpc": "2.0", "id": 1, "result": "0x20"})
        if "eth_getLogs" in body:
            return Response({"jsonrpc": "2.0", "id": 1, "result": [event, dict(event, logIndex="0x1")]})
        raise AssertionError(body)

    with pytest.raises(RegistryError):
        SiloV3FactoryEnumerator(
            RpcTransport(_pool(), opener=opener),
            FreshnessPolicy(),
            event_topic0=topic0,
        ).enumerate("net:1", factory, from_block=32, to_block=32)


def test_silo_factory_enumerator_rejects_snapshot_advance():
    from ghost_hunter.silo_v3_factory_enumerator import SiloV3FactoryEnumerator
    from ghost_hunter.runtime_freshness import FreshnessPolicy

    topic0 = "0x" + "a" * 64
    factory = "0x" + "8" * 40
    calls = {"blocks": 0}

    def opener(request, timeout):
        body = request.data.decode()
        if "eth_blockNumber" in body:
            calls["blocks"] += 1
            result = "0x20" if calls["blocks"] == 1 else "0x21"
            return Response({"jsonrpc": "2.0", "id": 1, "result": result})
        if "eth_getLogs" in body:
            return Response({"jsonrpc": "2.0", "id": 1, "result": []})
        raise AssertionError(body)

    with pytest.raises(RegistryError):
        SiloV3FactoryEnumerator(
            RpcTransport(_pool(), opener=opener),
            FreshnessPolicy(),
            event_topic0=topic0,
            strict_current=True,
        ).enumerate("net:1", factory, from_block=32, to_block=32)
