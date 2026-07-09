"""Content tests for Ho System, Actually — facts about this instance's nodes and
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
    assert config.title == "Ho System, Actually"
    assert config.root_node == "what-is-ho-system"


class TestSeedGraph:
    def test_graph_weaves_strict(self) -> None:
        """The ingested graph: closed, no dangling edges, no warnings."""
        graph = build_graph(load_nodes(NODES_DIR))
        assert graph.warnings == ()
        assert len(graph.nodes) >= 58  # a floor; grows as ho-system expands and we re-ingest
        for node_id in (
            "what-is-ho-system",
            "mind-hand",
            "dandori",
            "mutability",
            "kamae-addendum",
        ):
            assert node_id in graph.nodes

    def test_root_is_reachable_forward(self) -> None:
        graph = build_graph(load_nodes(NODES_DIR))
        assert graph.neighborhoods["what-is-ho-system"].forward

    def test_root_shape(self) -> None:
        node = parse_node(NODES_DIR / "what-is-ho-system.md")
        assert node.type is NodeType.CONCEPT
        assert node.layer(1).markdown == "What the Ho System Is"

    def test_provenance_discipline_holds(self) -> None:
        """Every seed layer is provenance-marked; the seed is all extracted."""
        for node in load_nodes(NODES_DIR).values():
            for layer in node.layers:
                assert layer.provenance == "extracted", (
                    f"{node.id} depth {layer.depth} is not extracted — synthesized "
                    "prose needs a voice-audit before it ships"
                )

    def test_framework_juice_reaches_depth(self) -> None:
        """The ingest pulls cited framework sections into deeper layers — the
        glossary is surface; the docs are the juice."""
        nodes = load_nodes(NODES_DIR)
        deep = [n for n in nodes.values() if n.depth_levels >= 4]
        assert len(deep) >= 20
        ho = nodes["ho"]
        assert ho.depth_levels >= 4
        assert "invariant" in ho.layer(4).markdown.lower()
