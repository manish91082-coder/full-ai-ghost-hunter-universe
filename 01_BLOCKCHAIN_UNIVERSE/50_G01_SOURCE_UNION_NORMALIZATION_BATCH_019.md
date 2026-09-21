# G01 SOURCE-UNION NORMALIZATION — MACRO-BATCH 019

Date: 21 September 2026
Status: NORMALIZATION + PRIMARY IDENTITY PASS / G01 NOT SATURATED
Repository: manish91082-coder/full-ai-ghost-hunter-universe
Branch: main
Live trading: STOP

## 1. Objective

Take the 21 discovery inputs added in Macro-Batch 018 and reconcile them against the current canonical seed and the reconciled Morpho 50-row deployment source.

The purpose is to prevent duplicate chain counting and to promote only evidence-supported identities toward the G01 identity/lifecycle layer.

## 2. Result

21 discovery inputs reviewed.

- 10 confirmed overlaps with existing canonical/Morpho records.
- 11 candidates remain newly introduced relative to the currently inspected seed + Morpho reconciliation.
- The 11 figure is provisional because the DEX-derived deployment union and additional native ecosystem registries are not yet fully joined.

This corrects the earlier implicit assumption that all 21 entries were unique additions.

## 3. Confirmed overlaps

| Discovery input | Canonical linkage | Normalization |
|---|---|---|
| Lighter | BC-036 | exact identity |
| RISE | Morpho row 36 | RISE/Rise alias normalization |
| Abstract | Morpho row 03 | exact identity |
| Plume Network | Morpho row 34 | Plume/Plume Network normalization |
| Sei | Morpho row 39 | execution-plane metadata retained |
| Kaia | Morpho row 23 | exact identity |
| Aptos | BC-028 | exact identity |
| Sui | BC-029 | exact identity |
| Near Protocol | BC-027 | Near Protocol/NEAR normalization |
| Injective | BC-026 | native + EVM execution planes retained |

## 4. Eleven remaining newly introduced candidates

1. Fuel Ignition
2. Reya Network
3. PlayBlock
4. EDU Chain
5. Eclipse
6. Xai
7. Powerloom
8. Gravity L1
9. Berachain
10. Hedera Mainnet
11. Starknet

These records remain G01 candidates only. No flash-loan or trading capability is inferred.

## 5. Primary identity/lifecycle verification findings

| Network | Mainnet identity | Evidence state | Notes |
|---|---|---|---|
| Fuel Ignition | chain ID 9889 | PRIMARY VERIFIED | Official Fuel documentation distinguishes mainnet from testnet. |
| Reya Network | mainnet exists | PRIMARY MAINNET EXISTENCE | Official documentation describes Reya as an Ethereum-based ZK rollup/trading network; exact network identifier still requires direct identity extraction. |
| PlayBlock | chain ID 1829 | SECONDARY PROVISIONAL | Current public source identifies PlayBlock mainnet and chain ID 1829; primary PlayBlock docs still required for G01 freeze. |
| EDU Chain | chain ID 41923 | PRIMARY VERIFIED | Official Open Campus developer documentation identifies mainnet and testnet separately. |
| Eclipse | mainnet exists | PRIMARY MAINNET EXISTENCE | Official Eclipse docs identify Eclipse Mainnet and mainnet program deployments; exact chain/network identifier still requires direct extraction. |
| Plume | chain ID 98866 | PRIMARY VERIFIED | Official Plume network documentation identifies mainnet and testnet separately. |
| Xai | chain ID 660279 | PRIMARY VERIFIED | Xai official network documentation identifies Xai mainnet and chain ID 660279. |
| Powerloom | chain ID 7869 | PRIMARY VERIFIED | Official Powerloom docs identify Mainnet V2 and chain ID 7869. |
| Gravity L1 | chain ID 127001 | PRIMARY VERIFIED | Galxe's official transition announcement identifies Gravity L1 mainnet and chain ID 127001. |
| Berachain | chain ID 80094 | PRIMARY VERIFIED | Current official Berachain documentation identifies mainnet 80094 and testnet 80069. |
| Hedera Mainnet | chain ID 295 | PRIMARY VERIFIED | Hedera documentation identifies mainnet 295 and separate testnet/previewnet values. |
| Starknet | SN_MAIN | SECONDARY/PARTIAL | Mainnet identity is represented as SN_MAIN in current public ecosystem documentation; stronger official capture is still required. |
| Aptos | chain ID 1 | PRIMARY VERIFIED | Aptos maintained source defines Mainnet as chain ID 1. |
| Sui | mainnet native identity | PRIMARY MAINNET EXISTENCE | Sui mainnet is confirmed; runtime chain identifier uses Sui-native semantics rather than an EVM numeric chain ID. |
| NEAR | network ID mainnet | PRIMARY NETWORK-ID EVIDENCE | NEAR tooling distinguishes mainnet from testnet using the network ID. |
| Injective | native injective-1; EVM 1776 | PRIMARY VERIFIED | Injective official docs identify native mainnet as injective-1; official Injective site identifies EVM network chain ID 1776. |
| Sei | EVM 1329; native pacific-1 | PRIMARY VERIFIED | Sei official docs distinguish EVM 1329 and native Cosmos pacific-1. |
| Kaia | chain ID 8217 | PRIMARY VERIFIED | Kaia official docs distinguish mainnet 8217 from Kairos testnet 1001. |
| Lighter | chain ID 304 | SECONDARY/PROVISIONAL | Current public technical material identifies mainnet chain ID 304, but the captured source is not official documentation. |
| RISE | mainnet | PRIMARY MAINNET EXISTENCE | Official RISE documentation identifies RISE as an Ethereum L2; exact chain identifier remains to be extracted and verified. |

## 6. Critical identity-model corrections

### Injective
Injective must not be reduced to one numeric EVM chain ID. The native Cosmos chain identity is injective-1; the EVM-compatible execution surface uses numeric chain ID 1776. These are execution-plane metadata under one ecosystem identity and must be kept distinct for routing and capability checks.

### Sei
Sei similarly exposes an EVM surface (1329) and a native Cosmos chain identity (pacific-1). The registry must retain both execution planes rather than collapsing them into an arbitrary single identifier.

### Sui
Sui's identity model is not an EVM numeric chain ID. The project must retain a native chain identifier mechanism and query the current identifier/state dynamically where required.

### NEAR
NEAR tooling uses a network identifier such as mainnet, so the canonical identity schema must allow native network IDs rather than forcing numeric EVM semantics.

## 7. Machine-readable canonical source

01_BLOCKCHAIN_UNIVERSE/data/G01_SOURCE_UNION_REGISTRY_v001.json

This machine-readable layer is intentionally NOT execution authorization. It is a versioned external registry input and can be replaced/replayed without changing source algorithms.

## 8. Remaining normalization gaps

- Join against the full Uniswap/Balancer and other DEX-derived network deployment unions.
- Join against native ecosystem registries for Cosmos/IBC, Solana/SVM, Move, Near/WASM, Tron/TVM and other relevant execution models.
- Extract official identity pages for Lighter, PlayBlock and Starknet.
- Extract exact mainnet identifiers for Reya, Eclipse and RISE.
- Reconcile lifecycle/deprecation state.
- Resolve remaining alias/rebrand conflicts.
- Build exclusions with evidence.
- Establish freshness deadlines.
- Generate a deduplicated source-union counter after all source surfaces are joined.

## 9. Decision

G01 remains ACTIVE / NOT SATURATED.

Normalization is materially improved, but no final global chain count is declared.

Live trading remains STOP.