# PHASE 01 MACRO-BATCH 011 — UNISWAP DEPLOYMENT MATRIX + CAPABILITY GATE DESIGN v001

Date: 21 सितम्बर 2026
Status: PARTIAL PASS / INTEGRATED

## Objective
Compress the Uniswap deployment work into one canonical downstream-ready model instead of continuing with small per-contract chat steps.

## Fresh official verification
Uniswap's official unified Deployments page currently exposes 1,022 deployments and shows Uniswap v4 PoolManager on 24 networks. The page is the authoritative discovery surface, while version-specific pages provide contract-level mappings. citeturn0search3turn0search1

Official v2 documentation provides chain-specific Factory and Router02 mappings and confirms the unified deployments feed is also available. citeturn0search2

Official v3 documentation lists production deployments across Ethereum, Unichain, Arbitrum, Optimism, Polygon, Base, BNB, Avalanche, Celo, ZKsync, Zora, World Chain, X Layer, Monad, MegaETH, Tempo and Robinhood Chain, and explicitly requires chain-specific address confirmation. citeturn0search0

Official v4 documentation provides core/periphery/Universal Router mappings and explicitly warns against assuming identical deployment addresses across chains. citeturn0search1

## Canonical Uniswap model
Uniswap is now represented as:
UNISWAP -> VERSION -> NETWORK -> CONTRACT ROLE -> ADDRESS -> CODE STATE -> CAPABILITY -> POOL STATE -> LIQUIDITY -> ROUTE -> SIMULATION -> ECONOMIC GATE -> EXECUTION AUTHORIZATION

Version-specific capability flags:
- V2_FLASH_SWAP
- V3_FLASH
- V4_POOLMANAGER_ATOMIC_COMPOSITION
- V4_HOOK_DEPENDENT
- ROUTER_SWAP
- QUOTER_READ
- POOL_DISCOVERY

No generic UNISWAP_FLASH=true flag is permitted.

## High-confidence sampled production mappings

### V2
Ethereum:
Factory 0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f
Router02 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D

Unichain:
Factory 0x1f98400000000000000000000000000000000002
Router02 0x284f11109359a7e1306c3e447ef14d38400063ff

Arbitrum:
Factory 0xf1D7CC64Fb4452F05c498126312eBE29f30Fbcf9
Router02 0x4752ba5dbc23f44d87826276bf6fd6b1c372ad24

Avalanche:
Factory 0x9e5A52f57b3038F1B8EeE45F28b3C1967e22799C
Router02 0x4752ba5dbc23f44d87826276bf6fd6b1c372ad24

Source: official v2 deployment documentation. citeturn0search2

### V3
Ethereum Factory:
0x1F98431c8aD98523631AE4a59f267346ea31F984

Base Factory:
0x33128a8fC17869897dcE68Ed026d694621f6FDfD

Polygon Factory:
0x1F98431c8aD98523631AE4a59f267346ea31F984

Avalanche Factory:
0x740b1c1de25031C31FF4fC9A62f554A55cdC1baD

ZKsync Factory:
0x8FdA5a7a8dCA67BBcDd10F02Fa0649A937215422

World Chain Factory:
0x7a5028BDa40e7B173C278C5342087826455ea25a

Monad Factory:
0x204faca1764b154221e35c0d20abb3c525710498

These are official documented production mappings. citeturn0search5turn0search4turn0search10turn0search11turn0search12turn0search7turn0search9

### V4
Ethereum PoolManager:
0x000000000004444c5dc75cB358380D2e3dE08A90

Base PoolManager:
0x498581ff718922c3f8e6a244956af099b2652b2b

Arbitrum PoolManager:
0x360e68faccca8ca495c1b759fd9eee466db9fb32

Polygon PoolManager:
0x67366782805870060151383f4bbff9dab53e5cd6

Avalanche PoolManager:
0x06380c0e0912312b5150364b9dc4542ba0dbbc85

World Chain PoolManager:
0xb1860d529182ac3bc1f51fa2abd56662b7d13f33

Ink PoolManager:
0x360e68faccca8ca495c1b759fd9eee466db9fb32

Official v4 documentation supplies these mappings and additional periphery roles. citeturn0search1

## Important correction to architecture
The same hexadecimal address can legitimately appear on multiple networks. Therefore:
PRIMARY KEY = (network_id, protocol_version, contract_role, address)
NOT address alone.

The V4 examples prove this operationally: Arbitrum and Ink share a PoolManager address in the official registry, while their network identities remain distinct. citeturn0search1

## Dynamic pool layer
V3 pools are unique deployed contract instances. Pool discovery must use factory state/getPool and then verify code, token0/token1, fee, tick spacing, current liquidity/state and executable route. citeturn0search0turn0search4

V4 requires an additional pool-key/hook state layer because hook configuration can materially alter execution semantics. A PoolManager deployment alone does not prove an executable profitable pool.

## Testnet isolation
Official documentation includes testnet mappings such as Ethereum Sepolia, Base Sepolia and Unichain Sepolia. These are discovery/test environments and are excluded from production executable universe until explicitly classified as production by current evidence. citeturn0search2turn0search4turn0search8

## Downstream verification pipeline
For every candidate:
1. network identity
2. contract address
3. bytecode exists/current
4. ABI/interface
5. version/capability
6. pool/market state
7. available liquidity at requested size
8. flash/atomic repayment semantics
9. route
10. deterministic simulation
11. gas + protocol fees + slippage + execution costs
12. expected net profit > USD 0.20
13. security/risk gate
14. execution authorization

## Saturation result
The deployment-discovery layer is sufficiently structured to move downstream without waiting for manual contract-by-contract chat turns. Exhaustive 1,022-record machine extraction remains a repository/data-engineering task, not a reason to block architecture progress.

## Remaining blockers
- Full machine extraction of all 1,022 records
- Direct bytecode/interface verification
- Dynamic pool universe
- current liquidity-at-size
- cross-venue route graph
- deterministic simulation
- economic qualification
- security/execution authorization

Live trading: STOP.
