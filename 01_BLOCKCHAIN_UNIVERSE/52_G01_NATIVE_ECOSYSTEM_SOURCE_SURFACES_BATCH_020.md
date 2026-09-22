# G01 NATIVE ECOSYSTEM SOURCE SURFACES — MACRO-BATCH 020

Date: 21 September 2026
Status: SOURCE-SURFACE VERIFIED / EXTRACTION PENDING
Repository: manish91082-coder/full-ai-ghost-hunter-universe
Branch: main
Live trading: STOP

## 1. Objective

Expand G01 beyond EVM-centric discovery by formally joining native execution-model source surfaces. This batch does not promote flash-loan capability and does not advance any dependent gate.

## 2. Cosmos Chain Registry

The current Cosmos Chain Registry is a major structured discovery source. Its repository states that it contains chain.json, assetlist.json and versions.json data for numerous Cosmos-SDK chains and assetlist data for non-Cosmos chains. citeturn0search1turn0search6

Direct GitHub API inspection of the current root produced:
- 290 root entries;
- 266 named top-level directories that are not internal underscore directories or dot-prefixed directories;
- a separate _non-cosmos registry surface.

The 266 figure is a source-surface directory count, not a final production-chain count. It includes entries that still require lifecycle, identity, duplicate and relevance reconciliation.

The registry schema carries fields such as chain name, status, network type, chain type and chain ID, which are suitable inputs to the G01 normalization pipeline. citeturn0search1turn0search2

## 3. Native / non-EVM execution surfaces

The Cosmos registry itself exposes a _non-cosmos surface containing entries for multiple external ecosystems. Observed examples include Solana, Sui, Tron, TON, XRPL, Polkadot, Stellar, Filecoin, Internet Computer, Zcash and others.

This is valuable because the discovery source is not limited to one execution model. It must nevertheless be treated as a source union, not as authoritative truth for every external ecosystem.

## 4. Solana

Official Solana documentation distinguishes Mainnet as the production environment, Devnet as public development/testing, and Testnet as validator/stress testing. Only Mainnet enters the production candidate denominator. Devnet/Testnet remain test identities and must not inflate G01 production coverage. citeturn0search0turn0search4

Solana therefore becomes an explicit native execution-model candidate in the G01 source union, with cluster-aware lifecycle semantics.

## 5. TRON

Official TRON documentation identifies Mainnet chain ID 728126428, Shasta testnet chain ID 2494104990, and Nile testnet chain ID 3448148188.

The official documentation also explains that TRON TVM has EVM-compatible interfaces but network/runtime semantics differ, so a simple EVM-equivalence assumption is invalid. citeturn1search0turn1search1

Only TRON Mainnet enters the production candidate denominator. Shasta and Nile remain test identities.

## 6. Explicit structured candidates captured

| Candidate | Identity | Source | G01 state |
|---|---|---|---|
| Osmosis | cosmos: osmosis-1 | Cosmos Chain Registry | DISCOVERY-SOURCE VERIFIED |
| Neutron | cosmos: neutron-1 | Cosmos Chain Registry | DISCOVERY-SOURCE VERIFIED |
| dYdX Protocol | cosmos: dydx-mainnet-1 | Cosmos Chain Registry | DISCOVERY-SOURCE VERIFIED |
| Sei | cosmos: pacific-1 | Cosmos Chain Registry | MATCH EXISTING |
| Solana | mainnet cluster | Solana official | DISCOVERY-SOURCE VERIFIED |
| TRON | mainnet chain ID 728126428 | TRON official | DISCOVERY-SOURCE VERIFIED |

The Cosmos examples are directly represented by live/mainnet chain.json records in the registry, including status=live and network_type=mainnet. citeturn0search2turn0search9

## 7. Critical normalization law strengthened

ecosystem source surface → candidate network → canonical identity → execution plane → lifecycle → production eligibility → downstream capability verification

Therefore:
- a registry directory is not automatically a chain;
- a chain is not automatically a smart-contract execution environment;
- a smart-contract environment is not automatically flash-capable;
- flash capability is not automatically economically executable;
- executable capability is not automatically profitable.

## 8. Remaining work

1. Enumerate all eligible live production records from the Cosmos Chain Registry without relying on manual sampling.
2. Join its _non-cosmos surface against existing G01 candidates.
3. Add dedicated primary registries for Solana/SVM, Move, Near/WASM, TON, XRPL, Polkadot/Substrate, Bitcoin-derived programmable networks and other relevant models.
4. Reconcile every new candidate against the current canonical registry.
5. Apply lifecycle and retirement filters.
6. Preserve exclusions and evidence.
7. Complete DEX-derived network union.
8. Produce the final deduplicated G01 denominator only after all source surfaces are joined.

## 9. Gate decision

G01 remains ACTIVE / NOT SATURATED.

This batch closes the native-ecosystem source-surface discovery sub-objective but not G01.

Dependent gates remain blocked. Live trading remains STOP.