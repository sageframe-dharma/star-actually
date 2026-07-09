---
created: 2026-07-03
status: complete
type: system-design
project: star-actually
stage: kamae-2
kamae-chain: "seed → **system-design** → readme → ho-overview"
builds-on: kamae-1-star-actually-seed
next: kamae-3-star-actually-readme
---

# \*, Actually — System Design (Kamae 2)

**100% signal, 0% noise.**

> You arrive with a question. The receptionist walks you to the right room and leaves. From there it's you and the knowledge: a graph of concepts, each one dialable from its name down to its theory, your path always visible, your way back always one keypress. The whole thing is files on a disk behind a web server. It should feel like 1996 found out about good typography — hyperlinked documents, before anybody figured out how to ruin them.

---

## 1. Architecture Overview

\*, Actually is **fully static**. The build runs once, ahead of time, and produces every page, every fragment, every index the reader will ever touch. At read time there is no application server, no database, no rendering, no state on anyone's machine but the reader's own browser. Caddy serves files.

The one exception is the AI portal — a micro-endpoint that maps a natural-language question to a node and a depth. It is deliberately outside the core: the site is complete without it, degrades gracefully when it's down, and never touches content.

Five components:

| Component | What it is | Where it runs |
|---|---|---|
| **The Nodes** | Authored markdown files with YAML frontmatter and depth layers. The only place knowledge lives. | `nodes/` in the repo |
| **The Loom** | The Python build system. Parses nodes, validates the graph, weaves the site. | Build time only |
| **The Terminal** | The reading experience: HTML + CSS + HTMX + a small file of vanilla JS. | The reader's browser |
| **The Index** | Full-text search (Pagefind), built after rendering. | Build time; queried client-side |
| **The Receptionist** | The AI portal: one endpoint, one Haiku call, question in → node + depth out. | A tiny container |

Data flows one direction: `nodes/*.md` → Loom → `dist/` → browser. The Receptionist reads a catalog the Loom emits; it never reads the nodes themselves.

**The domain boundary.** Nothing in the Loom, the Terminal, the Index, or the Receptionist knows what SSH is. All domain knowledge lives in `nodes/` and a small `site.yaml` (title, tagline, prompt text, domain). This is the extraction seam: when the second domain arrives, the engine walks out of this repo along that line. Until then it stays put — build concretely, extract from a working system.

---

## 2. Component Breakdown

### The Nodes

One markdown file per concept. Frontmatter declares identity and relationships; the body carries the depth layers. The full schema is in §4. Nodes are the source of truth for *everything* — the graph, the navigation neighborhoods, the search index, the Receptionist's catalog are all computed from them. Adding a node is: write the file, rebuild.

### The Loom

A Python package (`star_actually`, src layout, uv-managed) with four stages, each a pure function of the previous:

1. **Parse** — read `nodes/*.md`, split frontmatter from depth layers, strip provenance markers (§4), produce typed Node objects.
2. **Validate** — every referenced id exists; no duplicate ids; depth layers are contiguous starting at 1; every node has at least depths 1–2; `site.yaml` is complete. A broken graph fails the build loudly. There is no "mostly built" site.
3. **Weave** — compute the graph: backlinks, forward neighborhoods (who requires me → where you can go next), lateral neighborhoods (related, as a symmetric union), and the entry catalog.
4. **Render** — Jinja2 templates emit the full site into `dist/`: one page and one fragment-per-depth for every node, the entry screen, the catalog, the help screen. Then Pagefind indexes the rendered pages.

The Loom is a CLI: `star-actually build` (also `validate` and `serve`, a thin dev server wrapping `http.server`). Rebuild is manual — `make build`. A watcher is an authoring convenience for the second domain, not MVP.

### The Terminal

The reading experience, and the place where "classic 1996 but gorgeous" gets earned. Design lineage: The Monospace Web (Oskar Wickström) — strict monospace grid, semantic HTML, restraint as the aesthetic. System monospace stack; no webfonts, no icons, no images, no external requests of any kind. One stylesheet.

Three layers, each functional without the next:

- **HTML** — every node is a real page at a real URL with real `<a>` links. Curl it, read it, bookmark it. The no-JS floor is a complete, navigable site.
- **HTMX** — depth dialing and node movement become fragment swaps against static paths (`/n/agent-forwarding/d3.html`). No full reloads. This is the smooth-flowing part.
- **Vanilla JS** — one file, budget ~400 lines, no build step. It owns: keyboard handling, the journey (path memory in `sessionStorage`), the branch stack, the action bar state, and deep-link depth (`?d=4`). If the file fails to load, the site degrades to the HTML floor, not to a blank screen.

Screen anatomy (terminal-width column, centered):

```
  past ▸ what-ssh-is @2 › key-pairs @3            ← the journey (dimmed)
  ────────────────────────────────────────────
  AGENT FORWARDING                    concept
  depth ▮▮▮▯▯ 3/5

  [the content at depth 3]

  ── onward ──────────────────────────────────
  ↓ proxy-jump          ↓ trust-boundaries      ← forward neighborhood
  → hardware-keys-ssh                           ← lateral (branch)
  ────────────────────────────────────────────
  ↑ back  ↓ onward  +/− depth  → branch  ↩ return  / search  ? help
```

The action bar is always visible and always true — it shows what the keys do *in the current context*, Claude Code style. Nobody memorizes anything.

### The Index

Pagefind, run over the rendered `dist/` at build time, pinned version, invoked via `npx` (the only Node touchpoint in the project, build-time only). `/` opens search; results are nodes, entered at default depth. The Loom also emits `catalog.json` — id, title, type, summary, entry phrases for every node — which the Terminal uses for instant prompt-matching before/without the Receptionist.

### The Receptionist

FastAPI, one route: `POST /ask` with `{question}` returns `{node_id, depth, alternates}`. The system prompt embeds the catalog; a Haiku-class model maps the question to an entry point and infers starting depth from the question's sophistication. Stateless, cacheable, rate-limited by Caddy. Runs as a tiny container on a homelab Docker host; Caddy routes `ssh-actually.sageframe.net/ask` to it.

Failure mode is the design: if `/ask` errors or is absent, the Terminal answers the same prompt with catalog matching + Pagefind, and the reader never sees a broken feature — just a slightly less clairvoyant doorman. The AI is the receptionist, not the doctor, and the clinic functions when the receptionist calls in sick.

---

## 3. Core Interaction

**Arrival.** Dark screen. Prompt: *"What do you want to know about SSH, actually?"* Blinking cursor. Type a question → Receptionist (or fallback) → you land on a node at an inferred depth. Or press `↓` to skip the question and enter at the root node. Or `/` to search.

**Reading.** The node renders at one depth at a time. `+` reveals the next layer *additively* (you keep what you've read — dialing 2→3 appends usage under the definition); `−` folds back up. The depth gauge always shows where you are and how deep the node goes.

**Moving.** `↓` follows the forward neighborhood (numbered if multiple). `↑` walks back along your journey, restoring the depth you were at. Every move appends to the journey; the past rail renders it.

**Branching.** `→` follows a lateral into a branch: the journey pins your position (*node @ depth*), the rail shows you're on a branch, and `↩` returns you to the pinned position in one keypress — however deep the rabbit hole went. Branches nest; `↩` pops one level.

**Recentering.** Clicking/selecting any node in the rail or neighborhoods makes it the present; past/future recompute around it. (Static neighborhoods — the graph's geometry doesn't change, only your position in it.)

**The invariant:** getting lost is not possible. At every moment the screen answers: where am I, how deep am I, where did I come from, where can I go, how do I get back.

---

## 4. Data Model

The node schema — frontmatter plus depth-layered body:

```yaml
---
id: agent-forwarding          # kebab-case, unique, the URL and the graph key
title: Agent Forwarding
type: concept                 # concept | procedure | definition | scenario | troubleshooting
requires: [ssh-agents, key-pairs, ssh-config-basics]
related: [proxy-jump, trust-boundaries, hardware-keys-ssh]
entry_points: [ssh forwarding, multi-hop, jump host]   # phrases, for the catalog
summary: >                    # one line; catalog + search result text
  Let a remote server borrow your local SSH agent — convenient, and dangerous.
---

<!-- depth:1 -->
Agent Forwarding

<!-- depth:2 -->
A feature that lets a remote server use your local SSH agent to
authenticate onward — without your private key leaving your machine.

<!-- depth:3 -->
[usage and context]

<!-- depth:4 -->
[relationships — how this connects, when to choose it over what]

<!-- depth:5 -->
[theory — the forwarded socket, the agent protocol, the attack surface]
```

**Decisions baked in:**

- **Depth semantics are fixed:** 1 name · 2 definition · 3 usage/context · 4 relationships · 5 theory. A node stops where it stops — a `definition` node may end at 2; nothing pads layers to fill the scale.
- **`depth_levels` is computed by the parser**, not declared. (Refinement over the seed's draft schema: the frontmatter field was redundant with the body, and redundant declarations drift.)
- **Depth markup is `<!-- depth:N -->`** — invisible in every markdown renderer, trivial to parse, and nobody is hand-typing it in volume: decomposition is agent-driven. Re-litigate if hand-authoring domain #2 hurts. *(Seed open question 1: closed.)*
- **Provenance markers** — during decomposition every layer carries `<!-- provenance: extracted -->` or `<!-- provenance: synthesized -->`. Extracted = the practitioner's words from the guide, possibly trimmed. Synthesized = new prose, which gets voice-audited and human-reviewed. The Loom strips both; they are scaffolding, never product. Markers are removed entirely once the practitioner signs off on the content set.
- **Granularity principle: one mental model per node.** If explaining it requires teaching two distinct models, split it. Glossary terms become `definition` nodes. Expected yield from the SSH guide: 40–60 nodes. *(Seed open question 4: closed.)*

**Graph semantics:**

- `requires` — directed: what you should have before this node. Its inverse is the **forward neighborhood** (I'm listed in their `requires` → they're where you go next).
- `related` — symmetric union: the **lateral neighborhood**. Branches.
- **Backlinks** — computed, shown at depth 4+ as "what points here."
- **Neighborhoods are static** — computed at build time from the graph, identical for every reader. The *path-aware* part of the experience (past rail, return points) is client-side journey state, not server logic. Dynamic, path-dependent forward suggestions are a v2 question. *(Seed open question 2: closed.)*

**Site output (`dist/`):**

```
dist/
├── index.html              ← the prompt screen
├── n/<id>/index.html       ← full page, node at default depth, noscript-complete
├── n/<id>/d<k>.html        ← fragment: this node at depth k (HTMX target)
├── catalog.json            ← the node catalog (Terminal fallback + Receptionist)
├── pagefind/               ← search index
└── assets/                 ← one CSS file, one JS file, htmx.min.js (vendored)
```

Neighborhood data rides inside each fragment as `data-*` attributes on the root element — no secondary fetches, no client-side graph computation.

**Default depth is 2.** A page showing only a term name looks broken to a first visitor; definition is the natural landing. The Receptionist overrides on question entry; revisiting a node via `↑` restores the depth you left it at. *(Seed open question 3: closed.)*

**Branch rendering (MVP):** single reading column, always. The rail above the content shows the journey; on a branch it pins the return point — `↩ key-pairs @3` — as a persistent line. No split panes, no faded second column; the seed's spatial diagram is realized as the rail + neighborhoods + action bar, not as literal screen quadrants. If the interaction test says the branch feeling isn't landing, that's a design ho, not a patch. *(Seed open question 5: closed — for MVP.)*

---

## 5. Technology Stack

| Layer | Choice | Why |
|---|---|---|
| Build | Python 3.12+, uv, src layout | House standard; the Loom is `star_actually` |
| Parsing | PyYAML + markdown-it-py | Boring, correct, typed |
| Templates | Jinja2 | Boring, correct |
| Interaction | HTMX (vendored, pinned) | The design philosophy, actually |
| Behavior | One vanilla JS file, ≤~400 lines, no build step | Readable by a person; the constraint is the feature. *(Seed open question 7: closed — yes, keyboard needs JS, and this much is acceptable.)* |
| Style | One CSS file, monospace grid, system mono stack | Monospace Web lineage; zero external requests |
| Search | Pagefind (pinned, via npx, build-time) | Static-native full-text search |
| Portal | FastAPI + Anthropic SDK, Haiku-class model | Smallest possible dynamic surface |
| Verification | ruff · mypy strict · pytest ≥90% on `star_actually` · pre-commit | House standard; JS is covered by the smoke walk and the human interaction test, not unit coverage |

**Rebuild is manual** (`make build`). *(Seed open question 6: closed.)*

**Extraction** happens when the second domain arrives, along the `site.yaml` + `nodes/` seam, from working code. *(Seed open question 8: closed.)*

---

## 6. Deployment Model

- **The site:** `dist/` synced to a homelab host, served by Caddy at `ssh-actually.sageframe.net`. Static files, immutable per build. Public exposure, if/when wanted, via Cloudflare Tunnel — not open ports.
- **The Receptionist:** one small container on a Docker host (jodo/chumon), deployed via the `sageframe-docker-deploy` skill; Caddy routes `/ask` to it. The API key lives in the container's env, never client-side.
- **No CI dependency for serving.** Build locally, rsync `dist/`. (Ironic and correct: the SSH guide deploys over SSH.)

---

## 7. Scope Boundaries

**MVP commitments** — the SSH guide decomposed into 40–60 nodes with authored depth layers · fully static build · depth dial · journey rail with branch/return · keyboard-first with visible action bar · search · Receptionist with graceful fallback · deployed on sageframe.net.

**Architecturally prepared for, not built:** second domain / engine extraction · path-aware forward suggestions · authoring watcher · global depth preference · public exposure · reader themes.

**Not this system, ever** (from the seed, still true): wiki editing · phone-book lookup · a mobile app · an AI product.

---

## Provisional Ho Sequence

Refined in Kamae 4. The shape: a foundation phase (scaffold; schema + parser + exemplar nodes), an engine phase (graph; render), an experience phase (terminal shell; navigation; search; receptionist), a content phase running in parallel from the moment the schema freezes (decomposition in agent-task batches), and a ship phase (integration; smoke test; deploy; **stop at the human interaction test**).

## Deferred Decisions

- **Branch rendering beyond the rail** — revisit after the practitioner walks the site (interaction test finding, not a spec).
- **Path-aware neighborhoods** — v2; needs evidence the static ones fall short.
- **Receptionist model + prompt tuning** — a ho decides the exact model id and prompt against the real catalog.
- **Public exposure and analytics-free-ness** — after the site exists; default is private-network + tunnel, no analytics.
