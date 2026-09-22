# 🌐 PHASE 01 — DISCOVERY SOURCE MATRIX v1.0

**Phase:** Global Blockchain Universe  
**Status:** Discovery framework verified; factual universe construction in progress  
**Live Trading:** STOP  
**Date:** 21 सितम्बर 2026

## 1. Purpose

इस file का काम blockchain universe के लिए discovery sources को नियंत्रित करना है। यह स्वयं “complete blockchain list” नहीं है। इसका उद्देश्य source coverage, source role और verification hierarchy को lock करना है।

## 2. Source Hierarchy

### Tier 1 — Primary / On-chain
- Official blockchain documentation
- Official protocol deployment documentation
- Verified explorer contract/source
- On-chain deployment/state evidence
- Official governance/deployment repositories

### Tier 2 — Authoritative ecosystem datasets
- DeFiLlama chain universe
- L2BEAT scaling ecosystem
- Other specialized protocol/network registries after validation

### Tier 3 — Discovery-only aggregators
- Chain directories
- ecosystem lists
- third-party datasets

Tier 3 data can create candidates but cannot alone establish critical execution facts.

## 3. Initial Evidence Observed

### DeFiLlama
DeFiLlama currently exposes a broad “All Chains” dataset and separate EVM/non-EVM/grouped views. Its chain page reports chain-level protocol counts, DeFi TVL, DEX volume and other metrics. This makes it useful as a broad discovery source, not as final flash-loan eligibility proof. citeturn0search0turn0search1

### L2BEAT
L2BEAT provides a structured Layer-2 ecosystem view, including rollups and other scaling systems, and therefore supplies an important L2 discovery branch that should not be inferred only from generic chain lists. citeturn0search2

### Aave
Aave's current deployment documentation lists official deployments across multiple networks, demonstrating that protocol-level deployment evidence must be tracked independently from generic chain existence. citeturn0search6

## 4. Important Audit Finding

A blockchain appearing in a chain directory or DeFi dataset does not prove:
- flash-loan availability;
- atomic-liquidity availability;
- executable arbitrage path;
- sufficient liquidity;
- current deployment status;
- valid contract addresses.

Therefore Phase 01 must use:

**Discovery Candidate → Capability Verification**

## 5. Required Discovery Branches

1. EVM chains
2. Ethereum L2/L3 and rollup ecosystems
3. Non-EVM smart-contract chains
4. Bitcoin-derived smart-contract/DeFi ecosystems
5. Cosmos-family ecosystems
6. Solana/SVM ecosystems
7. Move-family ecosystems
8. Other programmable/DeFi-capable ecosystems
9. New/emerging networks
10. Retired/inactive networks for exclusion audit

## 6. Record-Level Evidence Requirement

Every candidate record must eventually contain:

canonical_name | aliases | network_family | execution_model | chain_id_or_native_identifier | status | explorer | RPC_candidates | DeFi_evidence | trading_venue_evidence | flash_liquidity_status | source_refs | verification_state | checked_at | exclusion_reason

## 7. Current Research Decision

The first pass will deliberately over-discover candidates rather than prematurely exclude them. Exclusion happens only after a documented capability/status check.

**Next sub-operation:** construct the normalized candidate registry from multiple discovery branches, then verify flash-liquidity and trading capability separately.
