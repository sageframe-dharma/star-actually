---
id: project-lifecycle
title: project lifecycle
type: definition
requires: []
related: [kamae, shu-ha-ri, state-summary-block]
entry_points: [project lifecycle]
summary: >
  A one-word label for how far along a project is, from planning to shipped.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
project lifecycle

<!-- depth:2 -->
<!-- provenance: extracted -->
A one-word label for how far along a project is, from planning to shipped.

<!-- depth:3 -->
<!-- provenance: extracted -->
Where the thing being built sits in its life: `kamae` (pre-build, still
framing), `dev` (building, not yet user-exercised), `beta` (real users or the practitioner
driving it, hardening), `production` (shipped, in use). The fourth field of the
**state-summary block**. Orthogonal to the practitioner's **shu-ha-ri** stage and to the
`stage:` Kamae field — and deliberately not named "status," which belongs to a document's own
`status:` frontmatter state.

<!-- depth:4 -->
<!-- provenance: extracted -->
**The State-Summary Block.** Every ho closes, and every session ends, with a **state-summary block**: four fields, fixed
order, fixed labels. It is the answer to *"where is this build, in one glance?"*

```
**STATE-SUMMARY**
- **COMPLETED** — what was just finished this session/stretch.
- **NEXT** — the single clear pointer to what comes next.
- **ACTION ITEMS / BLOCKS** — open items needing action, and anything blocking progress. A
 blocked build must say so loudly here (`BLOCKED: …`), never bury it. Write `none` when clear.
- **PROJECT LIFECYCLE** — `kamae` | `dev` | `beta` | `production`.
```

**The four fields are verbatim and ordered.** The block leads with the literal token
`STATE-SUMMARY` and the four labels in this sequence. This is deliberate: the block is a **hook
surface**. A greppable, fixed-shape block lets ntfy alerts, dashboards, the practitioner's
memory system, or any other tool extract build state without parsing prose. Free-form status
notes are not this; the value is in the fixed form. Keep it that way even when it feels rigid —
the rigidity is what makes it machine-findable.

**Project lifecycle** is where the *thing being built* sits in its life. It is orthogonal to
the two "stage" notions in the framework — [[shu-ha-ri|shu-ha-ri]]
(framework/structure/shu-ha-ri.md) is the *practitioner's* skill stage, and the `stage:`
frontmatter field is the *Kamae* position — and it is unrelated to the `status:` frontmatter
field, which is a *document's* own state (`draft`, `complete`, `stable`). The word "status" was
deliberately kept off this field to avoid that collision: […]
