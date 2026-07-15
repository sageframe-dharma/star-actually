---
id: kamae-addendum
title: Kamae addendum (kamae-N.M)
type: procedure
requires: []
related: [kamae, supersedes]
entry_points: [kamae addendum]
summary: >
  A follow-on decision document that overrides a named part of an earlier framing document without editing it, carrying its own justification and record.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Kamae addendum (kamae-N.M)

<!-- depth:2 -->
<!-- provenance: extracted -->
A follow-on decision document that overrides a named part of an earlier framing document without editing it, carrying its own justification and record.

<!-- depth:3 -->
<!-- provenance: extracted -->
A decimal-suffixed decision document that supersedes a
named part of a frozen Kamae document without editing it; carries the reopening
justification, the declined alternatives, and the propagation record. Forward-only applied
to architecture.

<!-- depth:4 -->
<!-- provenance: extracted -->
**Anatomy.** Filename: `ho-process/kamae-<N>.<M>-<project>-<slug>.md`, where N is the parent Kamae
number and M increments per addendum (2.1, 2.2, …).

Frontmatter (from the live instances):

```yaml
---
created: 2026-07-01
status: decided
type: decision
project: sharibako
stage: kamae-2.1
kamae-chain: seed → system-design → **injection-decision** → readme → ho-overview
supersedes: kamae-2 §7 (partial—the "no runtime injection" architectural commitment)
builds-on: kamae-1-sharibako-seed, kamae-2-sharibako-system-design
next: reflected in kamae-1 seed (parti), kamae-4 (adds ho-04.5), README, SECURITY.md
---
```

Field notes:

- **`supersedes:` is section-precise.** Not "supersedes kamae-2"—"kamae-2 §7
 (partial—the specific line)." The reader must be able to tell exactly which
 commitments fell and, by implication, which stand. The addendum body repeats this
 as prose: "All other Kamae 2 commitments … stand unchanged."
- **`kamae-chain:` shows the insertion position**—where the addendum sits in the
 reading order, bolded.
- **`next:` names the propagation set**—every downstream document the decision was
 reflected into (see §4).

Body sections (both instances follow this arc): […]
