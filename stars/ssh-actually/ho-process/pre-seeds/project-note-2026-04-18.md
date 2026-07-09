# \*, Actually — Interactive System: Project Note

**Date:** April 18, 2026
**Status:** Planned — content decomposition needed before build
**Context:** This note captures the plan to build the interactive navigable version of \*, Actually, using SSH, Actually as the first content set.

---

## What Exists

- **SSH, Actually guide** — a complete static document covering SSH, key pairs, hardware security keys, and modern authentication. Organized around mental models, not commands. Published on GitHub.
- **\*, Actually seed document (v4)** — full project seed defining the vision, architecture, content model, navigation model, and identity. Ready for System Design.
- **about-the-hero page on atmarcus.net** — a proof of concept for progressive-depth explanation (zero to full implementation in 9 sections with depth badges and interactive demos). Not a \*, Actually instance, but demonstrates the approach.

## What Needs to Happen

### Phase 1: Content Decomposition (the real work)

The SSH, Actually guide needs to be decomposed from a linear document into nodes with authored depth layers.

**Each node is a concept** with up to five depth levels:

1. **Name** — just the term
2. **Definition** — one or two sentences
3. **Usage and context** — when you encounter this, what it does
4. **Relationships** — how this connects to other concepts
5. **Theory / deep technical** — the full treatment, edge cases, internals

**The content already exists.** This is decomposition, not creation. The guide covers: SSH basics, key pairs, key types, SSH agents, agent forwarding, SSH config, ProxyJump, hardware security keys, FIDO2/WebAuthn, git SSH configuration, multi-account setups, trust boundaries, and more.

**AI-assisted workflow:**

- Use Claude to decompose the existing guide into candidate nodes
- Use Claude to draft depth layers from existing content
- Human judgment: what belongs at depth 2 vs. depth 4, what relationships exist, what the entry points are
- Human authorship: final voice, final structure, final decisions

**Output:** Markdown files with YAML frontmatter, one per node:

```yaml
---
id: agent-forwarding
title: Agent Forwarding
type: concept
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

### Phase 2: System Build

**Stack (from seed):** HTMX + FastAPI. Terminal-aesthetic. Keyboard-driven. Zero framework overhead.

**Components:**

- FastAPI backend serving rendered HTML fragments (node ID + depth level → HTML)
- HTMX frontend: click node → load content at current depth. Dial deeper/shallower → swap fragment. No full page reload.
- Graph display: SVG with clickable nodes showing current position, connections, and navigation history. Simple for v1 — can get beautiful later.
- Question entry: text input that maps natural language questions to the nearest node in the graph. Can start simple (keyword matching) and get smarter.

**This is a standard Ho System project.** The architecture is defined in the seed. The stack is decided. The build is a few weeks once the content nodes exist.

### Phase 3: Polish and Ship

- Deploy to ssh-actually.sageframe.net
- Keyboard navigation
- Path memory (where you've been)
- Mobile responsive
- Open source the system (star-actually repo) separate from the content (ssh-actually repo)

---

## What's Novel (honest assessment)

The individual principles are established: progressive disclosure, knowledge graphs, depth-layered content, question-based entry. The synthesis is new:

- **Per-node depth control** — not per-page beginner/advanced, but per-concept depth dial
- **Entry from question, not index** — you don't find the right page first, you ask what you want to know
- **Content organized around concept relationships** — not product features or chapter order
- **Authored depth layers** — not AI-generated summaries at different compression levels, but intentionally written explanations at each tier

Nobody has built this combination as a designed experience. The closest things (Gwern.net, TiddlyWiki, DevDocs, man pages) each have one piece but not the synthesis.

---

## Priority

This project is deferred until job search pressure reduces. The seed is complete. The guide content exists. When the time comes, Phase 1 (content decomposition) is the bottleneck — the build is straightforward.

---

_Note created April 18, 2026. Drop into the star-actually or ssh-actually repo as PROJECT-NOTE.md._
