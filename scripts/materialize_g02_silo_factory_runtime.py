#!/usr/bin/env python3
"""Materialize the bounded SiloFactory/NewSilo runtime denominator."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from ghost_hunter.provider_pool import ProviderPool
from ghost_hunter.provider_registry import load_provider_endpoints
from ghost_hunter.registry import RegistryError
from ghost_hunter.rpc_transport import RpcTransport
from ghost_hunter.runtime_freshness import FreshnessPolicy
from ghost_hunter.silo_v3_factory_enumerator import SiloV3FactoryEnumerator
from ghost_hunter.silo_v3_factory_materializer import NEWSILO_TOPIC0, materialization_document, materialize_factories

def load_scan_plan(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != "g02.silo.factory.scan.plan.v2":
        raise RegistryError("unsupported SiloFactory scan-plan schema")
    records = data.get("records")
    if not isinstance(records, list) or not records:
        raise RegistryError("scan plan has no records")
    if data.get("execution_authority") not in (None, "NONE"):
        raise RegistryError("scan plan cannot grant execution authority")
    return data

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan-plan", default="02_FLASH_LOAN_UNIVERSE/data/G02_SILO_FACTORY_SCAN_PLAN_v001.json")
    ap.add_argument("--output", default="02_FLASH_LOAN_UNIVERSE/data/G02_SILO_FACTORY_RUNTIME_OBSERVATION_v001.json")
    ap.add_argument("--max-block-lag", type=int, default=2)
    ap.add_argument("--chunk-size", type=int, default=100_000)
    ap.add_argument("--stop-on-error", action="store_true")
    args = ap.parse_args()
    if args.max_block_lag < 0 or args.chunk_size <= 0:
        raise RegistryError("invalid runtime bounds")
    plan = load_scan_plan(Path(args.scan_plan))
    providers = load_provider_endpoints("GH_PROVIDER_RUNTIME")
    transport = RpcTransport(ProviderPool.from_providers(providers))
    enumerator = SiloV3FactoryEnumerator(
        transport, FreshnessPolicy(args.max_block_lag),
        event_topic0=NEWSILO_TOPIC0, chunk_size=args.chunk_size, strict_current=True)
    results = materialize_factories(plan["records"], enumerator, stop_on_error=args.stop_on_error)
    document = materialization_document(results, expected_factory_count=len(plan["records"]), scan_plan_path=args.scan_plan)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"overall_status={document['overall_status']} materialized={document['materialized_factory_count']}/{document['expected_factory_count']} -> {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
