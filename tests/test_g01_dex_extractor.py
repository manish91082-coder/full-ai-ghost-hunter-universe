from ghost_hunter.g01_dex_extractor import (
    extract_defillama_dex_protocol_relationships,
    extract_defillama_dex_chain_surface,
    deduplicate_relationships,
)


def test_protocol_chain_relationships_require_dex_category():
    payload = [
        {"name": "Example DEX", "category": "Dexs", "slug": "example", "chains": ["Ethereum", "Base", "Solana"]},
        {"name": "Lending Example", "category": "Lending", "chains": ["Ethereum"]},
    ]
    rows = extract_defillama_dex_protocol_relationships(payload, "llama-protocols", "fixture:protocols")
    assert {(r.protocol_name, r.chain_name) for r in rows} == {
        ("Example DEX", "Ethereum"), ("Example DEX", "Base"), ("Example DEX", "Solana")
    }


def test_relationship_preserves_identity_and_evidence():
    payload = [{"name": "DEX A", "category": "DEX", "slug": "dex-a", "chains": ["Base"]}]
    rows = extract_defillama_dex_protocol_relationships(payload, "src", "evidence://1")
    assert rows[0].protocol_slug == "dex-a"
    assert rows[0].source_id == "src"
    assert rows[0].evidence_ref == "evidence://1"


def test_invalid_chain_values_are_not_promoted():
    payload = [{"name": "DEX A", "category": "Dexes", "chains": ["Base", "", None, 8453]}]
    rows = extract_defillama_dex_protocol_relationships(payload, "src", "fixture")
    assert [r.chain_name for r in rows] == ["Base"]


def test_chain_surface_preserves_source_chain_id_only():
    payload = [{"name": "Base", "chainId": 8453}, {"name": "Solana", "chainId": None}]
    rows = extract_defillama_dex_chain_surface(payload, "llama-dex-chains", "fixture:chains")
    assert rows[0].chain_name == "Base"
    assert rows[0].source_chain_id == "8453"
    assert rows[1].source_chain_id is None


def test_relationship_deduplication():
    payload = [{"name": "DEX A", "category": "Dexes", "slug": "dex-a", "chains": ["Base", "Base"]}]
    rows = extract_defillama_dex_protocol_relationships(payload, "src", "fixture")
    assert len(deduplicate_relationships(rows)) == 1


def test_protocol_name_is_not_chain_identity():
    payload = [{"name": "Chainflip", "category": "Dexes", "slug": "chainflip", "chains": ["Ethereum", "Bitcoin"]}]
    rows = extract_defillama_dex_protocol_relationships(payload, "src", "fixture")
    assert {r.chain_name for r in rows} == {"Ethereum", "Bitcoin"}
    assert all(r.protocol_name == "Chainflip" for r in rows)
