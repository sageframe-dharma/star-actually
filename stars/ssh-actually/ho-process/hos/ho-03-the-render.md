---
created: 2026-07-03
status: complete
type: ho
project: star-actually
ho: ho-03
title: The Render
builds-on: ho-02-the-graph
---

# ho-03 — The Render

**Goal:** the site exists. Every node × every depth as a static fragment, every node as a noscript-complete page, the entry screen, the catalog — the full `dist/` layout from Kamae 2 §4, emitted by a CLI.

## Scope

**In:** `star_actually.render` (markdown rendering via markdown-it-py with tables, Jinja2 templates, full `dist/` emission, asset copying), `star_actually.cli` (`build | validate | serve`, `--allow-dangling`, `--out`), templates (`base`, `fragment`, `index`, `help`), vendored htmx 2.0.4 (pinned, the only third-party client code), placeholder stylesheet and JS (made real in ho-04/ho-05).

**Out:** visual design (ho-04), keyboard/journey behavior (ho-05), search (ho-06).

## Decisions made here

- **Depth fragments are cumulative.** `d3.html` contains layers 1–3, and the dial swaps the whole article. Dialing deeper *appends* from the reader's point of view (you keep what you've read); implementation stays trivial (one swap target, no client-side stitching).
- **The `<h1>` is depth 1.** A node's name layer renders as the title line, not as a body section; body sections start at depth 2. Landing at depth 1 is legal and shows exactly the name — the seed's "you see the name, you move on" survives.
- **Navigation is server-rendered into every fragment.** Onward/lateral links (backlinks from depth 4 up) ride in the fragment HTML; `data-*` attributes carry only machine state (id, depth, max). No client-side graph computation, no secondary fetches.
- **Every link is a real link.** `href` points at the node page (noscript floor); `hx-get` points at the fragment (smooth path); `hx-push-url` keeps URLs honest.

## Verification

`make verify` green, coverage ≥90%; golden-content assertions against a synthetic closed graph and the real exemplars (dangling-allowed); `star-actually build` emits a complete `dist/` and `validate` exits nonzero on a broken graph.
