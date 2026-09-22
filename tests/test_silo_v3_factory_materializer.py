from ghost_hunter.silo_v3_factory_materializer import materialization_document, materialize_factories

class C:
    provider_id="p1"; current_complete=True; event_count=1
class E:
    network_id="net:1"; factory="0x"+"8"*40; implementation="0x"+"1"*40
    token0="0x"+"2"*40; token1="0x"+"3"*40; silo0="0x"+"4"*40; silo1="0x"+"5"*40
    silo_config="0x"+"6"*40; block_number=32; transaction_hash="0x"+"a"*64; log_index=0
class O:
    events=(E(),); completeness=C()
class Enum:
    def enumerate(self, network_id, factory, *, from_block):
        assert network_id=="net:1" and from_block==0
        return O()

def test_read_only_observation():
    rows=materialize_factories([{"factory_id":"F1","network_id":"net:1","factory":E.factory,"scan_start_block_inclusive":0}],Enum())
    assert rows[0].status=="ENUMERATED_READ_ONLY"
    assert rows[0].event_count==1

def test_failed_factory_is_incomplete():
    class Bad:
        def enumerate(self,*a,**k): raise RuntimeError("provider unavailable")
    rows=materialize_factories([{"factory_id":"F1","network_id":"net:1","factory":E.factory,"scan_start_block_inclusive":0}],Bad())
    doc=materialization_document(rows,expected_factory_count=1,scan_plan_path="plan.json")
    assert rows[0].status=="FAILED_CLOSED" and doc["overall_status"]=="INCOMPLETE"

def test_invalid_start_block_fails_closed():
    rows=materialize_factories([{"factory_id":"F1","network_id":"net:1","factory":E.factory,"scan_start_block_inclusive":-1}],Enum())
    assert rows[0].status=="FAILED_CLOSED"

def test_missing_denominator_identity_keeps_batch_incomplete():
    rows=materialize_factories([{"factory_id":"F1","network_id":"net:1","factory":E.factory,"scan_start_block_inclusive":0}],Enum())
    doc=materialization_document(rows,expected_factory_count=2,scan_plan_path="plan.json")
    assert doc["overall_status"]=="INCOMPLETE"
