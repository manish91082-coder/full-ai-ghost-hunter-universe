# CI FAILURE ROOT-CAUSE AUDIT — G02 — 21 September 2026

## Scope

Audited the repository state from the G01 final exit handoff through current main, including the CI workflow, machine-readable G02 registries, all discovered pytest files, G02 runtime tests, and the failover implementation introduced before the failing runs.

## Findings

### 1. CI environment was not deterministic
The workflow invoked pytest -q after actions/setup-python, but did not explicitly install pytest. The workflow has now been changed to install pytest and invoke python -m pytest -q.

### 2. Python import path was inconsistent
The repository uses a src/ghost_hunter layout. Several tests use from ghost_hunter... while others use from src.ghost_hunter.... The CI workflow did not define PYTHONPATH. The workflow now sets PYTHONPATH=src for the test step.

### 3. A concrete regression existed in the failover test
RpcTransport.call() was deliberately changed in Batch 015 to retry the same logical request through another available provider after failure. The existing test_failure_rotates_provider still expected the first call to raise RegistryError, which contradicted the new retry contract.

The test has been corrected to assert that the same call succeeds through provider p2 after p1 fails.

### 4. G02 machine-readable validation is not the observed failure
Current canonical state was parsed directly:
- mechanism records: 21
- declared mechanism total: 21
- deployment records: 38
- deployment duplicate keys under the CI identity formula: 0
- execution eligibility: all 38 = NEVER_FROM_RESEARCH

Therefore the CI machine-state assertions are internally satisfied by current repository data.

## Important verification limitation

The available GitHub workflow-run connector in this environment exposes pull-request-associated runs only. It does not expose the push-triggered main runs visible in the repository Actions UI. Therefore the exact historical red-job log cannot be independently retrieved from that connector.

The supplied screenshot is direct evidence that the displayed G02 runs failed. Repository inspection identifies the concrete deterministic test regression above and the CI-environment hardening gap.

## Correction applied

- .github/workflows/data-plane-ci.yml
  - explicit pytest installation
  - PYTHONPATH=src
  - python -m pytest -q
- tests/test_rpc_transport.py
  - failover test aligned with in-request retry contract

## Gate decision

G02 remains ACTIVE / NOT SATURATED.
No execution authority was added.
Live trading remains STOP.
No CI GREEN claim is made until a fresh push-triggered data-plane-ci run is visibly successful.
