---
created: 2026-07-03
status: complete
type: ho
project: star-actually
ho: ho-00
title: Orientation
builds-on: kamae-4-star-actually-ho-overview
---

# ho-00 — Orientation

**Goal:** the encoded environment. A fresh session lands in this repo and finds the standard already declared: verification stack green, layout in place, documents pointing at each other in reading order.

## Scope

**In:** uv project, `star_actually` package (src layout), ruff + mypy strict + pytest with ≥90% coverage floor, pre-commit hooks, Makefile, project CLAUDE.md, `site.yaml`, directory skeleton (`nodes/`, `templates/`, `assets/`, `portal/`), runtime deps declared (PyYAML, markdown-it-py, Jinja2).

**Out:** any parsing, rendering, or content. The package ships `__version__` and nothing else. ho-01 starts the real work.

## Deliverables

1. `pyproject.toml` from the practitioner baseline, filled for this project (py312, package `star_actually`, CLI entry `star-actually`).
2. `.pre-commit-config.yaml` from baseline, `types-PyYAML` added for mypy.
3. `Makefile`: `verify` (lint → typecheck → test), `build`, `serve`, `install`.
4. `CLAUDE.md` with reading order, verification rhythm, and project rules (JS budget, zero external requests, provenance discipline, dual licensing).
5. `site.yaml` — the domain boundary: everything SSH-specific that isn't a node.
6. Green verification stack: `make verify` passes with the skeleton suite.

## Verification

`uv sync` clean · `pre-commit run --all-files` clean · `make verify` green (coverage floor met on the skeleton).
