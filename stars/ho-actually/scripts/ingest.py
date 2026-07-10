#!/usr/bin/env python
"""Ingest — crawl the Ho System source into *, Actually nodes.

The Ho System repo is the single source of truth. This crawl is **idempotent**:
a deterministic parse, re-run whenever ho expands. It regenerates the *extracted*
depth layers from source and **preserves** any hand-authored `synthesized`
layers already in ``nodes/``, as well as curated frontmatter wiring (`related`
is unioned with the generated edges; non-empty `requires` / `entry_points` are
kept as-is). Depth layers are the practitioner's own prose, pulled forward —
never generated.

Where the depth comes from: the glossary gives surface (name, definition, use);
the *juice* is the framework docs. Each glossary entry cites the exact section
that defines it — ``ho — (ho-structure 2.3 §1)`` — and this crawl resolves those
citations into the numbered doc sections (``## 1. …``), pulling them forward as
the deeper layers, verbatim.

Usage:
    python scripts/ingest.py [--source PATH] [--dry-run]

``--source`` defaults to the sibling ho-system clone.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

MAX_DEPTH = 5
SECTION_CHAR_CAP = 1600  # keep a single depth layer digestible

DEFAULT_SOURCE = Path.home() / "Vaults/sageframe-no-kaji-dev/ho-system"
NODES_DIR = Path(__file__).resolve().parent.parent / "nodes"

# The glossary headword → node id, where a plain slug would be wrong or the id
# is load-bearing (the root is referenced by site.yaml).
ID_OVERRIDES = {
    "agent task (AT)": "agent-task",
    "architectural register / executable register": "registers",
    "build record": "build-record",
    "cross-session continuity": "cross-session-continuity",
    "eval (graded eval)": "graded-eval",
    "ho 0.5": "ho-0-5",
    "ho-process/": "ho-process",
    "hot / cold": "hot-cold",
    "Kamae addendum (kamae-N.M)": "kamae-addendum",
    "mind / hand": "mind-hand",
    "notes/": "notes",
    "project lifecycle": "project-lifecycle",
    "spike (design)": "spike",
    "state memory (Kamae 6)": "state-memory",
    "state-summary block": "state-summary-block",
    "Think / Execute / Reflect": "think-execute-reflect",
    "verification / validation": "verification-validation",
    "working-memory handoff": "working-memory-handoff",
}
ROOT_ID = "what-is-ho-system"

# Pointer-only glossary entries ("register — see architectural register") that
# should not become their own node.
SKIP_HEADWORDS = {"register"}

# Glossary type heuristics: default `definition`; these headwords are concepts,
# these procedures. (The engine's NodeType allows concept/definition/procedure/
# scenario/troubleshooting.)
CONCEPT_TERMS = {
    "arc",
    "closure",
    "design-tuning",
    "forward-only",
    "ha",
    "ho",
    "kamae",
    "kokoroe",
    "mind-hand",
    "mutability",
    "parti",
    "phase",
    "registers",
    "ri",
    "shu",
    "shu-ha-ri",
    "think-execute-reflect",
    "tiered-understanding",
    "verification-validation",
}
PROCEDURE_TERMS = {
    "builds-on",
    "dandori",
    "declared-compression",
    "kamae-addendum",
    "precedential-thinking",
    "propagation-ledger",
    "supersedes",
}
# Foundational terms require the root, so the entry screen has forward paths.
FOUNDATIONS = {"ho", "kamae", "shu-ha-ri", "mind-hand", "verification-validation"}


@dataclass
class Section:
    number: str  # "1", "3.5"
    heading: str
    body: str


@dataclass
class Doc:
    slug: str
    title: str
    sections: dict[str, Section] = field(default_factory=dict)


@dataclass
class Node:
    id: str
    title: str
    type: str
    summary: str
    layers: list[tuple[int, str, str]]  # (depth, provenance, markdown)
    requires: list[str] = field(default_factory=list)
    related: list[str] = field(default_factory=list)
    entry_points: list[str] = field(default_factory=list)


# ── slugging ──────────────────────────────────────────────────────────────


def slug(headword: str) -> str:
    if headword in ID_OVERRIDES:
        return ID_OVERRIDES[headword]
    s = headword.split("(")[0].strip()  # drop Japanese readings / parentheticals
    s = s.replace("/", " ").replace("'", "")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s


# ── framework docs ────────────────────────────────────────────────────────


def parse_doc(path: Path) -> Doc:
    text = path.read_text(encoding="utf-8")
    fm = re.search(r'title:\s*"?([^"\n]+)"?', text)
    title = fm.group(1).strip() if fm else path.stem
    doc = Doc(slug=path.stem, title=title)

    # Split on ## / ### headings; capture numbered ones (## 1. , ### 3.5 ).
    heading_re = re.compile(r"^(#{2,3})\s+(\d+(?:\.\d+)*)\.?\s+(.+)$", re.M)
    matches = list(heading_re.finditer(text))
    for i, m in enumerate(matches):
        number = m.group(2)
        heading = m.group(3).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        doc.sections[number] = Section(number=number, heading=heading, body=body)
    return doc


def section_layer(doc: Doc, number: str) -> str | None:
    """Extract a cited section as a depth layer: heading + prose, capped."""
    sec = doc.sections.get(number)
    if sec is None:
        return None
    body = sec.body
    # Trim to the first sub-subsection to avoid dumping a whole numbering chapter.
    cut = re.search(r"\n#{3,4}\s", body)
    if cut and cut.start() > 200:
        body = body[: cut.start()].strip()
    if len(body) > SECTION_CHAR_CAP:
        body = body[:SECTION_CHAR_CAP].rsplit("\n\n", 1)[0].strip() + " […]"
    return f"**{sec.heading}.** {body}" if body else None


# ── glossary ──────────────────────────────────────────────────────────────

CITATION_RE = re.compile(r"([a-z][a-z0-9-]+)\s+\d+(?:\.\d+)*\s*(?:§(\d+(?:\.\d+)*))?")


def parse_glossary(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    body = text.split("---", 2)[-1]  # past the frontmatter
    entries = []
    # Each entry: **headword** — body … _Plain: cut._
    for m in re.finditer(
        r"\*\*(?P<hw>[^*]+)\*\*\s*—\s*(?P<def>.*?)\n\n_Plain:\s*(?P<plain>.*?)_\n",
        body,
        re.S,
    ):
        definition = m.group("def").strip()
        citation = ""
        # re.S: the glossary line-wraps long citation parentheticals; without
        # DOTALL the capture dies at the newline and the entry silently loses
        # its depth-4+ cited-section layers. Collapse the wrap to one line.
        cm = re.search(r"_\((.*?)\)_\s*$", definition, re.S)
        if cm:
            citation = " ".join(cm.group(1).split())
            definition = definition[: cm.start()].strip()
        entries.append(
            {
                "headword": m.group("hw").strip(),
                "definition": definition,
                "plain": " ".join(m.group("plain").split()),
                "citation": citation,
            }
        )
    return entries


# ── assembly ──────────────────────────────────────────────────────────────


def clean(md: str) -> str:
    """Drop stray citation parentheticals; collapse whitespace runs."""
    md = re.sub(r"_\([^)]*\)_", "", md)
    md = re.sub(r"[ \t]+", " ", md)
    return md.strip()


def build_nodes(source: Path) -> list[Node]:
    docs = {
        p.stem: parse_doc(p)
        for p in [
            source / "framework/the-ho-system.md",
            *sorted((source / "framework/structure").glob("*.md")),
        ]
    }
    entries = [
        e
        for e in parse_glossary(source / "framework/glossary.md")
        if e["headword"] not in SKIP_HEADWORDS
    ]

    hw_to_id = {e["headword"]: slug(e["headword"]) for e in entries}
    all_ids = set(hw_to_id.values()) | {ROOT_ID}

    nodes: list[Node] = []

    # The root, from the-ho-system overview.
    root_layers = [
        (1, "extracted", "What the Ho System Is"),
        (
            2,
            "extracted",
            "The Ho System is a structured methodology for building production-quality "
            "software using AI as an implementation partner — for people who think in "
            "systems but haven't followed a traditional developer path.",
        ),
        (
            3,
            "extracted",
            "The bottleneck in AI-assisted development isn't access to tools; it is "
            "*judgment* — knowing what to build, whether what was built is correct, and "
            "when the AI is wrong. The Ho System develops that judgment through structured "
            "practice on real projects. **Ho** (歩) means *step*: each unit of work is a "
            "deliberate, bounded step forward.",
        ),
    ]
    nodes.append(
        Node(
            id=ROOT_ID,
            title="What the Ho System Is",
            type="concept",
            summary="Building production software with AI while developing real judgment.",
            layers=root_layers,
            related=sorted(FOUNDATIONS),
            entry_points=["what is the ho system", "is this for me", "how does ho work"],
        )
    )

    for e in entries:
        nid = slug(e["headword"])
        if nid == ROOT_ID:
            continue
        title = e["headword"].split("(")[0].strip()
        if "(" in e["headword"]:  # keep Japanese reading in the title
            title = e["headword"].strip()
        ntype = (
            "concept"
            if nid in CONCEPT_TERMS
            else "procedure"
            if nid in PROCEDURE_TERMS
            else "definition"
        )

        layers: list[tuple[int, str, str]] = [
            (1, "extracted", title),
            (2, "extracted", clean(e["plain"])),
        ]
        definition = clean(e["definition"])
        if definition:
            layers.append((3, "extracted", definition))

        # Depth 4-5: the juice - cited framework sections, verbatim.
        depth = 4
        seen_secs: set[tuple[str, str]] = set()
        for cm in CITATION_RE.finditer(e["citation"]):
            doc_slug, section = cm.group(1), cm.group(2)
            if depth > MAX_DEPTH or doc_slug not in docs or not section:
                continue
            key = (doc_slug, section)
            if key in seen_secs:
                continue
            seen_secs.add(key)
            layer = section_layer(docs[doc_slug], section)
            if layer:
                layers.append((depth, "extracted", clean(layer)))
                depth += 1

        # Related: the entry's *deliberate* cross-references (bolded) come first
        # — high signal. Then fill toward a small floor with plain mentions so
        # nothing is orphaned. Capped, and the engine caps the display too, so
        # rich entries stay rich without any node becoming a wall.
        related: list[str] = []
        for bolded in re.findall(r"\*\*([^*]+)\*\*", e["definition"]):
            bid = slug(bolded.strip())
            if bid in all_ids and bid != nid and bid not in related:
                related.append(bid)
        if len(related) < 4:
            for hw, other_id in hw_to_id.items():
                token = hw.split("(")[0].strip()
                if (
                    other_id != nid
                    and other_id not in related
                    and len(token) > 3
                    and re.search(rf"\b{re.escape(token)}\b", e["definition"])
                ):
                    related.append(other_id)
        related = sorted(dict.fromkeys(related))[:6]

        requires = [ROOT_ID] if nid in FOUNDATIONS else []

        nodes.append(
            Node(
                id=nid,
                title=title,
                type=ntype,
                summary=clean(e["plain"]),
                layers=layers,
                requires=requires,
                related=[r for r in related if r != ROOT_ID],
                entry_points=[title.split(" (")[0].lower()],
            )
        )

    # No orphans: any node with no edge in or out links to the root.
    linked = set()
    for n in nodes:
        linked.update(n.requires + n.related)
    for n in nodes:
        if n.id == ROOT_ID:
            continue
        has_out = bool(n.requires or n.related)
        if not has_out and n.id not in linked:
            n.related = [ROOT_ID]

    return nodes


# ── writing (idempotent, preserve authored) ─────────────────────────────────


def existing_synthesized(nid: str) -> list[tuple[int, str, str]]:
    """Any hand-authored `synthesized` layers already in nodes/<id>.md."""
    path = NODES_DIR / f"{nid}.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    kept = []
    for m in re.finditer(
        r"<!-- depth:(\d+) -->\s*\n<!-- provenance: (\w+) -->\s*\n(.*?)(?=\n<!-- depth:|\Z)",
        text,
        re.S,
    ):
        if m.group(2) == "synthesized":
            kept.append((int(m.group(1)), "synthesized", m.group(3).strip()))
    return kept


FM_LIST_RE = re.compile(r"^(requires|related|entry_points):\s*\[(.*)\]\s*$", re.M)


def existing_frontmatter(nid: str) -> dict[str, list[str]]:
    """Curated frontmatter lists already in nodes/<id>.md (hand-wired graph edges)."""
    path = NODES_DIR / f"{nid}.md"
    if not path.exists():
        return {}
    parts = path.read_text(encoding="utf-8").split("---", 2)
    if len(parts) < 3:
        return {}
    return {
        m.group(1): [s.strip() for s in m.group(2).split(",") if s.strip()]
        for m in FM_LIST_RE.finditer(parts[1])
    }


def render(node: Node) -> str:
    layers = {d: (p, md) for d, p, md in node.layers}
    for d, prov, md in existing_synthesized(node.id):  # authored layers win
        layers[d] = (prov, md)

    # Curation survives re-ingest: union hand-wired `related` edges with the
    # generated ones; keep curated `requires` / `entry_points` when non-empty.
    # (Extracted body layers still regenerate; synthesized layers still win.)
    curated = existing_frontmatter(node.id)
    if curated.get("related"):
        node.related = sorted(dict.fromkeys(node.related + curated["related"]))
    if curated.get("requires"):
        node.requires = curated["requires"]
    if curated.get("entry_points"):
        node.entry_points = curated["entry_points"]

    fm = [
        "---",
        f"id: {node.id}",
        f"title: {node.title}",
        f"type: {node.type}",
        f"requires: [{', '.join(node.requires)}]",
        f"related: [{', '.join(node.related)}]",
        f"entry_points: [{', '.join(node.entry_points)}]",
        "summary: >",
        f"  {node.summary}",
        "---",
        "",
    ]
    body = []
    for d in sorted(layers):
        prov, md = layers[d]
        body += [f"<!-- depth:{d} -->", f"<!-- provenance: {prov} -->", md, ""]
    return "\n".join(fm + body).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not (args.source / "framework/glossary.md").exists():
        print(f"ho-system source not found at {args.source}", file=sys.stderr)
        return 1

    nodes = build_nodes(args.source)
    new_ids = {n.id for n in nodes}

    NODES_DIR.mkdir(exist_ok=True)
    written = 0
    for node in nodes:
        content = render(node)
        path = NODES_DIR / f"{node.id}.md"
        if not args.dry_run:
            path.write_text(content, encoding="utf-8")
        written += 1

    # Remove stale extracted-only nodes the crawl no longer produces.
    removed = []
    for path in sorted(NODES_DIR.glob("*.md")):
        if path.stem not in new_ids and not existing_synthesized(path.stem):
            removed.append(path.stem)
            if not args.dry_run:
                path.unlink()

    verb = "would write" if args.dry_run else "wrote"
    print(f"{verb} {written} nodes; removed {len(removed)} stale: {removed}")
    total_deep = sum(1 for n in nodes if any(d >= 4 for d, _, _ in n.layers))
    print(f"nodes with depth ≥4 (framework juice): {total_deep}/{len(nodes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
