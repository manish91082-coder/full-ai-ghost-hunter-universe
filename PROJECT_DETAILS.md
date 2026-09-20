# 📘 PROJECT DETAILS

## 1. Project Charter

Full AI, autonomous, multi-chain flash-loan trading research and execution system.

**Discover → Verify → Model → Simulate → Gate → Execute → Measure → Learn → Audit → Repeat**

## 2. Target Universe

Blockchain ecosystems with relevant smart-contract execution, flash-loan/atomic-liquidity primitives, trading venues, executable swaps, liquidity and composable paths.

## 3. Static Knowledge Target

Before live hunting, where feasible and verifiable, precompute:
chain IDs, native assets, explorers, RPC candidates, flash-loan deployments, lending/provider addresses, DEX factories/routers/quoters, pool discovery mechanisms, token addresses/decimals, pool/pair addresses, fee tiers, ABI/source references, protocol constraints and deployment metadata.

## 4. Dynamic Data Layer

Live layer includes reserves/liquidity, prices/ticks/state, gas, block height, route availability, quote freshness, provider health and execution latency.

## 5. Strategy Layers

### A — Known
Documented strategies.

### B — Composed
New combinations of verified primitives.

### C — Novel
AI-generated hypotheses requiring formal validation.

## 6. Opportunity Pipeline

**Market Snapshot → Candidate Generation → Route Search → Flash Liquidity Feasibility → Price Impact → Slippage → Gas/Fees → Failure/Revert Risk → Simulation → Net Profit → Safety Gate → Execution Decision**

## 7. Execution Gate

Fresh data + valid addresses/contracts + liquidity + route + flash liquidity + repayment + output + fees + gas + slippage + profit threshold + simulation + transaction validity + provider health.

Critical failure → **DO NOT EXECUTE**.

## 8. Infrastructure

**Free-first → local/open-source → lightweight → distributed only when justified.**

Every free dependency still requires reliability, freshness and rate-limit assessment.

## 9. AI Architecture

Research, evidence, discovery, strategy, route optimization, opportunity detection, simulation analysis, risk, execution supervision, audit/gap and learning agents are planned.

## 10. Operating Doctrine

Authoritative doctrine: `00_GOVERNANCE/OPERATING_DOCTRINE.md`

Core model:

**Mission → Evidence → Architecture → Build → Test → Audit → Saturate → Deploy**

Autonomy is bounded autonomy. Deterministic safety/economic gates remain authoritative.

## 11. Phase 01

Authoritative plan: `01_BLOCKCHAIN_UNIVERSE/PHASE_01_PLAN.md`

Completion requires discovery, normalization, evidence, verification states, conflict handling, gap analysis, recheck and versioned audit.


## 13. Phase 01 Discovery Source Layer

The project now has a dedicated discovery-source layer:

- 01_BLOCKCHAIN_UNIVERSE/01_DISCOVERY_SOURCE_MATRIX.md
- 01_BLOCKCHAIN_UNIVERSE/02_DISCOVERY_BATCH_001.md
- 01_BLOCKCHAIN_UNIVERSE/03_AUDIT_001_SOURCE_DISCOVERY.md

The source hierarchy separates primary/on-chain evidence, authoritative ecosystem datasets and discovery-only aggregators.

## 14. Phase 01 Current State

The discovery methodology has passed its first audit at 99/100. The remaining gap is freshness automation plus construction of the normalized canonical candidate registry.

No factual claim of global blockchain completeness has been made at this stage.


## 15. Phase 01.2 — Canonical Candidate Registry

The first normalized discovery seed is now stored in `01_BLOCKCHAIN_UNIVERSE/04_CANONICAL_CANDIDATE_REGISTRY_v001.md` and audited in `01_BLOCKCHAIN_UNIVERSE/05_AUDIT_002_CANONICAL_REGISTRY.md`.

The registry is intentionally not an executable universe. Chain listing, TVL, protocol deployment or ecosystem membership do not by themselves prove flash-loan capability, atomic composability, executable venue routes or sufficient liquidity.

Required next layer: primary-source identity/lifecycle verification, followed by capability matrices and network-specific address verification.

## 16. Phase 01.3 — Identity + Lifecycle Verification

The project now maintains a dedicated identity/lifecycle verification layer. Verification records capture canonical identity, aliases, execution model, network identifier, environment, lifecycle, evidence timestamp and confidence.

Important architectural correction: the schema is execution-model aware. It does not force every ecosystem into an EVM-style numeric chain-ID model.
 
## 17. Phase 01.4 — Flash-Liquidity Capability Layer

The project now has a dedicated flash-liquidity capability matrix and audit.

The capability model separates:
- protocol deployment;
- flash-loan / flash-swap / flash-mint primitive;
- atomicity;
- callback or instruction ordering;
- repayment semantics;
- fee/capacity configuration;
- liquidity source;
- composability;
- network-specific deployment;
- execution readiness.

Verified sampled patterns include Aave V3, Aave GHO Flashmint, Morpho, Uniswap V2 flash swaps and Solana marginfi/Project 0.

Critical architectural rule: non-EVM atomic primitives are not forced into EVM callback semantics.

Next required layer: network-specific deployment/address verification and liquidity-at-size verification. No live execution is authorized.


## 18. Phase 01.5 — Network Deployment + Address Layer

The project now stores network-specific deployment records instead of protocol names alone.

Required deployment identity is:
**Network + Chain Identifier + Protocol + Version + Contract/Program Role + Address + Source + Timestamp + State**

Aave uses an official maintained address-book registry; Morpho uses its official network-specific address registry; Solana Project 0 uses its official program-address documentation.

The address layer remains fail-closed. Current code, capability, liquidity, fees, permissions, routes, simulation and economics must be revalidated before execution.
