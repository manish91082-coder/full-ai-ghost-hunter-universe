# G02 Silo V3 Market Enumeration Evidence — 21 September 2026

## Primary-source findings

The current Silo V3 documentation states that markets are permissionless to deploy and that each market consists of two ERC-4626 vaults. Therefore a finite UI-listed market set cannot be treated as the complete market universe.

The official Silo V3 API documentation states that its public API exposes comprehensive V3 silo/vault protocol data and provides a GraphQL endpoint at https://api-v3.silo.finance, including a markets query. The API is treated here as discovery/data evidence, not as on-chain execution authority.

## Required architecture

Silo discovery must therefore be split:

1. Discovery denominator: external Silo API / event or factory-derived market candidates.
2. Deployment verification: runtime chain-specific contract identity.
3. Market structure verification: SiloConfig, silo0, silo1 and token identities.
4. Runtime state: assets, borrowable liquidity, caps, fees, hooks and other market configuration.
5. Code identity: runtime bytecode / implementation identity where applicable.
6. Freshness: current block/state observation.
7. Canonical identity: (network, market/silo configuration identity) with duplicate fail-closed handling.

No API-discovered market is execution-eligible merely because it appears in the API.

## Sources

Official Silo V3 API documentation: https://docs.silo.finance/docs/developers/apis/api-overview

Official Silo V3 market architecture: https://docs.silo.finance/docs/developers/protocol-overview/architecture/

Official Silo V3 lending-market documentation: https://docs.silo.finance/docs/users/core-concepts/silo/

## Gate decision

This closes a discovery-boundary design gap, not runtime market saturation. G02 remains ACTIVE / NOT SATURATED.
