# G01 DEX LABEL RECONCILIATION BATCH 031

Date: 21 September 2026

Objective: convert the 419 observed DEX chain labels into a deterministic reconciliation queue without treating names as identity.

The corrected materialization produced 419 unique labels. 36 matched the current G01 union by name-level comparison. The remaining 383 labels are preserved as explicit unresolved observations.

This batch does not promote unresolved labels to canonical chains.

Reconciliation classes:
- EXACT_NAME_MATCH: exact normalized name match already represented in current union.
- LIKELY_ALIAS_CANDIDATE: deterministic lexical relationship suggests a possible alias, but primary identity evidence is required.
- EXECUTION_PLANE_VARIANT_CANDIDATE: label may represent a distinct execution plane or VM; never merge by name alone.
- POSSIBLE_NETWORK_CANDIDATE: label is structurally chain-like but identity/lifecycle remains unverified.
- NON_CHAIN_OR_PROTOCOL_LABEL_CANDIDATE: label may be a protocol/product/asset/ecosystem label rather than a canonical network.
- UNKNOWN: insufficient evidence for safe classification.

The authoritative current registry remains the single canonical state. This batch creates a reconciliation queue and evidence obligations only.

Hard rule: a DEX observation is not evidence of flash liquidity, executable trading, liquidity-at-size, route viability, simulation success, profitability or authorization.

Next: resolve the highest-information aliases and execution-plane variants first using primary network documentation and native registries, then expand to the remaining candidate set and run an adversarial missed-network audit.
