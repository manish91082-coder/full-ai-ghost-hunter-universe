"""Fail-closed read-only materialization for configured V2 factory universes."""
from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Any, Iterable
from .registry import RegistryError
from .v2_pair_enumerator import V2PairEnumerator

@dataclass(frozen=True)
class V2FactoryMaterialization:
    factory_id:str; protocol:str; network_id:str; factory:str; status:str
    factory_reported_count:int; enumerated_count:int; provider_id:str|None
    observed_block:int|None; pairs:tuple[dict[str,Any],...]=()
    states:tuple[dict[str,Any],...]=(); error:str|None=None

def materialize_v2_factories(records:Iterable[dict[str,Any]], enumerator:V2PairEnumerator, *, max_pairs:int)->tuple[V2FactoryMaterialization,...]:
    if max_pairs<0: raise RegistryError("max_pairs must be non-negative")
    out=[]
    for r in records:
        fid=str(r.get("id","")); protocol=str(r.get("protocol","")); network=str(r.get("network_id","")); factory=str(r.get("factory",""))
        try:
            if not fid or not protocol or not network or not factory: raise RegistryError("V2 factory identity is incomplete")
            pairs=enumerator.enumerate_pairs(network,factory,max_pairs=max_pairs)
            comp=enumerator.last_completeness
            if comp is None or comp.enumerated_count != comp.factory_reported_count: raise RegistryError("V2 completeness evidence missing")
            states=[asdict(enumerator.read_pair_state(network,p.pair_address)) for p in pairs]
            if len(states)!=len(pairs): raise RegistryError("V2 pair-state count mismatch")
            out.append(V2FactoryMaterialization(fid,protocol,network,factory,"RUNTIME_VERIFIED_READ_ONLY",comp.factory_reported_count,comp.enumerated_count,comp.provider_id,comp.end_block,tuple(asdict(p) for p in pairs),tuple(states)))
        except Exception as exc:
            out.append(V2FactoryMaterialization(fid,protocol,network,factory,"FAILED_CLOSED",0,0,None,None,error=str(exc)))
    return tuple(out)

def materialization_document(rows:Iterable[V2FactoryMaterialization], *, expected_factory_count:int, max_pairs:int)->dict[str,Any]:
    data=tuple(rows)
    complete=(len(data)==expected_factory_count and expected_factory_count>0 and all(r.status=="RUNTIME_VERIFIED_READ_ONLY" and r.enumerated_count==r.factory_reported_count for r in data))
    return {"schema_version":"g02.v2.factory.runtime.observation.v1","canonical_role":"CURRENT_RUNTIME_OBSERVATION_EVIDENCE","execution_authority":"NONE","live_trading":"STOP","expected_factory_count":expected_factory_count,"materialized_factory_count":len(data),"max_pairs_per_factory":max_pairs,"overall_status":"COMPLETE" if complete else "INCOMPLETE","records":[asdict(r) for r in data]}
