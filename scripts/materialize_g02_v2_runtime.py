#!/usr/bin/env python3
"""Materialize read-only G02 V2 runtime observations from external providers.

This command is deliberately fail-closed. Missing runtime provider configuration,
provider rotation inside a coherent snapshot, stale blocks, count mismatches, or
invalid pair state abort the materialization. It never signs or submits anything.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from ghost_hunter.provider_registry import load_provider_endpoints
from ghost_hunter.provider_pool import ProviderPool
from ghost_hunter.rpc_transport import RpcTransport
from ghost_hunter.runtime_freshness import FreshnessPolicy
from ghost_hunter.v2_pair_enumerator import V2PairEnumerator


def load_config(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("execution_authority") != "NONE":
        raise RuntimeError("runtime factory config is not observation-only")
    records = data.get("records")
    if not isinstance(records, list) or not records:
        raise RuntimeError("runtime factory config has no records")
    return data


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="02_FLASH_LOAN_UNIVERSE/data/G02_V2_FACTORY_RUNTIME_CONFIG_v001.json")
    ap.add_argument("--output", default="02_FLASH_LOAN_UNIVERSE/data/G02_V2_RUNTIME_OBSERVATION_v001.json")
    ap.add_argument("--max-pairs", type=int, default=100000)
    ap.add_argument("--max-block-lag", type=int, default=2)
    args = ap.parse_args()

    if args.max_pairs < 0 or args.max_block_lag < 0:
        raise RuntimeError("bounds must be non-negative")

    config = load_config(Path(args.config))
    providers = load_provider_endpoints("GH_PROVIDER_RUNTIME")
    pool = ProviderPool.from_providers(providers)
    transport = RpcTransport(pool)
    enumerator = V2PairEnumerator(transport, FreshnessPolicy(args.max_block_lag))

    observations = []
    for record in config["records"]:
        network_id = record["network_id"]
        factory = record["factory"]
        pairs = enumerator.enumerate_pairs(network_id, factory, max_pairs=args.max_pairs)

        states = []
        for pair in pairs:
            state = enumerator.read_pair_state(network_id, pair.pair_address)
            states.append({
                "pair_address": state.pair_address,
                "token0": state.token0,
                "token1": state.token1,
                "reserve0": state.reserve0,
                "reserve1": state.reserve1,
                "observed_block": state.observed_block,
                "provider_id": state.provider_id,
                "bytecode_sha256": state.bytecode_sha256,
            })

        completeness = enumerator.last_completeness
        observations.append({
            "factory_record_id": record["id"],
            "protocol": record["protocol"],
            "network_id": network_id,
            "factory": factory,
            "router": record["router"],
            "provider_id": completeness.provider_id,
            "factory_bytecode_sha256": completeness.factory_bytecode_sha256,
            "start_block": completeness.start_block,
            "end_block": completeness.end_block,
            "factory_reported_count": completeness.factory_reported_count,
            "enumerated_count": completeness.enumerated_count,
            "pair_states": states,
            "status": "OBSERVED_READ_ONLY",
        })

    output = {
        "schema_version": "g02.v2.runtime.observation.v1",
        "canonical_role": "CURRENT_RUNTIME_OBSERVATION_EVIDENCE",
        "execution_authority": "NONE",
        "source_config": args.config,
        "provider_env": "GH_PROVIDER_RUNTIME",
        "observation_count": len(observations),
        "records": observations,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"materialized {len(observations)} V2 factory observations -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
