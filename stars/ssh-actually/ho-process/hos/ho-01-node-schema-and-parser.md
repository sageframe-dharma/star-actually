---
created: 2026-07-03
status: complete
type: ho
project: star-actually
ho: ho-01
title: The Node Schema and Parser
builds-on: ho-00-orientation
---

# ho-01 — The Node Schema and Parser

**Goal:** freeze the schema from Kamae 2 §4 and prove it against real guide content.

## Scope

**In:** `star_actually.nodes` — typed Node/DepthLayer models, single-file parser (frontmatter split, depth-layer split, provenance capture), single-file validation (kebab-case id matching filename, known type, contiguous depths 1..≤5, minimum depths 1–2, non-empty layers, no unknown frontmatter keys), directory loader with duplicate-id detection. Three exemplar nodes hand-decomposed from the guide into `nodes/`: `agent-forwarding` (concept), `blob` (definition), `permission-denied` (troubleshooting).

**Out:** cross-node validation, graph computation, rendering (ho-02, ho-03).

## Decisions made here

- **Depth ceiling is 5.** The seed mused about 6–7 layers for core concepts; the fixed semantic scale (name/definition/usage/relationships/theory) caps at 5 and a node that wants more is two nodes.
- **Unknown frontmatter keys fail the parse.** Typos in `related:` vs `releated:` must die at build time, not silently drop edges.
- **Provenance markers are per-layer, at most one, immediately after the depth marker.** Captured into the model (review tooling reads them), stripped from content.

## Verification

`make verify` green, coverage ≥90%; the three exemplar nodes parse and validate; schema-violation fixtures each raise with a message naming the file and the fix.
