# G01 EXECUTION-PLANE PRIMARY VERIFICATION BATCH 045

Date: 21 September 2026

## Mission
Run a bounded verification cycle focused on unresolved execution-plane labels. Only current production identities supported by primary/official evidence are promoted. Historical or superseded labels are not allowed to become false current networks.

## Primary Verification Results

| Candidate | Canonical identity | Evidence result |
|---|---|---|
| Cronos zkEVM | eip155:388 | Mainnet identity verified |
| Immutable zkEVM | eip155:13371 | Mainnet identity verified |
| IOTA EVM | eip155:8822 | Mainnet identity verified |
| Ontology EVM | eip155:58 | MainNet EVM identity verified |
| Polygon zkEVM | eip155:1101 | Production deployment/identity verified |
| EOS EVM | eip155:17777 | Mainnet identity verified |
| Neo X | eip155:47763 | MainNet + EVM identity verified |

Cronos official network information gives Cronos zkEVM Mainnet chain ID 388 and distinguishes its testnet. citeturn1search9
Immutable's official documentation identifies mainnet 13371 and testnet 13473. citeturn1search1turn1search3
IOTA's official product documentation identifies IOTA EVM on IOTA Mainnet with chain ID 8822. citeturn1search2
Ontology's official developer documentation identifies MainNet chain ID 58 and testnet 5851. citeturn1search7
The official Uniswap governance deployment list identifies Polygon zkEVM with chain ID 1101 and production V3 deployment. citeturn3search1
EOS Network's official announcement states EOS EVM Mainnet is live and gives chain ID 17777. citeturn3search2
Neo's official site confirms Neo X MainNet is live and EVM-based; current chain ID 47763 is independently corroborated in Chainlink's official documentation surface. citeturn3search10turn3search3

## Superseded Label Handling
Astar zkEVM is **not** promoted as a separate current canonical network in this cycle. Astar's official material records the transition of Astar zkEVM toward Soneium. citeturn0search6turn0search9 The historical label remains in the unresolved/evidence queue rather than being silently merged or deleted.

## State Delta
- Prior canonical records: 75
- New primary promotions: 7
- Current canonical records: 82
- Duplicate canonical keys: 0
- Live trading: STOP

## Remaining Obligations
- Continue bounded verification of remaining high-materiality execution-plane labels.
- Resolve aliases/rebrands and stale labels explicitly.
- Complete native ecosystem denominator reconciliation.
- Perform adversarial missed-network review.
- Formal G01 saturation/exit review only after evidence obligations and material gaps are closed or explicitly bounded.

## Decision
CONTINUE_TARGETED_CYCLE.
