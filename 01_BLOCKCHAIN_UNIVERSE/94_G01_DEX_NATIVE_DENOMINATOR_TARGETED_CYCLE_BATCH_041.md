# G01 DEX + NATIVE DENOMINATOR TARGETED CYCLE BATCH 041

Date: 21 September 2026

## Objective

Close a material subset of the 419-label DEX denominator using primary network evidence, while preserving non-EVM semantics and avoiding name-only canonicalization.

## Materialization baseline

The external DEX materialization contains:
- 3,346 unique protocol × chain observations
- 419 unique chain labels
- 36 name-level overlaps with the pre-existing G01 union
- 383 unresolved labels at the initial name-level pass

The 419 labels are observations, not 419 canonical production chains.

## Targeted high-information reconciliation

### Kava
DEX label: `Kava`

Primary evidence establishes Kava mainnet and its dual Cosmos/EVM execution architecture:
- Cosmos mainnet identifier: `kava_2222-10`
- EVM execution chain ID: 2222

The two identifiers are stored as different semantic layers. Kava is promoted as one canonical network.

### opBNB
DEX label: `Op_Bnb`

Primary BNB Chain documentation establishes:
- opBNB mainnet chain ID: 204
- opBNB testnet chain ID: 5611
- opBNB is a BNB Smart Chain Layer 2

Only mainnet enters the production candidate denominator.

### Cardano
DEX label: `Cardano`

Primary Cardano documentation establishes a production mainnet distinct from preview/pre-production test environments. Cardano remains native/non-EVM and is not assigned an EIP-155 identity.

### Klaytn
DEX label: `Klaytn`

Adversarial identity rule: do not create a second chain. Official Kaia documentation states Kaia is the hard fork/continuation of Klaytn and the chain ID remains unchanged. Therefore the DEX label is classified as an execution/network alias of the existing Kaia canonical record rather than a new canonical network.

## Canonical changes

Added in place:
- Kava
- opBNB
- Cardano

No new record for Klaytn because it resolves to existing Kaia identity.

Current canonical registry:
- total: 65
- MATCH_EXISTING: 11
- NEW_CANDIDATE: 54
- unique canonical keys: 65
- duplicate keys: 0

## Remaining material denominator

The 419-label surface remains open. High-frequency labels and ambiguous execution-plane labels should be prioritized, but no completeness claim may be made until the full semantic denominator has either been reconciled or explicitly classified into bounded unresolved/non-chain/alias/production-candidate states.

## Bounded exit decision

CONTINUE_TARGETED_CYCLE

Reason:
1. Material unresolved DEX denominator remains.
2. Native-source reconciliation remains incomplete.
3. Global production denominator is not yet frozen.

## Gate

G01 ACTIVE / NOT SATURATED
G02-G29 BLOCKED
LIVE TRADING STOP
