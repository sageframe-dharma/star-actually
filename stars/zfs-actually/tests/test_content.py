"""Content tests for ZFS, Actually — facts about this instance's nodes and
site.yaml, exercised through the star-actually engine.

The engine's own unit tests live in the engine repo. These assert things that
are true of *this subject's content*.
"""

from pathlib import Path

from star_actually.config import load_config
from star_actually.graph import build_graph
from star_actually.nodes import NodeType, load_nodes, parse_node

REPO_ROOT = Path(__file__).parent.parent
NODES_DIR = REPO_ROOT / "nodes"


def test_real_site_yaml_loads() -> None:
    config = load_config(REPO_ROOT / "site.yaml")
    assert config.title == "ZFS, Actually"
    assert config.root_node == "what-zfs-is"
    assert len(config.chains) == 4


def test_graph_weaves_strict() -> None:
    """The graph: closed, no dangling edges, no warnings, no orphans."""
    graph = build_graph(load_nodes(NODES_DIR))
    assert graph.warnings == ()
    assert len(graph.nodes) == 34
    for node_id in ("what-zfs-is", "vdev", "snapshot", "zil-slog", "replace-disk"):
        assert node_id in graph.nodes


def test_root_is_reachable_forward() -> None:
    graph = build_graph(load_nodes(NODES_DIR))
    assert graph.neighborhoods["what-zfs-is"].forward


def test_root_shape() -> None:
    node = parse_node(NODES_DIR / "what-zfs-is.md")
    assert node.type is NodeType.CONCEPT
    assert node.layer(1).markdown == "What ZFS Is"


def test_chains_reference_real_nodes() -> None:
    config = load_config(REPO_ROOT / "site.yaml")
    nodes = load_nodes(NODES_DIR)
    for chain in config.chains:
        for node_id in chain.nodes:
            assert node_id in nodes, f"chain {chain.id!r} references unknown node {node_id!r}"


def test_provenance_discipline_holds() -> None:
    """Every layer above depth 1 carries a provenance marker — the rough/solid
    signal the Peko arc left behind (synthesized until vetted, extracted after)."""
    for node in load_nodes(NODES_DIR).values():
        for layer in node.layers:
            if layer.depth == 1:
                continue
            assert layer.provenance in ("synthesized", "extracted"), (
                f"{node.id} depth {layer.depth} has no provenance marker"
            )


def test_destructive_procedures_carry_the_hazard_gate() -> None:
    """The Peko hazard gate (D2): destructive operations are marked inline."""
    for node_id in ("replace-disk", "rollback", "first-pool"):
        node = parse_node(NODES_DIR / f"{node_id}.md")
        body = "\n".join(layer.markdown for layer in node.layers)
        assert "DESTRUCTIVE" in body, f"{node_id} is missing its hazard marker"


def test_every_node_stops_honestly() -> None:
    """Depths 2 to 5, contiguous — the engine enforces this, but assert the
    instance-level shape: nothing below depth 2, nothing above 5."""
    for node in load_nodes(NODES_DIR).values():
        assert 2 <= node.depth_levels <= 5
