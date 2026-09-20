# AUDIT 015 — BALANCER ACTIVE ADDRESS EXTRACTION

Date: 21 सितम्बर 2026
Status: PARTIAL PASS

| Dimension | Score |
|---|---:|
| First-party deployment source | 10/10 |
| Concrete address extraction | 10/10 |
| Active/deprecated separation | 10/10 |
| V2/V3 separation | 10/10 |
| Network/address binding | 10/10 |
| Duplicate-address handling | 10/10 |
| Exhaustive network coverage | 5/10 |
| Direct bytecode | 0/10 |
| Flash capability | 0/10 |
| Current capacity | 0/10 |
| Pool discovery | 2/10 |
| Route | 0/10 |
| Simulation | 0/10 |
| Economics | 0/10 |
| Final executable count | NOT SCORED |

## Critical finding
The same Balancer Vault address can legitimately occur across multiple networks. Any registry keyed only by address would silently merge separate networks and corrupt the global universe.

## Decision
Sampled active Balancer Vault deployments accepted as canonical deployment evidence. Continue exhaustive network parsing and then live code/capability verification.

Live trading STOP.
