# G01 DEX-DERIVED NETWORK UNION — MACRO-BATCH 024

Date: 21 September 2026
Repository: manish91082-coder/full-ai-ghost-hunter-universe
Branch: main
Live trading: STOP

## Objective

Continue G01 from Macro-Batch 023 by joining a fresh DEX-derived discovery surface against the current canonical source union without treating dashboard counts as executable-chain truth.

## Fresh evidence

The current DeFiLlama DEX-by-chain surface reports **290 chains** and its DEX dashboard reports **794 DEX protocols**. The same surface currently exposes named chain rows including Solana, Ethereum, Robinhood Chain, BSC, Base, Hyperliquid L1, Near, Arbitrum, Polygon, Avalanche, Monad, Spark, Arc, edgeX L1, X Layer, Sui, OP Mainnet, Tron, Starknet and Unichain. citeturn1view0turn0search13

The non-EVM chain surface independently shows production DeFi activity across Sui, Starknet, Near, Aptos, TON and others, reinforcing that DEX discovery must not be EVM-only. citeturn1search0

## Semantic filtering

Not every item visible in a DEX dashboard is a chain:
- **Spark** resolves as a chain-level DeFiLlama object and is therefore retained as a G01 candidate pending primary identity/lifecycle verification. citeturn2search5
- **Native** resolves as a chain-level DeFiLlama object and is retained as a candidate pending primary identity/lifecycle verification. citeturn2search0
- **Chainflip** is deliberately NOT added as a chain. Its own documentation describes a Substrate-based application-specific State Chain plus cross-chain settlement infrastructure, so it requires separate protocol/network modeling rather than being blindly treated as a DEX-chain row. citeturn2search13turn2search1
- Existing candidates such as Solana, Near, Sui, Starknet, Unichain, Arc and others were recognized as overlaps and were not duplicated.

## Current-state changes

Added in place to:
`01_BLOCKCHAIN_UNIVERSE/data/G01_SOURCE_UNION_REGISTRY_v001.json`

New candidates:
1. Spark
2. Native

Both are marked:
`NEW_CANDIDATE / DEX_SOURCE_PRIMARY_IDENTITY_PENDING / NOT_VERIFIED`.

No flash-loan capability, liquidity, venue, route, simulation or profitability was inferred.

## Machine-readable source contract

Created:
`01_BLOCKCHAIN_UNIVERSE/data/G01_DEX_DISCOVERY_SURFACE_MANIFEST_v001.json`

This freezes the DEX source as a discovery input with:
- observed source counts;
- extraction rules;
- no-inference rules;
- protocol-vs-chain semantic separation;
- overlap handling;
- production-denominator rule.

## Saturation status

The DEX surface itself is now formally admitted into the G01 discovery union, but G01 is NOT saturated because:
- complete row extraction is still pending;
- complete protocol→chain relationship extraction is pending;
- identity/lifecycle verification is pending;
- native registries are not fully joined;
- exclusions/conflicts are not closed;
- final denominator is not yet reproducibly materialized.

## Next

Run full machine-readable DEX source extraction and semantic relationship reconciliation, then join remaining native-source candidates and execute the adversarial missed-network audit.

Live trading remains STOP.
