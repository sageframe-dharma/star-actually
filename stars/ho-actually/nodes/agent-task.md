---
id: agent-task
title: agent task (AT)
type: definition
requires: []
related: [dandori, tripwired]
entry_points: [agent task]
summary: >
  A precise, checkable spec an autonomous coding agent runs to do one bounded piece of work, halting rather than improvising when it meets a surprise.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
agent task (AT)

<!-- depth:2 -->
<!-- provenance: extracted -->
A precise, checkable spec an autonomous coding agent runs to do one bounded piece of work, halting rather than improvising when it meets a surprise.

<!-- depth:3 -->
<!-- provenance: extracted -->
The executable register: a surgical, command-verifiable spec an
autonomous coding agent reads to execute one bounded unit of work. Procedural (no
architectural decisions inside), executor-portable (names its `model:`), **tripwired**
(halts and surfaces on surprise), one commit per task. Authored via dandori. Child tasks
(`Ho-NN-AT-MM.md`) descend from a ho; standalone tasks stand alone.

<!-- depth:4 -->
<!-- provenance: extracted -->
**Agent tasks (ATs).** **Purpose:** the executable register — a surgical, command-verifiable spec an
autonomous coding agent reads to execute one bounded unit of work. No architectural
thinking inside; all decisions were extracted to the parent ho's Think phase.
**Authored by:** the kamae-5 skill's embedded dandori toolkit (child tasks) or the
practitioner directly via the standalone dandori skill (standalone tasks).
**Operational properties (the four that define the type):**

1. **Procedural.** The AT contains no undecided architecture. If specification
 requires a decision, the decision belongs upstream in the ho.
2. **Executor-portable.** Because there is no thinking in it, the AT can be dispatched
 to a cheaper model, a subagent, or any executor that reliably follows a procedural
 spec. Every AT names its executor in the `model:` frontmatter field — an unset
 model is an unmade decision. This is the operating discipline's model-choice-by-task
 principle made concrete.
3. **Escalating.** The AT is autonomous *until it finds something new*. A surprise —
 schema mismatch, wrong assumption in the spec, unanticipated dependency — halts the
 run and surfaces the finding to the practitioner. No silent architectural decisions
 inside an AT (kokoroe guideline 4, "Halt and surface"; `Stop Condition` sections
 name the anticipated surprises, the rule covers the unanticipated ones).
4. **One commit.** Each AT lands as a single commit, prefixed `ho-NN:` for child
 tasks, referencing the spec ID. The git log reads as a sequence of ATs grouped by
 ho — the split's visible signature. […]
