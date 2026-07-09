---
ho: ho-12
shape: ri
title: Engine extraction — ssh-actually becomes an instance
created: 2026-07-08
status: closed
supersedes: []
builds-on: [ho-08-integration-and-smoke]
---

# ho-12 — Engine extraction

## Problem

`*, Actually` was always meant to be a reusable system with `SSH, Actually` as
its first instance. The engine and the SSH content lived in one repo. To stand
up a second instance (`ho-actually`, the Ho System), the engine had to become a
shared package. This ho cuts that seam from the instance's side.

## What changed here

- **Removed** `src/star_actually/`, `templates/`, `assets/`, `portal/` — they
  moved to the new `star-actually` engine repo (`../star-actually/engine`).
- **`pyproject.toml`** is now a *virtual project* (no `[build-system]`): it
  declares a dependency on `star-actually` and pins it via `[tool.uv.sources]`
  — an editable path for local dev across the `star-actually/` family, with a
  git-tag pin noted for CI/deploy.
- **Tests**: the engine's unit tests left with the engine. The content-coupled
  tests that assert facts about *this subject* — the real 60-node graph, the
  real `site.yaml`, the exemplar node shapes, provenance discipline — were
  gathered into `tests/test_content.py` and now run against the installed
  engine.
- **`Makefile` / `.pre-commit-config.yaml`** now lint and typecheck `tests`
  only; `validate` / `build` / `serve` remain (this repo has content).
- **`CLAUDE.md`** updated: the engine-seam hard rule is now a repo boundary; the
  coverage floor and JS budget belong to the engine repo.

## Forward-only

The engine repo begins its own history at its `ho-00`, referencing this repo at
commit `2041f10` as the extraction origin. Nothing in the SSH build record
(`ho-00` → `ho-11`) was edited; this ho is the response to what the project now
knows. `ho-09` (deploy) and the provenance sign-off remain open and unchanged.

## The seam held

The extraction was the first real test of "the engine stays domain-blind." One
genuine coupling surfaced and was fixed **in the engine**, not here: the Loom
had resolved `templates/` and `assets/` from the working directory, which only
worked because the monorepo put them at the root. They are now engine package
data, loaded package-relative. The instance supplies only `nodes/` + `site.yaml`.

## Verification (by command)

- Engine: `make verify` green — ruff, mypy --strict, 70 synthetic tests, 97%
  coverage, with no `nodes/` or `site.yaml` in the repo.
- This instance: `star-actually validate` → `ok: 60 nodes, graph is sound`;
  `star-actually build` → `286 pages, 224 fragments`; `make verify` green — 9
  content tests pass; no new external requests in `dist/`.

## Not done (unchanged by this ho)

Deploy (`ho-09`), provenance sign-off (37 synthesized layers), the receptionist
wireup (now an engine concern), and the physical relocation of this repo into
`star-actually/` are all still open.
