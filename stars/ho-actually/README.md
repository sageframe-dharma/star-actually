# Ho System, Actually

The Ho System methodology as a navigable **`*, Actually`** knowledge graph:
authored depth layers, spatial navigation, fully static, terminal-aesthetic. The
second instance of `*, Actually` (after `ssh-actually`), and the one that turns
the framework's own vocabulary into a walkable graph.

## What it is

The reading experience is the [`star-actually` engine](../engine): the Loom
builds the site, the Terminal renders it, the Receptionist (later) answers
questions. This repo supplies only the domain:

- `site.yaml` — title, tagline, root node, the receptionist's prompt.
- `nodes/*.md` — the content: each a term or concept, as depth-layered markdown
  with YAML frontmatter. Depth 1 names it, 2 defines it, 3 shows use, 4
  relationships, 5 theory.

## Status: ingest-driven

Nodes are **crawled from ho-system** by `scripts/ingest.py` (`make ingest`), which
is idempotent and re-runnable as the framework expands. **ho-system is the single
source of truth** for extracted content — edit upstream, re-ingest.

The graph is **58 nodes**; **30 reach depth ≥4** — those deeper layers are the
*juice*, pulled verbatim from the framework structure docs via each glossary
entry's own citation (`ho → ho-structure §1`). Every layer is **extracted** (your
prose, correctly placed — never generated). See `ho-process/hos/ho-02-ingest.md`.

Still ahead: framework docs as their own nodes (fuller Phase B); richer
`entry_points`; and any genuinely *synthesized* connective theory, which stays a
voice-audit gate (none exists yet — the graph is all extracted).

## Build

```
make install      # uv sync + pre-commit
make validate     # parse nodes, check the graph is sound
make build        # weave dist/
make serve        # build + serve locally
make verify       # ruff + mypy --strict + content tests
```

## Licensing

Code is MIT (`LICENSE`). Content — `nodes/` — is CC BY-ND 4.0
(`LICENSE-CONTENT`), and is a decomposition of the Ho System framework
(`github.com/sageframe-no-kaji/ho-system`).
