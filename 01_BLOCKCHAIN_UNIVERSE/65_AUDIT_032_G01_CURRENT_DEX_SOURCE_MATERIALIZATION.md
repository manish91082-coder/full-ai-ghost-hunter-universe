# AUDIT 032 — G01 CURRENT DEX SOURCE MATERIALIZATION

Date: 21 September 2026
Status: PARTIAL PASS

| Control | Result |
|---|---|
| Current DEX dashboard re-observed | PASS |
| Current discovery metrics captured | PASS |
| Official/free API source documented | PASS |
| Raw payload retention contract | PASS |
| Payload hashing requirement | PASS |
| DEX filtering contract | PASS |
| Protocol × chain extraction contract | PASS |
| 49-record canonical join target | PASS |
| Complete raw /protocols payload captured | BLOCKED |
| Complete DEX relationship denominator | BLOCKED |
| Primary identity/lifecycle verification | PENDING |
| Adversarial missed-network audit | PENDING |
| G01 saturation | NOT SATURATED |
| Live execution | STOP |

## Adversarial finding

A tempting but invalid shortcut would be to treat the dashboard's 290-chain
number or 794-protocol number as the final universe. That is explicitly
rejected. The project requires named records, identity resolution, lifecycle
verification, execution-plane separation and provenance.

The current web retrieval tool also rejects the complete /protocols response
because its response size exceeds the retrieval limit. Therefore no complete
materialization claim is made.

## Gate decision

G01 remains ACTIVE / NOT SATURATED.
