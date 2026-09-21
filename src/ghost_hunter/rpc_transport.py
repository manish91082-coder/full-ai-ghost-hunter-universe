"""Read-only JSON-RPC transport with provider rotation and quorum checks.

This module performs observation only. It never constructs, signs, or submits
transactions and contains no authoritative endpoint constants.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Callable
from urllib.request import Request, urlopen

from .provider_pool import ProviderPool
from .registry import RegistryError


@dataclass(frozen=True)
class RpcObservation:
    provider_id: str
    network_id: str
    method: str
    result: Any


class RpcTransport:
    def __init__(self, pool: ProviderPool, *, timeout_seconds: float = 5.0,
                 opener: Callable[..., Any] = urlopen) -> None:
        if timeout_seconds <= 0:
            raise RegistryError("timeout_seconds must be positive")
        self.pool = pool
        self.timeout_seconds = timeout_seconds
        self._opener = opener

    def call(self, network_id: str, method: str, params: list[Any] | None = None,
             *, now_tick: int = 0) -> RpcObservation:
        if not method.strip():
            raise RegistryError("RPC method is required")
        last_error: Exception | None = None
        attempted: set[str] = set()
        while True:
            providers = tuple(
                p for p in self.pool.available(network_id, now_tick)
                if p.provider_id not in attempted
            )
            if not providers:
                if last_error is not None:
                    raise RegistryError("all providers failed for network") from last_error
                raise RegistryError("all providers unavailable for network")
            provider = providers[0]
            attempted.add(provider.provider_id)
            try:
                decoded = self._request(provider, method, params)
                self.pool.record_success(provider.provider_id, network_id)
                return RpcObservation(provider.provider_id, network_id, method,
                                      decoded["result"])
            except Exception as exc:
                last_error = exc
                self.pool.record_failure(provider.provider_id, network_id, now_tick=now_tick,
                                         error=str(exc))

    def _request(self, provider: Any, method: str,
                 params: list[Any] | None) -> dict[str, Any]:
        payload = json.dumps({
            "jsonrpc": "2.0", "id": 1, "method": method,
            "params": params or [],
        }).encode("utf-8")
        request = Request(provider.endpoint, data=payload,
                          headers={"Content-Type": "application/json"},
                          method="POST")
        try:
            with self._opener(request, timeout=self.timeout_seconds) as response:
                decoded = json.loads(response.read().decode("utf-8"))
            if not isinstance(decoded, dict) or decoded.get("jsonrpc") != "2.0":
                raise RegistryError("invalid JSON-RPC response")
            if decoded.get("id") != 1:
                raise RegistryError("JSON-RPC response id mismatch")
            if "error" in decoded:
                raise RegistryError("JSON-RPC provider returned an error")
            if "result" not in decoded:
                raise RegistryError("JSON-RPC result missing")
            return decoded
        except RegistryError:
            raise
        except Exception as exc:
            raise RegistryError("RPC transport failure") from exc

    def quorum_call(self, network_id: str, method: str,
                    params: list[Any] | None = None, *, now_tick: int = 0,
                    quorum: int = 2) -> RpcObservation:
        if quorum < 2:
            raise RegistryError("quorum must be at least 2")
        providers = self.pool.available(network_id, now_tick)
        if len(providers) < quorum:
            raise RegistryError("insufficient providers for quorum")
        observations: list[RpcObservation] = []
        for provider in providers:
            if len(observations) >= quorum:
                break
            try:
                decoded = self._request(provider, method, params)
                observations.append(RpcObservation(provider.provider_id, network_id,
                                                   method, decoded["result"]))
                self.pool.record_success(provider.provider_id)
            except Exception as exc:
                self.pool.record_failure(provider.provider_id, now_tick=now_tick,
                                         error=str(exc))
        if len(observations) < quorum:
            raise RegistryError("quorum observation unavailable")
        first = observations[0].result
        if any(o.result != first for o in observations[1:]):
            raise RegistryError("provider quorum disagreement")
        return observations[0]
