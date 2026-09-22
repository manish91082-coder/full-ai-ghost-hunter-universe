# 🛡️ OPERATING DOCTRINE — MILITARY / SURGICAL / AVIATION / ZERO-TRUST

**Project:** FULL AI GHOST HUNTER UNIVERSE  
**Repository:** `manish91082-coder/full-ai-ghost-hunter-universe`  
**Branch:** `main`  
**Status:** GOVERNANCE LOCKED — LIVE TRADING STOP  
**Version:** v1.0  
**Language:** Hindi-first

---

## 1. COMMAND PRINCIPLE

Project का नेतृत्व goal-centric होगा:

**Final Goal → Required Capability → Evidence → Architecture → Implementation → Test → Audit → Saturation → Deployment**

किसी feature, library, model, chain या strategy को केवल इसलिए नहीं जोड़ा जाएगा क्योंकि वह interesting है। हर निर्णय final live-hunting objective और safety/economic gates के विरुद्ध evaluate होगा।

---

## 2. DISCIPLINE STANDARD

हर engineering/research action पर चार discipline layers लागू होंगी:

### Military-grade discipline
- स्पष्ट mission;
- explicit state;
- controlled changes;
- no silent assumptions;
- no unauthorized scope drift;
- rollback/kill capability।

### Surgical discipline
- smallest justified change;
- exact evidence;
- dependency awareness;
- precondition/postcondition;
- failure isolation;
- no blind execution।

### Aviation-grade discipline
- pre-flight checks;
- independent verification;
- redundancy;
- health monitoring;
- abort criteria;
- incident recording;
- fail-safe behavior।

### Zero-trust discipline
- कोई external source automatically trusted नहीं;
- कोई model output truth नहीं;
- कोई quote guaranteed नहीं;
- कोई address label के आधार पर trusted नहीं;
- कोई RPC/provider inherently trusted नहीं;
- unknown remains unknown until verified।

---

## 3. ZERO-COST-FIRST RULE

Architecture का default:

**Free/Public/Open-source → Local → Free-tier distributed → Paid only if explicitly justified**

Paid infrastructure को default dependency नहीं बनाया जाएगा।

Zero-cost का अर्थ:
- licensing cost को minimize करना;
- free/public infrastructure को प्राथमिकता;
- lightweight compute;
- local caching;
- deterministic preprocessing;
- efficient polling/eventing;
- unnecessary cloud खर्च से बचना।

Zero-cost infrastructure को “always reliable” मानना prohibited है। Reliability evidence से तय होगी।

---

## 4. AI-FIRST, BUT NOT AI-TRUST

AI का उपयोग:
- discovery;
- classification;
- research;
- hypothesis generation;
- strategy generation;
- route optimization;
- anomaly detection;
- failure analysis;
- audit assistance;
- documentation;
- optimization;
- learning।

लेकिन:

**AI suggestion ≠ verified fact**  
**AI strategy ≠ executable strategy**  
**AI decision ≠ unrestricted wallet authority**

Final execution gates deterministic और independently validated होंगे।

---

## 5. AUTONOMY MODEL

Final system का लक्ष्य:

**Human sets mission/constraints → System operates autonomously inside hard boundaries.**

System को eventually स्वयं:
- discover;
- evaluate;
- prioritize;
- simulate;
- reject;
- execute when authorized;
- verify;
- learn;
- audit;
- recover;
- update its knowledge

करना चाहिए।

लेकिन hard safety/economic/security constraints model के बाहर enforce किए जाएँगे जहाँ संभव हो।

---

## 6. EXECUTION ECONOMIC LAW

Configured threshold:

**Expected Net Profit > USD 0.20**

Net calculation में applicable measurable costs शामिल होंगे:

- flash-loan fee;
- DEX fees;
- gas;
- slippage;
- execution costs;
- other known mandatory costs;
- configured safety buffer जहां आवश्यक।

महत्वपूर्ण:

**Expected profit ≠ guaranteed realized profit.**

अगर required costs reliably estimate नहीं हो सकते, transaction fail-closed होगा।

---

## 7. NO-GUESS / NO-FIXED-LOSS LAW

“Zero gas fees loss” को engineering objective माना जाएगा, guaranteed universal market property नहीं।

Trade reject होगा यदि:
- simulation revert;
- insufficient liquidity;
- stale/contradictory critical data;
- route invalid;
- repayment uncertain;
- provider unhealthy;
- gas/economic model unreliable;
- required contract state unverifiable;
- expected economics threshold से नीचे;
- execution risk gate fail।

---

## 8. OPPORTUNITY NON-DROP PRINCIPLE

Goal है कि valid profitable opportunities अनावश्यक रूप से miss न हों।

इसके लिए architecture:
- event-driven detection;
- parallel strategy workers;
- priority queues;
- deduplication;
- opportunity reservation;
- route caching;
- precomputed static universe;
- fast simulation;
- RPC/provider pools;
- workload partitioning;
- latency measurement

का उपयोग करेगा।

लेकिन unsafe/insufficiently verified opportunity को “profit बचाने” के लिए execute नहीं किया जाएगा।

---

## 9. PARALLEL STRATEGY PRINCIPLE

सभी strategies को एक giant sequential loop में नहीं चलाया जाएगा।

Architecture:

**Strategy Universe → Partition → Parallel Workers → Shared Market State → Candidate Queue → Simulation Queue → Risk/Profit Gates**

Strategy classes और chain/venue partitions independently scale होंगे।

एक failed strategy पूरे hunter को रोक नहीं सकेगी।

---

## 10. MINUTE-LEVEL HUNTING PRINCIPLE

Target:

**हर relevant strategy को minute-level या बेहतर evaluation coverage देना।**

यह target chain block time, RPC limits, data freshness, compute, rate limits और safety constraints के अधीन होगा।

जहाँ block/event frequency minute से तेज है वहाँ event-driven execution preferred होगा।

जहाँ event subscription practical नहीं है वहाँ adaptive polling होगा।

---

## 11. PRECOMPUTE-FIRST PRINCIPLE

Live hunting से पहले static information जितनी संभव हो उतनी verified रूप से precompute होगी:

- chain IDs;
- native assets;
- protocol contracts;
- flash-loan contracts;
- DEX factories;
- routers;
- quoters;
- pool managers;
- token addresses;
- pool/pair addresses;
- fee tiers;
- ABI/source references;
- deployment metadata;
- protocol constraints;
- discovery mechanisms।

Dynamic state live layer में रहेगा।

---

## 12. EVIDENCE LAW

हर critical fact का provenance होना चाहिए:

**Source → Timestamp → Network → Address/Identifier → Verification Method → Confidence → Evidence Reference**

Conflicting sources को merge करके छुपाया नहीं जाएगा। Conflict record बनेगा।

---

## 13. SATURATION LAW

हर phase पर mandatory loop:

**Discover → Normalize → Cross-check → Verify → Test → Audit → Gap Analysis → Missing Discovery → Add → Re-test → Re-audit → Saturation Check**

जब तक predefined acceptance criteria pass नहीं होते, phase complete नहीं माना जाएगा।

---

## 14. MATHEMATICAL COMPLETENESS

हर phase में measurable dimensions define होंगे।

उदाहरण:
- discovery coverage;
- verification coverage;
- address coverage;
- contract coverage;
- data freshness;
- evidence coverage;
- test coverage;
- failure-mode coverage;
- strategy coverage;
- execution coverage।

**10/10 या 100/100 केवल documented criteria के against दिया जाएगा।**

Absolute “world is permanently complete” claim prohibited है।

---

## 15. CHANGE CONTROL

कोई material architectural change:
1. reason;
2. evidence;
3. impact;
4. alternatives;
5. risk;
6. validation;
7. decision;
8. affected files

के साथ logged होगा।

---

## 16. FAILURE MANAGEMENT

Failure को hide नहीं किया जाएगा।

हर meaningful failure:
**Observed → Classified → Reproduced where possible → Root cause → Containment → Fix → Regression test → Log**

---

## 17. LIVE-TRADING AUTHORIZATION

Live trading तब तक **STOP** रहेगा जब तक required readiness gates independently pass नहीं होते।

Minimum gates:
- verified chain universe;
- verified flash-liquidity universe;
- verified venue/address universe;
- route discovery;
- fresh market data;
- deterministic simulation;
- profitability accounting;
- risk gates;
- security controls;
- kill switch;
- observability;
- controlled deployment test;
- rollback/recovery capability.

---

## 18. DEFINITION OF DONE

किसी phase का “done” केवल file created या code written होना नहीं है।

Phase Done =
**Scope Covered + Evidence + Verification + Tests + Audit + Gap Review + Acceptance Criteria + Logged Decision**

---

## 19. RESPONSE-TO-REPOSITORY SYNCHRONIZATION RULE

हर material project iteration के बाद repository control state synchronize होगी:

- relevant phase file;
- PROJECT_STATUS.md;
- PROJECT_MEMORY.md when a durable decision is locked;
- PROJECT_DETAILS.md when specification changes;
- PROJECT_LOG.md for chronology;
- README.md when public project state changes.

---

## 20. CURRENT COMMAND

**Governance is now locked.**

Next command target:

# PHASE 01 — GLOBAL BLOCKCHAIN UNIVERSE

Phase 01 का पहला deliverable होगा:

**Evidence-backed candidate blockchain universe + inclusion criteria + discovery source matrix + capability verification schema + audit/gap framework.**

Live trading remains STOP.
