# G02 MACRO-BATCH 017 — V2 ENUMERATION CONSISTENCY + EXTERNAL FACTORY INPUTS

Date: 21 September 2026

## Objective

Close the immediate safety gaps in the generic V2 pair enumeration boundary without promoting research evidence into execution authority.

## Implemented

1. Provider consistency is now fail-closed.
   - Factory pair count, pair-address enumeration, and enumeration pre/post block observations must use the same provider.
   - Pair state code, token, reserve and post-block observations must use the same provider as the opening block observation.
   - Provider rotation remains available at the transport layer, but a rotated observation cannot silently become part of one supposedly coherent V2 state snapshot.

2. Enumeration freshness is now bracketed.
   - A start block is captured before the factory count.
   - An end block is captured after the last pair.
   - The configured freshness policy must accept the complete enumeration window.
   - The result records factory-reported count and enumerated count. A count mismatch fails closed.
   - Safety bounds fail closed rather than truncating.

3. Pair runtime code identity is now observed.
   - eth_getCode is required before pair state is accepted.
   - Empty/non-hex bytecode fails closed.
   - Exact runtime bytecode is represented by a SHA-256 digest in the read-only observation object.
   - This is evidence of observed code bytes, not a universal code-identity claim or execution authorization.

4. External V2 factory inputs are materialized.
   - QuickSwap Polygon V2 factory/router.
   - PancakeSwap BNB Smart Chain V2 factory/router.
   - These values live in a machine-readable external configuration file, not in the executable enumerator.

## Safety Boundary

The new configuration is data, not executable authority. Factory deployment identity still does not establish pair liquidity, fee state, callback authenticity, executable capacity, or profitability.

## Remaining G02 Obligations

- Live RPC observation against the external factory set.
- Pair-level runtime enumeration at production scale.
- Pair bytecode classification and authenticity policy.
- Current fee/configuration state.
- Live reserves/liquidity-at-size.
- Provider quorum/state consistency at production scale.
- Silo V3 market-level enumeration.
- Broader adversarial atomic-liquidity denominator closure.

G02 remains ACTIVE / NOT SATURATED. G03-G29 remain BLOCKED. Execution authority NONE. Live trading STOP.
