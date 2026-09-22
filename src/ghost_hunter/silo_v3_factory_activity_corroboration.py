"""Fail-closed validator for secondary SiloFactory activity corroboration."""

def validate_activity_corroboration(payload: dict) -> dict:
    if payload.get("schema_version") != "g02.silo.factory.activity.corroboration.v1":
        raise ValueError("invalid schema_version")
    records = payload.get("records")
    if not isinstance(records, list) or len(records) != 38:
        raise ValueError("expected exactly 38 corroboration records")
    keys = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("record must be an object")
        network_id = record.get("network_id")
        factory = record.get("factory")
        start_silo_id = record.get("start_silo_id")
        if not isinstance(network_id, str) or not network_id.startswith("eip155:"):
            raise ValueError("invalid network_id")
        if not isinstance(factory, str) or len(factory) != 42 or not factory.startswith("0x"):
            raise ValueError("invalid factory")
        if not isinstance(start_silo_id, int) or start_silo_id < 1:
            raise ValueError("invalid start_silo_id")
        key = (network_id, factory.lower())
        if key in keys:
            raise ValueError("duplicate (network_id,factory)")
        keys.add(key)
    if payload.get("authority") != "CORROBORATING_ONLY_NO_SCAN_START_AUTHORITY":
        raise ValueError("authority boundary changed")
    return {"valid": True, "record_count": len(records), "identity_count": len(keys)}
