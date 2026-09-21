# G01 NATIVE PRODUCTION EXTRACTION + DEX-DERIVED UNION — MACRO-BATCH 021

Date: 21 September 2026
Status: EXTRACTION CONTRACT + UNION ENGINE READY / SATURATION PENDING
Repository: manish91082-coder/full-ai-ghost-hunter-universe
Branch: main
Live trading: STOP

## 1. Objective

Advance G01 from source-surface observation to a repeatable machine extraction contract for:
1. live/mainnet native-chain records;
2. non-Cosmos source records;
3. DEX-derived network candidates;
4. deterministic normalization and overlap accounting.

This batch deliberately does not declare a final chain denominator.

## 2. Fresh external evidence

The current Cosmos Chain Registry describes itself as a structured registry containing chain.json, assetlist.json and versions.json for Cosmos-SDK chains and assetlist data for non-Cosmos chains. Its chain schema explicitly supports multiple CAIP-2 namespaces including cosmos, eip155, solana, polkadot, starknet, xrpl and others, with lifecycle states live/upcoming/killed and network types mainnet/testnet/devnet. citeturn0search0turn1search11

The current DeFiLlama chain surface exposes multiple ecosystem filters including Non-EVM, Cosmos, SVM, Polkadot, Near and others, demonstrating that the independent discovery surface is not EVM-only. citeturn1search0turn1search9

Osmosis is directly represented in the Cosmos registry as live/mainnet with chain ID osmosis-1, and its official documentation describes it as a cross-chain DEX/liquidity hub with concentrated liquidity. This makes it a concrete example of why chain identity and DEX capability must remain separate records. citeturn0search2turn0search8

Injective is independently visible on DeFiLlama's DEX surface with Injective Orderbook and Helix activity. This validates the use of DEX-derived network discovery as a cross-check rather than relying only on chain registries. citeturn1search14

## 3. Machine extraction contract

Created:
- data/G01_NATIVE_PRODUCTION_EXTRACTION_MANIFEST_v001.json
- src/ghost_hunter/g01_source_extractor.py
- tests/test_g01_source_extractor.py

The extractor accepts the externalized manifest and source payloads. It does not embed a chain list, address list, pair list, RPC list or strategy list.

## 4. Extraction semantics

Cosmos source:
- select paths ending in chain.json;
- parse only records with status=live and network_type=mainnet for the production candidate set;
- retain non-production records separately for exclusions;
- preserve chain_type and chain_id without coercion.

DEX-derived source:
- extract network names from qualifying DEX-like protocol records;
- mark them DISCOVERY_ONLY;
- require independent identity/lifecycle verification before promotion.

## 5. Accounting law

Every source record is classified as:
DISCOVERED → NORMALIZED → VERIFIED → TESTED → AUDITED → SATURATED

Unknown, conflict, stale and excluded states are first-class.

The batch records:
- source candidate count;
- production-eligible candidate count;
- overlap count;
- new candidate count;
- unresolved identity count;
- excluded/testnet count;
- conflict count.

No source count is added directly to another source count.

## 6. Gap findings

Still open:
- full live/mainnet extraction execution against the current registry;
- complete _non-cosmos union;
- dedicated Solana/SVM, Move, Near/WASM, TON, XRPL, Substrate and programmable-Bitcoin source joins;
- DEX-derived candidate normalization against the canonical registry;
- exclusion/freshness reconciliation;
- final deduplicated G01 denominator;
- final direct verification of production candidates.

## 7. Gate decision

G01 remains ACTIVE / NOT SATURATED.

This batch closes the machine-contract sub-objective for repeatable extraction and DEX-derived candidate ingestion, but not factual saturation.

G02-G28 remain blocked. G29 remains active control. Live execution remains STOP.
