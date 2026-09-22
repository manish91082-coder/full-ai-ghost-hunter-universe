# G02 PRIMARY MECHANISM DISCOVERY BATCH 001

Date: 21 September 2026

## Objective
Start G02 with a normalized atomic-liquidity primitive registry and verify mechanism semantics before attempting deployment-scale enumeration.

## Verified primitive families
1. Aave V3 flash loans.
2. Aave GHO flash minting.
3. Morpho Blue flash loans.
4. Uniswap V2 flash swaps.
5. Euler Vault Kit flash loans.
6. Project 0 / marginfi Solana flash loans.

Aave's current production documentation describes Aave V3 and current governance material demonstrates flash-borrower configuration. citeturn584306search6turn584306search2
Aave's GHO documentation identifies a Flashmint Facilitator that mirrors flash-loan functionality and governance-controlled bucket capacity. citeturn584306search0turn584306search10
Morpho documents same-transaction flashLoan execution with callback and repayment mechanics. citeturn362893search3
Uniswap V2's technical whitepaper documents flash swaps and end-of-transaction payment/return requirements. citeturn979903search7
Euler's current EVK whitepaper describes flashLoan behavior and hook-dependent fee/utilization rules. citeturn979903search1
Project 0 documents its bracketed flashloan instructions, final health check, revert behavior, current zero flashloan fee and Solana mainnet program deployment. citeturn362893search0turn362893search8turn362893search9

## Discovery candidates
Balancer, Venus and Radiant remain explicit discovery candidates. Their inclusion in the registry is not a capability assertion; mechanism semantics, deployments and current state must be verified before promotion.

## Safety boundary
No address, fee, capacity or deployment row in this research registry is execution authorization. Capacity, fees and availability are dynamic/current-state fields and must be re-read at runtime.

## State
Verified primitive records: 6
Discovery candidates: 3
Total G02 mechanism records: 9
Live trading: STOP

## Decision
CONTINUE_TARGETED_CYCLE. Next G02 work should enumerate production deployments and current on-chain/code evidence for the verified primitives, while adversarial discovery searches for additional native atomic-liquidity mechanisms.