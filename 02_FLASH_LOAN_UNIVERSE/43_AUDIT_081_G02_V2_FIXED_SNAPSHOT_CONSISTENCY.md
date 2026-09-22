# G02 Audit 081 — V2 Fixed-Snapshot Pair-State Consistency

**Decision:** PASS FOR BOUNDED SNAPSHOT-CONSISTENCY HARDENING / G02 CONTINUE

The V2 materializer now binds every pair's token identities, reserves and runtime-bytecode evidence to one fixed per-factory block: the enumeration postflight block.

The fixed block is required to be at or below the provider head when each pair is read, and the existing freshness policy rejects an observation that becomes stale while the materializer is running. Provider identity is also required to remain consistent with the factory enumeration provider.

A complete factory therefore cannot silently mix pair states from different blocks inside one materialization result. Any snapshot drift, provider mismatch, stale observation or pair-state failure causes the factory to become FAILED_CLOSED and the overall materialization to remain INCOMPLETE.

This closes a real determinism/current-state consistency gap in the V2 observation substrate. It does not establish fee state, callback authenticity, executable liquidity-at-size, route profitability or execution authorization.

Production observation is still not claimed without actual GH_PROVIDER_RUNTIME execution. Live trading remains STOP.
