# G01 CURRENT DEX SOURCE MATERIALIZATION PLAN — MACRO-BATCH 026

Date: 21 September 2026
Live trading: STOP

## Purpose

Close the remaining gap between the DEX extraction contract and an actual
current machine-readable source payload.

## Current verified external facts

The current DeFiLlama DEX chain surface reports 290 chains, while the DEX
dashboard reports 794 DEX protocols. These are discovery metrics only.
The DeFiLlama API documentation identifies the free /protocols endpoint and
documents protocol chain coverage fields. citeturn0search0turn0search1turn0search2

## Materialization design

The runtime/research collector will:

1. fetch the external /protocols payload;
2. capture the exact retrieval timestamp;
3. hash the raw payload;
4. preserve the raw evidence object;
5. filter DEX-class protocol records;
6. emit protocol × chain observations;
7. deduplicate semantically;
8. reconcile against the current 49-record G01 source union;
9. classify overlaps, new candidates, aliases, conflicts and non-chain labels;
10. send unresolved identities to primary verification;
11. keep the dashboard counts as non-authoritative discovery metrics.

## Current limitation

The available web retrieval surface cannot safely materialize the complete
4MB+ /protocols response into this conversation. It therefore would be unsafe
to claim that the complete current DEX denominator has been fetched.

The GitHub tool surface also does not expose an arbitrary command runner. This
batch consequently freezes the reproducible source contract and materialization
plan without fabricating a complete dataset.

## Gate decision

G01 remains ACTIVE / NOT SATURATED.

No downstream gate advances.

Next macro objective:
execute the materialization through the repository's external execution
environment or a supported scheduled/CI runner, then perform full union,
identity, lifecycle and adversarial coverage reconciliation.

Live trading remains STOP.
