# G02 Audit 080 — V2 Factory Runtime Materializer

**Decision:** PASS FOR READ-ONLY V2 OBSERVATION BOUNDARY / G02 CONTINUE

This batch adds a machine-readable materializer for the configured QuickSwap V2 Polygon and PancakeSwap V2 BNB Smart Chain factory inputs. It enumerates the complete factory-reported pair count under an explicit safety bound, then reads token0/token1/reserves/runtime bytecode for every returned pair at the observed block.

A factory is COMPLETE only when every configured factory materializes successfully and its enumerated count equals its factory-reported count. RPC/provider failures produce FAILED_CLOSED and never become a complete denominator.

The configured factories are observation inputs only. This artifact does not establish fee state, callback authenticity, executable liquidity-at-size, route profitability or execution authority.

Production observation is not claimed until GH_PROVIDER_RUNTIME is actually configured and the script is executed. Live trading remains STOP.
