---
created: 2026-07-04
status: complete
type: ho
project: star-actually
ho: ho-06
title: The Index
builds-on: ho-05-the-motion
---

# ho-06 — The Index

**Goal:** the question box works without any AI. Catalog matching for concept entry, Pagefind for full-text, both from the entry screen — the complete no-Receptionist entry path.

## Scope

**In:** search corpus pages (`n/<id>/full.html` — every node at max depth, unlinked, indexing-only), Pagefind at build time (pinned 1.3.0 via npx, glob-limited to the corpus), `--no-search` flag for fast/dev builds, entry-screen behavior in `app.js`: as-you-type catalog scoring (title > entry phrases > summary), full-text fallback via Pagefind's JS API, Enter lands on the top hit.

**Out:** the Receptionist (ho-07) — it will sit in front of this and degrade to it.

## Decisions made here

- **Index the deepest layer, land at the default.** Search reads `full.html` (all layers, so "StrictModes" finds permission-denied); results link to the node page at its landing depth. The corpus page is a search artifact, never navigation.
- **Catalog first, full-text second.** A title/entry-phrase hit is a concept answer; prose hits are the fallback, labeled as such.
- **Pagefind's JS API, not its UI bundle.** The entry screen stays ours; Pagefind contributes results, not chrome.

## Verification

`make verify` green; built site has `/pagefind/pagefind.js` and per-node `full.html`; entry screen matches "forwarding" → Agent Forwarding via catalog and "StrictModes" → Permission Denied via full-text; `app.js` stays ≤ ~400 lines.
