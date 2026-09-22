# G02 Deployment Denominator Batch 009

Date: 2026-09-21
Scope: Silo V3 + QuickSwap V2 deployment/code-identity boundary

## Objective
Convert primary capability evidence into concrete deployment-denominator evidence without treating deployment as live liquidity or execution authority.

## Verified primary-source findings

### Silo V3
Silo's official V3 repository publishes deployed lending-market versions by network and gives current SiloDeployer, Silo Implementation and Silo Factory addresses for:
- Sonic: current v3.5.0
- Arbitrum: current v3.5.0
- Optimism: current v3.5.0
- Ink: current v3.5.0
- Avalanche: current v3.8.0

The same repository documents that a Silo is deployed on-chain and that the resulting address is saved in deployment artifacts. It also demonstrates market-level Silo0/Silo1 identity and states that each market consists of two ERC-4626 vaults unified by SiloConfig.

Critical boundary: these factory/deployer/implementation addresses do NOT enumerate all currently executable markets or prove current borrowable liquidity, flash-loan fee, hook receiver, or freshness. Permissionless market creation means market-level enumeration remains mandatory.

### QuickSwap V2
Official QuickSwap contracts documentation currently publishes Polygon POS V2:
- Router: 0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff
- Factory: 0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32

The official V2 factory documentation describes PairCreated and getPair/allPairs discovery semantics.

Critical boundary: factory identity does NOT prove any specific pair's current reserves, pair bytecode identity, current fee configuration, or executable opportunity.

## Gate result
G02 remains ACTIVE / NOT SATURATED.
No execution authority granted.
G03-G29 remain BLOCKED.
Live trading remains STOP.
