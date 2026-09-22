"""Fail-closed freshness and observation-consistency contracts.

Pure validation only. No network I/O and no authoritative chain constants.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .registry import RegistryError
from .rpc_transport import RpcObservation


@dataclass(frozen=True)
class FreshnessPolicy:
    max_block_lag: int = 2

    def validate(self) -> None:
        if self.max_block_lag < 0:
            raise RegistryError("max_block_lag must be non-negative")


@dataclass(frozen=True)
class FreshnessObservation:
    network_id: str
    provider_id: str
    observed_block: int
    latest_block: int

    @property
    def lag(self) -> int:
        return self.latest_block - self.observed_block


def validate_block_numbers(observed_block: int, latest_block: int,
                           policy: FreshnessPolicy) -> FreshnessObservation:
    policy.validate()
    if observed_block < 0 or latest_block < 0:
        raise RegistryError("block number cannot be negative")
    if observed_block > latest_block:
        raise RegistryError("observed block is ahead of latest block")
    if latest_block - observed_block > policy.max_block_lag:
        raise RegistryError("observation is stale")
    return FreshnessObservation("", "", observed_block, latest_block)


def require_same_network(previous: RpcObservation, current: RpcObservation) -> None:
    if previous.network_id != current.network_id:
        raise RegistryError("provider switch changed network identity")
    if previous.method != current.method:
        raise RegistryError("revalidation method mismatch")


def require_revalidated(previous: RpcObservation, current: RpcObservation) -> None:
    require_same_network(previous, current)
    if previous.result != current.result:
        raise RegistryError("revalidation state disagreement")


def parse_hex_block(value: Any) -> int:
    if not isinstance(value, str) or not value.startswith("0x"):
        raise RegistryError("block number must be hexadecimal JSON-RPC value")
    try:
        return int(value, 16)
    except ValueError as exc:
        raise RegistryError("invalid hexadecimal block number") from exc
