---
ho: ho-01
shape: ri
title: Content Phase A — glossary passthrough
created: 2026-07-08
status: closed
builds-on: [ho-00-orientation]
---

# ho-01 — Content Phase A: glossary passthrough

## Problem

The seed (ho-00) proved the instance renders real content, but at 10 nodes it was
a slice. Phase A of the content-track overview: turn the **whole glossary** into
nodes at depths 1–3, all `extracted`, without touching the depth 4–5 voice-audit
gate.

## What was built

The graph grew from **10 → 58 nodes**. The 48 remaining glossary terms were
authored from `ho-system/framework/glossary.md` — the practitioner's own words,
reflowed — each with:

- `summary` = the term's `_Plain:_` cut, verbatim.
- Depth 1 = the title; depths 2–3 = definition and fuller context, extracted.
  Thin entries (`splits-from`, `precedential-thinking`, …) stop at depth 2 rather
  than pad.
- `provenance: extracted` on every one of the 172 layers.

## How (method note)

Authored by five parallel agents against a single dandori spec
(`ho-process/agent-tasks/phase-a-node-authoring.md`) carrying the **canonical id
list** — so `requires`/`related` could only reference real nodes, and the graph
stayed **closed by construction**. It validated sound on the first pass: 58
nodes, no dangling edges, no requires-cycles, no orphans. (The Ho System building
its own site with the Ho System's own delegation discipline.)

## Verification (by command)

- `star-actually validate` → `ok: 58 nodes, graph is sound`.
- `star-actually build` → `232 pages, 172 fragments`.
- depth-1 == title on all 58; no glossary citations leaked; all 172 layers
  `extracted`.
- `make verify` green; no external requests in `dist/`.

## Not done (the gate ahead)

- **Depths 4–5** (relationships, theory) — synthesized prose. Phase C of the
  content-track overview: the voice-audit gate. Not authored here.
- **Framework documents as nodes** (Phase B) — the 13 structure docs.
- `entry_points` were authored per node but not yet curated as a set.
- Provenance is uniform `extracted`; the sign-off surface (extracted vs
  synthesized) becomes meaningful once Phase C adds synthesized layers.
