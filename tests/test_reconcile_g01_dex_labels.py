from ghost_hunter.reconcile_g01_dex_labels import classify, norm

def test_alias_hint_is_not_promotion():
    state, suggested = classify("Plume Mainnet", set())
    assert state == "LIKELY_ALIAS_CANDIDATE"
    assert suggested == "Plume"

def test_execution_plane_variant_is_conservative():
    state, suggested = classify("Example EVM", set())
    assert state == "EXECUTION_PLANE_VARIANT_CANDIDATE"
    assert suggested is None

def test_unknown_never_promotes():
    state, suggested = classify("Unknown Chain", set())
    assert state == "UNKNOWN"
    assert suggested is None

def test_normalization_is_deterministic():
    assert norm("NEAR Protocol") == norm("near-protocol")
