# AUDIT 075 — G02 SILO FACTORY HISTORICAL SCAN PLAN

Date: 22 September 2026  
Gate: G02 — Atomic / Flash Liquidity Universe  
Result: PASS FOR SCAN-PLAN BOUNDARY / G02 CONTINUE

The bounded denominator is 37 known-created SiloFactory identities plus 1 current Optimism deployment candidate, for 38 scan identities. Identity is network-scoped as (network_id, factory).

Primary-source Foundry deployment receipts in the pinned Silo repository snapshot provide exact CREATE-block starts for 8 known-created factory identities plus the separate current Optimism deployment candidate. The block from one factory or network is never reused for another identity.

The remaining 29 identities have no accepted exact-identity start-block artifact in the inspected source snapshot and are explicitly BLOCKED_MISSING_START_BLOCK. No block number was guessed or inferred from factory-list order or event order. In particular, the same factory address appearing on Sonic and XDC does not transfer Sonic deployment evidence to XDC.

The current Optimism deployment 0x8ab5D81d342f14e594c65a6B33582b57e78E4a9d is retained separately from the historical factory-list identity 0xFa773e2c7df79B43dc4BCdAe398c5DCA94236BC5.

This closes the machine scan-plan boundary, not the G02 market denominator. Historical range closure, NewSilo enumeration, market reconciliation, both-vault runtime verification, code authenticity, liquidity, fees, authorization/hooks/oracles and freshness remain open.

Execution authority: NONE.  
Live trading: STOP.  
G03-G29: BLOCKED.

Primary evidence: silo-finance/silo-contracts-v3 at commit 564fcf86f6e64171f2f7f9402d50ad63d2b54c83, document silo-core/docs/SiloFactoryList.md, plus exact factory deployment receipt artifacts under silo-core/broadcast/SiloFactoryDeploy.s.sol/.
