import os
import pytest
from src.ghost_hunter.runtime_config import RuntimeConfig, ConfigurationError

def test_critical_runtime_values_are_external(monkeypatch):
    values={
        "GH_ENVIRONMENT":"test",
        "GH_STATE_STORE_URI":"memory://test",
        "GH_PROVIDER_CONFIG_URI":"config://providers",
        "GH_UNIVERSE_REGISTRY_URI":"registry://universe",
        "GH_STRATEGY_REGISTRY_URI":"registry://strategies",
        "GH_MIN_NET_PROFIT_USD":"0.20",
        "GH_MAX_HOPS":"4",
        "GH_MAX_CANDIDATES_PER_CYCLE":"100",
    }
    for k,v in values.items(): monkeypatch.setenv(k,v)
    c=RuntimeConfig.from_env()
    assert str(c.economic_gate_usd)=="0.20"
    assert c.max_hops==4

def test_missing_critical_value_fails_closed(monkeypatch):
    monkeypatch.delenv("GH_MIN_NET_PROFIT_USD", raising=False)
    with pytest.raises(ConfigurationError):
        RuntimeConfig.from_env()
