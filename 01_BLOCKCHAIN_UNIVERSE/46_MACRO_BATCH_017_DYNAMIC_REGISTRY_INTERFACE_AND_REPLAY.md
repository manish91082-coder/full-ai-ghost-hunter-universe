# MACRO-BATCH 017: DYNAMIC REGISTRY INTERFACE + REPLAY CONTRACT

Date: 21 September 2026

## Mission
Convert the dynamic-execution invariant into an executable architecture boundary. The code may define schemas and validation algorithms, but authoritative runtime universe data must enter through versioned external registries and current state collectors.

## Completed capability

### 1. Dynamic registry contract
Added:
- src/ghost_hunter/registry.py
- tests/test_registry.py

The registry layer defines:
- RegistryEntry with canonical identity and provenance
- RegistrySnapshot with version and manifest hash
- duplicate identity detection
- status control: ACTIVE / RETIRED / QUARANTINED
- authorized-version gate
- runtime projection only from loaded snapshots

No chain, RPC, address, token, pool, venue or strategy universe is embedded in the module.

### 2. Replay principle
A registry snapshot is treated as an input artifact, not as source code. A future collector/replay runner must be able to load snapshot A, produce behavior A, then load snapshot B and produce behavior B without changing Python source.

Required acceptance test:
**same executable + different valid runtime snapshot => different resulting state/opportunity universe.**

### 3. Fail-closed rules
Reject:
- missing registry identity
- invalid SHA-256 manifest/payload hash
- duplicate canonical identity
- unauthorized registry version
- retired/quarantined entries when a caller requires ACTIVE
- contradictory critical runtime state

### 4. External data hierarchy
Execution-time authority remains:
bootstrap configuration -> authorized/versioned registry -> dynamic discovery -> current on-chain state -> deterministic simulation -> economic/risk gate.

The registry is not a substitute for live verification. It is a durable, versioned source of topology/configuration.

## Live-data design constraint
Morpho's current documentation separates cursor-paginated market discovery from dynamic state and liquidity. The liquidity response includes current market liquidity and last-indexed-block metadata. Morpho also explicitly recommends fallback mechanisms because its API has no SLA. This supports the project's registry + dynamic-state + provider-fallback design, but does not itself authorize execution.

## Provider design
The collector will keep provider endpoints outside source code. web3.py documents provider selection through runtime configuration/environment and supports HTTP/WebSocket/IPC provider classes; multiple connections can be represented by separate Web3 instances. citeturn0search0

## Next integration
1. runtime-backed registry loader
2. signed/versioned manifest verification
3. dynamic chain/contract registry adapter
4. dynamic provider registry adapter
5. replay test proving snapshot substitution changes state without source modification
6. then market collectors and route graph

Live trading: STOP.
