# G02 ADVERSARIAL ATOMIC-LIQUIDITY DENOMINATOR BATCH 007

**Date:** 21 September 2026
**Gate:** G02 Atomic / Flash Liquidity Universe
**Mode:** Maximum Macro Mode
**Result:** CONTINUE / NOT SATURATED

## Objective

Attack the current atomic-liquidity denominator from independent protocol families rather than merely expanding the existing known list. The search targeted lending markets, DEX vaults, V2-style flash swaps, Solana instruction-paired liquidity and protocol-specific flash-loan paths.

## New primary-source discovery candidates

| ID | Protocol | Primitive | Evidence state | Why it matters |
|---|---|---|---|---|
| ALU-0016 | Silo V3 | Flash loan | DISCOVERY_CANDIDATE | Official docs expose a flash-loan hook/action, same-transaction repayment and dynamic market fee/config fields. |
| ALU-0017 | SyncSwap | Vault flash loan | DISCOVERY_CANDIDATE | Official architecture explicitly states its permissionless Vault supports flash loans. |
| ALU-0018 | QuickSwap | Flash swap | DISCOVERY_CANDIDATE | Official docs expose reserve-sized flash swaps and same-transaction repayment. |
| ALU-0019 | PancakeSwap | V2-style flash swap | DISCOVERY_CANDIDATE | Official PancakeSwap code contains an ExampleFlashSwap using pancakeCall. |
| ALU-0020 | Drift | Flash-loan/BeginSwap-EndSwap path | DISCOVERY_CANDIDATE | Official Drift material describes flash-loan-powered leveraged swaps; current runtime/program constraints remain to verify. |
| ALU-0021 | Save / Solend | Flash loan | DISCOVERY_CANDIDATE | Current Save documentation retains flash-loan/fee concepts, while older official documentation reports implementation limitations. This conflict requires fresh runtime verification before promotion. |

## Adversarial findings

1. Flash loan is not one mechanism family. The denominator must include lending-market flash loans, vault-based flash loans, V2-style flash swaps, ERC-3156 lenders, protocol-native instruction-paired Solana paths and other atomic-capital surfaces.
2. Protocol existence is insufficient. Each candidate requires current deployment, executable code identity, capability, asset availability, capacity, fee, authorization/enablement and freshness verification.
3. Historical documentation is not current-state authorization. Save/Solend is deliberately retained as a candidate with a conflict/staleness flag, not promoted to verified primitive.
4. Permissionless market creation expands the deployment denominator. Silo demonstrates why protocol-level deployment enumeration and market-level runtime enumeration must remain separate.
5. DEX flash swaps are part of atomic capital discovery. They are economically distinct from lending flash loans and must not be omitted merely because the source is a DEX.

## Bounded saturation test

The search expanded across EVM lending protocols, EVM vault/aggregator DEX architecture, V2-style pair flash swaps, Solana lending and Solana margin/spot-market flash-loan paths.

The marginal-yield test is NOT saturated because multiple newly discovered primary-source candidates still require deployment and runtime verification, and the global mechanism denominator has not been independently closed.

## Safety boundary

No candidate in this batch authorizes execution. All six new records are DISCOVERY_CANDIDATE; execution authority remains NONE. Live trading remains STOP.

## Sources

- Silo: https://docs.silo.finance/docs/developers/dev-tutorials/hooks/
- Silo deployments: https://docs.silo.finance/docs/developers/resources/deployments/
- SyncSwap: https://docs.syncswap.xyz/syncswap/smart-contracts/overview
- QuickSwap: https://docs.quickswap.exchange/technical-reference/core-concepts/flash-swaps
- PancakeSwap code: https://github.com/pancakeswap/pancake-swap-periphery/blob/master/contracts/examples/ExampleFlashSwap.sol
- Drift: https://www.drift.trade/updates/leveraged-swaps
- Save/Solend: https://docs.save.finance/developers/flash-loans
- Save parameters: https://docs.save.finance/protocol/parameters
