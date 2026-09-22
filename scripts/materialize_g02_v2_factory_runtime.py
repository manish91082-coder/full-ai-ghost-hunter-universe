#!/usr/bin/env python3
"""Materialize configured V2 factory/pair state using GH_PROVIDER_RUNTIME."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from ghost_hunter.provider_pool import ProviderPool
from ghost_hunter.provider_registry import load_provider_endpoints
from ghost_hunter.rpc_transport import RpcTransport
from ghost_hunter.runtime_freshness import FreshnessPolicy
from ghost_hunter.v2_pair_enumerator import V2PairEnumerator
from ghost_hunter.v2_factory_materializer import materialize_v2_factories,materialization_document
def main()->int:
 ap=argparse.ArgumentParser(); ap.add_argument("--config",default="02_FLASH_LOAN_UNIVERSE/data/G02_V2_FACTORY_RUNTIME_CONFIG_v001.json"); ap.add_argument("--output",default="02_FLASH_LOAN_UNIVERSE/data/G02_V2_FACTORY_RUNTIME_OBSERVATION_v001.json"); ap.add_argument("--max-pairs",type=int,default=1_000_000); ap.add_argument("--max-block-lag",type=int,default=2); a=ap.parse_args()
 plan=json.loads(Path(a.config).read_text(encoding="utf-8"))
 if plan.get("execution_authority") not in (None,"NONE"): raise RuntimeError("config cannot grant execution authority")
 providers=load_provider_endpoints("GH_PROVIDER_RUNTIME"); transport=RpcTransport(ProviderPool.from_providers(providers)); enum=V2PairEnumerator(transport,FreshnessPolicy(a.max_block_lag))
 rows=materialize_v2_factories(plan["records"],enum,max_pairs=a.max_pairs); doc=materialization_document(rows,expected_factory_count=len(plan["records"]),max_pairs=a.max_pairs)
 out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(doc,indent=2,sort_keys=True)+"
",encoding="utf-8"); print(f"overall_status={doc['overall_status']} materialized={doc['materialized_factory_count']}/{doc['expected_factory_count']}"); return 0
if __name__=="__main__": raise SystemExit(main())
