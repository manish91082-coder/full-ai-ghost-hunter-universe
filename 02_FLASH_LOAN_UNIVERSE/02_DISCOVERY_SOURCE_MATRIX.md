# G02 DISCOVERY SOURCE MATRIX - INITIAL

Date: 21 September 2026

| Family | Primary source | Initial status | Required follow-up |
|---|---|---|---|
| Aave | Official Aave documentation/governance | DISCOVERED | Enumerate production deployments and exact flash-loan state |
| Morpho | Official Morpho Docs | VERIFIED_PRIMITIVE | Enumerate all production deployments and current capacity |
| Balancer | Official Balancer Docs | DISCOVERED | Enumerate Vault generations/networks and exact atomic-loan semantics |
| Uniswap V2 | Official Uniswap technical documentation | VERIFIED_PRIMITIVE | Enumerate production factories/pairs and flash-swap execution paths |
| Euler EVK | Official Euler EVK documentation | VERIFIED_PRIMITIVE | Enumerate production networks/hooks/fee variants |
| Project 0 / marginfi | Official Project 0 documentation | VERIFIED_PRIMITIVE | Verify current Solana programs, instructions and dynamic bank capacity |
| Venus | Official Venus documentation | DISCOVERY_FAMILY | Verify current flash-loan mechanism/deployments |
| Radiant | Official Radiant documentation | DISCOVERY_FAMILY | Verify current v3 mechanism/deployments and exclude deprecated v1 |
| Additional native mechanisms | Native protocol registries / primary code | OPEN | Adversarial discovery required |

## Current primary evidence examples
Morpho documents flashLoan with same-transaction repayment and callback semantics.
Project 0 documents paired start/end flashloan instructions, same-transaction final health validation and currently states no flashloan fee.
Uniswap V2 technical documentation describes flash swaps that release assets and require payment/return by the end of the transaction.
Euler's current EVK documentation describes flash-loan hooks and notes that a hook may enforce a fee or utilization cap.
Balancer's current documentation exposes the v3 developer, integration and deployment surface.

## Rule
This matrix is a discovery/verification starting point, not a complete protocol list and not execution authorization. G02 saturation requires adversarial expansion beyond these known families.