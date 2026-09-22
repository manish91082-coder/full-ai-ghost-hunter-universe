# PHASE 01.6 BATCH 008 — BALANCER OFFICIAL DEPLOYMENT REGISTRY EXTRACTION v001

Date: 21 सितम्बर 2026
Status: PARTIAL PASS

## Fresh evidence
Balancer's official documentation links directly to Deployment Addresses. citeturn1view0 The official balancer-deployments repository states that it contains V2 and V3 deployed contract addresses and ABIs, and that canonical deployments can be retrieved by deployment task, contract and network. It also explicitly separates deprecated deployments. citeturn1search0turn1search2

Balancer's official bal_addresses repository further states that its address book separates **active** and **old** addresses and is regenerated regularly. It provides chain-keyed deployment/contract mappings and a latest-contract lookup. citeturn1search1

## Verified architecture finding
The correct extraction source is not a flat list of pools. It is:
**chain → active deployment → contract role → address → version/task → status**.

Pool contracts created dynamically by factories are intentionally handled separately because the official deployment repository states that their addresses are not stored as canonical deployment outputs and must be discovered from on-chain state/events. citeturn1search0

## Current canonical Balancer anchors
- Canonical Vault lookup is explicitly supported by the official address book.
- The official deployment repository contains V2 and V3 deployment namespaces.
- V3 deployment tasks include V3 Vault and associated routers/registries.
- Deprecated deployment tasks are separately documented and must not be promoted into the active executable universe. citeturn1search0turn1search1

## Critical correction to prior step
The previous batch correctly refused to fabricate a deployment table. This batch now establishes the official machine-readable sources, but exact network-by-network address extraction is still a separate parsing operation. Therefore no invented address list is added here.

## Canonical state model
DISCOVERY_ONLY → DEPLOYMENT_SOURCE_VERIFIED → ADDRESS_PARSED → CODE_VERIFIED → FLASH_CAPABILITY_VERIFIED → CAPACITY_VERIFIED → VENUE_VERIFIED → ROUTE_VERIFIED → SIMULATED → ECONOMICALLY_ELIGIBLE → EXECUTION_AUTHORIZED

Any conflict, stale address, deprecated deployment, missing code, insufficient capacity, failed simulation or economics below threshold blocks progression.

## Next extraction target
Parse the official active address books by chain, beginning with canonical Vault/V3 Vault and flash-relevant contracts. Then reconcile against deployment tasks and exclude deprecated/testnet records.

Live trading: STOP.
