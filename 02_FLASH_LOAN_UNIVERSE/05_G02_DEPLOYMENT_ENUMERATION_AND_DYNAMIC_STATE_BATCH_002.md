# G02 DEPLOYMENT ENUMERATION + DYNAMIC STATE BOUNDARY — MACRO-BATCH 002

**Date:** 21 September 2026
**Active gate:** G02 Atomic / Flash Liquidity Universe
**Source of truth:** GitHub main
**Live trading:** STOP

## Objective
Move G02 from mechanism-family discovery into deployment/state identity without inventing runtime values.

## Primary mechanism boundary advanced
The current G02 universe includes Aave V3, Aave GHO Flashmint, Morpho Blue, Uniswap V2 flash swaps, Euler EVK, Project 0/marginfi, Balancer V2 Vault, Venus Core Pool, Radiant V3, Uniswap V3 Pool flash, Sky/Dai ERC-3156 flash mint, Sky/Dai Vat Dai flash mint, ERC-3156 implementation discovery, and Aave V4 verification candidate.

## Deployment model
A deployment is represented separately from capability and runtime liquidity:
mechanism → network → deployment → code/interface → capability → asset → capacity → fee → authorization → freshness.

Where current evidence is unavailable, the canonical state is explicitly pending/dynamic rather than guessed.

## Current source-backed surfaces
Aave current deployment documentation exposes its named production market/deployment surface. Morpho official material states Morpho Blue is deployed across 50 chains, and the existing project-side 50-row reconciliation remains the canonical fan-out reference. Project 0 has a current Solana mainnet program surface. Uniswap V3 documents pool-level `flash()` and callback repayment. Sky/Dai documents both ERC-3156 flash mint and Vat Dai flash mint. Venus documents asset enablement, initiator authorization, fee parameters and repayment handling. Balancer's Vault interface documents `flashLoan` and `receiveFlashLoan`.

## Runtime-state boundary
No fabricated numeric balance, fee, capacity, utilization, authorization or bytecode hash is promoted to current truth. Such fields remain dynamic or pending until direct runtime evidence exists.

## No execution leap
Every deployment record must remain non-authorizing research state. G03-G29 remain blocked. Live trading remains STOP.

## Remaining material work
Exact address fan-out, bytecode/source verification, asset-level current capacity, fee state, authorization/enablement, additional native and DEX atomic mechanisms, runtime refresh and final bounded saturation audit remain open.
