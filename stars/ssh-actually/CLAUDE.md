# SSH, Actually / \*, Actually

The first instance of \*, Actually: the SSH guide decomposed into a navigable knowledge graph — authored depth layers, spatial navigation, fully static, terminal-aesthetic. The build engine — the Loom (build), the Terminal (HTML + CSS + HTMX + one vanilla JS file), and the Receptionist — is the `star-actually` package, extracted to its own repo (`../star-actually/engine`) as of ho-12. This repo is an *instance*: content (`nodes/`) and config (`site.yaml`) that the engine renders.

## Languages

@~/.claude/modules/languages-python.md
@~/.claude/modules/languages-web.md

## Reading order for a fresh session

1. `README.md` — what the project is (Kamae 3)
2. `ho-process/kamae-2-star-actually-system-design.md` — committed architecture (Kamae 2)
3. `ho-process/kamae-4-star-actually-ho-overview.md` — build sequence (Kamae 4)
4. The current ho in `ho-process/hos/` — the bounded scope for this session (Kamae 5)

## Verification rhythm

Run after every implementation, before every commit:

- `make verify` — ruff format check + ruff lint + mypy strict + pytest (content tests)
- The engine's unit tests and **≥90% coverage floor** live in the `star-actually` engine repo, not here. This repo's tests (`tests/test_content.py`) assert facts about the SSH content — the real 60-node graph, the exemplar node shapes, provenance discipline.
- `star-actually validate && star-actually build` must succeed whenever nodes change

## Kokoroe

- **The spec is the authorization.** The ho document bounds the session; work outside it is not authorized by momentum.
- **Verify by command, not by assertion.** A claim that the build passes is a transcript, not a sentence.
- **Halt on surprise.** Unexpected state, failing assumptions, or off-spec discoveries stop the work and surface to the practitioner.
- **Propose, don't decide.** Architectural questions the documents don't answer go back to the practitioner.

## Hard rules (this project)

- **Never sign commits or PRs with AI attribution tags.** No `Co-Authored-By: Claude`, no `Generated with Claude Code` — anywhere. Strip any template that includes one.
- **Zero external requests in the shipped site.** No webfonts, no CDNs, no analytics, no icons. htmx is vendored. If a feature needs an external request, the feature is wrong.
- **The JS budget (one file, no build step) is the engine's** — `assets/app.js` now lives in the `star-actually` repo, and the practitioner ruled its ceiling at ~450 lines (2026-07-05). This instance ships no JS of its own.
- **The engine is domain-blind and now a separate repo.** `src/star_actually`, `templates/`, and `assets/` were extracted to `star-actually` (ho-12); templates and assets are package data there. This repo may carry SSH only in `nodes/` and `site.yaml`. If a change needs engine code, it belongs in the engine repo. The extraction seam is now a repo boundary.
- **Depth layers are authored, never generated.** During decomposition, every layer carries a provenance marker (`extracted` | `synthesized`); synthesized prose is voice-audited and human-reviewed before sign-off. The Loom strips markers at build.
- **Dual licensing.** Code is MIT (`LICENSE`); content — `guide/` and `nodes/` — is CC BY-ND 4.0 (`LICENSE-CONTENT`). Content edits are edits to a licensed, published work; treat with care.

## Project conventions

- Node schema is Kamae 2 §4 and frozen as of ho-01. Schema changes after that are a new ho, not a drive-by.
- `dist/` is build output, never committed, never edited.
- Pagefind runs via pinned `npx` at build time — the only Node touchpoint; nothing from npm ships to the client except vendored htmx.
- Engine template/render tests live in the `star-actually` repo. This repo's `tests/test_content.py` asserts the real 60-node graph and exemplar node shapes against the installed engine.
- HTMX endpoints are static files: fragments return HTML, neighborhood data rides as `data-*` attributes.

## Ho process

- `ho-process/` is tracked publicly — the build record is part of the methodology demonstration.
- `ho-process/hos/` — per-ho documents (Kamae 5); `ho-process/agent-tasks/` — dandori specs for content batches.
- Content track (ho-C*) runs parallel to the system track; batch boundaries are practitioner review surfaces.

## References

- Ho System framework: https://github.com/sageframe-no-kaji/ho-system
- Sibling precedent (public ho-process): https://github.com/sageframe-no-kaji/sharibako
- Design lineage: The Monospace Web — https://owickstrom.github.io/the-monospace-web/
