---
id: hot-cold
title: hot / cold
type: definition
requires: []
related: [build-record, forward-only, mutability, reflect, working-memory-handoff]
entry_points: [hot / cold]
summary: >
  The split between a scratch memory you keep rewriting and the permanent record you never edit — with the rule that the permanent one always wins.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
hot / cold

<!-- depth:2 -->
<!-- provenance: extracted -->
The split between a scratch memory you keep rewriting and the permanent record you never edit — with the rule that the permanent one always wins.

<!-- depth:3 -->
<!-- provenance: extracted -->
The two temperatures of a build's memory. **hot** — mutable, non-canonical,
overwritten every pause: the working-memory handoff file, its live queues and `NEXT:` pointer.
**cold** — sealed and canonical: git, Reflect, the build record. On conflict the cold record
wins; forward-only governs cold, and hot is exempt because it is not the record. A finding lives
hot, then graduates cold at ho close (the hot/cold finding lifecycle); a sealed decision banks
cold at the moment of sealing, the hot copy a cache.

<!-- depth:4 -->
<!-- provenance: extracted -->
**Authority — Hot and Cold.** The working-memory file duplicates state that also lives in the build record, the Reflect
phases, and the git log. That duplication is only safe under an explicit authority rule:

> **The working-memory file is HOT: mutable, non-canonical, a fast-pickup cache derived from
> and subordinate to the cold canonical record.** The cold record — the git history, the per-ho
> **Reflect**, and the **build record** (§8) — is the source of truth. When the hot file and the
> cold record disagree, the **cold record wins**, and the hot file is corrected to match.

The hot file is an *index* of state optimized for fast reconstitution, never the record itself.
This is what keeps a mutable first-read file from becoming a shadow source of truth that cuts
against forward-only. […]
