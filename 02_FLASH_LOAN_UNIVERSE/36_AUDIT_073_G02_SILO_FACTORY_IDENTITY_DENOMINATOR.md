# AUDIT 073 — G02 SILO FACTORY IDENTITY DENOMINATOR

Date: 22 September 2026
Gate: G02 — Atomic / Flash Liquidity Universe
Result: PASS FOR BOUNDED FACTORY-IDENTITY DENOMINATOR / G02 CONTINUE

## What closed

The project now materializes the Silo primary-source factory identity denominator from Silo's own SiloFactoryList.md.

- 13 EVM networks are represented.
- 37 SiloFactory contract identities are represented.
- Per-network source order is retained as provenance only.
- No historical start block is invented.
- No SiloFactory ID is inferred from event/log order.
- The NewSilo event signature and derived topic0 are fixed in the registry validator.
- Canonical factory identity is (network_id, factory) and duplicate identities fail closed.
- A scan plan can only be built when the caller supplies an explicit historical start block for every factory and no extras.

## Why this matters

Silo documents that markets are permissionless, multiple factories can exist over the lifecycle of a chain, and older factories can remain active. Therefore a five-network current-version list is insufficient for market discovery, and a single latest factory is not a complete historical denominator.

The primary source also states that scanning NewSilo events across all factories yields the market/pool discovery surface. The project therefore separates:

factory identity denominator -> explicit historical event range -> NewSilo market candidates -> runtime SiloConfig/silo0/silo1 verification -> current liquidity/fee/authorization/freshness

## What is still open

This artifact does not claim that 37 is a permanently exhaustive global truth. It is the current bounded denominator exposed by the cited primary Silo source. Reconciliation against future source changes, newly published factories, production event ranges, runtime code, implementation/proxy authenticity, hooks/oracles, executable liquidity at trade size and actual flash-fee quotes remains mandatory.

Production RPC observation was not claimed by this batch. Execution authority remains NONE and live trading remains STOP.

## Evidence

Primary source: https://github.com/silo-finance/silo-contracts-v3/blob/develop/silo-core/docs/SiloFactoryList.md
Source commit inspected: 564fcf86f6e64171f2f7f9402d50ad63d2b54c83

The source explicitly lists SiloFactory contracts per chain, notes that older factories stay active, and gives the NewSilo event structure used by the scan boundary.

## Validation boundary

Deterministic tests verify 37/13 counts, duplicate network/factory rejection, strict explicit start-block coverage and no implicit range inference.

## Gate decision

Continue G02. Do not advance G03.


## POST-CHANGE EXACT-SHA VERIFICATION — 22 September 2026

Current main SHA: 2d8d9379c1f3267d10e02c7a00b66386d5140a3b
data-plane-ci run 35726250434: completed / SUCCESS.
data-plane job data-plane-validation 106740492243: completed / SUCCESS; all listed steps completed successfully, including G02 machine-readable state validation and repository tests.
project-execution-verifier run 35726273234: completed / SUCCESS.
Verifier job verify 106740574598: completed / SUCCESS.
Both workflow runs have head_sha exactly equal to current main SHA.
Execution authority remains NONE; live trading remains STOP.