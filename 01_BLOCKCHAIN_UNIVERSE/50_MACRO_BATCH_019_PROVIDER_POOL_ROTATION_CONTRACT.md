# MACRO-BATCH 019 — PROVIDER POOL ROTATION CONTRACT

Date: 21 September 2026

## Objective
Turn the runtime provider abstraction into a deterministic, fail-closed provider pool contract without embedding any provider universe.

## Implemented
- runtime-supplied provider identities only;
- per-network selection;
- health-aware deterministic ordering;
- failure cooldown and rotation;
- success recovery;
- empty/all-unavailable pool fails closed;
- duplicate provider identity rejected;
- no network I/O in the policy layer.

## Safety
A provider failure must not silently become an opportunity loss or an unsafe fallback. The pool exposes deterministic next-provider selection; the caller must re-query/validate the same runtime state after switching provider.

Provider switching does NOT imply state continuity. Block/state freshness, response provenance and request-level consistency remain caller obligations.

## Not implemented
- live RPC transport;
- endpoint discovery;
- quorum/cross-provider response comparison;
- block-height freshness enforcement;
- automatic opportunity rescan;
- private-key or transaction handling.

G02 remains ACTIVE / NOT SATURATED. Execution authority NONE. Live trading STOP.
