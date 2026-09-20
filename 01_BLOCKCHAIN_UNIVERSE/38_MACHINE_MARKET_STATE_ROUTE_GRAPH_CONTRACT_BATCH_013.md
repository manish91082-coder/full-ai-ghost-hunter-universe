# PHASE 01 MACRO-BATCH 013 — MACHINE-READABLE MARKET STATE + ROUTE GRAPH CONTRACT v001

Date: 21 सितम्बर 2026
Status: INTEGRATED IMPLEMENTATION CONTRACT

## Objective
Convert the ALU/TSU architecture into deterministic machine contracts so collectors, adapters, route builders and the future simulator can operate without schema drift.

## Fresh evidence
Morpho's current API separates market discovery from dynamic state and exposes liquidity, supply, borrow and utilization. Its liquidity endpoint also returns indexed-block metadata. citeturn0search0turn0search2turn0search3
Morpho states its public API has no SLA and recommends fallback mechanisms and avoiding hard dependencies for critical production operations. citeturn0search1
Midnight market discovery uses chain-aware filters for address fields and provides dynamic state separately; its market list is cached for seconds, reinforcing freshness and on-chain revalidation. citeturn0search6turn0search8

## 1. Canonical state envelope
Every collected object must carry:
- object_type
- canonical_id
- network_id/native_network_id
- source
- observed_block
- observed_at
- collector_version
- schema_version
- freshness_deadline
- evidence_ref
- verification_state
- confidence
- raw_payload_hash

No downstream component may silently consume an object missing these fields.

## 2. ALU record
Required:
- atomic_source_id
- protocol/version
- network
- contract/address/program
- asset
- capacity
- fee_model
- callback_model
- repayment_model
- current_capacity
- capacity_block
- capability_state

Capacity must be expressed in asset-native units; normalized USD is secondary metadata.

## 3. TSU record
Required:
- venue_id
- protocol/version
- network
- pool/pair identifier
- pool address or native pool key
- token path
- fee tier
- hook/configuration state where applicable
- reserve/concentrated-liquidity state
- quote state
- gas estimate
- observed block
- freshness deadline

## 4. Route edge contract
Each edge must declare:
token_in -> token_out
venue
pool
amount_in
amount_out
fee
price_impact
state_block
gas_delta
execution_constraints
valid_until

An edge is invalid if its state is stale or its required contract state cannot be verified.

## 5. Route graph
Graph key:
network + token + venue/pool state version

Separate:
- static topology graph
- dynamic state graph

Static graph changes slowly: factories, pools, token relationships, fee tiers, hooks.
Dynamic graph changes rapidly: reserves, ticks, liquidity, quotes, gas, block state.

Only dynamic-valid edges may enter the simulation queue.

## 6. Candidate generation
Candidate:
atomic_source -> token_in -> edge_1 -> edge_2 ... -> token_out == atomic_asset

Minimum viable closed loop:
borrow asset A
→ route A→B
→ route B→C...
→ route ...→A
→ repay source

Multi-hop and multi-venue paths must be bounded by configurable search limits. Coverage metrics must record what was searched.

## 7. Freshness and invalidation
A state object becomes invalid when:
- block advances beyond configured threshold
- pool event changes relevant state
- quote age exceeds max_age
- source reports stale/error
- conflicting providers disagree beyond tolerance
- required contract state cannot be revalidated

Invalidation is event-driven where possible and periodic as fallback.

## 8. Provider trust model
External APIs are discovery/acceleration layers, not final execution authorities.
Critical execution facts:
API → cross-check → direct RPC/on-chain read → deterministic simulation.

Provider failure triggers provider-pool switching, not silent opportunity deletion.

## 9. Route-search controls
Required:
- max_hops
- max_pools
- max_candidate_edges
- max_simulations_per_cycle
- per-network budget
- per-strategy budget
- dedup fingerprint
- priority score
- starvation prevention

The scheduler must record searched_space and pruned_space so exhaustive search is never falsely claimed.

## 10. Completeness metrics
Track:
- network coverage
- venue coverage
- pool coverage
- token coverage
- state freshness coverage
- route-search coverage
- simulation coverage
- failed-provider coverage
- opportunity-rejection reasons

## 11. Morpho adapter requirements
Use API pagination for discovery and state/liquidity endpoints for acceleration, but retain direct chain reads for execution-critical confirmation. Compare API indexed block with local chain head. citeturn0search0turn0search2

## 12. Fail-closed conditions
Reject candidate when:
- atomic capacity unknown
- pool state stale
- route edge unverifiable
- repayment uncertain
- simulation non-deterministic
- gas unknown beyond allowed bound
- required state conflicts
- security gate fails
- expected net profit <= $0.20

## Saturation result
The shared substrate now has explicit machine contracts for:
ALU → TSU → Edge → Graph → Candidate → Simulation.

Implementation can proceed without inventing schemas later.

Live trading: STOP.
