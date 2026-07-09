---
ho: ho-02
shape: ri
title: The ingest — ho-system as source of truth, depth from the docs
created: 2026-07-09
status: closed
builds-on: [ho-01-content-phase-a]
---

# ho-02 — The ingest

## Problem

The glossary is, by definition, surface material — one paragraph per term — so
Phase A nodes were thin (depths 1–3). The Ho System keeps expanding, and
hand-authoring nodes doesn't scale to a moving source. Two needs: (1) re-derive
nodes when ho changes, idempotently; (2) reach the *juice* — the deep prose in
the framework structure docs.

## What was built

`scripts/ingest.py` — a deterministic crawl of the ho-system repo (`make ingest`):

- **ho-system is the single source of truth** for extracted content. The crawl
  regenerates the extracted layers each run; you edit content upstream and
  re-ingest, rather than hand-editing nodes here.
- **The juice comes from your own citations.** Each glossary entry cites the
  exact section that defines it — `ho — (ho-structure 2.3 §1)`. The crawl
  resolves those citations into the numbered doc sections (`## 1. …`) and pulls
  them forward, verbatim, as depths 4–5. The depth is your prose, correctly
  placed — extracted, never generated (the system's hard rule holds).
- **Idempotent.** A deterministic parse — byte-identical across re-runs
  (verified by hash). Stale nodes the crawl no longer produces are removed;
  hand-authored `synthesized` layers are preserved.

## Result (by command)

- 58 nodes; **30 carry depth ≥4, 2 reach depth 5** — the framework juice.
- `star-actually validate` → 58 nodes, sound; `build` → 266 pages, 206 fragments.
- `make verify` green (6 content tests, incl. a depth-juice assertion); `ingest.py`
  is under ruff + mypy --strict.

## Not done (follow-ups)

- **`entry_points` are thin** (title only) — could derive from the plain cut.
- **Section truncation** shows a `[…]` marker when a cited section exceeds the
  char cap — crude; could link to source or split.
- **Framework docs as their own nodes** (fuller Phase B) — the crawl currently
  enriches term nodes from doc sections but doesn't yet make the docs nodes.
- **Reproducibility:** the source defaults to the local ho-system clone; vendor
  or pin it (submodule / tag) for CI, like hosystem does.
- **Synthesized depth** (connective theory not in any doc) remains a voice-audit
  gate — none was written here; everything is extracted.
