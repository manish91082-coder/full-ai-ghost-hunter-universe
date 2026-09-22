"""Fail-closed validator for pinned SiloFactory deployment-block evidence."""

def validate_deployment_block_evidence(payload: dict) -> dict:
    if payload.get("schema_version") != "g02.silo.factory.deployment.block.evidence.v1":
        raise ValueError("invalid schema_version")
    if payload.get("authority") != "HISTORICAL_SCAN_LOWER_BOUND_FOR_EXACT_FACTORY_ONLY":
        raise ValueError("invalid authority boundary")
    records = payload.get("records")
    blocked = payload.get("blocked")
    if not isinstance(records, list) or not isinstance(blocked, list):
        raise ValueError("records/blocked must be lists")
    keys=set()
    for r in records:
        if not isinstance(r,dict): raise ValueError("record must be object")
        key=(r.get("network_id"), str(r.get("factory","")).lower())
        if key in keys: raise ValueError("duplicate identity")
        keys.add(key)
        if not isinstance(r.get("deployment_block"),int) or r["deployment_block"] < 0: raise ValueError("invalid deployment block")
        if not isinstance(r.get("create_tx_hash"),str) or len(r["create_tx_hash"]) != 66: raise ValueError("invalid tx hash")
    for r in blocked:
        key=(r.get("network_id"), str(r.get("factory","")).lower())
        if key in keys: raise ValueError("identity both evidenced and blocked")
        keys.add(key)
        if not r.get("reason"): raise ValueError("blocked reason required")
    if len(keys) != 13: raise ValueError("expected 13 current deployment identities")
    return {"valid":True,"evidenced_count":len(records),"blocked_count":len(blocked),"identity_count":len(keys)}
