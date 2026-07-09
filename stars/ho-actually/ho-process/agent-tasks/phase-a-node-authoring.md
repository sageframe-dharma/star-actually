# Dandori — Phase A node authoring (Ho System, Actually)

You are authoring `*, Actually` **nodes** for the Ho System instance. Each node is
a markdown file: YAML frontmatter + a body of depth layers. You extract content
**faithfully from the practitioner's own glossary** — his words, reflowed. You do
not invent, embellish, or synthesize. Every layer is marked `extracted`.

## Source (read this)

The glossary: `/Users/atmarcus/Vaults/sageframe-no-kaji-dev/ho-system/framework/glossary.md`.
Each term is a bold headword, a definition paragraph (with document citations in
`_(...)_` — ignore those), and a `_Plain: …_` line. Read your assigned entries.

## Exemplars (match these exactly)

Already authored, in `/Users/atmarcus/Vaults/sageframe-no-kaji-dev/star-actually/ho-actually/nodes/`:
`ho.md`, `mind-hand.md`, `agent-task.md`, `verification-validation.md`. Read one
or two before you start and mirror the format precisely.

## Output

Write each node to
`/Users/atmarcus/Vaults/sageframe-no-kaji-dev/star-actually/ho-actually/nodes/<id>.md`
using this exact structure:

```
---
id: <id>                      # exactly the id given; matches the filename stem
title: <title>                # exactly the title given
type: <type>                  # exactly the type given
requires: [<ids>]             # 1–2 more-foundational ids, or []
related: [<ids>]              # 1–3 sibling ids, or []
entry_points: [three or four natural-language questions a reader might ask]
summary: >
  The term's `_Plain:_` line from the glossary, verbatim (drop the leading
  "Plain:"). One sentence, no jargon.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
<the title, verbatim>

<!-- depth:2 -->
<!-- provenance: extracted -->
<the definition: one or two sentences, drawn from the glossary entry's opening —
the "what it is". Plain, no citations.>

<!-- depth:3 -->
<!-- provenance: extracted -->
<usage / fuller context: the rest of the glossary entry's substance — how it is
used, its distinctions, its tradeoffs — reflowed into a short paragraph or two.>
```

## Hard rules

1. **Extracted only.** Use the glossary's own wording, lightly reflowed. No new
   claims, no invented examples. If the entry is thin, author depths 1–2 only
   (contiguous — never depth 1 then 3).
2. **Depth 1 is the title, verbatim.** Nothing else on that layer.
3. **`summary` is the Plain cut, verbatim** (minus the "Plain:" label).
4. **Every layer carries `<!-- provenance: extracted -->`.**
5. **Edges may only use ids from the canonical list below.** This keeps the graph
   closed. `requires` points toward more-foundational terms (never a cycle);
   `related` names siblings. Prefer connecting to the foundational nodes so
   nothing is orphaned. When unsure, fewer edges.
6. **Markdown** in bodies: `**bold**`, `*italic*`, `>` blockquotes are fine, as in
   the exemplars. Keep Japanese readings where the glossary has them.

## Canonical id list (the only ids edges may reference)

what-is-ho-system, ho, kamae, shu-ha-ri, mind-hand, agent-task,
verification-validation, forward-only, tiered-understanding, devlog, arc,
registers, basis-of-design, builds-on, closure, compressed-chain,
constitutive-child, dandori, declared-compression, design-tuning, dogfood,
graded-eval, ha, ho-document, ho-overview, ho-00, ho-0-5, ho-process,
interaction-test, kamae-addendum, kagen, kokoroe, landing-ho,
learning-walkthrough, mutability, notes, orientation-ho, parti, phase,
precedential-thinking, propagation-ledger, reflect, release-tag,
replan-checkpoint, ri, seed, shape, shu, sidecar, sidequest, smoke-test, spike,
splits-from, standalone-agent-task, supersedes, think-execute-reflect, tripwired,
tuner

## Return

A short list: the ids you wrote, and any assigned term you could not map (with
why). Your files are the deliverable; keep the message terse.
