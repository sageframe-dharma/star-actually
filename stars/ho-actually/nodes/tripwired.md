---
id: tripwired
title: tripwired
type: definition
requires: []
related: [agent-task]
entry_points: [tripwired]
summary: >
  Built to run on its own within set bounds but stop and raise a flag the instant it meets something unexpected.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
tripwired

<!-- depth:2 -->
<!-- provenance: extracted -->
Built to run on its own within set bounds but stop and raise a flag the instant it meets something unexpected.

<!-- depth:3 -->
<!-- provenance: extracted -->
The property that makes an agent task safe to delegate: autonomous within its
bounds, but the moment it hits something unanticipated it halts and surfaces rather than
adapting. Bounded autonomy with a halt-and-surface tripwire. _Escalation_ is the mechanism;
_tripwired_ is the property — "ATs are safe to delegate because they are tripwired."

<!-- depth:4 -->
<!-- provenance: extracted -->
**Escalating — autonomous until something new surfaces.** The AT is executed autonomously — *unless it finds something new*. When execution
surfaces something the ho didn't anticipate — a schema mismatch, a wrong assumption in
the spec, a real-data shape that contradicts the fixtures, an unanticipated
dependency — the executing agent stops and surfaces the finding. It does not adapt
silently, does not rationalize the surprise as "probably fine," and does not acquire
architectural authority because something feels suboptimal mid-execution.

Two mechanisms carry this:

- **Stop Conditions** (a spec section) name the *anticipated* surprises: "If a real
 export reveals shape mismatches with the schema, stop and surface findings before
 modifying the data model."
- **The general rule** covers the unanticipated ones: any surprise halts the loop.
 This is kokoroe guideline 4 ("Halt and surface") and it applies whether or not a
 Stop Condition section exists.

This is the operating discipline's *stop for decisions, not permissions* rule applied
at the AT layer. The decision that comes back goes to the practitioner (or a heavier
model in a discursive session); its resolution lands in the parent ho (see §6), and
execution resumes against the updated record.

This property — bounded autonomy with a halt-and-surface tripwire — is what makes an AT
safe to delegate to a cheaper executor: the AT is **tripwired**. *Escalation* is the
mechanism; *tripwired* is the property. It is the word to reach for in the explanatory
sentence — "ATs are safe to delegate because they are tripwired."
