# G02 RUNTIME BOUNDARY BATCH 006

**Date:** 21 September 2026  
**Gate:** G02 Atomic / Flash Liquidity Universe  
**Result:** CONTINUE

## High-value runtime-boundary finding: Project 0 / marginfi

Official Project 0 documentation confirms the Solana mainnet program identity:
`MFv2hWf31Z9kbCa1snEPYctwafyhdvnV7FZnsebVacA`.

The official flashloan guide states:
- flashloans are atomic and uncollateralized;
- start and end instructions bookend the transaction;
- the transaction reverts if the account is not healthy at the end;
- flashloans cannot be nested;
- flashloans cannot be invoked through CPI;
- flashloan fee is zero.

The official SDK documentation adds an important current-state compatibility boundary:
- mainnet moved to program 0.1.10 on 2026-08-25;
- the subsequent 0.1.11 oracle upgrade requires `@0dotxyz/p0-ts-sdk@^2.8.0`;
- the deprecated `@mrgnlabs/marginfi-client-v2` is not valid for the current flashloan integration path;
- current bank state includes caps, weights, oracle state and operational conditions that must be read from chain.

## Canonical promotion

The deployment registry now records for the marginfi mainnet deployment:
- primary-source program identity;
- primary-source capability evidence;
- documented current zero flashloan fee;
- current SDK/program compatibility obligation;
- capacity = UNKNOWN_RUNTIME;
- enablement = UNKNOWN_RUNTIME;
- authorization = primitive-level permissionless semantics, subject to account/health state.

No live capacity was invented.

## G02 safety boundary

Documentation-derived capability is not the same as live executable liquidity. The remaining runtime obligations are:
1. read current bank accounts;
2. determine borrowable liquidity/caps for each supported asset;
3. read operational/circuit-breaker/oracle state;
4. verify current program executable identity against on-chain state;
5. establish freshness at block/slot level;
6. preserve evidence provenance.

G02 remains ACTIVE / NOT SATURATED. G03-G29 remain blocked. Live trading remains STOP.
