# G01 COSMOS SEMANTIC RECONCILIATION QUEUE BATCH 037

Date: 21 September 2026

## Objective

Convert the 225-record Cosmos production observation set into a machine-readable, conservative semantic reconciliation queue in one executable CI path.

## Why this batch

The previous audit correctly identified 221 observations as unresolved after four direct overlaps. The next useful step is not 221 independent manual searches. It is deterministic grouping/classification so primary verification can be focused on high-information classes and duplicate candidates first.

## Implementation

Added:
- `scripts/reconcile_g01_cosmos.py`
- `.github/workflows/g01-cosmos-semantic-reconciliation.yml`

The workflow:
1. checks out the current canonical G01 registry;
2. re-materializes the pinned Cosmos production source;
3. creates a semantic queue;
4. preserves native chain IDs;
5. detects conservative exact/canonical-name overlaps;
6. flags possible execution-plane labels;
7. flags protocol/bridge/relationship labels for review;
8. sends all remaining candidates to PRIMARY_IDENTITY_REVIEW;
9. never promotes identity or authorizes execution;
10. uploads machine-readable evidence.

## No-drift rule

This batch does not mutate the current canonical registry. Queue classification is not identity verification.

## Saturation control

This is a bounded targeted cycle under the new exit-control register. It is not a new broad discovery sweep.

## Gate

G01 ACTIVE / NOT SATURATED.

G02-G29 BLOCKED.

LIVE TRADING = STOP.

## Next

Observe the CI queue artifact. If the queue is internally consistent, use its classification distribution to select the smallest high-information primary-verification set and then perform an explicit G01 exit review rather than restarting broad discovery.
