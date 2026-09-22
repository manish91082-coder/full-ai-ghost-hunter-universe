# AUDIT 076 — G02 SILO FACTORY ACTIVITY CORROBORATION

Date: 22 September 2026

## Result

PASS FOR CORROBORATING SUBSYSTEM / G02 CONTINUE

## Scope

The pinned Silo V3 source commit provides a secondary operational metadata file, silo-core/scripts/withdrawFeesForge/factories.json, containing 38 exact (network,factory) identities and a startSiloId value for each.

This corroborates factory activity/operational handling for the bounded 38-identity scan denominator and independently catches identity-key mistakes.

## Critical boundary

startSiloId is NOT a deployment block and is NOT converted into a block number. It is never used to reconstruct SiloFactory IDs from NewSilo log ordering. Historical scan start remains blocked unless exact deployment CREATE-block evidence exists for the same (network_id,factory) identity.

The Sonic/XDC identical factory address is explicitly treated as two identities.

## Outcome

- 38/38 bounded identities corroborated by the secondary source.
- 0 new historical scan-start blocks authorized by this artifact.
- G02 remains ACTIVE / NOT SATURATED.
- G03-G29 remain BLOCKED.
- Execution authority: NONE.
- Live trading: STOP.
