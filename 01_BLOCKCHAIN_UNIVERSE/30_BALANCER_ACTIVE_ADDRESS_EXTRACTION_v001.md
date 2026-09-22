# PHASE 01.6 BATCH 009 — BALANCER ACTIVE ADDRESS EXTRACTION v001

Date: 21 सितम्बर 2026
Status: PARTIAL PASS

## Fresh primary-source extraction
The official balancer-deployments repository contains network-keyed deployment JSON files, active/deprecated status, versions, addresses and ABIs. It explicitly warns that dynamically created pool addresses must be obtained from on-chain state/events rather than treated as canonical deployment outputs. citeturn0search0

## Concrete active deployment records

| Network file | Version/task | Role | Address | Status |
|---|---|---|---|---|
| mainnet | 20210418-vault | Vault | 0xBA12222222228d8Ba445958a75a0704d566BF2C8 | ACTIVE v2 |
| arbitrum | 20210418-vault | Vault | 0xBA12222222228d8Ba445958a75a0704d566BF2C8 | ACTIVE v2 |
| base | 20210418-vault | Vault | 0xBA12222222228d8Ba445958a75a0704d566BF2C8 | ACTIVE v2 |
| polygon | 20210418-vault | Vault | 0xBA12222222228d8Ba445958a75a0704d566BF2C8 | ACTIVE v2 |
| mainnet | 20241204-v3-vault | Vault | 0xbA1333333333a1BA1108E8412f11850A5C319bA9 | ACTIVE v3 |
| arbitrum | 20241204-v3-vault | Vault | 0xbA1333333333a1BA1108E8412f11850A5C319bA9 | ACTIVE v3 |
| base | 20241204-v3-vault | Vault | 0xbA1333333333a1BA1108E8412f11850A5C319bA9 | ACTIVE v3 |
| optimism | 20241204-v3-vault | Vault | 0xbA1333333333a1BA1108E8412f11850A5C319bA9 | ACTIVE v3 |

The official source shows the same V2/V3 Vault address can be deployed on multiple networks. Therefore address uniqueness is not a network identity. The canonical key remains network + chain identifier + task/version + role + address + source. citeturn0search0turn0search3

## Additional concrete Ethereum V2 anchors
The official deployment source lists Ethereum V2 Vault, BalancerHelpers and ProtocolFeesCollector as active, while several older pool factory deployments are marked deprecated. The official documentation also exposes Ethereum deployment addresses including Vault and factories. citeturn0search0turn0search1

## Important false-positive prevention
- ACTIVE deployment does not prove current flash capacity.
- Vault deployment does not prove a selected token has enough liquidity for a trade.
- V2 and V3 are distinct execution surfaces.
- Deprecated task IDs remain historical and must not be promoted to executable candidates.
- Dynamically created pool addresses require on-chain discovery.
- A known address is not proof of current bytecode/interface without live verification.

## Next verification gates
1. Normalize chain identifiers for these records.
2. Verify bytecode on each network.
3. Verify flashLoan interface and callback semantics.
4. Read current Vault balances/capacity and applicable fee configuration.
5. Discover active pools from on-chain state/events.
6. Cross with independent DEX venues and route graph.
7. Deterministic simulation.
8. Apply net-profit gate > USD 0.20 after all applicable costs.

## Decision
Balancer active canonical Vault anchors are now concretely evidenced for the sampled networks. This is still a sample, not exhaustive Balancer network coverage and not an execution authorization.

Live trading: STOP.
