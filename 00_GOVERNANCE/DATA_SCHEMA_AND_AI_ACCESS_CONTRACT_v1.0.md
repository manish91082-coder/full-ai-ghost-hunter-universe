# DATA SCHEMA + AI ACCESS CONTRACT v1.0

**Project:** FULL AI GHOST HUNTER UNIVERSE  
**Date:** 21 September 2026  
**Status:** ACTIVE GOVERNANCE CONTRACT  
**Live trading:** STOP

## 1. Canonical object envelope

All major machine-readable objects should use this conceptual envelope:

```json
{
  "schema_version": "domain.schema.v1",
  "canonical_id": "stable-id",
  "object_type": "chain|protocol|deployment|venue|token|pool|pair|strategy|route|provider|evidence",
  "namespace": "explicit-namespace",
  "lifecycle_state": "ACTIVE",
  "verification_state": "VERIFIED",
  "first_seen": "2026-09-21T00:00:00Z",
  "last_seen": "2026-09-21T00:00:00Z",
  "last_verified": "2026-09-21T00:00:00Z",
  "freshness_deadline": "2026-09-21T01:00:00Z",
  "source_refs": ["source-id"],
  "evidence_refs": ["evidence-id"],
  "content_hash": {"algorithm": "sha256", "value": "..." },
  "relationships": [],
  "attributes": {}
}
```

This is a conceptual contract, not a license to add redundant fields to every domain. Domain schemas may specialize it.

## 2. Required controlled states

### Lifecycle
DISCOVERED, ACTIVE, DEGRADED, RETIRED, SUPERSEDED, UNKNOWN, QUARANTINED

### Verification
UNVERIFIED, PROVISIONAL, VERIFIED, CONFLICTED, STALE, REJECTED

### Evidence quality
S0, S1, S2, S3, S4, S5, S6

### Data state
CURRENT, HISTORICAL, REPLAY_ONLY, NON_AUTHORITATIVE

## 3. Required semantic distinctions

Never collapse:
- chain identity vs execution environment;
- protocol vs deployment;
- deployment vs capability;
- capability vs liquidity;
- liquidity vs executable liquidity;
- route existence vs profitable route;
- source observation vs canonical fact;
- current state vs historical state;
- unknown vs zero;
- alias vs distinct object;
- testnet vs production;
- native execution plane vs EVM compatibility layer.

## 4. Domain primary keys

Minimum conceptual identity:

CHAIN:
namespace + canonical_network_id

PROTOCOL:
protocol_namespace + protocol_id + version

DEPLOYMENT:
network_identity + protocol_id + version + contract_role + address

VENUE:
network_identity + venue_namespace + venue_id + version

TOKEN:
network_identity/execution_plane + token_namespace + token_id

POOL:
network_identity + venue_identity + pool_id/address + topology discriminator

PAIR:
network_identity + venue_identity + pool_identity + ordered/typed asset identities + fee/hook/topology where applicable

STRATEGY:
strategy_namespace + strategy_id + version

ROUTE:
route_id derived from ordered execution edges plus state context/version

PROVIDER:
provider_id + network/method capability context

EVIDENCE:
source_id + observation_id/version + payload_hash

## 5. Units and numerical safety

Every economic quantity must define:
- numeric value;
- unit;
- currency/denomination;
- precision;
- timestamp/block context where applicable.

Do not mix:
USD, USDC, native gas token, basis points, percent, wei-like integers, human decimal values.

Rounding rules must be explicit and deterministic.

## 6. Time law

Use ISO-8601 UTC for timestamps.

On-chain state must also retain:
- chain/network identity;
- block/slot/version;
- block timestamp when available;
- observation timestamp.

Freshness is a policy field, not an assumption.

## 7. Evidence references

A canonical record should reference evidence rather than copy it.

Evidence records should retain:
- source identity;
- source URI/location where permitted;
- observation time;
- retrieval method;
- block/version;
- raw payload hash;
- parser/collector version;
- transformation IDs;
- verification result;
- freshness;
- licensing/access notes where relevant.

## 8. Delta/change representation

A batch must describe changes using operations such as:

ADD_OBJECT
MERGE_OBJECT
UPDATE_FIELD
ADD_ALIAS
RESOLVE_CONFLICT
MARK_STALE
RETIRE_OBJECT
SUPERSEDE_OBJECT
REJECT_CANDIDATE
REFRESH_EVIDENCE
CHANGE_SCHEMA
CHANGE_POLICY

A delta must identify before/after canonical identity and reason.

## 9. No-duplication query rule

A consumer must query the current canonical index first.

It may then follow:
canonical_id → evidence_refs → relationships → dependent objects.

It must not union all historical snapshots into a candidate list.

## 10. AI access modes

READ_CURRENT:
current canonical state only.

READ_EVIDENCE:
current canonical state plus linked evidence.

REPLAY:
historical snapshot + exact transformation/schema versions.

AUDIT:
current state + evidence + deltas + exclusions + unresolved space.

RUNTIME:
only current state objects that satisfy all independent readiness gates.

AI models must declare which access mode they are using when producing authoritative project decisions.

## 11. Machine-actionability checklist

A domain is AI-ready only if:
- schema is documented;
- identifiers are stable;
- fields have defined semantics;
- controlled states are enumerated;
- units are explicit;
- provenance is addressable;
- freshness is explicit;
- relationships are typed;
- duplicates are prevented;
- historical/current separation is enforced;
- validation tests exist;
- examples/fixtures exist;
- deterministic parsing exists.

## 12. Scaling law

If a registry becomes too large:
domain → deterministic shard → global index → canonical record.

Never:
domain → copied registry per batch → copied registry per AI → copied registry per chain.

The latter creates reconciliation failure.

## 13. Human-readable vs machine-readable

Markdown:
- explanations;
- audits;
- decisions;
- methodology;
- change records.

JSON/JSONL/DB:
- canonical records;
- evidence;
- indexes;
- deltas;
- machine queries.

Both must reference the same stable canonical IDs.

## 14. Minimum acceptance test

A new domain cannot become authoritative until a fresh AI consumer can:
1. discover the schema;
2. parse one record;
3. identify its canonical key;
4. locate evidence;
5. understand lifecycle and verification;
6. distinguish current from historical;
7. follow at least one relationship;
8. reproduce a deterministic transformation;
9. detect a duplicate;
10. fail closed on malformed/ambiguous data.

## 15. Compatibility target

The contract is intentionally model-neutral. GPT-family, Gemini-family, Claude-family, open-source models and future models must consume the same canonical machine-readable state without special hidden mappings.

Model-specific adapters may optimize retrieval or reasoning, but they may not redefine canonical meaning.

## 16. External standards alignment

The contract aligns conceptually with FAIR requirements for machine-actionable findability, accessibility, interoperability and reuse, including persistent identifiers, rich metadata, qualified references and detailed provenance. W3C PROV is a compatible provenance model for entities, activities, agents and derivations. citeturn0search2turn0search0turn0search8

## 17. Final rule

If a model cannot determine what a record means from the schema, metadata, controlled vocabulary and referenced evidence, the data contract is not complete.

Do not solve schema ambiguity with model memory or guesswork.
