# G02 MACRO-BATCH 020 — FACTORY RUNTIME CODE IDENTITY + SILO RUNTIME BOUNDARY PREPARATION

Date: 22 September 2026

## Objective

Advance G02 from deployment identity toward runtime-verifiable state without opening any downstream gate and without introducing authoritative runtime constants into executable source.

## Pre-change control

Authoritative main was re-verified before this change:
- SHA: 89ac75f31109a5178b28884ca896bf55990df188
- exact-main data-plane-ci: SUCCESS
- exact-main project-execution-verifier: SUCCESS

## Implemented

### 1. V2 factory runtime code identity

The generic V2 pair enumerator now performs a read-only `eth_getCode` observation against the configured factory at the same captured opening block used for pair-count enumeration.

Fail-closed conditions:
- provider changes during the preflight;
- empty or invalid factory bytecode;
- later freshness or completeness failure.

The exact factory runtime bytes are represented by SHA-256 evidence metadata in `EnumerationCompleteness` and in the runtime materializer output.

This proves only that code existed at the observed block. It does not prove:
- factory authenticity against a canonical implementation;
- current pair liquidity;
- current fee economics;
- callback authenticity;
- permission/authorization;
- profitability;
- execution eligibility.

### 2. Runtime observation artifact integration

`scripts/materialize_g02_v2_runtime.py` now persists `factory_bytecode_sha256` alongside the factory and pair observations.

The observation path remains:

external provider config → ProviderPool → read-only RpcTransport → block-pinned V2 enumeration → factory code evidence → pair completeness → pair code/token/reserve evidence → observation artifact.

No signing or transaction submission exists in this path.

### 3. Silo V3 denominator boundary

Fresh official Silo documentation confirms:
- Silo V3 markets are permissionless to deploy;
- each market consists of two ERC-4626 silos;
- SiloConfig exposes the two-silo relationship;
- a UI-listed market set is therefore not a complete deployment denominator.

Primary sources:
- https://docs.silo.finance/docs/users/core-concepts/silo/
- https://docs.silo.finance/docs/developers/protocol-overview/architecture/
- https://docs.silo.finance/docs/developers/dev-tutorials/silo-config/
- https://docs.silo.finance/docs/developers/dev-tutorials/create-a-silo/create-silo/

The repository's Silo API parser remains discovery-only. The next runtime boundary must verify chain-specific deployment, code identity, market structure, runtime configuration/liquidity and freshness from external runtime candidates.

## Safety decision

No execution authority was added.

## Remaining G02 blockers

1. Production RPC observation for QuickSwap/PancakeSwap factory sets.
2. Pair-level runtime state at production scale.
3. Pair bytecode classification/authenticity policy.
4. Current fee/configuration state.
5. Live liquidity-at-size.
6. Provider quorum and state consistency at production scale.
7. Silo market deployment denominator and runtime market verification.
8. Broader adversarial atomic-liquidity denominator closure.

## Gate state

- G01: FROZEN / BOUNDED EXIT PASS
- G02: ACTIVE / NOT SATURATED
- G03-G29: BLOCKED
- Execution authority: NONE
- Live trading: STOP
