---
created: 2026-07-03
status: active
type: ho-overview
project: star-actually
stage: kamae-4
kamae-chain: "seed → system-design → readme → **ho-overview**"
builds-on: kamae-2-star-actually-system-design
---

# \*, Actually — Ho Overview

**The build sequence for SSH, Actually.**

---

## What this is, and what it is not

This is the ordered decomposition of the system design into bounded working sessions. Each ho below gets its own Kamae 5 document when it opens; this overview fixes the sequence, the phase boundaries, and where the deferred decisions land. It is a plan, not a promise — replan checkpoints are marked, and the numbering scheme absorbs splits and insertions without renumbering.

Two tracks run in this project: the **system track** (phases 1–4, sequential) and the **content track** (phase C, parallel). The content track opens the moment ho-01 freezes the node schema and runs alongside everything else — it is editorial work with its own rhythm, executed as agent-task batches with practitioner review at batch boundaries.

---

## Phase 1 — Foundation

### ho-00 — Orientation

Scaffold the encoded environment: uv project with src layout (`star_actually`), ruff + mypy strict + pytest + coverage ≥90% floor, pre-commit hooks, Makefile, project CLAUDE.md, `site.yaml`, directory skeleton (`nodes/`, `templates/`, `assets/`, `portal/`). Deliverable: a green (empty) verification stack and a repo a fresh session can orient in from documents alone.

### ho-01 — The Node Schema and Parser

Freeze the schema from Kamae 2 §4. Build the parse stage: frontmatter + depth-layer splitting, provenance-marker handling, typed Node objects, single-file validation (contiguous depths, required layers, well-formed frontmatter). Hand-decompose **three exemplar nodes** from the guide — one `concept` (agent-forwarding), one `definition` (blob), one `troubleshooting` (permission-denied) — as fixtures and as the proof the schema fits real content. **Closing this ho opens the content track.**

**Replan checkpoint 1** — after ho-01: does the schema survive contact with real guide content? Schema changes after this point cost a content-track rework, so the checkpoint is honest, not ceremonial.

---

## Phase 2 — The Loom

### ho-02 — The Graph

Cross-node validation (every referenced id exists, no duplicates, no orphans without intent), backlink computation, forward/lateral neighborhood computation, `catalog.json` emission. Property: a broken graph fails the build with an error message that names the file and the fix.

### ho-03 — The Render

Jinja2 templates; emit the full `dist/` layout from Kamae 2 §4 — entry screen, node pages (noscript-complete), per-depth fragments with neighborhood `data-*` attributes, catalog, help. CLI: `star-actually build | validate | serve`. Golden-file tests against the exemplar nodes.

---

## Phase 3 — The Terminal

### ho-04 — The Look

The stylesheet. Monospace grid (Monospace Web lineage), screen anatomy from Kamae 2 §2, depth gauge, rail, neighborhoods, action bar — all as static rendering first. Terminal-width column, system mono stack, zero external requests. The 1996-but-gorgeous bar is cleared here or not at all.

### ho-05 — The Motion

HTMX wiring (depth dial as additive fragment swaps, node moves), then the one JS file: keyboard map, journey in `sessionStorage`, branch stack + one-keypress return, recentering, deep-link depth, action-bar context switching. Budget ≤~400 lines, no build step. Ends with a full keyboard walk of the exemplar graph.

**Replan checkpoint 2** — after ho-05: the feel is now testable against exemplar nodes. Optional early practitioner peek — cheap course-correction beats polished wrongness.

### ho-06 — The Index

Pagefind at build time (pinned, npx); `/` search UI; catalog prompt-matching as the no-Receptionist entry path. Entry screen fully functional without the portal.

---

## Phase C — The Content (parallel track; opens after ho-01)

### ho-C1 — The Node Map

Before any batch runs: the full decomposition map. Every candidate node from the guide + commands reference — id, type, one-line scope, `requires`/`related` edges, source sections. Target 40–60 nodes, one mental model each. This is the editorial architecture of the whole graph and the practitioner-facing review artifact; batches execute against it.

### ho-C2 … ho-C*n* — The Batches

Agent-task batches of ~8–12 nodes each (dandori specs in `ho-process/agent-tasks/`), executed in parallel. Every depth layer carries a provenance marker; synthesized prose is voice-audited (`voice-atm`) before review. Batch boundary = practitioner review surface: extracted layers skimmed, synthesized layers read. Expected: 4–6 batches.

### ho-C-final — The Graph Review

The assembled graph, whole: orphan check, edge sanity, granularity regrets, entry-point coverage against the seed's example questions. Practitioner walks the map, not yet the site.

---

## Phase 4 — The Ship

### ho-07 — The Receptionist

FastAPI `POST /ask`, prompt built against the real catalog, model id decided here (Haiku-class), Terminal wiring with graceful fallback, rate limiting. Local run + recorded-fixture tests; no live-key tests in CI.

### ho-08 — Integration and Smoke

Full build with the complete node set. The agent walks the smoke test end-to-end: arrival → question → landing depth → dial → onward → branch → rabbit hole → one-keypress return → search → no-JS floor → curl a node. Findings fixed, build green, coverage ≥90%.

**→ STOP: human interaction test.** The smoke test is the floor, not the verdict. The practitioner navigates the real site and judges function *plus feel* — the depth dial, the branch return, whether the spatial model lands. Findings become hos, not patches.

### ho-09 — The Deploy

After the interaction verdict: `dist/` behind Caddy at `ssh-actually.sageframe.net` (internal network), Receptionist container via `sageframe-docker-deploy`, `/ask` route. Public exposure is a separate, later decision (Cloudflare Tunnel, if ever).

---

## What's NOT in this sequence

Engine extraction (`star-actually` repo) · second domain · path-aware neighborhoods · authoring watcher · themes · analytics (never) · mobile app (never).

## Numbering and insertion

House rules: splits become ho-N.1/ho-N.2; insertions take half-numbers; abandoned numbers stay dead. Content batches number ho-C2, ho-C3, … as they're cut from the node map.

## Dependency summary

```
ho-00 → ho-01 → ho-02 → ho-03 → ho-04 → ho-05 → ho-06 ─┐
           └──→ ho-C1 → ho-C2…Cn → ho-C-final ─────────┼→ ho-08 → [interaction test] → ho-09
                                    ho-02 ──→ ho-07 ───┘
```

The system track builds against the three exemplar nodes throughout — it never waits on the content track until ho-08 needs the full graph.
