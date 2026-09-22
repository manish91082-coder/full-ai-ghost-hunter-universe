# MACRO-BATCH 014 — COLLECTOR + NORMALIZED STATE STORE FOUNDATION

Date: 21 Sept 2026

## Objective
Turn the frozen ALU/TSU contracts into a production-oriented collector/state-store foundation without authorizing live execution.

## Evidence-driven design
Morpho's API provides cursor-paginated market discovery, separate dynamic state/liquidity endpoints, and indexed-block metadata. The API has no SLA, so collectors require fallback paths. citeturn0search0turn0search1turn0search3

## Collector pipeline
SOURCE
→ FETCH
→ RAW CAPTURE
→ SCHEMA VALIDATION
→ NORMALIZE
→ IDENTITY/DEDUP
→ FRESHNESS CHECK
→ CROSS-SOURCE CHECK
→ STATE STORE
→ CHANGE EVENT
→ ROUTE GRAPH INVALIDATION

## Required stores
1. Raw Evidence Store: immutable payload + hash + source + retrieval time.
2. Canonical State Store: normalized latest state.
3. History Store: append-only state transitions.
4. Rejection Store: invalid/stale/conflicting records and reason.
5. Coverage Store: discovered, collected, verified, failed, skipped and pruned counts.

## Canonical state lifecycle
DISCOVERED → FETCHED → VALIDATED → NORMALIZED → FRESH → VERIFIED
or
REJECTED / STALE / CONFLICT / UNAVAILABLE

No rejected state may silently become valid.

## Idempotency
Every ingestion operation uses deterministic identity:
network + protocol/version + object role + native identifier/address.
Repeated fetches update state history, never create duplicate logical objects.

## Freshness
Freshness is object-specific. Each record has observed_block, observed_at and freshness_deadline. A state crossing its deadline is automatically invalidated.

## Provider pool
Each source adapter must expose:
- primary
- fallback list
- health
- latency
- error rate
- last-success
- rate-limit state

Provider failure causes controlled switching and records the event.

## Cross-source disagreement
If critical fields disagree:
1. normalize formats
2. compare observed blocks/timestamps
3. prefer newer independently verified state only when policy permits
4. otherwise mark CONFLICT
5. do not authorize downstream execution

## Morpho-specific adapter
Use cursor pagination for Blue markets. Dynamic state and liquidity are separate fetches. Compare API indexed block with chain head. Do not replace missing state with zero. Morpho's own guidance shows some critical state still requires RPC and that REST responses may span indexed blocks. citeturn0search4turn0search7

Midnight state is similarly separated from immutable market configuration and exposes last indexed block. citeturn0search8turn0search10

## Performance architecture
- async collection
- per-network queues
- per-provider concurrency limits
- batch reads where safe
- cache immutable metadata
- event-driven refresh for dynamic objects
- periodic reconciliation
- backpressure
- bounded retries
- circuit breakers

## Zero-cost principle
Prefer public/free RPC and APIs, then distributed provider pool, then local/open-source infrastructure. Paid infrastructure is not a prerequisite for the architecture.

## Safety
This batch creates no wallet authority and no live execution path.

Live trading: STOP.
