# G01 MACHINE-RUNNABLE DEX MATERIALIZATION / MACRO-BATCH 027

**Date:** 21 September 2026  
**Gate:** G01 Global Blockchain Universe  
**Live execution:** STOP

## Objective

Remove the previous materialization bottleneck by adding a reproducible, externalized GitHub Actions path for the public DeFiLlama /protocols discovery payload.

## Preflight

Canonical repository verified:

`manish91082-coder/full-ai-ghost-hunter-universe`

Canonical branch:

`main`

Starting durable checkpoint:

`0e39cc655b1b29ea9ab2fbe056533de1b0804040`

Current canonical G01 source-union target remains one current registry:

`01_BLOCKCHAIN_UNIVERSE/data/G01_SOURCE_UNION_REGISTRY_v001.json`

with 49 records at the prior checkpoint.

## Implemented

### 1. External materializer

Created:

`scripts/materialize_g01_dex.py`

The utility:

- fetches the public DeFiLlama `/protocols` endpoint at runtime;
- records UTC retrieval time;
- computes SHA-256 over the exact raw payload;
- retains the raw JSON as a CI artifact;
- filters DEX-class protocol rows;
- emits protocol × chain observations as JSONL;
- deduplicates observations deterministically;
- produces a machine-readable materialization summary;
- performs only a conservative name-level comparison with the current G01 registry;
- explicitly leaves identity and lifecycle resolution as downstream verification gates;
- never authorizes execution;
- embeds no authoritative runtime chain/address/token/pool/pair/strategy universe.

### 2. CI workflow

Created:

`.github/workflows/g01-dex-materialization.yml`

The workflow supports:

- manual `workflow_dispatch`;
- push-triggered execution when the materializer contract changes;
- read-only repository permissions;
- a bounded 10-minute job;
- artifact upload with 30-day retention.

The workflow is deliberately research-only. It does not modify the canonical registry and does not contain trading credentials or execution permissions.

## Evidence boundary

The workflow provides the missing **external execution path**, but creation of a workflow is not equivalent to successful execution.

The complete payload, payload hash, extracted relationship count and artifact integrity become authoritative only after an actual CI run is observed and audited.

## Saturation impact

This batch removes the architectural blocker:

**PENDING_EXTERNAL_FETCH → EXECUTION_PATH_AVAILABLE**

It does **not** advance G01 to saturated.

Still required:

1. successful CI materialization run;
2. raw payload + SHA-256 evidence retention;
3. complete protocol × chain observation audit;
4. semantic identity/lifecycle verification;
5. reconciliation against the 49-record current canonical union;
6. native-source gap scan;
7. adversarial missed-network audit;
8. final production denominator construction;
9. re-test, re-audit and saturation decision.

## No-drift decision

No second canonical registry was created.

Historical artifacts remain append-only. Current canonical state remains in the existing current path.

## Final state

**G01: ACTIVE / NOT SATURATED**

**G02-G29: BLOCKED**

**Live trading: STOP**