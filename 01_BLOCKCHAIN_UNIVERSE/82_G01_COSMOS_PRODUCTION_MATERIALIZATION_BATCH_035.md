# G01 COSMOS PRODUCTION MATERIALIZATION BATCH 035

Date: 21 September 2026

## Objective

Materialize the current Cosmos Chain Registry production subset through a reproducible CI path, using the pinned upstream Git tree SHA from the preflight observation.

## Control decisions

- Source: official Cosmos Chain Registry.
- Pinned source tree: `810b0b68e4591078295ccce76205e970b3c002e5`.
- Candidate files: paths ending `/chain.json), excluding internal underscore/dot namespaces.
- Production filter: `status == live AND network_type == mainnet`.
- Native `chain_id`, `chain_type`, and network semantics are preserved.
- Non-production observations remain outside the production JSONL and are counted explicitly.
- Fetch errors are explicit and fail the workflow.
- Raw payload hashes and materialization timestamp are retained.
- The artifact is discovery/reconciliation input only.

## Implementation

Added `scripts/materialize_g01_cosmos.py`.

Added `.github/workflows/g01-cosmos-materialization.yml`.

The script retrieves the upstream Git tree, discovers current chain.json paths, fetches each pinned raw payload, applies the production lifecycle filter, emits JSONL production observations, records errors, and produces a deterministic summary with SHA-256 hashes.

## No-drift boundary

This batch does NOT mutate `G01_SOURCE_UNION_REGISTRY_v001.json`. Reconciliation against the current 57-record canonical state occurs only after the CI artifact is independently observed and audited.

## Gate state

G01 remains ACTIVE / NOT SATURATED.

G02-G29 remain BLOCKED.

LIVE TRADING = STOP.

## Next

Observe the CI run and audit its materialization counts, hashes and errors. Then reconcile the production subset against the current canonical G01 source-union without duplicate growth.
