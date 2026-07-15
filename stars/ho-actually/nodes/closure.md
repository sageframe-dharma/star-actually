---
id: closure
title: closure
type: concept
requires: []
related: [reflect]
entry_points: [closure]
summary: >
  The moment a unit of work and its look-back are finished and its status is marked done.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
closure

<!-- depth:2 -->
<!-- provenance: extracted -->
The moment a unit of work and its look-back are finished and its status is marked done.

<!-- depth:3 -->
<!-- provenance: extracted -->
The state change when a ho's work and reflection are done. Canonical signal:
frontmatter `status: draft → complete` (after Reflect for ha, Results for ri, authoring for
orientation), optionally with a `commit:` field; `superseded` is the second terminal state.
Forward-only applies from closure onward.

<!-- depth:4 -->
<!-- provenance: extracted -->
**Closure signal.** A ho signals that it is closed through its `status:` frontmatter field. There are two terminal states:

- **`complete`**—the ho's deliverable is done and committed. The flip happens after the phase that closes the work: Reflect for ha, Results for ri, and authoring for orientation hos (which are complete once written). An optional `commit:` field records the closing commit hash.
- **`superseded`**—a later ho has overtaken this one's decisions under the forward-only principle (§3.5). The ho stays in the record; the `status:` marks that its conclusions no longer hold, and the superseding ho is named per the bidirectional-supersession rule. The flip is exclusive: when a later ho supersedes this one, its status moves from `complete` to `superseded` and the `superseded-by:` field names the successor—the two terminal states never coexist.

These two are the whole vocabulary—earlier projects drifted into `closed`, `done`, and `-DONE-` filename prefixes; those are superseded by `complete`. Where a project also keeps a human-readable Reflect trailer at the end of the ho document (a one-line "closed on / by" note), that trailer is a *complementary* signal, not a replacement for the `status:` field.

---
