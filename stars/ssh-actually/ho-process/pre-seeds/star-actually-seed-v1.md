# \*, Actually — Project Seed

**Version:** Draft 1
**Date:** April 11, 2026
**Status:** In progress — open threads remain

---

## 1. The Problem

Technical knowledge is inaccessible — not because it's secret, but because it's structured wrong.

Documentation is organized around products, not around people trying to use them. Help systems mirror the software's menu structure. Tutorials teach commands without understanding. Reference docs assume expertise the reader doesn't have. The result is a landscape with only two altitudes: dumbed-down tutorials that build no mental model, and expert-only references that assume you already have one.

The middle ground — deep, real understanding delivered at the depth you need, entered from the problem you actually have — does not exist as a designed experience.

Google patches over this by accident. You search your problem, find a blog post written by a stranger, build your mental model from their partial understanding, and move on. This works until it doesn't. The mental model you build is fragmented, full of gaps, and shaped by whoever happened to rank highest that day.

The structural failure is the same one that plagues education: content is organized for the system's convenience, not for how people actually learn. Curricula follow semesters. Documentation follows feature lists. Neither follows the learner's path.

The problem is not a lack of information. The problem is that information is organized around the wrong axis.

---

## 2. The Landscape

**Wikis (Wikipedia, Arch Wiki, various project wikis)**
Hyperlinked, extensive, community-maintained. The backlink model is right. The depth model is wrong — every article is one altitude, and that altitude is either too shallow or too deep. The navigation model is wrong — you follow links without any sense of where you are in a knowledge structure. The rabbit hole problem is real: you start wanting to understand SSH and end up reading about elliptic curve cryptography with no path back.

**Man pages / info pages**
Definition-first, exhaustive, zero narrative. Designed for people who already understand the concept and need the syntax. The right instinct (text-first, no decoration, keyboard-navigable) applied to the wrong audience (experts only).

**TiddlyWiki**
The closest existing thing to what \*, Actually wants to be. Self-contained, node-based, hyperlinked, runs without a server. The content architecture is right. The UX is dated and clunky. No depth model. No navigation awareness. No sense of "where am I and how do I get back."

**DevDocs.io**
Unified search across API documentation. Search is good. Content is other people's docs repackaged. No mental models, no progressive understanding, no authored depth.

**Gwern.net**
Layered depth (collapsible sections, sidenotes, progressive disclosure). Backlinks. Authored with care. Single-author knowledge site that takes information architecture seriously. The closest in spirit, but it's a personal site, not a reusable system. The depth mechanism is CSS toggles, not a designed navigation model.

**Obsidian**
The graph model is right — nodes, backlinks, relationships. The graph _visualization_ is almost useless for navigation (pretty, zero signal). What Obsidian gets right is structural: every note knows what links to it. What it gets wrong is presentation: it's a tool for the author, not a reading experience for the learner.

**Interactive tutorials (Codecademy, freeCodeCamp, etc.)**
Guided paths through material. The depth is always shallow. The structure is rigid. You cannot enter from your problem — you enter from lesson one. They teach commands, not understanding.

**What doesn't exist:**
A system where knowledge is structured as a navigable graph of interconnected nodes, each with authored depth layers, discoverable through problem-oriented entry points, navigable with keyboard-driven spatial awareness (what's ahead, what's behind, where you came from), and readable in a terminal-aesthetic text-first interface that treats the content as the only thing that matters.

The pieces exist separately. The synthesis does not.

---

## 3. The Vision

\*, Actually makes technical knowledge navigable.

You arrive with a problem. You find your entry point — through search, through an AI-assisted query, or by browsing. You land on a node. You see where you are: the nodes ahead of you, the nodes behind you, the depth available beneath you. You read at whatever altitude makes sense for your current understanding. If you need more depth, you drill down — the content expands in place. If you need a related concept, you move laterally to a neighboring node. The system always knows where you came from and can bring you back.

The content is mental-model-first. It doesn't just tell you _what_ to type — it builds understanding of _why_ the system works the way it does. Deep domain knowledge, no gatekeeping, no prerequisites beyond curiosity.

The experience is text-first, keyboard-driven, fast. No images, no animations, no framework overhead. A love letter to the early web, when hyperlinked documents were a revelation and the browser hadn't been colonized by ads and modals and newsletter popups.

The first instance is SSH, Actually — a complete, navigable knowledge base for SSH, key pairs, hardware security keys, and modern authentication. The system underneath it is designed for extraction: any domain of technical knowledge that is specific, relational, and concept-dependent can be structured this way.

---

## 4. Audience

Two audiences:

**Readers:** Technically capable people who are confused by a specific domain and tired of bad documentation. Developers, homelab operators, sysadmins, self-hosters, students — anyone who has a real problem, has googled it, found five conflicting Stack Overflow answers, and wants someone to just explain the actual mental model. The SSH guide's audience is the first instance of this: people who use SSH but don't understand it.

**Authors (future):** People who have deep domain knowledge and want to structure it for others. This audience doesn't exist yet — it emerges when the system proves itself with SSH, Actually and the authoring workflow is documented. The author mode is for me first and for others later.

---

## 5. Identity

**The system:** \*, Actually (pronounced "star actually" or "anything actually")

**The first instance:** SSH, Actually

**The name:** A triple reference. HTMX, Actually — the build philosophy (you don't need React for this). Love Actually — the pop culture hook (actually, let me explain this properly). And the conversational "actually" — the word you use when you're about to correct a misconception. "Actually, SSH doesn't work that way."

**The repo:** `ssh-actually` for the first instance. System repo TBD.

**The tone:** Don't Panic. Deep knowledge delivered with geeky joy, not institutional authority. You Suck at Coding energy — expert-level understanding that never makes you feel stupid for not already having it. The humor is real, not performed. The knowledge is serious, not solemn.

100% signal, 0% noise.

---

## 6. Project Nature and Intent

**Open source.** The system and the content. GPL or MIT — TBD.

**Published on GitHub** under `sageframe-no-kaji` (or a dedicated org if the project grows).

**SSH, Actually is both the first product and the proof of concept.** If the navigation model, depth dial, and content architecture work for SSH, the system is validated. If they don't, the system is wrong, and that's important to know before building for other domains.

**The system is designed for extraction.** SSH, Actually is built with the \*, Actually architecture, but the architecture is not SSH-specific. The build system, the node schema, the navigation model, the HTMX rendering — all of it should be reusable for any domain.

**A demonstration of the broader practice.** This project is an expression of the same principles behind Kṣetra-Ops, the Ho System, and the writing practice: understand the system before you build in it, design for the human's path, put philosophy before implementation.

---

## 7. Architecture Direction

_Opinions, not commitments._

### Content architecture

Each piece of content is a **node** — a markdown file with YAML frontmatter:

```yaml
---
id: agent-forwarding
title: Agent Forwarding
type: concept # concept | procedure | definition | scenario | troubleshooting
requires: [ssh-agents, key-pairs, ssh-config-basics]
related: [proxy-jump, trust-boundaries, hardware-keys-ssh]
entry_points: [ssh-forwarding, multi-hop, jump-host]
depth_levels: 3 # how many authored depth layers this node has
---
```

Node types constrain presentation and behavior:

- **concept** — explains a mental model (e.g., "Where State Lives")
- **procedure** — step-by-step with commands (e.g., "Set Up Multiple GitHub Accounts")
- **definition** — single term, brief (e.g., "Blob")
- **scenario** — problem/recovery pattern (e.g., "Lost Hardware Key")
- **troubleshooting** — diagnostic workflow (e.g., "Permission Denied")

Depth layers within a node are authored, not generated. The author writes each layer:

- **Layer 1:** One-sentence definition or summary
- **Layer 2:** Mental model — the "why" explanation
- **Layer 3:** Full technical treatment with edge cases and examples
- Additional layers as warranted by content complexity

Layers are separated within the markdown file using a delimiter (TBD — possibly `<!-- depth:2 -->` comments or YAML-delimited sections).

### Navigation model

The reader is always "at" a node, at a depth. The visible neighborhood shows:

- The current node at the current depth
- 4–6 forward nodes (where you could go next, based on the graph)
- 2–3 backward nodes (where you came from)
- Available depth (can you drill down? can you lift up?)

Nodes are rendered as minimal cards — title, type indicator, current depth level. The active node's content is expanded. Navigation is keyboard-driven:

- Arrow keys or similar for lateral movement between visible nodes
- Depth up/down keys for vertical movement within a node
- A "zoom out" key to leave the neighborhood and enter a broader view (search, category, or graph overview)
- Breadcrumb / path state maintained so "back" returns to your previous position _and_ depth

### Presentation

**Text-first.** Monospace or clean sans-serif — TBD. No images. No icons (or minimal). No color beyond functional contrast. The aesthetic is "well-designed terminal" — information-dense, zero decoration, the content is the interface.

**Terminal-inspired UX.** An entry prompt: "What do you want to know about SSH, actually?" Keyboard shortcuts visible on screen — the interface always tells you what keys are available. Think `lazygit` or `ranger` — tools that show you what you can do at every moment.

**HTMX for partial loading.** Moving between nodes, expanding depth, loading neighbors — all partial page swaps. No full reloads. No client-side routing framework. The server (or static build) serves HTML fragments. HTMX swaps them in.

### Build system

**Static site generator** — likely a custom Python script or a lightweight tool. Reads the node directory, parses frontmatter, computes the dependency graph and backlinks, generates HTML pages and HTMX partials, builds the search index.

**Search:** Client-side (Pagefind or Lunr.js). No server dependency for search. The fuzzy AI query portal is a separate, optional layer — not required for the site to function.

**AI portal (v2):** A single input that takes a natural language query, maps it to the right entry node (or sequence of nodes), and hands off to the static architecture. The AI interprets. The architecture delivers. Then the AI is off. Implementation TBD — could be a small API endpoint, could be client-side with a lightweight model, could be a Claude API call. Not in v1.

### Hosting

sageframe.net. Served from existing infrastructure. Static files behind Caddy. No application server needed for v1.

---

## 8. Constraints

**Skills:** I am not a frontend developer. I build production software using the Ho System with AI collaboration. Python, basic HTML/CSS, HTMX — all within reach. Complex JavaScript frameworks are not. The architecture must be buildable with simple tools.

**Time:** SSH, Actually needs to ship before the system is perfect. The content already exists — the SSH guide and commands reference are written. The build system and navigation model are the new work.

**Infrastructure:** Must run on the existing sageframe.net infrastructure (Caddy, Docker, Proxmox). No external dependencies for the core site. The AI portal can use external APIs but must be optional.

**Content:** The SSH guide needs restructuring into nodes. This is editorial work, not engineering — but it's real work. Each section of the current guide becomes one or more nodes, frontmatter must be authored, depth layers must be written. The guide has ~15 major sections which will probably become 40–60 nodes.

---

## 9. Scope Boundaries

**This IS \*, Actually:**

- A system for structuring and navigating technical knowledge as an interconnected graph
- A static-first web experience built with HTMX
- Keyboard-navigable, text-first, depth-adjustable
- SSH, Actually as the first instance

**This is NOT \*, Actually:**

- A wiki anyone can edit (single-author or curated-author model)
- A real-time application requiring a backend
- A replacement for Obsidian (Obsidian is the author's workspace; \*, Actually is the reader's experience)
- An AI product (AI is a portal, not the product)
- A mobile app
- A framework for non-technical content

**MVP line:** SSH, Actually ships as a navigable site with the full SSH guide content restructured into nodes, keyboard navigation, depth layers on at least the core concept nodes, search, and the neighborhood navigation model. No AI portal. No author mode UI. Nodes are authored as markdown files and built with a script. The build system does not need to be extractable yet — it needs to work for SSH, Actually.

---

## 10. Success Criteria

1. Someone who doesn't understand SSH can arrive at the site, enter their problem, navigate to the relevant concepts, and build a working mental model — without leaving the site and without reading the whole guide sequentially.

2. The depth dial works: a reader can start at summary depth, drill down where they need more, and stay at surface level where they don't. The same site serves a beginner setting up their first SSH key and an experienced user trying to understand resident vs. non-resident hardware keys.

3. The rabbit hole problem is solved: a reader who follows three lateral links can get back to where they started in one action.

4. Someone looking at the site's source can understand the node schema, create a new node with correct frontmatter, and add it to the site with a rebuild.

5. The site loads fast, works without JavaScript disabled (progressive enhancement), and feels like a place you want to spend time reading — not a place you want to escape from.

---

## 11. Where I'm Starting From

**Content:** The SSH guide is written — 2,000+ lines of structured, progressive, definition-first technical documentation. The commands reference is written. Both need restructuring into nodes, but the hard work (the actual knowledge, the mental models, the pedagogical sequencing) is done.

**Tech:** I can build Python tools and static sites. I have shipped production software. HTMX is new to me but its philosophy aligns with how I think. Complex frontend work is outside my current skills — the architecture must not require it.

**Design:** I have a trained eye for information architecture (MIT M.Arch, 15 years of curriculum design, assessment systems, and pedagogical frameworks). The navigation model draws directly on how I think about learning paths. The depth dial draws on my experience watching students at different levels encounter the same material.

**Infrastructure:** sageframe.net exists, Caddy runs, Docker hosts are available. Deployment is a solved problem.

---

## 12. What I Want to Learn

How to build a genuinely novel navigation model for knowledge — something that works better than wikis, better than docs sites, better than tutorials. If the depth dial and neighborhood navigation work, that's a contribution to how technical knowledge is structured, not just a contribution to SSH documentation.

Whether HTMX can deliver the interaction model I'm imagining — partial swaps, keyboard navigation, spatial awareness — without a JavaScript framework.

Whether the node architecture is sufficient or whether it breaks at scale (60 nodes is one thing; 600 is another).

---

## 13. Open Questions

1. **Depth layer markup:** How are layers delimited within a markdown file? HTML comments? YAML frontmatter sections? Separate files per layer? Need to prototype and see what feels right to author.

2. **Graph computation:** How is the "neighborhood" computed? The `requires` field gives a dependency tree. `related` gives lateral connections. But the 4–6 forward nodes need to be computed contextually — what's "ahead" depends on where you came from. Is this a static computation or does it need path-aware state?

3. **Keyboard navigation framework:** Does a lightweight JS library for terminal-style keyboard UIs exist, or does this need custom code? The interaction model (visible shortcuts, modal key bindings, spatial navigation) is specific enough that existing solutions may not fit.

4. **Depth dial vs. progressive disclosure:** Is the depth dial a discrete setting (I'm at level 2, show me level-2 content for all nodes) or per-node (this node is at level 3, that node is at level 1)? Per-node is more powerful but harder to render.

5. **Node granularity:** How small is a node? Is "SSH" a node or is it ten nodes? The current guide has 15 major sections. Some (Section 12, hardware keys for SSH) are really 4–5 distinct concepts. Others (Section 3, signatures) are one clean idea. The right granularity probably becomes clear during the content restructuring.

6. **The prompt/entry UX:** How literal is the terminal metaphor? A blinking cursor on a dark background? Or a minimal text input on a light page with terminal-style typography? This affects the entire visual identity.

7. **Author mode:** Is this a v1 feature or a v2 feature? For SSH, Actually, I'm the only author. A UI for creating nodes is nice but not essential if the markdown-with-frontmatter workflow is clean.

8. **The \*, Actually system extraction:** When does the SSH-specific build become a reusable system? After SSH, Actually ships? During? The temptation to abstract too early is real.

9. **Tone in the interface itself.** The nodes are content. But the navigation chrome — prompts, error states, empty states, help text — also needs the Don't Panic energy. How much personality goes into the chrome vs. the content?

---
