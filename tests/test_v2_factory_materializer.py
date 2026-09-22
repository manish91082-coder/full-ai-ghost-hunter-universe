from ghost_hunter.v2_factory_materializer import materialize_v2_factories,materialization_document
class C: factory_reported_count=1; enumerated_count=1; provider_id="p1"; end_block=100
class P: pair_address="0x"+"1"*40
class S: pair_address=P.pair_address; token0="0x"+"2"*40; token1="0x"+"3"*40; reserve0=10; reserve1=20; observed_block=100; provider_id="p1"; bytecode_sha256="abc"
class E:
 last_completeness=C()
 def enumerate_pairs(self,*a,**k): return [P()]
 def read_pair_state_at_block(self,*a,**k): return S()
def test_complete_read_only_materialization():
 rows=materialize_v2_factories([{"id":"V2","protocol":"QuickSwap","network_id":"eip155:137","factory":"0x"+"8"*40}],E(),max_pairs=10)
 assert rows[0].status=="RUNTIME_VERIFIED_READ_ONLY" and rows[0].enumerated_count==1
 assert rows[0].observed_block==100
 assert rows[0].states[0]["observed_block"]==100
 assert materialization_document(rows,expected_factory_count=1,max_pairs=10)["overall_status"]=="COMPLETE"
def test_failure_is_incomplete():
 class Bad:
  def enumerate_pairs(self,*a,**k): raise RuntimeError("rpc unavailable")
 rows=materialize_v2_factories([{"id":"V2","protocol":"QuickSwap","network_id":"eip155:137","factory":"0x"+"8"*40}],Bad(),max_pairs=10)
 assert rows[0].status=="FAILED_CLOSED"
 assert materialization_document(rows,expected_factory_count=1,max_pairs=10)["overall_status"]=="INCOMPLETE"
def test_snapshot_mismatch_fails_closed():
 class BadSnapshot(E):
  def read_pair_state_at_block(self,*a,**k):
   raise RuntimeError("snapshot drift")
 rows=materialize_v2_factories([{"id":"V2","protocol":"QuickSwap","network_id":"eip155:137","factory":"0x"+"8"*40}],BadSnapshot(),max_pairs=10)
 assert rows[0].status=="FAILED_CLOSED"
