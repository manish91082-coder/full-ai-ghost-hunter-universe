# MACRO-BATCH 030 — G01 DEX SOURCE MATERIALIZATION + FILTER CORRECTION

**Date:** 21 September 2026  
**Gate:** G01 Global Blockchain Universe  
**Status:** ACTIVE / NOT SATURATED  
**Live Execution:** STOP

## Objective

Execute the machine-runnable DEX discovery materialization, verify the produced artifact, detect extractor/source-shape defects, correct them, rerun, and preserve evidence.

## Discovery Execution

GitHub Actions run:
- Workflow: `G01 DEX Source Materialization`
- Run ID: `35565925917`
- Head SHA: `2881749310895b8f1696acb15cff7062bcaca476`
- Conclusion: **SUCCESS**
- Artifact ID: `10623718283`
- Artifact digest: `sha256:6435bf77aaafa67fcd79f2a38a06b445674275fe2b2f8509720159eb22aff5da`

## Defect Found and Corrected

The first successful materialization run produced zero DEX rows because the live DeFiLlama payload uses category spelling **`Dexs`**, while the extractor recognized `dex`, `dexes`, `exchange`, `amm`, and `orderbook`.

The live payload was independently inspected before correction:
- 8,315 protocol rows
- category frequency showed **2,106 `Dexs` rows**

Correction:
- Added `dexs` to the machine-readable extractor category set.
- Added `dexs` to the CI materializer category set.
- Updated the fixture to explicitly cover the observed spelling.

## Corrected Materialization Result

The corrected run produced:
- **8,315** source protocol rows
- **2,106** DEX-category rows
- **3,346** unique protocol×chain observations
- **419** unique chain labels observed
- **36** name-level overlaps with the current 49-record G01 source union
- **383** name-level unmatched labels

Raw source:
- bytes: **8,878,272**
- SHA-256: `901e709098d11404dff8dc5afae1decb29d8281155f177169b38e071529a877a`
- retrieved: `2026-09-21T05:48:24.760007+00:00`

## Critical Interpretation

The **419 labels are NOT 419 verified blockchains**.

The 383 unmatched labels are not automatically new canonical networks. They may include:
- aliases
- alternate naming
- execution-plane variants
- non-chain/protocol labels
- legacy or stale labels
- real new networks
- spelling/normalization differences
- networks requiring native identity verification

The 36 overlaps are also only **name-level joins**, not identity proof.

No flash-loan capability, executable venue, liquidity-at-size, route, simulation, economics or execution authorization is inferred.

## Evidence Preservation

A machine-readable evidence manifest has been added:
`01_BLOCKCHAIN_UNIVERSE/data/G01_DEX_MATERIALIZATION_RUN_003_EVIDENCE.json`

The runtime source manifest now records the exact workflow run, artifact digest, raw payload hash, retrieval time and materialization counts.

## Gate Impact

This batch removes the previous **execution-observability blocker** for DEX source materialization.

It does NOT saturate G01.

Remaining G01 work:
1. Normalize 419 observed labels.
2. Semantic identity resolution.
3. Primary lifecycle verification.
4. Reconcile 383 unmatched labels.
5. Search independent/native surfaces for missed networks.
6. Classify aliases/conflicts/non-chain labels.
7. Adversarial missed-network audit.
8. Establish defensible production denominator.
9. Re-test and re-audit before G01 freeze.

## Anti-Drift

**Final goal:** global opportunity coverage  
**Active gate:** G01  
**Completed capability:** reproducible current DEX discovery materialization with evidence/hash and corrected source-shape handling  
**Current blocker:** semantic reconciliation and primary verification  
**Next macro objective:** exhaustive normalization/reconciliation of the 419-label DEX observation surface.

