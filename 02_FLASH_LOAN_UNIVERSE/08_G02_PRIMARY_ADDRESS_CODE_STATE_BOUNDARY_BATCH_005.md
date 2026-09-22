# G02 PRIMARY ADDRESS + CODE/STATE BOUNDARY BATCH 005

**Date:** 21 September 2026  
**Gate:** G02 Atomic / Flash Liquidity Universe  
**Mode:** Maximum Macro Mode  
**State:** CONTINUE, NOT SATURATED

## Objective

Close the highest-information deployment-identity gaps without treating deployment evidence as execution authorization.

## Primary-source materialization

The canonical deployment registry was updated in place with directly supported production identities:

1. **Project 0 / marginfi v2, Solana mainnet**
   - Program: `MFv2hWf31Z9kbCa1snEPYctwafyhdvnV7FZnsebVacA`
   - Official source confirms the program is the Solana mainnet Project 0 marginfi v2 program.
   - A current program-upgrade source records the 2026-08-25 production flip and the flash-loan-sensitive instruction layout.

2. **Sky / Dai MCD_FLASH**
   - Current Sky mainnet address: `0x60744434d6339a6B27d73d9Eda62b6F66a0a04FA`
   - The source also exposes a legacy `MCD_FLASH` address. The legacy address was not promoted as current.
   - The same flash module supports both ERC-3156 DAI flash mint and the Vat-Dai flash path.

3. **Venus Core Pool, BNB Chain**
   - Core Pool Unitroller reference: `0xfd36e2c2a6789db23113685031d7f16329158384`
   - Flash-loan capability remains subject to current runtime enablement and initiator authorization.

4. **Balancer V2 Vault**
   - Ethereum: `0xBA12222222228d8Ba445958a75a0704d566BF2C8`
   - Polygon: `0xBA12222222228d8Ba445958a75a0704d566BF2C8`
   - Arbitrum: `0xBA12222222228d8Ba445958a75a0704d566BF2C8`
   - Optimism: `0xBA12222222228d8Ba445958a75a0704d566BF2C8`
   - Gnosis: `0xBA12222222228d8Ba445958a75a0704d566BF2C8`
   - Official Balancer sources independently document the flashLoan interface and these network deployments.

## Direct code/interface evidence

Primary source review confirms:
- Balancer `IVault.flashLoan` invokes `receiveFlashLoan` and requires repayment plus fee before completion.
- Balancer implementation checks pre-loan balances, executes the callback, verifies post-loan balances and fee payment, and reverts on failure.
- Sky's DssFlash repository implements the flash-mint module and both flash callback paths.
- marginfi official documentation exposes the mainnet program identity and current flash-loan instruction compatibility boundary.
- Venus official documentation exposes the Core Pool architecture and flash-loan controls.

These are **source/interface observations**, not runtime bytecode hashes.

## Canonical state after Batch 005

- Deployment records: **34**
- Unique canonical deployment keys: **34**
- Duplicate keys: **0**
- Primary-source address verified: **26**
- Address pending: **5**
- Execution eligibility from research: **0**
- All 34 records remain `NEVER_FROM_RESEARCH`

## Deliberately unresolved

The following remain open and are not inferred:
- runtime bytecode/code hash;
- proxy/implementation resolution;
- current asset balances and borrowable capacity;
- current fee values;
- flash-loan enablement flags;
- initiator/ACL authorization;
- block-level freshness;
- current chain-specific deployment coverage for all mechanism families;
- adversarial mechanism denominator closure.

## Safety boundary

A current address is an identity fact. It does not establish that the contract currently contains sufficient liquidity, permits the requested asset, accepts the borrower, charges a known current fee, or is safe/economic to execute.

Live trading remains **STOP**.
