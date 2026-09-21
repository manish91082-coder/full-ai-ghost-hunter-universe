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
\n\n## 19. Phase 01.6 — Dynamic Verification + Final Chain Count Contract\n\nPhase 01.6 introduced the dynamic verification layer and locked the final chain-count methodology.\n\n### Three counters\n- **Discovery Count:** all normalized candidate networks discovered.\n- **Flash Capability Count:** networks with verified atomic flash liquidity.\n- **Executable Flash-Trading Count:** networks with verified flash liquidity plus executable trading venues/routes.\n\nOnly the third count is the final Ghost Hunter universe count.\n\n### Provisional checkpoint\nFresh evidence currently identifies **27 unique network candidates** across Aave, Morpho, Uniswap and Solana Project 0 evidence. The 27 figure is deliberately labelled provisional.\n\n### Final mathematical rule\n**Final Trading Chains = Deduplicated Union of all verified flash-liquidity networks intersected with all verified executable trading networks.**\n\nA final count cannot be accepted until protocol registries, DEX registries and chain branches have explicit closure criteria and candidate records have current evidence, capability state, trading state, conflict state and lifecycle state.\n\n### Non-negotiable\nThe project must never say “all chains = N” merely because N appears in one protocol's deployment list.\n

## 20. Phase 01.6 Batch 002 — Protocol Discovery Expansion

The protocol universe was expanded beyond the initial Aave/Morpho/Uniswap/Project-0 sample. Balancer, Venus, Radiant and Euler EVK/EVC were added as formally evidenced flash-liquidity families. Their network deployments are not yet blindly counted.

The project now treats protocol discovery and network discovery as separate axes. This prevents a deployment on one network from being incorrectly generalized to all networks, and prevents a chain list from being treated as proof of flash-trading capability.

The canonical future artifact is a mechanically generated protocol×network×primitive×deployment×trading-venue matrix.


## 21. Phase 01.6 Batch 003 — Canonical Protocol × Network Matrix

A dedicated matrix has been created at 01_BLOCKCHAIN_UNIVERSE/16_PROTOCOL_NETWORK_MATRIX_BATCH_003_v001.md and audited at 01_BLOCKCHAIN_UNIVERSE/17_AUDIT_008_PROTOCOL_NETWORK_MATRIX.md.

The matrix now records deployment evidence by protocol and network while preserving separate states for flash capability, code, liquidity, venue, route, simulation and economics.

Fresh source evidence:
- Aave current production deployment list. citeturn0search4
- Morpho official 50-chain Morpho Blue address registry. citeturn2view0
- Venus production subgraph deployment set. citeturn3search0
- Euler production network set. citeturn4search0
- Radiant v3 core origin/deposit networks and v1 deprecation. citeturn1search13turn1search5
- Project 0 Solana flashloan/arbitrage semantics. citeturn0search2

### Important Specification Correction
Protocol-specific deployment counts are not additive. Network aliases are normalized and one blockchain is counted once regardless of how many flash-liquidity protocols deploy there.

### Final Count
No final executable chain count is declared yet. The remaining gates are exhaustive protocol/address parsing, direct code verification, current flash capacity, DEX/venue intersection, route verification, deterministic simulation, freshness and conflict reconciliation.

Next controlled artifact: Batch 004 exhaustive deployment registry parsing.


## 22. Phase 01.6 Batch 004 — Morpho 50-Chain Registry Parse
The canonical registry now has a dedicated Morpho parsing artifact. Official documentation declares 50 Morpho Blue chains and exposes network-specific contract addresses. citeturn1view0 27 concrete records were directly parsed in this batch. Remaining 23 rows, chain identifiers, live code, flash capability, liquidity, venue and route verification remain open.


## 23. Phase 01.6 Batch 004B — Morpho 50-Row Canonical Reconciliation
The full Morpho Blue source section has been structurally reconciled into 50 rows. The abscan row is corrected to Abstract; Arbitrum is separately bound to arbiscan. Base Sepolia and Ethereum Sepolia are testnet records. citeturn1view0turn3search1 Production candidate count from this Morpho registry = 48, pending lifecycle and execution verification. This is not the final global chain count.


## 22. Macro-Batch Execution Architecture

The project is upgraded from micro-step progression to maximum-safe macro-batches.

Execution unit: Macro Objective -> Parallel Research -> Normalize -> Verify -> Test -> Audit -> Gap Expansion -> Integrate -> Re-test -> Re-audit -> Saturate -> Freeze.

The 30 roadmap phases are architectural domains. Multiple related phases may be progressed in one macro-batch when dependencies permit. Safety and authorization gates cannot be bypassed.

Authoritative continuation file: 00_GOVERNANCE/CHAT_CONTINUATION_PROTOCOL.md
Execution doctrine: 00_GOVERNANCE/MACRO_BATCH_EXECUTION_DOCTRINE.md

Routine project decisions are owned by the AI project lead. The intended normal user command is next.

Speed is obtained through batch parsing, parallel research, machine-readable registries, precomputed static state, incremental verification, automated audits and event-driven architecture, not by removing quality gates.


## 23. Uniswap Canonical Downstream Model

Uniswap is represented as protocol version × network × contract role × address, followed by code/interface/capability/pool/liquidity/route/simulation/economic/security gates.

V2 flash swap, V3 flash, and V4 PoolManager/hook execution are separate capability flags.

Dynamic pool discovery is a first-class layer. Address equality across networks does not imply network identity.

The project now advances downstream without requiring a separate chat turn for each deployment record.

## 24. Atomic Liquidity + Trading State Substrate

ALU stores atomic liquidity source, capacity, fee, callback and repayment semantics with freshness/evidence.

TSU stores venue, pool, token, fee/hook, reserves/concentrated state, quotes, gas and freshness.

Opportunity composition joins ALU, asset, route graph and TSU, then requires deterministic simulation, economic and risk gates.

The system uses event-driven invalidation plus periodic safety scans.

## 25. Machine Market-State and Route-Graph Contracts

Canonical envelope fields: object type, canonical ID, network, source, observed block/time, collector/schema versions, freshness deadline, evidence, verification state, confidence and raw payload hash.

ALU, TSU and route-edge contracts are defined. Static topology is separated from dynamic state. Route search is bounded and measurable. Provider failure triggers switching/fallback rather than silent opportunity deletion.

## 26. Collector and State Store Foundation

The collector architecture preserves raw evidence, canonical latest state, append-only history, rejection records and coverage metrics. Dynamic objects carry freshness deadlines and indexed block information where available.

Provider health and fallback are first-class. Event-driven refresh is combined with periodic reconciliation and bounded retries.

No collector has live wallet authority.

## 27. First Runnable Collector/State Store Core

The first dependency-light Python core is committed under src/ghost_hunter. It implements state envelopes, evidence hashing, append-only history, rejection/coverage counters and provider health/failover primitives. Deterministic unit-test fixtures are under tests/.

This is non-trading code only.

## 28. Dynamic Execution Requirement

Execution is configuration/data driven. Authoritative runtime universe data is externalized. No strategy/executor source may embed chain lists, RPC URLs, contract addresses, token/pool matrices or strategy inventory as authoritative data.

Runtime configuration is loaded from external inputs and fails closed when critical values are missing. Dynamic registries will later provide current universe and strategy data.

This is a mandatory acceptance gate for all future execution components.

## 29. Dynamic Registry Contract

Macro-Batch 017 converted the dynamic-execution requirement into a machine-level registry boundary.

The source layer defines only schemas and validation. Authoritative runtime universe data must arrive through external/versioned snapshots.

Registry records require:
- registry type;
- canonical ID;
- network ID;
- version;
- source/provenance reference;
- observation timestamp;
- payload hash;
- lifecycle status.

Registry snapshots require a manifest hash and version. Duplicate canonical identities, invalid hashes, invalid lifecycle states and unauthorized versions fail closed.

The registry is not current-state proof. Current on-chain state, freshness and execution-critical facts remain separate verification layers.

### Replay Acceptance Criterion

A valid runtime snapshot substitution must change resulting state/opportunity coverage without changing executable source code.

This becomes a mandatory acceptance gate before execution architecture is allowed to advance toward live authorization.

Live trading remains STOP.


## 30. NO-DRIFT SATURATION CONTROL ARCHITECTURE

Date: 21 September 2026

The project specification is now governed by two permanent artifacts:
- 00_GOVERNANCE/NO_DRIFT_SATURATION_CONTROL_CHARTER_v1.0.md
- 00_GOVERNANCE/SATURATION_GATE_REGISTER_v1.0.md

### Locked progression
G00 Governance is frozen.
G01 Global Blockchain Universe is active and must be saturated before dependent universe domains are treated as authoritative.
G02-G29 are blocked or design-only according to the gate register.

### Chain-wise storage
Each blockchain receives a dedicated namespace with identity, RPC, flash liquidity, protocols, DEX, contracts, ABI, tokens, pools, pairs, liquidity, market state, quotes, routes, strategies, evidence, audits and snapshots.

### Static/dynamic separation
Verified topology and slow-changing facts are precomputed. Current market/execution state remains dynamic and freshness-bound.

### Provider rotation
Provider pools use explicit health states, adaptive cooldown/retest and recovery. Temporary failure is not permanent blacklist. Persistent/security failures may enter quarantine with evidence.

### Performance architecture
Heavy discovery, AI research and historical processing stay off the hot path. The live decision substrate uses precomputed indexes, hot state caches, incremental invalidation and parallel workers. Final latency must be measured under real provider/chain constraints.

### Acceptance rule
No downstream domain is declared saturated merely because files or code exist. Evidence-backed gate closure is mandatory.



## 31. CANONICAL REPOSITORY BOUNDARY

Date: 21 September 2026

The project has one authoritative Git boundary:
`manish91082-coder/full-ai-ghost-hunter-universe` / `main`

This is an architectural/governance boundary, not a convenience preference.

Repository name symmetry, historical repositories, forks and experiments cannot cause repository selection.

Canonical identity must be checked before planning, reading project state for continuation, or writing project artifacts.

## 32. G01 Global Chain Discovery Expansion — Macro-Batch 018

Date: 21 September 2026

G01 discovery coverage was expanded using independent current discovery surfaces. DeFiLlama's DEX-by-chain dataset reports 290 chains, CoinGecko documents 100+ supported on-chain networks, and L2BEAT provides an independent scaling/activity discovery surface. These datasets are deliberately treated as overlapping discovery denominators, not additive chain counts. citeturn0search9turn0search6turn3search8

Batch 018 promoted 21 concrete candidates from discovery signals into individually trackable G01 records. They remain DISCOVERED only.

The next authoritative G01 task is source-union normalization plus primary identity/lifecycle verification, followed by exclusion/retired reconciliation and a final deduplicated discovery counter. Dependent gates remain blocked by governance until G01 is frozen.

## 33. G01 Source-Union Normalization — Macro-Batch 019

Date: 21 September 2026

Machine-readable registry added at 01_BLOCKCHAIN_UNIVERSE/data/G01_SOURCE_UNION_REGISTRY_v001.json.

Macro-Batch 019 reviewed 21 discovery inputs and confirmed 10 overlaps against the current seed/Morpho reconciliation. Eleven remain newly introduced at the current join point, subject to further DEX-derived and native-registry joins.

Primary identity/lifecycle evidence has been strengthened for multiple candidates while keeping unresolved identifiers explicitly partial/unknown. The source-union layer is evidence/provenance only and never execution authorization.

Next G01 layer: union with DEX/native ecosystem registries, full lifecycle and retired-state reconciliation, exclusions, freshness and final deduplicated discovery denominator.
## 34. G01 Native Ecosystem Source Surfaces — Macro-Batch 020

Date: 21 September 2026

Added machine-readable source-surface registry: 01_BLOCKCHAIN_UNIVERSE/data/G01_NATIVE_ECOSYSTEM_SOURCE_SURFACES_v001.json.

The current Cosmos Chain Registry root inspection produced 290 entries and 266 named top-level directories after internal-directory filtering. It also exposes a _non-cosmos source surface. This is source coverage only, not final chain coverage.

Solana Mainnet and TRON Mainnet were added as explicit native execution-model candidates, with testnet exclusion semantics captured. Osmosis, Neutron and dYdX were directly inspected as live/mainnet Cosmos records.

Next authoritative G01 work is full native-registry extraction and union reconciliation, followed by DEX-derived network union and final denominator construction.

## SECTION 35 — G01 NATIVE PRODUCTION EXTRACTION + DEX UNION / MACRO-BATCH 021

The project now contains an externalized manifest defining current discovery inputs and extraction rules for the Cosmos Chain Registry, DeFiLlama chain discovery and DEX-derived protocol-chain discovery. A deterministic Python extraction layer and fixture tests were added. The extractor emits explicit production, non-production, unknown and discovery-only states and deduplicates only on available identity fields. Full source execution and final G01 denominator remain open.


## SECTION 36 — DATA LIFECYCLE / ANTI-DUPLICATION ARCHITECTURE

The project now has two explicit data planes:

1. **Evidence plane:** append-only source observations, hashes, provenance, timestamps/blocks, conflicts and historical snapshots.
2. **Canonical materialized plane:** one deduplicated current record per canonical identity, updated in place.

Git commit history preserves prior canonical states. New full registry files are prohibited for ordinary state evolution. Macro-batch artifacts are delta/audit records and must not reproduce complete datasets.

G01 source-union registry was upgraded in place to v002 with CURRENT_MATERIALIZED_STATE role and canonical record keys. This is a governance correction, not a deletion of historical data.
