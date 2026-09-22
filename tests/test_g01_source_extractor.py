from ghost_hunter.g01_source_extractor import (
    deduplicate_candidates,
    extract_cosmos_tree_records,
    extract_defillama_chain_records,
    extract_dex_protocol_chains,
)


def test_cosmos_production_filter_and_exclusion():
    tree = {"tree": [
        {"path": "alpha/chain.json"},
        {"path": "beta/chain.json"},
    ]}
    payloads = {
        "alpha/chain.json": {
            "chain_name": "alpha",
            "pretty_name": "Alpha",
            "chain_type": "cosmos",
            "chain_id": "alpha-1",
            "status": "live",
            "network_type": "mainnet",
        },
        "beta/chain.json": {
            "chain_name": "beta",
            "chain_type": "cosmos",
            "chain_id": "beta-test",
            "status": "live",
            "network_type": "testnet",
        },
    }
    rows = extract_cosmos_tree_records(tree, payloads, "cosmos", "fixture:cosmos")
    assert rows[0].state == "VERIFIED_CANDIDATE"
    assert rows[1].state == "EXCLUDED_NONPRODUCTION"


def test_dex_discovery_and_defillama_chain_ingestion():
    chains = extract_defillama_chain_records(
        [{"name": "Solana", "chainId": None}, {"name": "Base", "chainId": 8453}],
        "llama-chains", "fixture:llama"
    )
    dex = extract_dex_protocol_chains(
        [{"name": "Example DEX", "category": "DEX", "chains": ["Solana", "Base"]}],
        "llama-dex", "fixture:dex"
    )
    assert len(chains) == 2
    assert {x.name for x in dex} == {"Solana", "Base"}


def test_deduplication_requires_identity_fields():
    rows = extract_defillama_chain_records(
        [{"name": "Base", "chainId": 8453}, {"name": "Base", "chainId": 8453}],
        "llama", "fixture"
    )
    assert len(deduplicate_candidates(rows)) == 1
