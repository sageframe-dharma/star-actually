---
created: 2026-07-04
status: complete — awaiting human interaction test
type: ho
project: star-actually
ho: ho-08
title: Integration and Smoke
builds-on: ho-07-the-receptionist
---

# ho-08 — Integration and Smoke

**Goal:** the whole thing, together, walked. Strict-mode build over the complete 60-node graph, Pagefind indexed, and an agent-run smoke walk of the real function. Ends at the handoff the framework mandates: the smoke test is the floor a human interaction test has to clear, never a verdict.

## What was walked

- **Strict build:** 62 pages, 224 fragments, search index — zero warnings. The dangling-edge development mode is retired; the shipping gate is the default.
- **Completeness:** every catalog node has its page, its search corpus, and exactly its declared depth fragments — no gaps, no phantoms beyond the ceiling.
- **Link integrity:** 6,854 internal `href`/`hx-get` targets, all resolving to real files. The noscript floor is complete.
- **Purity:** zero external asset requests in any emitted page. The only outbound URL anywhere is the honest source link in help.
- **Provenance discipline:** no markers leaked into the product; review copy lives in `ho-process/provenance-report.md`.
- **Behavioral floor:** depth dial links gate correctly at both ends; backlinks appear at depth ≥4 only; entry screen carries prompt, results container, and the ↓-to-begin path; `app.js` parses clean at 403 lines.
- **Live serve:** all route types 200 over HTTP.

## Known limits of this smoke (honestly)

- **JS behavior was reviewed and syntax-checked, not browser-executed.** The journey rail, branch/return, and keyboard map meet their spec on paper; whether they *feel* right is structurally unreachable by an agent walkthrough — that is the interaction test's question, by design.
- **The Receptionist ran only against fixture clients.** No `ANTHROPIC_API_KEY` in the build environment; the first live `/ask` happens at deployment (ho-09) or on the practitioner's machine (`uv run uvicorn portal.app:app --port 8322` with a key and `STAR_ACTUALLY_CATALOG=dist/catalog.json`). The site is fully functional without it — that degradation path is the design and it is what the smoke exercised.

## → STOP: human interaction test

`make serve` → http://localhost:8321. Walk in with a real question. Findings become hos, not patches; ho-09 (deploy) waits on the verdict.
