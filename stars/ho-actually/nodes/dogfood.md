---
id: dogfood
title: dogfood
type: definition
requires: []
related: []
entry_points: [dogfood]
summary: >
  Learning a tool by actually using it on a real task, the way a real user would.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
dogfood

<!-- depth:2 -->
<!-- provenance: extracted -->
Learning a tool by actually using it on a real task, the way a real user would.

<!-- depth:3 -->
<!-- provenance: extracted -->
A validation modality (d): learning the tool by _actually using it_ on a real
task, as a real user. Produces a **dogfood finding**—the practitioner's real query, the
attempts, the ranked results, the finding—which is a record (terminal on creation), not
work, and feeds later hos' Think phases. Human-run; a validation modality, not verification.

<!-- depth:4 -->
<!-- provenance: extracted -->
**The Validation Layer.** The verification stack answers one question: **did we build it _right_?**—does the code match the spec. Every layer in Section 2 serves that question. It is only half of quality.

The other half is **validation**: **did we build the _right thing_, and is it _good_?** A system can pass every test, clear every linter, and survive cross-agent and human architectural review—and still be the wrong thing, or a right thing that is confusing, unpleasant, or useless in real hands. Verification cannot catch this, because verification measures conformance to a spec, and the spec itself is what validation interrogates.

This is Section 1's thesis extended. The research there—that humans overestimate AI-assisted work—was about correctness. It holds at least as strongly for goodness. An agent reporting "the feature works" is reporting that it ran; it is not reporting that the feature is _good_, because good is not a property the agent is positioned to judge. Validation is the antidote to overconfidence about goodness, exactly as verification is the antidote to overconfidence about correctness.

<!-- depth:5 -->
<!-- provenance: extracted -->
**Dogfood finding *(canonical-provisional—adopt on 2nd use)*.** **Purpose:** a real-use finding—the practitioner's actual query *as a user*, the attempts,
the ranked results, and the finding that falls out (2.7 §3, modality *d*). Documents a real
hunt, not planned work; nothing to execute. Named after the *finding*.
**Lifecycle:** `recorded`—terminal on creation. Never "completed"; it is evidence, and its
findings feed later hos' Think phases.
**Location:** `ho-process/hos/`. shodo's instances are the mislabeled
`ho-<NN>-smoke-sidequest-<M>-<slug>.md` files; the `smoke-sidequest` token predates this
correction—new instances drop `sidequest`.
**Instances:** shodo (5 with frontmatter + 2 pre-convention drafts).

> The earlier "sidequest frontmatter schema" open question (two variants in shodo) is
> **withdrawn**: it analyzed the dogfood-finding schema, not the §3.1 sidequest type.

---
