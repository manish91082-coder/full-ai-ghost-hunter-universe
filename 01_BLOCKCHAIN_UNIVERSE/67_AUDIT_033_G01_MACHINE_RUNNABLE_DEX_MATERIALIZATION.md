# AUDIT 033 — G01 MACHINE-RUNNABLE DEX MATERIALIZATION

**Date:** 21 September 2026  
**Gate:** G01  
**Status:** PARTIAL PASS

## PASS

- [x] Canonical repository identity preserved.
- [x] Main branch preserved.
- [x] No alternate repository introduced.
- [x] External source URL is runtime-configured by the materializer.
- [x] Raw payload is hashed with SHA-256.
- [x] Raw evidence is retained as a CI artifact.
- [x] DEX filtering is explicit and deterministic.
- [x] Protocol × chain observations are machine-readable.
- [x] Observation deduplication is deterministic.
- [x] Current canonical registry is read-only during materialization.
- [x] Identity/lifecycle are not inferred from DEX labels.
- [x] No authoritative runtime universe is embedded in the new materializer.
- [x] Workflow has no trading credentials or execution permission.
- [x] Workflow does not mutate canonical project state.

## NOT YET VERIFIED

- [ ] Successful CI execution observed.
- [ ] Exact raw `/protocols` payload captured and independently audited.
- [ ] Payload hash independently recorded in the project evidence plane.
- [ ] Complete DEX protocol × chain denominator reconciled.
- [ ] All unmatched chain labels identity-resolved.
- [ ] Lifecycle/production status primary-verified.
- [ ] Native-source gap scan completed.
- [ ] Adversarial missed-network audit completed.
- [ ] Final deduplicated G01 production denominator frozen.

## Important distinction

A GitHub Actions workflow being present proves that a reproducible execution path exists. It does **not** prove that the external source was successfully fetched or that the resulting dataset is complete.

Therefore this audit intentionally does not claim materialization success.

## Safety

Live execution remains **STOP**.

## Gate decision

**G01 remains ACTIVE / NOT SATURATED.**

The next macro-batch must inspect the first available CI execution result and, if successful, promote its raw payload/hash/relationship outputs into the evidence and reconciliation pipeline.