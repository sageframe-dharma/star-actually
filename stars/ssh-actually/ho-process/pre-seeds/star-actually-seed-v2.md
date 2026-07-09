# \*, Actually — Project Seed

**Version:** Draft 2
**Date:** April 11, 2026
**Status:** In progress — open threads remain

---

## 1. The Problem

Technical knowledge is inaccessible — not because it's secret, but because it's structured wrong.

Documentation is organized around products, not around people trying to learn. Help systems mirror the software's menu structure. Tutorials teach commands without understanding. Reference docs assume expertise the reader doesn't have. The result is a landscape with only two altitudes: dumbed-down tutorials that build no mental model, and expert-only references that assume you already have one.

The middle ground — deep, real understanding delivered at the depth you need, entered from the question you actually have — does not exist as a designed experience.

Google patches over this by accident. You search your question, find a blog post written by a stranger, build your mental model from their partial understanding, and move on. This works until it doesn't. The mental model you build is fragmented, full of gaps, and shaped by whoever happened to rank highest that day.

Man pages have the right instinct — text-first, no decoration, definition-forward — but they're built for people who already understand the concept and need the syntax. They're reference, not learning.

The structural failure is the same one that plagues education: content is organized for the system's convenience, not for how people actually learn. Curricula follow semesters. Documentation follows feature lists. Neither follows the learner's path.

The problem is not a lack of information. It is not even that information is poorly written — much of it is excellent. The problem is that information is organized around the wrong axis.

---

## 2. The Landscape

**Wikis (Wikipedia, Arch Wiki, various project wikis)**
Hyperlinked, extensive, community-maintained. The backlink model is right. The depth model is wrong — every article is one altitude, and that altitude is either too shallow or too deep. The navigation model fails: you follow links without any sense of where you are in a knowledge structure or how to get back. You start wanting to understand the War of 1812 and end up reading about the sex organs of Javanese native flowers. The rabbit hole isn't a feature — it's a navigation failure.

**Man pages / info pages**
Definition-first, exhaustive, zero narrative. The right instinct (text-first, no decoration, keyboard-driven) applied to the wrong audience (experts only) with no depth adjustment. They should be the best thing in computing. They kind of suck.

**TiddlyWiki**
The closest existing thing to what \*, Actually wants to be. Self-contained, node-based, hyperlinked, runs without a server. The content architecture is right. The UX is dated and clunky. No depth model. No navigation awareness. No sense of "where am I and how do I get back."

**DevDocs.io**
Unified search across API documentation. Search is good. Content is other people's docs repackaged. No mental models, no progressive understanding, no authored depth.

**Gwern.net**
Layered depth (collapsible sections, sidenotes, progressive disclosure). Backlinks. Single-author knowledge site built with real care for information architecture. Closest in spirit — but the experience is more "brilliant person's research notebook" than "navigable knowledge." Interesting but unhinged in a way that doesn't lead to greater clarity. A reference, not a model.

**Obsidian**
The graph model is right — nodes, backlinks, relationships. The graph _visualization_ is almost useless for navigation (pretty, zero signal). What Obsidian gets right is structural: every note knows what links to it. What it gets wrong is that it's a tool for the author, not a reading experience for the learner.

**Interactive tutorials (Codecademy, freeCodeCamp, etc.)**
Guided paths through material. Always shallow. Always rigid. You cannot enter from your question — you enter from lesson one. They teach commands, not understanding.

**YSAP (You Suck at Programming / ysap.sh)**
The tone is right — deep domain knowledge (sysadmin, Unix, bash) delivered without gatekeeping, with personality and humor. The format is video and blog, not navigable knowledge architecture. A spiritual predecessor in energy, not in structure.

**What doesn't exist:**
A system where knowledge is structured as a navigable graph of interconnected concepts — not facts, but _relationships_ between ideas — each with authored depth layers, discoverable through questions, navigable with spatial awareness (what's ahead, what's behind, where you came from, how to get back), rendered in a terminal-aesthetic text-first interface where the content is the only thing that matters.

The pieces exist separately. The synthesis does not.

---

## 3. The Vision

\*, Actually makes technical knowledge navigable.

You arrive with a question. Not a problem — a question. The question could be "What is SSH?" It could be "How the fuck do I juggle three GitHub SSH logins across multiple repositories?" It could be "At what point do I need a physical auth key?" or "Is OAuth plus password plus Tailscale plus MFA too much for my home network?" or "How does Proton encrypt my mail?" Some are practical. Some are curiosity. All are valid entry points.

You type your question into a prompt. The system maps it to the right place in the knowledge graph. You land on a node. You see where you are: the path you've traveled above, the directions you could go below, the lateral detours available to the sides. You're reading at whatever depth your question implies — a sophisticated question dials you in deeper than a basic one.

Each node is a concept, tuned to a depth. You see the name. If you know what it means, you move on. If you don't, you dial down: the definition appears. Dial again: usage and context. Again: how this concept relates to others. Again: the full theory. You stop when you understand. You never read more than you need.

If you detour laterally — follow a relationship to a connected concept — you're on a branch. Your main inquiry stays visible. When you're done exploring the branch, you return to where you were, at the depth you were at. The system remembers your path. Getting lost is not possible.

The content is built around mental models and relationships, not facts. *, Actually doesn't tell you what to type. It builds understanding of *why* the system works the way it does, how its pieces connect, and where you stand inside it. The knowledge is relational: concepts depend on, illuminate, and constrain each other. The graph *is\* the understanding.

The experience is pure terminal. Dark screen. Blinking cursor. "What do you want to know about SSH, actually?" Available actions are always visible on screen. Navigation is keyboard-driven. There is no chrome, no decoration, no framework overhead, no newsletter modal. A love letter to the early web, when hyperlinked documents were a revelation and nobody had figured out how to ruin them yet.

Problems? No question. Questions? No problem.

100% signal, 0% noise.

---

## 4. Audience

**Learners:** Technically capable people with questions about a specific domain. Developers, homelab operators, sysadmins, self-hosters, students — anyone who has a real question, has googled it, found five conflicting Stack Overflow answers, and wants someone to explain the actual mental model. They're not stupid. They're underserved. The documentation they've found is organized for someone else.

**Authors (future, post-v1):** People with deep domain knowledge who want to structure it for others. This audience emerges when the system proves itself with SSH, Actually and the authoring workflow is documented. The author mode is for me first and for others later.

---

## 5. Identity

**The system:** \*, Actually (spoken: "star actually" or "anything actually")

**The first instance:** SSH, Actually

**The name:** The asterisk is a wildcard — a glob pattern. "Actually" is the correction — the word you use when you're about to fix a misconception. Together: anything you thought you understood but actually didn't, explained properly. The repo name `ssh-actually` carries the joke for those who catch it. The system name `star-actually` or `*-actually` carries the extensibility.

**The tone:** Don't Panic. Deep knowledge delivered with geeky joy. YSAP energy — expert-level understanding that never makes you feel stupid for not already having it. The humor is earned, not performed. The knowledge is serious, not solemn. The energy is what I bring to it, not a design system applied on top.

**Tagline:** 100% signal, 0% noise.

---

## 6. Project Nature and Intent

**Open source.** The system and the content. License TBD.

**Published on GitHub** under `sageframe-no-kaji`.

**SSH, Actually is both the first product and the proof of concept.** If the navigation model, depth dial, and content architecture work for SSH, the system is validated. If they don't, the system is wrong.

**Built SSH-first, designed system-agnostic.** The data model, build system, and navigation are not SSH-specific. SSH, Actually is the first content set, not the only possible one. But the system is designed _through_ building SSH, Actually — not abstracted in advance. Good programming means building concretely and extracting the general case when the concrete case works.

**Domains where \*, Actually works:** Technical knowledge that is _relational_ — concepts that depend on, connect to, and illuminate each other. SSH. Linux. Networking. Grammar and linguistics. Architectural history. Any domain where understanding requires navigating relationships, not looking up isolated facts. This is not a phone book. This is not a changelog. This is not step-by-step software support. This works where knowledge is a graph.

**What this is also:** A demonstration of a broader practice. This project is an expression of the same principles behind Kṣetra-Ops, the Ho System, and the writing practice: understand the system before you build in it, design for the human's path, put philosophy before implementation.

---

## 7. Architecture Direction

_Opinions, not commitments._

### Content architecture

Each piece of content is a **node** — a markdown file with YAML frontmatter:

```yaml
---
id: agent-forwarding
title: Agent Forwarding
type: concept  # concept | procedure | definition | scenario | troubleshooting
requires: [ssh-agents, key-pairs, ssh-config-basics]
related: [proxy-jump, trust-boundaries, hardware-keys-ssh]
entry_points: [ssh-forwarding, multi-hop, jump-host]
depth_levels: 5
---

<!-- depth:1 -->
Agent Forwarding

<!-- depth:2 -->
A feature that lets a remote server use your local SSH agent to authenticate onward — without your private key leaving your machine.

<!-- depth:3 -->
When you SSH to Server A and need to reach Server B, agent forwarding sends authentication challenges back through the connection to your local agent. The key never travels. But anyone with root on Server A can use your agent for the duration of your session.

<!-- depth:4 -->
[Full usage context, when to use vs ProxyJump, trust implications...]

<!-- depth:5 -->
[Deep technical: how the forwarded socket works, the agent protocol, attack surface analysis...]
```

Node types constrain presentation and behavior:

- **concept** — explains a mental model (e.g., "Where State Lives")
- **procedure** — step-by-step with commands (e.g., "Set Up Multiple GitHub Accounts")
- **definition** — single term, brief (e.g., "Blob")
- **scenario** — problem/recovery pattern (e.g., "Lost Hardware Key")
- **troubleshooting** — diagnostic workflow (e.g., "Permission Denied")

Depth layers are authored, never generated. The progression within a node:

1. **Name** — just the term
2. **Definition** — one or two sentences
3. **Usage and context** — when you encounter this, what it does
4. **Relationships** — how this connects to other concepts
5. **Theory / deep technical** — the full treatment, edge cases, internals

Not every node needs all five layers. A definition node might have two. A core concept might have six or seven. The depth count is in the frontmatter so the system knows what's available.

### Navigation model

The screen is spatially organized:

```
              [lateral: related concept]
                        │
    [past node 2]       │
    [past node 1]       │
         ↑              │
   ┌─────────────┐      │
   │   PRESENT   │──────┘
   │  (depth: 3) │──────┐
   └─────────────┘      │
         ↓              │
    [future node 1]     │
    [future node 2]     │
    [future node 3]     │
                        │
              [lateral: related concept]
```

**Vertical axis:** Past (above) → Present (center) → Future (below). Past nodes are where you came from. Future nodes are where the graph says you could go next.

**Horizontal axis:** Lateral moves — related concepts that aren't on your current path. Detours. Branches.

**Depth axis:** Within the present node, dial up (`+`/`=`) or down (`-`). The content at the current depth renders in the main reading area. The node's available depth range is always visible.

**Path memory:** The system tracks your path — every node visited, at what depth. Your path is visible on screen (the "past" nodes above). Returning to any previous node restores your position _and_ depth at that node. One keypress returns you to your previous position. The path is your commit history. The present is HEAD.

**Branch model:** When you move laterally, you're branching. Your main inquiry (the vertical path) stays visible. You can explore the branch as deep as you want. When you return, you're back on main at the exact node and depth where you left.

**Recentering:** The present stays centered unless you consciously recenter. If you jump way ahead or zoom out, you can recenter on any node — making it the new "present" and recalculating past/future around it.

### Presentation

**Pure terminal.** Dark background. Monospace font. Blinking cursor at the entry prompt. The interface looks and feels like a terminal — not hostile like VIM, but clean and inviting like Claude Code.

**Available actions always visible.** The bottom of the screen (or a persistent bar) shows what keys do in the current context. You never memorize commands. The screen tells you: `↑↓ navigate` `+- depth` `← return` `→ branch` `/search` `? help`. Context changes the available actions. This is how Claude Code works and it's right.

**Slash commands for meta-actions.** `/search` to search. `/path` to see your full history. `/reset` to start over. `/about` for project info. Small set, always discoverable.

**No images. No icons. No color beyond functional contrast.** The content is the interface. The design is the information architecture.

### Build system

**Static site generator.** A build script (Python, probably) that:

1. Reads the node directory (markdown files with YAML frontmatter)
2. Parses frontmatter, computes dependency graph and backlinks
3. Generates HTML pages and HTMX partials for each node and depth layer
4. Builds the client-side search index (Pagefind or Lunr.js)
5. Outputs a static site

**Adding a node = adding a file + rebuild.** The node file is the source of truth. The build computes everything else — graph relationships, backlinks, navigation neighborhoods. The system doesn't change when content changes. Only the data available to it changes.

**HTMX for all interaction.** Moving between nodes, expanding depth, loading neighbors — all partial page swaps served as HTML fragments. No full reloads. No JavaScript framework. The implementation must be simple and pure. If HTMX can't do it simply, we find what can.

### AI portal

**In v1.** A natural language query is mapped to the right entry node (or sequence of nodes). The AI parses the question, identifies the target concept(s), infers an appropriate starting depth from the sophistication of the query, and hands off to the static architecture. Then the AI is off. The architecture delivers from there.

The implementation is trivial: a single API call to parse a query and return node IDs and depth settings. Haiku-class model is sufficient. The prompt is small, the node catalog is finite, the mapping is deterministic once the AI identifies intent. Token cost is negligible.

The more specific your question, the more specific your entry point. "What is SSH?" lands you at the root, depth 1. "How do I manage multiple GitHub identities with hardware keys?" lands you three nodes deep at depth 3. The AI dials you in. The architecture takes over.

**The AI is the receptionist, not the doctor.** It gets you to the right room. The knowledge does the rest.

### Hosting

sageframe.net. Static files behind Caddy. No application server needed for the core site. The AI portal is a small endpoint — could be a serverless function, a tiny Flask app, or a client-side API call.

---

## 8. Constraints

**Skills:** Not a frontend developer. I build production software using the Ho System with AI collaboration. Python, HTML/CSS, HTMX — all within reach. Complex JavaScript frameworks are not, and are not wanted. The implementation must be simple.

**Time:** SSH, Actually needs to ship before the system is perfect. The content already exists — the SSH guide and commands reference are written. The build system and navigation model are the new work.

**Infrastructure:** Must run on existing sageframe.net infrastructure (Caddy, Docker, Proxmox). No external dependencies for the core site.

**Content restructuring:** The SSH guide needs decomposition into nodes. Each section becomes one or more nodes, frontmatter must be authored, depth layers must be written. The guide has ~15 major sections which will probably become 40–60 nodes. This is editorial work — significant but not engineering.

**The system must be simple.** Not simple as in limited. Simple as in: a person reading the code can understand what it does. No magic. No framework abstractions. HTML files, a build script, HTMX attributes. The spirit of the early web applied to the build, not just the presentation.

---

## 9. Scope Boundaries

**This IS \*, Actually:**

- A system for structuring and navigating relational technical knowledge as an interconnected graph
- A learning tool, not just a reference tool — designed for understanding, not extraction
- A static-first web experience built with HTMX
- Keyboard-navigable, terminal-aesthetic, depth-adjustable
- SSH, Actually as the first instance, system designed to be domain-agnostic

**This is NOT \*, Actually:**

- A wiki anyone can edit (single-author or curated-author model)
- A factual lookup tool (phone book, changelog, API reference)
- A step-by-step software support system
- A real-time application requiring a backend
- A replacement for Obsidian (Obsidian is the author's workspace; \*, Actually is the reader's experience)
- An AI product (AI is a portal, not the product)
- A mobile app
- A framework for non-relational content

**MVP line:** SSH, Actually ships as a navigable site with the full SSH guide content restructured into nodes. Keyboard navigation. Depth layers on core concept nodes. Search. Neighborhood navigation model (past/present/future/lateral). AI query portal. Path memory with one-keypress return. Nodes are authored as markdown files and built with a script. The build system is designed cleanly but does not need to be extracted as a reusable tool yet.

---

## 10. Success Criteria

1. Someone who doesn't understand SSH can arrive at the site with a question, find their entry point, navigate the concepts they need, and build a working mental model — without leaving the site and without reading sequentially.

2. The depth dial works: a reader can start at the name, dial down to definition, dial further to theory, and stop wherever understanding clicks. The same site serves a beginner who doesn't know what a key pair is and an experienced user trying to understand resident vs. non-resident hardware keys.

3. The rabbit hole problem is solved: a reader who follows three lateral branches can return to their main inquiry in one keypress, at the exact node and depth where they left.

4. The AI portal correctly maps a natural language question to the right entry node(s) and depth. A vague question gets a broad entry. A specific question gets a precise one.

5. Someone reading the source can understand the node schema, create a new node with correct frontmatter and depth layers, drop it in the directory, rebuild, and see it integrated into the graph.

6. The site loads fast, works in a terminal-width browser window, and feels like a place you want to explore — not a place you want to escape from.

---

## 11. Where I'm Starting From

**Content:** The SSH guide is written — 2,000+ lines of structured, progressive, definition-first technical documentation with a companion commands reference. Both need decomposition into nodes, but the knowledge, the mental models, and the pedagogical sequencing are done.

**Tech:** Python, basic HTML/CSS, production software shipped via Ho System. HTMX is new but philosophically aligned. Terminal-style UIs are familiar from daily use of Claude Code and standard Linux tools.

**Design:** Trained eye for information architecture (MIT M.Arch, 15 years of curriculum design, assessment systems, pedagogical frameworks). The navigation model draws on how I design learning paths. The depth dial draws on watching students at different levels encounter the same material.

**Infrastructure:** sageframe.net runs, Caddy serves, Docker hosts are available. Deployment is solved.

---

## 12. What I Want to Learn

How to build a genuinely novel navigation model for relational knowledge — something that works better than wikis, better than docs sites, better than tutorials. If the depth dial and spatial navigation work, that's a contribution to how technical knowledge is structured, not just to SSH documentation.

Whether a graph of 40–60 authored nodes with depth layers produces a qualitatively different learning experience than the same content in a linear document.

How the git-like branch/return model feels in practice for knowledge navigation. Whether path memory and one-keypress return actually solve the rabbit hole problem or just move it.

---

## 13. Open Questions

1. **Depth layer markup format.** HTML comments (`<!-- depth:2 -->`) work but are ugly to author. Alternatives: separate files per depth layer (clean but many files), YAML-delimited sections, or custom delimiters. Need to prototype what feels right to write.

2. **Neighborhood computation.** The "future" nodes (what's ahead) depend on where you came from — the graph has many paths through it. Is the neighborhood computed statically (always show the same forward nodes) or dynamically (show forward nodes based on your current path)? Static is simpler to build but less smart. Dynamic requires path-aware state.

3. **Default depth.** Does every node start at depth 1 (name only) when you arrive? Or do you set a global default ("I'm comfortable at depth 3, show me that everywhere")? Or does the AI portal set your initial depth and you adjust from there?

4. **Node granularity.** How small is a node? "SSH" might be ten nodes. "Signature" might be one. The right granularity probably becomes clear during content decomposition, but a principle would help: one concept per node? One mental model per node?

5. **The branch visualization.** When you're on a lateral branch, how is the main path shown? A sidebar? A faded column? A breadcrumb? The spatial model is clear conceptually but the rendering needs design.

6. **Rebuild trigger.** Is the rebuild manual (`make build`) or automatic (file watcher)? For v1, manual is fine. For the authoring experience, automatic would be better.

7. **HTMX and keyboard navigation.** HTMX handles partial page swaps cleanly. Keyboard event handling may need a small amount of vanilla JS. How small? Need to prototype.

8. **The \*, Actually system extraction.** When does SSH-specific code become domain-agnostic code? After SSH, Actually ships? During? The instinct is: build concretely, extract when the second domain arrives.

---

## Bookmarked for Later

**Substack essay:** "Understand the system before you build in it, design for the human's path, put philosophy before implementation." A throughline piece connecting Kṣetra-Ops, the Ho System, _, Actually, and the writing practice as expressions of the same design principle. Not an essay about _, Actually — an essay about the principle that \*, Actually demonstrates.

**Voice DNA connection:** The node architecture (tagged, typed, linked, layered) may be relevant to the compression/data structure problem for Voice DNA. Pure intuition at this stage. The connection is that both problems are fundamentally about structuring relational knowledge — one domain is SSH concepts, the other is writing patterns. If the data model works for one, it might inform the other. This is a separate investigation, not part of this build.

**Git visualization as navigation precedent:** The branch/return model maps to git's checkout/merge mental model. Investigate existing git visualization tools for UX precedent — how do they show branches, show HEAD, show history? The path display in \*, Actually could learn from this.

---
