# PHASE 01 MACRO-BATCH 012 — UNIFIED ATOMIC LIQUIDITY + MARKET-STATE SUBSTRATE v001

Date: 21 सितम्बर 2026
Status: INTEGRATED DESIGN PASS

## Objective
Stop treating flash liquidity and trading venues as separate lists. Define the canonical substrate that connects atomic liquidity providers to real-time markets, liquidity-at-size, routes and deterministic execution.

## Fresh official evidence
Morpho documents flash loans as same-transaction atomic borrowing with callback and repayment; repayment failure reverts the transaction. citeturn0search0
Morpho's API exposes paginated market discovery, chain filters, loan/collateral filters and real-time state including supplyAssets, borrowAssets, liquidityAssets and utilization. citeturn0search2
Morpho Blue markets are immutable isolated markets defined by loan asset, collateral asset, LLTV, oracle and IRM. citeturn0search1
Morpho Midnight separately exposes flashLoan for arrays of tokens/assets and callback repayment, so it must not be collapsed into the Blue flash capability model. citeturn0search4

## Architectural breakthrough
The engine needs two linked but independent universes:

### A. Atomic Liquidity Universe (ALU)
protocol, version, network, contract, asset, available amount, fee, callback semantics, repayment semantics, current block, freshness, evidence.

### B. Trading State Universe (TSU)
network, venue/version, factory/router/pool manager, pool/pair, token0/token1, fee tier/hook configuration, reserves or concentrated-liquidity state, tick/sqrtPrice where applicable, current block, quote state, gas estimate, freshness, evidence.

## Opportunity composition
An executable opportunity is NOT simply ALU + TSU.

It is:
ALU × Asset × Route Graph × Market State × Atomic Execution Contract × Simulation × Economic Gate × Risk Gate

## Canonical opportunity record
opportunity_id
network
atomic_source
atomic_asset
atomic_capacity
atomic_fee
venue_path[]
pool_path[]
token_path[]
quote_block
quote_timestamp
expected_output
gas_estimate
protocol_fees
slippage_cost
execution_buffer
expected_net_profit_usd
simulation_status
risk_status
freshness_status
authorization_status

## Liquidity-at-size rule
TVL is never used as a substitute for executable liquidity.

For every candidate amount A:
1. source capacity >= A
2. every pool's executable capacity at A
3. price impact / fee / hook effects
4. full atomic-path simulation
5. repayment verification
6. all execution costs
7. expected net profit > USD 0.20

## Freshness model
Every market quote gets observed_block, observed_at, source, latency_ms, max_age_ms and stale=true/false. A stale quote cannot authorize execution.

## Event-driven + periodic hybrid
The final hunter should use block/event triggers, periodic safety scans, a priority queue, normalized opportunity fingerprints, simulation queue, execution queue and post-trade verification. This minimizes missed opportunities without pretending zero opportunity loss can be mathematically guaranteed.

## Morpho market-state adapter
Official API/on-chain data can accelerate discovery and state collection, but execution authorization must revalidate critical values on-chain immediately before transaction construction/submission. The API is an accelerator, not a trust anchor. citeturn0search2turn0search6

## Cross-protocol normalization
The canonical layer must support Aave flash loans, Morpho Blue flash loans, Morpho Midnight flash loans, Balancer Vault liquidity, Uniswap V2 flash swaps, Uniswap V3 flash and Uniswap V4 atomic PoolManager/hook compositions, plus future protocol families.

Protocol adapters may expose richer fields, but the normalized opportunity schema remains stable.

## Critical distinction
available liquidity != borrowable liquidity != route-usable liquidity != profitable liquidity

All four must remain separate.

## Saturation decision
The project now has a canonical bridge:
Global Chain Universe → Atomic Liquidity Universe → Trading State Universe → Route Graph → Candidate Opportunity → Simulation → Economics → Risk → Execution.

## Remaining implementation gates
1. machine-readable ALU schema
2. TSU schema
3. adapter interfaces
4. dynamic pool/state collectors
5. route graph
6. deterministic simulator
7. economics engine
8. freshness/invalidations
9. opportunity scheduler
10. security/authorization gates

Live trading: STOP.
