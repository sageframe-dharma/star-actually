"""Content tests for SSH, Actually — facts about this instance's nodes and
site.yaml, exercised through the star-actually engine.

The engine's own unit tests live in the engine repo. These assert things that
are true of *this subject's content*: the shipped graph, the real site.yaml,
and the exemplar node shapes.
"""

from pathlib import Path

from star_actually.config import load_config
from star_actually.graph import build_graph
from star_actually.nodes import NodeType, load_nodes, parse_node
from star_actually.render import render_site

REPO_ROOT = Path(__file__).parent.parent
NODES_DIR = REPO_ROOT / "nodes"


def test_real_site_yaml_loads() -> None:
    config = load_config(REPO_ROOT / "site.yaml")
    assert config.title == "SSH, Actually"
    assert config.root_node == "what-ssh-is"


class TestRealGraph:
    def test_full_graph_weaves_strict(self) -> None:
        """The shipped content: 60 nodes, closed graph, no warnings."""
        graph = build_graph(load_nodes(NODES_DIR))
        assert len(graph.nodes) == 60
        assert graph.warnings == ()
        assert "agent-forwarding" in graph.nodes

    def test_root_node_is_reachable_forward(self) -> None:
        """The root anchors the graph: things point onward from it."""
        graph = build_graph(load_nodes(NODES_DIR))
        assert graph.neighborhoods["what-ssh-is"].forward


class TestExemplarNodes:
    """The schema proven against real, shipped content."""

    def test_all_exemplars_parse(self) -> None:
        nodes = load_nodes(NODES_DIR)
        assert {"agent-forwarding", "blob", "permission-denied"} <= set(nodes)

    def test_agent_forwarding_shape(self) -> None:
        node = parse_node(NODES_DIR / "agent-forwarding.md")
        assert node.type is NodeType.CONCEPT
        assert node.depth_levels == 5
        assert node.layer(1).markdown == "Agent Forwarding"
        assert "proxy-jump" in node.related

    def test_blob_shape(self) -> None:
        node = parse_node(NODES_DIR / "blob.md")
        assert node.type is NodeType.DEFINITION
        assert node.depth_levels == 4

    def test_permission_denied_shape(self) -> None:
        node = parse_node(NODES_DIR / "permission-denied.md")
        assert node.type is NodeType.TROUBLESHOOTING
        assert node.depth_levels == 4

    def test_provenance_discipline_holds(self) -> None:
        """Every exemplar layer is provenance-marked until practitioner sign-off."""
        for node in load_nodes(NODES_DIR).values():
            for layer in node.layers:
                assert layer.provenance in {
                    "extracted",
                    "synthesized",
                }, f"{node.id} depth {layer.depth} lacks a provenance marker"


def test_real_content_builds_strict(tmp_path: Path) -> None:
    """The shipped content builds in strict mode with no warnings."""
    out = tmp_path / "dist"
    result = render_site(REPO_ROOT, out)
    assert (out / "n" / "agent-forwarding" / "d5.html").exists()
    assert result.warnings == ()
    fragment = (out / "n" / "agent-forwarding" / "d5.html").read_text(encoding="utf-8")
    assert "provenance" not in fragment  # markers never reach the product
