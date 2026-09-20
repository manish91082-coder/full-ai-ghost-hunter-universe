# MACRO-BATCH 016 — DYNAMIC EXECUTION CONFIGURATION CONTRACT

Date: 21 Sept 2026
Status: LOCKED ARCHITECTURE + CODE

## User directive integrated
Execution-time behavior must not depend on hardcoded chains, RPC URLs, contract addresses, token lists, pool lists, strategy lists, gas assumptions, or opportunity parameters.

## Dynamic rule
Source code defines algorithms and validation rules. Runtime data defines:
- chains
- RPC/provider endpoints
- protocol deployments
- contract addresses
- tokens/pools/pairs
- fee tiers
- strategy registry
- gas parameters
- liquidity limits
- freshness windows
- route/search budgets
- economic thresholds
- execution permissions

## Configuration hierarchy
Environment/bootstrap config
→ signed/versioned configuration manifest
→ dynamic discovery registries
→ current on-chain state
→ deterministic decision

Critical values missing or contradictory = FAIL CLOSED.

## No static execution identity
Addresses, RPC endpoints and chain lists must never be embedded as execution constants in strategy/execution source.

## Dynamic economics
The $0.20 gate remains a mission constraint, but its runtime representation is configurable and must be validated against the mission policy before execution. It must not be silently changed by strategy code.

## Dynamic provider pool
Providers are discovered/configured externally. Health, latency, rate limits and availability determine runtime selection.

## Dynamic strategy registry
Strategies are data/registry entries with version, constraints, supported capabilities and risk requirements. New strategies can be added without rewriting the executor.

## Dynamic route universe
Pools/routes are discovered from registries and on-chain state. No hardcoded pair matrix is authoritative.

## Dynamic safety
Execution permission, chain enablement and kill-switch state are runtime policy inputs.

## Test requirement
Any future live-execution component must include tests proving that changing runtime registries/configuration changes behavior without source modification.

## Fresh evidence
Morpho's current API is cursor-paginated and separates immutable market discovery from dynamic state; liquidity responses include last indexed block. Its public API has no SLA and explicitly recommends fallbacks, supporting our externalized-provider/freshness architecture. citeturn0search0turn0search1turn0search2
Web3.py documents provider configuration through provider instances and environment-variable configuration, supporting external provider selection rather than embedded endpoints. citeturn0search3

## Live trading
STOP.
