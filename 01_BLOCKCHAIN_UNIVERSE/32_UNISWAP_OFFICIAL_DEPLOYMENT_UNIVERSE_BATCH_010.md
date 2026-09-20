# PHASE 01.6 BATCH 010 — UNISWAP OFFICIAL DEPLOYMENT UNIVERSE v001

Date: 21 सितम्बर 2026
Status: PARTIAL PASS

## Fresh official evidence
Uniswap's unified official deployment registry currently exposes 1,022 deployments across protocols and networks and lists v4 PoolManager across 24 networks. citeturn0search1
Uniswap v2 official documentation provides factory/router addresses by network and a deployments feed. citeturn0search0
Uniswap v3 official documentation lists production deployments and warns not to assume addresses are shared across chains. citeturn0search2
Uniswap v4 official documentation provides current PoolManager and periphery deployment mappings. citeturn0search4

## Strategic finding
Uniswap must be modeled as a multi-version, multi-contract deployment universe, not as one DEX.

## Version axes
- V2: Factory + Router02 + pair contracts
- V3: Factory + router/quoter/position manager + pools
- V4: PoolManager + position manager + Universal Router + Quoter + hooks

## Concrete V2 sample
| Network | Factory | Router02 |
|---|---|---|
| Ethereum | 0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f | 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D |
| Unichain | 0x1f98400000000000000000000000000000000002 | 0x284f11109359a7e1306c3e447ef14d38400063ff |
| Arbitrum | 0xf1D7CC64Fb4452F05c498126312eBE29f30Fbcf9 | 0x4752ba5dbc23f44d87826276bf6fd6b1c372ad24 |
| Avalanche | 0x9e5A52f57b3038F1B8EeE45F28b3C1967e22799C | 0x4752ba5dbc23f44d87826276bf6fd6b1c372ad24 |

These mappings are from official Uniswap documentation. citeturn0search0

## Concrete V4 sample
The official registry lists PoolManager on 24 networks, including Ethereum, Arbitrum, Arc, Avalanche, Base, BNB Chain, Celo, Ink, Linea, MegaETH, Monad, Optimism, Polygon, Robinhood Chain, Soneium, Tempo, Unichain, World Chain, X Layer and Zora. citeturn0search1
Ethereum PoolManager is 0x000000000004444c5dc75cB358380D2e3dE08A90. citeturn0search4

## Critical flash-trading implications
V2 flash swaps, V3 flash and V4 PoolManager/hook execution are separate primitives. They must not share one generic capability flag.

A deployment is not enough. Verify exact pool state, liquidity, fee or hook configuration, atomic callback semantics, route composition, simulation, execution costs and expected net profit above USD 0.20.

## Pool discovery rule
For V3, each pool is a unique contract instance and can be discovered through the factory getPool function. Therefore deployment feeds into a separate dynamic pool discovery engine. citeturn0search2

## Testnet rule
Testnet deployments are never promoted into the production executable universe.

## Next
Machine-parse the unified Uniswap deployment feed into a canonical protocol × network × version matrix, then join it with flash-capability and dynamic pool-discovery layers.

Live trading: STOP.
