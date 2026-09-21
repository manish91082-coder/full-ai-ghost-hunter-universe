# PHASE 02 - FLASH-LOAN / ATOMIC-LIQUIDITY UNIVERSE

## Mission
Build the globally comprehensive, evidence-backed Atomic Liquidity Universe required by the final Ghost Hunter goal.

## Scope
Discover and verify, without assuming EVM-only semantics:
- flash loans
- flash borrows
- flash mints
- vault-based atomic liquidity
- protocol-specific same-transaction borrow/repay primitives
- technically equivalent atomic-liquidity mechanisms

## Required record dimensions
provider, chain/execution plane, protocol, mechanism, contract/program, assets, fee model, limits/capacity, callback/instruction rules, repayment semantics, atomicity rule, deployment evidence, source/ABI/code evidence, current lifecycle, dynamic availability, freshness, provenance, verification state, rejection/uncertainty reason.

## G02 acceptance gates
1. Identity and deployment verified.
2. Mechanism semantics verified from primary evidence.
3. Contract/program and callable path identified.
4. Fee and repayment behavior verified.
5. Capacity/availability model defined as dynamic where applicable.
6. Unsupported/unknown mechanisms remain explicit and fail closed.
7. Source/code evidence and provenance captured.
8. Cross-chain deduplication and execution-plane separation verified.
9. Adversarial discovery challenges the known-protocol list.
10. Saturation and exit review pass before G03.

## Non-goals
G02 does not authorize execution. Profitability, routes, pool state, risk and live execution remain downstream gates.

## Goal pull
A chain is useful to the final system when it can be intersected with a verified atomic-liquidity source and eventually a verified executable market route. G02 converts the world/network envelope into the financing-side universe of actual atomic capital.