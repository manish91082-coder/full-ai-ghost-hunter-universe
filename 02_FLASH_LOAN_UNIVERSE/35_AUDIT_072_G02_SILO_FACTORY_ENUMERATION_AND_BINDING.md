# AUDIT 072 — G02 SILO V3 FACTORY ENUMERATION + MARKET BINDING

Date: 22 September 2026

## Result

**PASS FOR THIS BOUNDED SUBSYSTEM / G02 CONTINUE**

## Completed

- Implemented read-only SiloFactory historical `NewSilo` event enumeration.
- Enforced externally supplied factory identity and event topic.
- Used chunked `eth_getLogs` scanning with pinned end block.
- Enforced provider identity consistency across the scan.
- Enforced strict-current snapshot closure and freshness validation.
- Rejected duplicate market identities.
- Explicitly avoided deriving SiloFactory IDs from log order.
- Added a fail-closed market binding layer that sends every enumerated market's two vaults to the existing Silo V3 runtime verifier.
- Binding requires event/runtime SiloConfig agreement, vault identity agreement, network identity agreement and provider identity agreement.
- Incomplete factory snapshots cannot be bound as runtime-observed markets.
- Added deterministic tests for event decoding, duplicate rejection, snapshot advance rejection, binding completeness, runtime mismatch, incomplete snapshots and provider mismatch.

## Exact verification

Authoritative current `main` HEAD:

`58afea8aa9773787658b7bf38f2930768794453d`

Exact `data-plane-ci`:

- Run ID: `35720727371`
- head SHA: `58afea8aa9773787658b7bf38f2930768794453d`
- status: completed
- conclusion: SUCCESS

Exact `project-execution-verifier`:

- Run ID: `35720764207`
- head SHA: `58afea8aa9773787658b7bf38f2930768794453d`
- status: completed
- conclusion: SUCCESS

A cancelled verifier attempt for the same SHA existed before the final verifier run. It is not treated as the authoritative verification result.

## Still open

- No production RPC observation has been claimed or executed.
- Exhaustive SiloFactory identity denominator remains open.
- Historical factory discovery across all relevant SiloFactory deployments remains open.
- Silo implementation/proxy authenticity remains open.
- Authorization, hooks and oracle runtime state remain open.
- Executable liquidity at actual trade size remains open.
- Flash-fee quote at actual trade size remains open.
- Broader adversarial atomic-liquidity denominator remains open.

## Gate decision

G02 remains **ACTIVE / NOT SATURATED**.
G03-G29 remain **BLOCKED**.
Execution authority: **NONE**.
Live trading: **STOP**.

## Next macro objective

Close the Silo denominator rather than adding isolated candidates: enumerate all relevant SiloFactory identities, prove their historical market-event ranges, reconcile discovered markets, then apply the runtime binding/verification boundary with completeness evidence. In parallel, continue the V2 executable-market denominator and adversarial atomic-mechanism gap audit.
