# G02 ADVERSARIAL ATOMIC MECHANISM DISCOVERY — MACRO-BATCH 003

**Date:** 21 September 2026
**Status:** DISCOVERY DELTA CAPTURED

## Search axes

Callback interfaces, ERC-3156 lender surfaces, pool-level flash functions, vault temporary liquidity, governance debt ceilings, instruction-bracket atomic borrowing, and protocol-internal flash facilities were searched beyond protocol-name recall.

## Material discoveries

1. Uniswap V3 Pool flash is distinct from V2 pair flash semantics and uses flash plus uniswapV3FlashCallback.
2. Sky/Dai exposes two distinct atomic mint paths: ERC-3156-compatible DAI Flash Mint and Vat Dai flash mint.
3. ERC-3156 is retained as a discovery family. A standard is not itself a provider; implementations require source/bytecode/interface enumeration.
4. Aave V4 remains a discovery/verification candidate. Its current deployment surface is documented, but current flash enablement and role-specific interfaces require direct verification.
5. Curve lending/flash-loan surfaces are retained as an adversarial research candidate. Current technical/audit evidence indicates explicit flash-loan lender functionality, but this does not yet establish a current production deployment/capacity universe in the canonical state.

## Negative controls

Never count deployment as active liquidity, a standard as a provider, historical fee as current fee, or documentation as current capacity. Never promote an address without network + role + provenance.

## Remaining bounded search

Additional ERC-3156 implementations, DEX pool flash semantics beyond Uniswap, native non-EVM atomic-liquidity equivalents, vault protocols with explicit same-transaction liquidity, and deprecated/dormant deployment reconciliation remain open.
