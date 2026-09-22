# DATA LIFECYCLE + DEDUPLICATION CONTROL POLICY v1.0

Date: 21 September 2026
Project: FULL AI GHOST HUNTER UNIVERSE
Branch: main
Live trading: STOP

## 1. Core distinction
Historical evidence is append-only. Current canonical/materialized state is deduplicated and updated in place.
Preserve history does NOT mean preserve duplicate current records.
Git history is the primary historical version chain for canonical files.

## 2. One current canonical object
For every major machine-readable domain, exactly one path is authoritative for CURRENT CANONICAL MATERIALIZED STATE.
Do not create registry_v002, registry_v003, final, final2 or latest files for ordinary updates.
Update the canonical state in place after normalization and deduplication.

## 3. Immutable evidence law
Raw evidence is never silently overwritten. Material observations retain source ID, observation time, method, block/version where applicable, payload hash, provenance, freshness and verification state.
Changed evidence becomes a new evidence observation. Conflicting evidence is preserved and marked CONFLICTED until resolved.

## 4. Canonical state law
Canonical state contains one record per canonical identity. Multiple sources attach to one record through evidence/provenance references. It must not contain repeated source copies of the same object.

## 5. Semantic identity law
Deduplication is semantic, not string-only. Prefer authoritative namespace, CAIP-2/native identity, EIP-155 where applicable, verified composite identity, then alias/rebrand evidence. Name similarity alone never proves identity.
Non-EVM identifiers are never coerced into EVM semantics. Different execution planes remain separate only when execution semantics materially differ and routing requires the distinction.

## 6. Example
Five sources identifying one chain produce one canonical chain record plus five provenance references, not five chain records.

## 7. Mandatory update algorithm
DISCOVER → CAPTURE EVIDENCE → HASH → NORMALIZE → IDENTITY RESOLUTION → DEDUPLICATE → MERGE INTO CURRENT CANONICAL STATE → PRESERVE PROVENANCE → RECONCILE CONFLICTS → LIFECYCLE/FRESHNESS → TEST → AUDIT → UPDATE CANONICAL FILE IN PLACE → APPEND CHANGE LOG/AUDIT → COMMIT

A discovery that adds no new object can still be valuable when it confirms a record, refreshes evidence, resolves an alias, changes a verified field, or creates/resolves a conflict.

## 8. Versioning law
Git commits provide full historical versions of canonical files. Record-level history may store first_seen, last_seen, last_verified, previous_state, change_reason and evidence_refs.
Do not create a full duplicate registry for ordinary changes.

## 9. Batch artifact law
Macro-batch reports are delta/audit records, not copies of the full dataset. They record searched scope, additions, merges, changes, retirements, conflicts, unknowns, coverage delta, tests, audit and next gap.

## 10. Existing-file migration
Existing historical files are preserved. If an existing file is the current working registry, upgrade it in place with canonical-role/schema metadata and deduplicated records. Its previous contents remain recoverable through Git history.
Legacy duplicate files are not deleted merely for cleanup. When needed, they are explicitly marked LEGACY/HISTORICAL/NON-AUTHORITATIVE.

## 11. Duplicate classification
EXACT_DUPLICATE = merge provenance, no second canonical object.
ALIAS = attach alias.
REBRAND = preserve historical/current names with evidence.
SAME_NETWORK_DIFFERENT_EXECUTION_PLANE = separate only when technically required.
RELATED_BUT_DISTINCT = separate with relationship.
CONFLICTED_IDENTITY = quarantine until resolved.
FALSE_MATCH = preserve evidence and reject merge.
SUPERSEDED = preserve traceability and relationship.

## 12. File-size law
Do not create unbounded monoliths. Partition by domain, chain/ecosystem, bounded shard or deterministic key range when needed. A global index must map each canonical identity to exactly one owning shard. Partitioning must never duplicate authoritative records.

## 13. Query law
Runtime/research code reads CURRENT CANONICAL STATE plus referenced evidence. Historical snapshots are for replay, audit, change analysis and regression only, never for accidental live candidate inclusion.

## 14. Saturation law
G01 can close only when source coverage, normalization, semantic deduplication, evidence preservation, alias/overlap reconciliation, exclusions/conflicts/unknowns, freshness, reproducible denominator and duplicate-free canonical state all pass audit.

## 15. Mandatory preflight for every next
1. Read latest canonical state.
2. Read latest evidence/change metadata.
3. Detect duplicate/identity anomalies.
4. Never treat old snapshots as current candidates.
5. Search uncovered, stale, conflicted and gap space.
6. Merge findings into current canonical state.
7. Preserve evidence and Git history.
8. Re-run deduplication.
9. Re-test and re-audit.
10. Commit one coherent checkpoint.

## 16. Non-negotiable invariant
Historical evidence may grow. Current canonical truth may change. Current canonical truth may NOT grow by duplication.

This policy is mandatory for every future macro-batch and is subordinate to the No-Drift Saturation Control Charter.
Live execution remains STOP.