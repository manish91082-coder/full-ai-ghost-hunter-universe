# G02 Pair Deployment Boundary Batch 010

Date: 21 September 2026

## Objective
Materialize primary deployment identities for QuickSwap V2 and PancakeSwap V2 while keeping pair universe and runtime state separate.

## QuickSwap V2
Polygon POS V2 Factory: 0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32
Polygon POS V2 Router: 0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff

Official documentation supports factory-based pair discovery and V2 flash swaps. Current pair reserves, pair bytecode, fee configuration and freshness remain runtime obligations.

## PancakeSwap V2
BNB Smart Chain Factory: 0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73
BNB Smart Chain Router: 0x10ED43C718714eb63d5aA57B78B54704E256024E

Official documentation exposes getPair/allPairs/allPairsLength and PairCreated semantics. The V2 documentation is older, therefore current code identity, pair universe, reserves, fee state and flash-callback behavior require fresh runtime verification.

## Boundary
Deployment identity does not equal pair enumeration, live liquidity, executable route or economic opportunity.

All four new deployment records remain NEVER_FROM_RESEARCH.
