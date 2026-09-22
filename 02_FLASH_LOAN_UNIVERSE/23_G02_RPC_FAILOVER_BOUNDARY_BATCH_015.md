# G02 RPC Failover Boundary — Macro-Batch 015

Date: 21 September 2026

## Objective

Close a concrete reliability gap in the read-only observation substrate without advancing execution authority.

## Change

The JSON-RPC transport now retries deterministically within the same logical observation request:

1. select the best currently available provider;
2. attempt the read-only request;
3. on provider failure, record failure/cooldown;
4. select the next eligible provider for the same network;
5. return the first valid observation;
6. if every configured provider fails, fail closed.

Quorum observation was also changed from a fixed first-N attempt set to a bounded walk across the available provider set until the requested number of successful observations is obtained or the provider set is exhausted.

## Safety Boundary

Provider switching is transport recovery, not state continuity. A returned observation still requires:

- network identity validation;
- block freshness validation;
- provenance capture;
- post-switch consistency/revalidation where required.

No transaction construction, signing or submission was added.

## Acceptance Tests

Added deterministic fixtures for:
- in-request provider failover;
- fail-closed quorum behavior when provider capacity is insufficient after failure.

Existing disagreement and read-only transport tests remain part of the suite.

## G02 Impact

This improves the transport substrate required for later market/pair enumeration. It does not close Silo market, QuickSwap pair or PancakeSwap pair denominators, and it does not authorize execution.

G02 remains ACTIVE / NOT SATURATED.
G03-G29 remain BLOCKED.
LIVE TRADING remains STOP.
