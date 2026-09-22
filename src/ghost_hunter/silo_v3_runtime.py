"""Read-only Silo V3 market runtime verification boundary.

This boundary verifies externally supplied Silo candidates against live runtime
state. It never discovers a finite market universe by itself and never grants
execution authority.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass

from .registry import RegistryError
from .rpc_transport import RpcObservation, RpcTransport
from .runtime_freshness import FreshnessPolicy, parse_hex_block, validate_block_numbers

CONFIG_SELECTOR = "0x79502c55"
GET_SILOS_SELECTOR = "0xaecc90cb"
ASSET_SELECTOR = "0x38d52e0f"
GET_LIQUIDITY_SELECTOR = "0x0910a510"
MAX_FLASH_LOAN_SELECTOR = "0x613255ab"
FLASH_FEE_SELECTOR = "0xd9d98ce4"
FACTORY_SELECTOR = "0xc45a0155"
BLOCK_METHOD = "eth_blockNumber"
GET_CODE_METHOD = "eth_getCode"
CALL_METHOD = "eth_call"

@dataclass(frozen=True)
class SiloRuntimeState:
    network_id: str
    silo: str
    config: str
    silo0: str
    silo1: str
    asset: str
    liquidity: int
    max_flash_loan: int
    flash_fee_probe_amount: int
    flash_fee: int
    factory: str
    observed_block: int
    provider_id: str
    silo_bytecode_sha256: str
    config_bytecode_sha256: str

def _word(value: str) -> str:
    if not isinstance(value, str) or not value.startswith("0x"):
        raise RegistryError("RPC hex result required")
    raw = value[2:]
    if not raw or len(raw) % 64:
        raise RegistryError("invalid ABI word encoding")
    return raw

def _address(value: str) -> str:
    raw = _word(value)
    return "0x" + raw[-40:]

def _uint(value: str) -> int:
    return int(_word(value)[-64:], 16)

def _address_calldata(selector: str, address: str) -> str:
    if not isinstance(address, str) or not address.startswith("0x") or len(address) != 42:
        raise RegistryError("invalid address")
    return selector + address[2:].lower().rjust(64, "0")

def _address_uint_calldata(selector: str, address: str, amount: int) -> str:
    if amount < 0:
        raise RegistryError("probe amount must be non-negative")
    return _address_calldata(selector, address) + format(amount, "064x")

def _bytecode_sha256(value: str) -> str:
    if not isinstance(value, str) or not value.startswith("0x"):
        raise RegistryError("RPC bytecode hex result required")
    raw = value[2:]
    if not raw or len(raw) % 2:
        raise RegistryError("invalid runtime bytecode")
    try:
        payload = bytes.fromhex(raw)
    except ValueError as exc:
        raise RegistryError("invalid runtime bytecode") from exc
    return hashlib.sha256(payload).hexdigest()

def _same_provider(observations: tuple[RpcObservation, ...], provider_id: str) -> None:
    if any(obs.provider_id != provider_id for obs in observations):
        raise RegistryError("provider changed during Silo runtime observation")

class SiloV3RuntimeVerifier:
    def __init__(self, transport: RpcTransport, freshness: FreshnessPolicy) -> None:
        self.transport = transport
        self.freshness = freshness

    def verify(self, network_id: str, silo: str, *, flash_fee_probe_amount: int = 1) -> SiloRuntimeState:
        if not silo.startswith("0x") or len(silo) != 42:
            raise RegistryError("invalid Silo address")
        if flash_fee_probe_amount < 0:
            raise RegistryError("probe amount must be non-negative")

        before = self.transport.call(network_id, BLOCK_METHOD)
        before_block = parse_hex_block(before.result)
        block_tag = "0x" + format(before_block, "x")

        silo_code = self.transport.call(network_id, GET_CODE_METHOD, [silo, block_tag])
        config_obs = self.transport.call(network_id, CALL_METHOD, [{"to": silo, "data": CONFIG_SELECTOR}, block_tag])
        config = _address(config_obs.result)
        config_code = self.transport.call(network_id, GET_CODE_METHOD, [config, block_tag])
        silos = self.transport.call(network_id, CALL_METHOD, [{"to": config, "data": GET_SILOS_SELECTOR}, block_tag])
        silo_words = _word(silos.result)
        if len(silo_words) < 128:
            raise RegistryError("invalid SiloConfig.getSilos ABI result")
        silo0 = _address("0x" + silo_words[:64])
        silo1 = _address("0x" + silo_words[64:128])

        asset_obs = self.transport.call(network_id, CALL_METHOD, [{"to": silo, "data": ASSET_SELECTOR}, block_tag])
        asset = _address(asset_obs.result)
        liquidity_obs = self.transport.call(network_id, CALL_METHOD, [{"to": silo, "data": GET_LIQUIDITY_SELECTOR}, block_tag])
        max_flash_obs = self.transport.call(network_id, CALL_METHOD, [{"to": silo, "data": _address_calldata(MAX_FLASH_LOAN_SELECTOR, asset)}, block_tag])
        fee_obs = self.transport.call(network_id, CALL_METHOD, [{"to": silo, "data": _address_uint_calldata(FLASH_FEE_SELECTOR, asset, flash_fee_probe_amount)}, block_tag])
        factory_obs = self.transport.call(network_id, CALL_METHOD, [{"to": silo, "data": FACTORY_SELECTOR}, block_tag])
        after = self.transport.call(network_id, BLOCK_METHOD)

        observations = (silo_code, config_obs, config_code, silos, asset_obs, liquidity_obs, max_flash_obs, fee_obs, factory_obs, after)
        _same_provider(observations, before.provider_id)

        after_block = parse_hex_block(after.result)
        validate_block_numbers(before_block, after_block, self.freshness)

        if silo.lower() not in {silo0.lower(), silo1.lower()}:
            raise RegistryError("Silo is not one of the two SiloConfig vaults")
        if silo0.lower() == silo1.lower():
            raise RegistryError("SiloConfig returned duplicate vault identities")

        return SiloRuntimeState(
            network_id=network_id,
            silo=silo,
            config=config,
            silo0=silo0,
            silo1=silo1,
            asset=asset,
            liquidity=_uint(liquidity_obs.result),
            max_flash_loan=_uint(max_flash_obs.result),
            flash_fee_probe_amount=flash_fee_probe_amount,
            flash_fee=_uint(fee_obs.result),
            factory=_address(factory_obs.result),
            observed_block=after_block,
            provider_id=before.provider_id,
            silo_bytecode_sha256=_bytecode_sha256(silo_code.result),
            config_bytecode_sha256=_bytecode_sha256(config_code.result),
        )
