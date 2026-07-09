---
doc: kamae-4
title: Content-track overview — Ho System, Actually
project: ho-actually
created: 2026-07-08
status: living
---

# Kamae 4 — Content-track overview

The build plan that carries the 10-node **seed** to a full `*, Actually`
instance at parity with `ssh-actually` (60 nodes, closed graph, authored depths
1–5, provenance sign-off). Phases first; the practitioner's review surfaces are
named. This is a **living** plan — the map, not the territory.

Source material and the full proposed node inventory (69 glossary terms + 13
framework structure docs → ~87 candidate nodes, with a depth-coverage gap
analysis) is the corpus map produced during setup; it is the raw input to
Phase A/B scoping, not a frozen decision.

## The provenance line (the governing rule)

Depths **1–3** are largely **extracted** — the practitioner's own words from the
glossary and framework docs, reflowed. Depths **4–5** (relationships, theory)
are largely **synthesized** — new prose. Per the project's licensing (`nodes/`
is CC BY-ND, published under the practitioner's name) and the operating
discipline, **no synthesized layer ships without a voice-audit and practitioner
review.** The seed is `extracted`-only on purpose: it is the honest floor.

## Phases

### Phase A — Glossary passthrough (extracted; low-risk)

The remaining ~59 glossary terms become nodes at depths 1–3, extracted from
`glossary.md` (definition + plain cut + fuller entry), like the seed. Edges wired
from the glossary's cross-references, closed at each step.

- **Deliverable:** ~69-node closed graph, depths 1–3, all `extracted`.
- **Gate:** `star-actually validate && build` clean; every edge resolves.
- **Review surface:** light — this is the practitioner's own prose, reorganized.

### Phase B — Framework documents as nodes (extracted → depth 4)

The 13 `framework/structure/` docs distill into concept/architecture nodes
(Kamae, project-arc, ho-structure, verification-practices, ho-task-decomposition,
design-work, …), extracted to depth 3–4 where the source supports it. Templates
stay reference material (linked, not nodes).

- **Deliverable:** the structural spine; graph depth and cross-links thicken.
- **Review surface:** moderate — distillation choices (which doc → which nodes).

### Phase C — Depth 4–5 synthesis  ⟵ **VOICE-AUDIT GATE**

The ~35–40 nodes the corpus map flags as needing authored relationships and
theory (why-ho-system, kamae, shu-ha-ri, mind-hand, verification-validation,
design-tuning, kagen, devlog, forward-only, tripwired, …). This is new prose in
the practitioner's voice.

- **Provenance:** `synthesized`. Each layer voice-audited (`voice-atm`) and
  **read by the practitioner** before its marker is cleared.
- **This phase is not autonomous.** It is the human-in-the-loop authoring effort,
  batched like `ssh-actually`'s content track (ho-C*), each batch a review
  surface.

### Phase D — Entry points, densification, sign-off, ship

`entry_points` arrays curated; `related`/`requires` densified; the provenance
report assembled (extracted vs synthesized per layer); practitioner sign-off
strips markers; smoke walk; static deploy (receptionist deferred).

## Parity targets (from ssh-actually)

- Closed graph, strict validation (no dangling edges, no requires-cycles, no
  orphans).
- Depth ceilings per node (not every node reaches 5).
- A provenance report as the sign-off surface before markers are stripped.
- Zero external requests in the shipped site.

## Open decisions for the practitioner

- **Scope of the graph:** all 69 glossary terms, or a curated core? (The corpus
  map proposes 87 nodes; that is a ceiling, not a mandate.)
- **Tagline / prompt / domain_word** in `site.yaml` are placeholders — the
  practitioner's to set (content/voice).
- **Deploy target:** homelab Caddy + Docker (like ssh-actually's plan) vs.
  Cloudflare Pages static. Decided when the graph is worth shipping.
