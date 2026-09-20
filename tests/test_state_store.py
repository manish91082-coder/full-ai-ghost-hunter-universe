from src.ghost_hunter.state_store import AppendOnlyStateStore, StateRecord, make_envelope
from src.ghost_hunter.collector import Collector, ProviderPool

def test_append_only_history():
    store = AppendOnlyStateStore()
    for block, amount, evidence in [(1,"1000","ev1"),(2,"1200","ev2")]:
        p={"chain_id":8453,"market_id":"m1","liquidity":amount}
        e=make_envelope(object_type="TSU",canonical_id="base:m1",network_id="8453",source="fixture",payload=p,observed_block=block,freshness_deadline="2099-01-01T00:00:00Z",evidence_ref=evidence)
        store.put(StateRecord(e,p))
    assert store.current("base:m1").payload["liquidity"]=="1200"
    assert len(store.history("base:m1"))==2
    assert store.history("base:m1")[0].payload["liquidity"]=="1000"

def test_provider_failover():
    pool=ProviderPool(["rpc-a","rpc-b"])
    pool.mark("rpc-a",healthy=False)
    assert [p.name for p in pool.ordered()]==["rpc-b"]

def test_collector_ingestion():
    store=AppendOnlyStateStore()
    c=Collector(store,ProviderPool(["fixture"]))
    r=c.ingest(object_type="TSU",canonical_id="x",network_id="1",source="fixture",payload={"x":1},observed_block=1,freshness_deadline="2099-01-01T00:00:00Z",evidence_ref="ev")
    assert r.accepted and store.coverage()["accepted"]==1

def test_missing_state_is_not_zero():
    assert AppendOnlyStateStore().current("missing") is None
