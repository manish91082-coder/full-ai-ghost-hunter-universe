from dataclasses import dataclass

from ghost_hunter.v2_factory_materializer import (
    materialization_document,
    materialize_v2_factories,
)
from ghost_hunter.v2_pair_enumerator import (
    EnumerationCompleteness,
    PairDiscovery,
    PairState,
)


@dataclass
class FakeEnumerator:
    last_completeness: EnumerationCompleteness

    def enumerate_pairs(self, *args, **kwargs):
        return [
            PairDiscovery(
                network_id="eip155:137",
                factory="0x" + "8" * 40,
                pair_index=0,
                pair_address="0x" + "1" * 40,
                provider_id="p1",
                observed_block=100,
            )
        ]

    def read_pair_state_at_block(self, network_id, pair, snapshot_block, *, provider_id=None):
        assert network_id == "eip155:137"
        assert pair == "0x" + "1" * 40
        assert snapshot_block == 100
        assert provider_id == "p1"
        return PairState(
            pair_address=pair,
            token0="0x" + "2" * 40,
            token1="0x" + "3" * 40,
            reserve0=10,
            reserve1=20,
            observed_block=100,
            provider_id="p1",
            bytecode_sha256="abc",
        )


def _complete_enumerator():
    return FakeEnumerator(
        EnumerationCompleteness(
            network_id="eip155:137",
            factory="0x" + "8" * 40,
            factory_reported_count=1,
            enumerated_count=1,
            start_block=99,
            end_block=100,
            provider_id="p1",
            factory_bytecode_sha256="factorysha",
        )
    )


def test_complete_read_only_materialization():
    rows = materialize_v2_factories(
        [
            {
                "id": "V2",
                "protocol": "QuickSwap",
                "network_id": "eip155:137",
                "factory": "0x" + "8" * 40,
            }
        ],
        _complete_enumerator(),
        max_pairs=10,
    )
    assert rows[0].status == "RUNTIME_VERIFIED_READ_ONLY"
    assert rows[0].enumerated_count == 1
    assert rows[0].observed_block == 100
    assert rows[0].states[0]["observed_block"] == 100
    assert materialization_document(
        rows, expected_factory_count=1, max_pairs=10
    )["overall_status"] == "COMPLETE"


def test_failure_is_incomplete():
    class Bad:
        def enumerate_pairs(self, *args, **kwargs):
            raise RuntimeError("rpc unavailable")

    rows = materialize_v2_factories(
        [
            {
                "id": "V2",
                "protocol": "QuickSwap",
                "network_id": "eip155:137",
                "factory": "0x" + "8" * 40,
            }
        ],
        Bad(),
        max_pairs=10,
    )
    assert rows[0].status == "FAILED_CLOSED"
    assert materialization_document(
        rows, expected_factory_count=1, max_pairs=10
    )["overall_status"] == "INCOMPLETE"


def test_snapshot_mismatch_fails_closed():
    class BadSnapshot(FakeEnumerator):
        def read_pair_state_at_block(self, *args, **kwargs):
            raise RuntimeError("snapshot drift")

    rows = materialize_v2_factories(
        [
            {
                "id": "V2",
                "protocol": "QuickSwap",
                "network_id": "eip155:137",
                "factory": "0x" + "8" * 40,
            }
        ],
        BadSnapshot(_complete_enumerator().last_completeness),
        max_pairs=10,
    )
    assert rows[0].status == "FAILED_CLOSED"
