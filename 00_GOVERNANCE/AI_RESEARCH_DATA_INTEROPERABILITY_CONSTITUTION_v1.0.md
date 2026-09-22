# AI RESEARCH + DATA INTEROPERABILITY CONSTITUTION v1.0

**Project:** FULL AI GHOST HUNTER UNIVERSE  
**Date:** 21 September 2026  
**Status:** GOVERNANCE CONTROL / ACTIVE  
**Live trading:** STOP

## 1. Purpose

This constitution defines how research, evidence, canonical data, AI agents, machine-readable schemas, audits, mission navigation and historical state must work together so that different AI models can consume the same project state without guessing, duplicating, drifting or silently changing meaning.

It is subordinate to the Operating Doctrine, No-Drift Saturation Control Charter, Saturation Gate Register, Repository Identity Lock and Data Lifecycle + Deduplication Control Policy.

## 2. Core design law

The project is a **machine-actionable, evidence-backed, provenance-preserving, deduplicated knowledge system**.

Every material fact follows:

DISCOVER → CAPTURE → IDENTIFY → NORMALIZE → DEDUPLICATE → VERIFY → CLASSIFY → MATERIALIZE → INDEX → TEST → AUDIT → FREEZE/UPDATE

No AI model may promote a discovery directly into execution truth.

## 3. Two-plane data architecture

### Plane A — Evidence / History

Purpose: preserve what was observed.

Properties:
- append-only;
- source-specific;
- timestamped;
- method recorded;
- block/version recorded when applicable;
- payload hash recorded;
- provenance recorded;
- freshness recorded;
- verification state recorded;
- contradictions preserved, never silently erased.

### Plane B — Current Canonical State

Purpose: provide one clean machine-readable current truth for computation.

Properties:
- one authoritative current record per canonical identity;
- deduplicated;
- updated in place;
- references evidence instead of copying evidence;
- explicit lifecycle/status;
- explicit freshness;
- explicit uncertainty/conflict;
- safe for runtime candidate selection.

Historical snapshots are never accidentally mixed into current runtime selection.

## 4. Canonical identity law

Identity resolution must use the strongest available namespace and execution semantics.

Priority:
1. authoritative global/native identifier;
2. CAIP-2 or equivalent canonical namespace where applicable;
3. EIP-155 numeric chain identity for EVM networks;
4. verified provider-specific identity;
5. verified composite identity;
6. aliases/names only as supporting evidence.

Name similarity is never identity proof.

Non-EVM systems must retain native semantics. Never fabricate EVM identifiers.

For contracts/pools/venues, identity must include the execution context required to distinguish materially different objects.

## 5. Canonical record pattern

Every major runtime object should expose, directly or by schema reference:

- canonical_id
- object_type
- namespace
- lifecycle_state
- verification_state
- first_seen
- last_seen
- last_verified
- freshness_deadline
- source_refs
- evidence_refs
- payload_hash / content_hash where applicable
- schema_version
- provenance
- relationships
- confidence/quality metadata
- change_reason when materially changed

Runtime-critical records additionally expose the exact fields required by their gate.

## 6. Evidence contract

Every authoritative claim must be traceable through:

source → observation → method → time/block/version → normalized identity → verification state → payload hash → freshness deadline → canonical record

Evidence quality is not the same as truth. A source may be authoritative for one field and insufficient for another.

AI-generated statements are hypotheses until independently evidenced.

## 7. Source hierarchy

Sources are classified, not blindly ranked globally:

S0 = direct on-chain/runtime observation  
S1 = official protocol/network/deployment registry or documentation  
S2 = official repository/source code/release artifact  
S3 = reputable structured indexer/data provider  
S4 = secondary technical analysis  
S5 = community/user-generated material  
S6 = AI-generated hypothesis

For execution-critical facts, prefer S0/S1/S2 and require corroboration when the domain demands it.

## 8. Research agent constitution

The research system is role-separated. A single model may perform several roles internally, but outputs must retain role labels.

Required logical roles:
1. Mission Navigator: protects final objective and current gate.
2. Discovery Agent: finds candidate sources/objects.
3. Source Critic: checks source authority and scope.
4. Identity Resolver: resolves aliases, rebrands and execution planes.
5. Normalization Agent: converts observations into canonical schema.
6. Deduplication Agent: prevents duplicate canonical objects.
7. Verification Agent: tests factual claims against primary evidence.
8. Contradiction Agent: isolates conflicting observations.
9. Coverage Agent: measures searched, covered, excluded, unknown and unsearched space.
10. Freshness Agent: tracks expiry and revalidation need.
11. Protocol/Domain Specialist: interprets domain-specific semantics.
12. Data Engineer: enforces schemas, indexes and referential integrity.
13. Adversarial Auditor: actively searches for missing data and false assumptions.
14. Reproduction Agent: reruns deterministic transformations/tests.
15. Saturation Judge: decides whether gate closure criteria are met.
16. Runtime Safety Agent: ensures stale/uncertain data cannot cross execution gates.
17. Change-Control Agent: ensures durable rules are changed only explicitly.

No role may silently override another role's evidence state.

## 9. AI research loop

For every research objective:

A. Read current canonical state and active gate.  
B. Read applicable governance contracts.  
C. Define search denominator and exclusions.  
D. Search independent discovery surfaces in parallel.  
E. Capture raw observations.  
F. Normalize identities.  
G. Deduplicate semantically.  
H. Cross-check critical fields.  
I. Verify with direct/primary evidence where required.  
J. Classify VERIFIED / PROVISIONAL / UNKNOWN / CONFLICTED / STALE / QUARANTINED / RETIRED.  
K. Merge only into current canonical state.  
L. Record delta, not a duplicate full dataset, in the batch report.  
M. Run structural, semantic and regression tests.  
N. Run adversarial gap audit.  
O. Search the discovered gaps again.  
P. Re-run deduplication and reconciliation.  
Q. Re-audit.  
R. Evaluate saturation criteria.  
S. Freeze the gate only when its denominator and evidence obligations are satisfied.

## 10. Data organization standard

The repository separates:

- governance/
- machine-readable canonical data/
- raw evidence/
- discovery inputs/
- domain registries/
- audits/
- tests/
- implementation/
- human-readable reports/
- historical snapshots/replay artifacts where required.

Machine-readable canonical data is authoritative for computation.

Markdown is explanatory/audit documentation, never the sole source for runtime computation.

## 11. Format law

Preferred machine formats:
- JSON for portable canonical records and registries;
- JSON Schema for validation contracts;
- JSONL for large append-oriented evidence/event streams;
- CSV only for flat interchange, never as the sole authoritative representation where relationships matter;
- Parquet or database tables may be introduced for scale, with schema/index contracts preserved;
- Markdown for human audit/readability;
- YAML only where configuration readability is materially useful and schema validation is enforced.

Every machine-readable object must declare or inherit a schema version.

## 12. Interoperability law

AI models must not need repository-specific hidden knowledge to interpret a record.

Therefore:
- field names are explicit;
- enumerations are controlled;
- units are explicit;
- timestamps are ISO-8601 UTC;
- chain IDs include namespace;
- addresses include network/context;
- monetary values include currency and precision;
- percentages/rates identify denominator and unit;
- hashes identify algorithm;
- references use stable IDs;
- relationships use explicit typed edges;
- unknown is represented explicitly, never as zero/null by implication.

The project may use JSON-LD/RDF/PROV-compatible mappings later, but no semantic dependency may be introduced without a documented schema contract. W3C PROV provides a useful interoperability model for entities, activities, agents and derivations, while FAIR emphasizes machine-actionable findability, accessibility, interoperability and reuse. citeturn0search8turn0search2

## 13. Unknown/null/zero law

These states are never interchangeable:

UNKNOWN = not established  
NOT_APPLICABLE = logically does not apply  
ZERO = verified numerical zero  
EMPTY = verified empty collection  
MISSING = expected field not supplied  
STALE = previously known but freshness expired  
CONFLICTED = credible sources disagree  
QUARANTINED = unsafe for use pending review

A missing value must never be interpreted as zero.

## 14. Relationship law

Use typed references instead of copied objects.

Examples:
chain → hosts → venue  
venue → deploys → contract  
venue → contains → pool  
pool → contains → token  
protocol → provides → atomic_liquidity  
route → traverses → pool/venue  
strategy → requires → capability  
strategy → evaluated_on → market_state  
evidence → supports → claim/record

This prevents duplication while retaining a navigable graph.

## 15. Current-state indexing

Every major domain must have:
- one current canonical registry;
- deterministic primary key;
- secondary lookup indexes;
- lifecycle index;
- verification index;
- freshness index;
- evidence-reference index;
- conflict/quarantine index;
- change/delta log.

A shard may exist for scale, but a global index must map each canonical object to exactly one owning shard.

## 16. Query contract for AI models

An AI consumer should be able to ask:

- What is the canonical object?
- Is it production?
- What is its verification state?
- What evidence supports it?
- When was it last verified?
- When does it become stale?
- What conflicts exist?
- What aliases exist?
- What changed since the previous checkpoint?
- What search space remains uncovered?
- Which gate does it belong to?
- What downstream objects depend on it?
- Is it execution-eligible?

If a query cannot answer these without reconstructing hidden context, the data contract is incomplete.

## 17. Mission navigation and anti-drift

Mission navigation is controlled by:

FINAL GOAL → ACTIVE GATE → CAPABILITY CONTRACT → CURRENT STATE → GAP REGISTER → NEXT MACRO-BATCH

Every batch must state:
- objective;
- active gate;
- current baseline;
- completed capability;
- new evidence;
- changes/merges;
- unresolved space;
- audit result;
- gate state;
- next objective;
- live authorization state.

A batch may not advance a blocked gate merely because useful work was discovered downstream.

## 18. Anti-duplication law

Before every material merge:
- compare canonical IDs;
- compare execution context;
- compare aliases;
- compare source references;
- compare deployment addresses;
- compare lifecycle;
- compare semantic relationships.

Duplicate-like observations are classified:
EXACT_DUPLICATE, ALIAS, REBRAND, SAME_NETWORK_DIFFERENT_EXECUTION_PLANE, RELATED_BUT_DISTINCT, CONFLICTED_IDENTITY, FALSE_MATCH, SUPERSEDED.

Only one canonical record survives for the same canonical identity.

## 19. Saturation law

“Saturated” never means “we searched a lot.”

A gate is saturated only when:
- scope is explicit;
- denominator is defensible;
- independent discovery surfaces are covered;
- candidates are normalized;
- duplicates are reconciled;
- primary facts are verified;
- exclusions are accounted for;
- unknown/conflict space is bounded;
- freshness policy exists;
- tests pass;
- audit finds no material resolvable gap;
- canonical state is duplicate-free;
- reproducibility is demonstrated;
- control files are synchronized;
- a durable Git checkpoint exists.

## 20. Adversarial audit law

The auditor must try to disprove completion.

Mandatory questions:
- What source family was not searched?
- Which objects may exist outside our current registry?
- Which aliases could have created duplicates?
- Which chains are non-EVM and therefore mis-modeled?
- Which records are stale?
- Which official deployments are not executable?
- Which capability claims lack direct evidence?
- Which data are copied rather than referenced?
- Which historical files could accidentally enter runtime selection?
- Which schema fields are ambiguous?
- Which AI assumptions were never independently verified?

## 21. Testing law

At minimum:
1. schema validation;
2. primary-key uniqueness;
3. foreign-key/reference integrity;
4. enum validity;
5. unit/precision validation;
6. timestamp validity;
7. hash integrity;
8. provenance completeness;
9. freshness logic;
10. deduplication regression;
11. lifecycle transition validity;
12. snapshot replay;
13. deterministic normalization;
14. conflict handling;
15. exclusion handling;
16. historical/current separation;
17. runtime fail-closed behavior;
18. no embedded authoritative runtime data;
19. cross-model parse compatibility;
20. adversarial negative tests.

## 22. Cross-model compatibility test

The same canonical dataset must be interpretable by different AI/model implementations without relying on conversation memory.

Compatibility test:
- Model/agent A reads schema and record.
- Model/agent B reads schema and record.
- Both identify the same canonical identity.
- Both distinguish UNKNOWN from ZERO.
- Both identify current vs historical state.
- Both locate evidence.
- Both respect lifecycle/freshness.
- Both produce the same eligibility classification when deterministic rules are involved.

Any disagreement becomes a schema/semantic audit finding.

## 23. Change-control law

Governance rules are not silently rewritten.

Changes require:
proposal → impact analysis → contradiction check → test update → audit → explicit change record → Git checkpoint.

Existing evidence is not rewritten to fit a new rule.

## 24. Runtime safety boundary

No research artifact authorizes live execution.

Execution requires independent gates for:
identity, current state, liquidity, route, simulation, economics, risk, security, provider health, authorization and freshness.

Live trading remains STOP until the project's independent readiness gates pass.

## 25. Final invariant

The system must be:

**ONE MISSION  
ONE GOVERNANCE CHAIN  
ONE CURRENT CANONICAL TRUTH PER DOMAIN  
MANY EVIDENCE SOURCES  
ZERO SILENT DUPLICATION  
ZERO HIDDEN ASSUMPTIONS  
FULL PROVENANCE  
EXPLICIT UNKNOWN/CONFLICT STATES  
REPRODUCIBLE TRANSFORMATIONS  
AUDITABLE HISTORY  
FAIL-CLOSED EXECUTION**

This constitution is permanent project control unless changed through explicit change-control.
