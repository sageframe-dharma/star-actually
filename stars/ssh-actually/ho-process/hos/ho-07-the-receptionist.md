---
created: 2026-07-04
status: complete
type: ho
project: star-actually
ho: ho-07
title: The Receptionist
builds-on: ho-06-the-index
---

# ho-07 — The Receptionist

**Goal:** the AI portal. One endpoint, one Haiku call: question in → node + depth out. Then the AI is off. Graceful degradation is the design, not an afterthought.

## Scope

**In:** `portal/app.py` — FastAPI, `POST /ask`, `GET /health`. System prompt built from the real `catalog.json`; structured output via `output_config.format` (JSON schema — guaranteed parseable); server-side validation (unknown node ids rejected, depth clamped to the node's actual range); CORS restricted; injectable Anthropic client for fixture tests. Terminal wiring in `app.js`: the entry form tries `/ask` first (same-origin, short timeout), falls back to catalog/search matching if the Receptionist is absent, slow, or wrong.

**Out:** deployment (ho-09 — container via sageframe-docker-deploy, Caddy `/ask` route), rate limiting (Caddy's job).

## Decisions made here

- **Model: `claude-haiku-4-5`** (per Kamae 2: Haiku-class is sufficient; the catalog is small, the mapping is nearly deterministic). Max ~300 output tokens.
- **Structured outputs, not prompt-and-pray.** `output_config.format` with a strict JSON schema; the model cannot return unparseable text.
- **The server never trusts the model.** node_id must exist in the catalog (alternates tried in order); depth clamps to `[1, depth_levels]`. A hallucinated id degrades to 404, which the client treats exactly like a portal outage: fall back to search.
- **API key lives in the container env only.** Never client-side; the site itself stays static and secretless.

## Verification

`make verify` green (portal type-checked strict, tests via injected fake client — no live API calls in the suite); manual live smoke with a real key happens in ho-08.
