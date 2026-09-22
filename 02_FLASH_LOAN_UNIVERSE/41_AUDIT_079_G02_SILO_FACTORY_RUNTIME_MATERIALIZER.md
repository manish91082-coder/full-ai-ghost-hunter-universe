# G02 Audit 079 — SiloFactory Runtime Materializer

**Date:** 22 September 2026

## Decision

**PASS FOR READ-ONLY MATERIALIZATION BOUNDARY / G02 CONTINUE**

## Added

- Machine-readable materializer for every bounded SiloFactory scan-plan identity.
- Canonical NewSilo topic0 derived from the pinned Silo V3 interface declaration.
- Explicit separation of event discovery, runtime verification and complete-denominator status.
- Partial or failed output is permanently classified as INCOMPLETE.
- Runtime provider endpoints remain external through GH_PROVIDER_RUNTIME.
- No signing or transaction submission path.

## Bounded denominator

The scan plan contains 38 identities: 37 historical known-created factories plus 1 current Optimism deployment candidate.

## Production boundary

This commit does not claim that production RPC observation has run. A real runtime result requires external GH_PROVIDER_RUNTIME configuration and an actual execution of the materializer.

## Required production closure

Every identity must pass:

scan-plan identity -> provider observation -> complete NewSilo range -> strict-current snapshot -> market records -> downstream two-vault runtime verification.

The materializer does not establish profitability, route viability, authorization, hook/oracle safety, trade-size liquidity or execution eligibility.

The pinned Silo V3 interface declares NewSilo with three indexed address fields followed by three non-indexed address fields, and SiloFactory emits those fields in that order. The project's decoder boundary matches that ABI layout.

Live trading remains STOP.
