# AUDIT 078 — G02 SILO FACTORY GENESIS FULL-CHAIN FALLBACK

Date: 22 September 2026

## Result

PASS FOR HISTORICAL RANGE FALLBACK BOUNDARY / G02 CONTINUE

## Change

The 29 SiloFactory identities without pinned deployment CREATE receipts are no longer dead-ended by missing deployment metadata. Their scan lower bound is now block 0, with an explicit GENESIS_FULL_CHAIN_REQUIRED state.

This is a scan boundary, not a deployment claim. No deployment block, SiloFactory ID, or market identity is inferred from it.

## Coverage

- Bounded scan identities: 38
- Deployment-receipt verified starts: 9
- Genesis full-chain fallback starts: 29
- Missing/guessed start blocks: 0

## Safety boundary

The enumerator must scan block 0 through the observed current snapshot in chunks, preserve provider identity, enforce strict-current freshness, reject duplicate market identities, and fail closed on incomplete snapshots. A provider that cannot support the required historical range does not authorize a partial result.

## Outcome

G02 remains ACTIVE / NOT SATURATED.
G03-G29 remain BLOCKED.
Execution authority: NONE.
Live trading: STOP.

## Next

Run production-capable historical NewSilo enumeration for the 38 bounded identities where GH_PROVIDER_RUNTIME permits. Feed every discovered market into the existing two-vault Silo runtime binding. Continue V2 executable-market and adversarial atomic-liquidity denominator closure in parallel.
