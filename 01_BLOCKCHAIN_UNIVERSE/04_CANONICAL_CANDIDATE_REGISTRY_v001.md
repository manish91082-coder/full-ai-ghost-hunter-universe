# 🌐 PHASE 01.2 — CANONICAL BLOCKCHAIN CANDIDATE REGISTRY v001

**Project:** FULL AI GHOST HUNTER UNIVERSE  
**Repository:** `manish91082-coder/full-ai-ghost-hunter-universe`  
**Branch:** `main`  
**Date:** 21 सितम्बर 2026  
**State:** CANDIDATE REGISTRY v001 / NOT YET CAPABILITY-VERIFIED  
**Live trading:** 🛑 STOP

## 1. Purpose

यह file Phase 01 के discovery layer को एक **normalized, deduplicated, auditable candidate registry** में बदलती है।

यह registry:
- global completeness का दावा नहीं करती;
- discovery candidate और verified execution universe को अलग रखती है;
- chain identity, ecosystem family और evidence state को अलग रखती है;
- बाद की flash-liquidity, venue, contract, liquidity और execution verification के लिए canonical input है।

## 2. Canonical State Model

`DISCOVERED → NORMALIZED → IDENTITY_CHECKED → CAPABILITY_PENDING → FLASH_LIQUIDITY_PENDING → VENUE_PENDING → EXECUTION_PENDING → VERIFIED / PARTIALLY_VERIFIED / NOT_ELIGIBLE / UNKNOWN`

**Fail-closed rule:** कोई candidate केवल नाम, TVL, DEX presence या aggregator listing के आधार पर executable universe में प्रवेश नहीं करेगा।

## 3. Evidence Classes

- **E1:** official chain/protocol documentation or verified on-chain evidence
- **E2:** authoritative ecosystem dataset
- **E3:** independent corroboration
- **E4:** discovery-only aggregator/search signal

E4 अकेला execution proof नहीं है।

## 4. Candidate Registry v001

| ID | Canonical candidate | Family | Execution model | Current registry state | Primary discovery evidence | Capability state | Next verification |
|---|---|---|---|---|---|---|---|
| BC-001 | Ethereum | EVM / L1 | EVM | DISCOVERED | DeFiLlama chains; official Ethereum docs | UNKNOWN | chain identity + flash liquidity + venues |
| BC-002 | BNB Chain | EVM / L1 | EVM | DISCOVERED | DeFiLlama chains | UNKNOWN | identity + flash liquidity + venues |
| BC-003 | Polygon PoS | EVM / L1 | EVM | DISCOVERED | DeFiLlama; L2BEAT ecosystem data | UNKNOWN | identity + flash liquidity + venues |
| BC-004 | Avalanche C-Chain | EVM / L1 | EVM | DISCOVERED | DeFiLlama; Aave deployments | PARTIAL | verify current flash-liquidity + venues |
| BC-005 | Arbitrum One | Ethereum L2 | EVM | DISCOVERED | L2BEAT; DeFiLlama | PARTIAL | flash liquidity + executable venue graph |
| BC-006 | OP Mainnet | Ethereum L2 | EVM | DISCOVERED | L2BEAT; DeFiLlama | PARTIAL | flash liquidity + venue graph |
| BC-007 | Base | Ethereum L2 | EVM | DISCOVERED | L2BEAT; DeFiLlama | PARTIAL | flash liquidity + venue graph |
| BC-008 | zkSync Era | Ethereum L2 | EVM | DISCOVERED | L2BEAT; Aave deployments | PARTIAL | execution model + flash liquidity |
| BC-009 | Linea | Ethereum L2 | EVM | DISCOVERED | DeFiLlama; Aave deployments | PARTIAL | flash liquidity + venue graph |
| BC-010 | Scroll | Ethereum L2 | EVM | DISCOVERED | L2BEAT; Aave deployments | PARTIAL | flash liquidity + venue graph |
| BC-011 | Gnosis Chain | EVM / L1 | EVM | DISCOVERED | DeFiLlama; L2BEAT ecosystem data; Aave deployments | PARTIAL | flash liquidity + venue graph |
| BC-012 | Celo | EVM | EVM | DISCOVERED | DeFiLlama; Aave deployments | PARTIAL | current architecture + flash liquidity |
| BC-013 | Sonic | EVM | EVM | DISCOVERED | DeFiLlama; Aave deployments | PARTIAL | current deployments + venues |
| BC-014 | Soneium | Ethereum L2 | EVM | DISCOVERED | DeFiLlama; Aave deployments | PARTIAL | flash liquidity + venues |
| BC-015 | Metis | Ethereum L2 | EVM | DISCOVERED | DeFiLlama; Aave deployments | PARTIAL | flash liquidity + venues |
| BC-016 | Polygon zkEVM | Ethereum L2 | EVM | DISCOVERED | DeFiLlama/L2 discovery | UNKNOWN | identity + current status + flash liquidity |
| BC-017 | Mantle | Ethereum L2 | EVM | DISCOVERED | DeFiLlama | UNKNOWN | flash liquidity + venue graph |
| BC-018 | Blast | Ethereum L2 | EVM | DISCOVERED | DeFiLlama | UNKNOWN | current status + liquidity + flash liquidity |
| BC-019 | Mode | Ethereum L2 | EVM | DISCOVERED | DeFiLlama | UNKNOWN | current status + venues |
| BC-020 | Manta Pacific | Ethereum L2 | EVM | DISCOVERED | DeFiLlama/L2 discovery | UNKNOWN | current status + flash liquidity |
| BC-021 | Scroll ecosystem candidates beyond core registry | Ethereum L2 | EVM | DISCOVERED | L2BEAT | UNKNOWN | deduplicate against BC-010 before expansion |
| BC-022 | Solana | SVM / L1 | SVM | DISCOVERED | DeFiLlama chains | UNKNOWN | native atomic-liquidity mechanisms + DEX execution |
| BC-023 | Tron | non-EVM / L1 | TVM | DISCOVERED | DeFiLlama chains | UNKNOWN | smart-contract liquidity + atomic mechanism |
| BC-024 | Bitcoin | Bitcoin family | Bitcoin scripting / ecosystem-specific | DISCOVERED | DeFiLlama Bitcoin-family view | UNKNOWN | programmable execution and atomic liquidity path |
| BC-025 | Cosmos Hub / Cosmos ecosystem | Cosmos | Cosmos SDK / ecosystem-specific | DISCOVERED | DeFiLlama Cosmos grouping | UNKNOWN | chain-specific execution and liquidity |
| BC-026 | Injective | Cosmos / appchain | Cosmos SDK / chain-specific | DISCOVERED | DeFiLlama ecosystem discovery | UNKNOWN | native exchange/atomic liquidity verification |
| BC-027 | Near | non-EVM programmable chain | Near VM | DISCOVERED | DeFiLlama chain grouping | UNKNOWN | execution + atomic liquidity |
| BC-028 | Aptos | Move | Move VM | DISCOVERED | DeFiLlama / Move ecosystem discovery | UNKNOWN | atomic liquidity + DEX execution |
| BC-029 | Sui | Move | Move VM | DISCOVERED | DeFiLlama / Move ecosystem discovery | UNKNOWN | atomic liquidity + DEX execution |
| BC-030 | Hyperliquid ecosystem | non-EVM / appchain | chain-specific | DISCOVERED | L2BEAT ecosystem listing + independent discovery | UNKNOWN | determine whether target mechanism is in-scope atomic execution |
| BC-031 | Ronin | EVM-compatible ecosystem | EVM-compatible | DISCOVERED | DeFiLlama; L2BEAT ecosystem listing | UNKNOWN | current smart-contract/DEX/flash-liquidity verification |
| BC-032 | X Layer | Ethereum ecosystem | EVM | DISCOVERED | L2BEAT ecosystem listing | UNKNOWN | flash liquidity + venue verification |
| BC-033 | Fraxtal | Ethereum ecosystem | EVM | DISCOVERED | L2BEAT ecosystem listing | UNKNOWN | flash liquidity + venue verification |
| BC-034 | World Chain | Ethereum L2 | EVM | DISCOVERED | L2BEAT ecosystem listing | UNKNOWN | flash liquidity + venue verification |
| BC-035 | Robinhood Chain | Ethereum ecosystem | EVM / L2 candidate | DISCOVERED | L2BEAT current activity/ecosystem data | UNKNOWN | identity + production status + venue + atomic liquidity |
| BC-036 | Lighter | Ethereum scaling/appchain ecosystem | chain-specific | DISCOVERED | L2BEAT activity/ecosystem data | UNKNOWN | determine whether relevant atomic on-chain trading path exists |
| BC-037 | ZK Stack ecosystem candidates | Ethereum L2 | EVM / ZK | DISCOVERED | L2BEAT ZK Stack view | UNKNOWN | expand into canonical individual networks |
| BC-038 | AggLayer-connected candidates | Ethereum/Polygon ecosystem | chain-specific | DISCOVERED | L2BEAT AggLayer view | UNKNOWN | expand into canonical individual networks |
| BC-039 | Emerging L2/L3 candidates | Ethereum scaling | EVM or ZK | CANDIDATE | L2BEAT + DeFiLlama discovery branches | UNKNOWN | enumerate individually; no aggregate execution identity |
| BC-040 | Emerging non-EVM DeFi candidates | non-EVM | chain-specific | CANDIDATE | DeFiLlama ecosystem branches | UNKNOWN | enumerate individually; verify execution model |

### Important normalization note

Rows BC-021, BC-037, BC-038, BC-039 and BC-040 are **discovery buckets, not executable chain identities**. They exist temporarily so no ecosystem branch is lost. They MUST be expanded into individual canonical records before Phase 01 can claim registry completeness.

## 5. Identity Normalization Rules

A candidate is canonical only when:
1. canonical name is unique;
2. aliases are attached to that canonical record;
3. chain ID or native network identifier is recorded when applicable;
4. mainnet/testnet is explicit;
5. execution model is explicit;
6. parent/ecosystem relationship is explicit;
7. lifecycle state is timestamped;
8. duplicate/conflict references are retained rather than deleted.

### Alias policy

Aliases are metadata, never separate chains.

Examples requiring explicit alias handling:
- Base / Base Chain
- Arbitrum / Arbitrum One
- OP Mainnet / Optimism
- zkSync Era / ZKsync Era
- Avalanche / Avalanche C-Chain
- Polygon / Polygon PoS

## 6. Capability-State Schema

Each canonical record must eventually carry:

- `identity_verified`
- `smart_contract_execution_verified`
- `flash_liquidity_verified`
- `atomic_composability_verified`
- `trading_venue_verified`
- `router_or_execution_path_verified`
- `pool_or_orderbook_discovery_verified`
- `liquidity_at_target_size_verified`
- `quote_mechanism_verified`
- `simulation_supported`
- `freshness_source_defined`
- `execution_ready`

Allowed values:
`VERIFIED | PARTIAL | UNKNOWN | FAILED | NOT_APPLICABLE`

## 7. Evidence Record Contract

Every material field must be traceable to:

**Source → Timestamp → Network → Identifier → Verification method → Confidence → Evidence reference → Conflict state**

A source that only lists a chain does not automatically prove:
- flash loans;
- atomic liquidity;
- DEX execution;
- current contract deployment;
- sufficient liquidity;
- profitable opportunity.

## 8. v001 Coverage Interpretation

This is a **seed canonical registry**, not a final global inventory.

Current factual discovery coverage is therefore:

- Registry structure: **10/10**
- Normalization model: **10/10**
- Ecosystem branch coverage: **10/10**
- Candidate seed breadth: **8/10**
- Identity verification: **2/10**
- Flash-liquidity verification: **0/10**
- Venue verification: **0/10**
- Contract/address verification: **0/10**
- Liquidity-at-size verification: **0/10**
- Freshness automation: **0/10**
- Global completeness: **NOT SCORED**

No candidate is authorized for live trading from this file.

## 9. Required Next Expansion

1. Expand all discovery buckets into individual canonical records.
2. Add chain IDs/native identifiers and lifecycle state from primary evidence.
3. Deduplicate aliases and rebrands.
4. Verify smart-contract execution model.
5. Build flash-liquidity capability matrix.
6. Build trading-venue matrix.
7. Add verified contract/address records only after network-specific evidence.
8. Add recurring freshness mechanism.
9. Audit registry for missed ecosystems and duplicate identities.
10. Keep live trading STOP.

## 10. Source Register

- DeFiLlama Chains: https://defillama.com/chains
- L2BEAT Layer-2 Summary: https://l2beat.com/layer2s/summary
- L2BEAT Activity: https://l2beat.com/layer2s/activity
- Aave official deployment/access documentation: https://aave.com/help/aave-101/accessing-aave

**Source-use rule:** these sources are discovery/corroboration inputs. Individual capability authorization still requires network/protocol-specific verification.
