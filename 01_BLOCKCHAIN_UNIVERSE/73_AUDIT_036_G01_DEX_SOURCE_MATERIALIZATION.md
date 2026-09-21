# AUDIT 036 — G01 DEX SOURCE MATERIALIZATION + FILTER CORRECTION

**Date:** 21 September 2026  
**Gate:** G01  
**Status:** PARTIAL PASS

## Execution Evidence

- [x] Push-triggered GitHub Actions execution observed.
- [x] Workflow completed successfully.
- [x] Artifact exists and is unexpired.
- [x] Artifact digest captured.
- [x] Raw payload extracted from artifact.
- [x] Raw payload SHA-256 independently recomputed.
- [x] Retrieval timestamp captured.
- [x] First-run zero-result condition investigated rather than accepted.
- [x] Live category distribution inspected.
- [x] Extractor/materializer corrected for observed `Dexs` category spelling.
- [x] Corrected CI run completed successfully.
- [x] Corrected artifact contains non-empty protocol×chain observations.
- [x] Discovery-only authority preserved.
- [x] No execution authorization inferred.

## Corrected Result

- Source protocol rows: 8,315
- DEX-category rows: 2,106
- Unique protocol×chain observations: 3,346
- Unique chain labels: 419
- Name-level overlap with current G01 union: 36
- Name-level unmatched labels: 383
- Raw payload SHA-256: `901e709098d11404dff8dc5afae1decb29d8281155f177169b38e071529a877a`

## Adversarial Finding

A superficially successful CI run can still be semantically empty if the source schema evolves or category labels differ from the extractor contract. Therefore CI success is not itself data correctness. The source payload must be inspected, distribution-checked, and reconciled.

## Remaining Gaps

- 419 labels are not verified network identities.
- 383 unmatched labels require semantic reconciliation.
- Primary identity/lifecycle verification remains pending.
- Native ecosystem gap scan remains pending.
- Adversarial missed-network audit remains pending.
- Final production denominator remains pending.
- G01 saturation remains pending.

## Gate Decision

**G01 remains ACTIVE / NOT SATURATED.**

Live execution remains **STOP**.
