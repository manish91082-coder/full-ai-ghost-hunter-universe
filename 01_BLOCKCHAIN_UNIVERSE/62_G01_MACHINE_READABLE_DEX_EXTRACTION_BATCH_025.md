# G01 MACHINE-READABLE DEX EXTRACTION AND RELATIONSHIP CONTRACT, MACRO-BATCH 025

Date: 21 September 2026
Repository: manish91082-coder/full-ai-ghost-hunter-universe
Branch: main
Live trading: STOP

## Objective

Convert the DEX discovery surface into a repeatable machine-readable extraction
contract while preserving the boundary between discovery, identity, lifecycle,
execution capability, liquidity, routes, simulation, economics and authorization.

## Evidence basis

DeFiLlama API documentation identifies /protocols as the free endpoint for
listing protocols and documents chains as the multi-chain protocol coverage
field. Independent examples show multi-chain protocols carrying multiple chain
values. This is discovery evidence, not execution eligibility. See cited web
sources in the audit trail.

## Implemented capability

Added:
- src/ghost_hunter/g01_dex_extractor.py
- tests/test_g01_dex_extractor.py

The extractor accepts external protocol payloads, filters DEX-classified rows,
emits typed protocol-to-chain observations, preserves source/evidence metadata,
rejects empty/non-string chain labels, deduplicates repeated observations and
keeps source chain IDs as observations only.

It never infers flash liquidity, production status, executable trading,
liquidity, profitability or permission.

## Identity law

Aliases are not resolved here. Non-EVM identifiers are not fabricated.
Protocol names are never promoted to chain identities. Identity and lifecycle
remain downstream evidence gates.

## Current-source execution state

Code-level fixture tests are defined. A live repository-wide test run and
complete current remote payload materialization are NOT claimed because the
available GitHub execution surface has no arbitrary command runner.

Machine extraction capability: IMPLEMENTED.
Current full DEX row materialization: PENDING.
Complete relationship denominator: PENDING.
Primary identity/lifecycle verification: PENDING.
Final production denominator: PENDING.
G01 saturation: NOT SATURATED.

## Next macro objective

Materialize the current DEX protocol × chain relationship dataset, join it
against the 49-record source union, resolve identity/lifecycle with primary
evidence, preserve exclusions/conflicts, then run the adversarial missed-network
audit.

Live trading remains STOP.
