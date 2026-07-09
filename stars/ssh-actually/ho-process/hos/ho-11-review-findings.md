---
created: 2026-07-04
status: complete
type: ho
project: star-actually
ho: ho-11
title: Review Findings
builds-on: ho-10-interaction-findings-1
---

# ho-11 — Review Findings

**Goal:** land the ten confirmed findings from the cross-model verification pass (high-effort multi-agent review, independent adversarial verification per finding). The build had been written and tested by one agent; this is the layer that catches what that agent couldn't see about itself.

## Fixed

1. **Entry-screen journey destruction** — `goBack`/`goReturn`/`goRailIndex` now refuse to mutate the journey unless a live node page is on screen; off the graph, back is the browser's back.
2. **`/ask` cost exposure** — in-process rate limiting (per-IP and global, env-tunable) plus prompt caching on the ~5k-token catalog system prompt (~90% input cost cut on warm asks). Caddy remains the real perimeter at deploy.
3. **Browser Back desync** — `htmx:historyRestore`/`popstate` now re-align the journey to whatever node is actually on screen (truncate to last visit, or record a new one).
4. **Dead `suppressRecord` flag** — replaced with a counter consumed once per suppressed swap; rapid back-presses no longer write phantom visits.
5. **Silent root_node typo** — strict validate *and* strict build now fail loudly when `site.root_node` doesn't exist; dangling mode keeps the warning.
6. **Search race** — a sequence token discards stale async Pagefind results.
7. **Enter felt dead when /ask hangs** — timeout tightened to 1.5s with a visible "asking the receptionist…" state; fallback clears it.
8. **Stale portal catalog** — mtime-keyed cache replaces `lru_cache`; a site rebuild is picked up on the next request.
9. **Bare-fragment noscript floor** — every depth now also renders as a full chrome page (`/n/<id>/dN/`); dial `href`s point at pages, htmx swaps keep using fragments. 286 pages, all shareable.
10. **Depth-1 prose loss** — the schema now enforces what the renderer assumes: the depth-1 layer must be exactly the title, so nothing can silently vanish.

Below-cap cleanups from the review (template duplication, per-request client construction, redundant renders) are noted in the review transcript and deliberately not taken — they're refactors, not defects.

## Constraint flag for the practitioner

`assets/app.js` is now **450 lines** against the encoded "~400, one file, no build step" budget. The 47 added lines are state-machine correctness (resync, guards, race token), not features. Ruling needed: amend the budget (~500) or direct a trim; the one-file/no-build/readable constraints are intact either way.

## Verification

`make verify` green (79 tests, 97% coverage); strict build 286 pages / 224 fragments; smoke walk re-run clean (12,067 links).
