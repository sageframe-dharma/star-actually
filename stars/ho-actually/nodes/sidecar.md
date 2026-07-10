---
id: sidecar
title: sidecar
type: definition
requires: []
related: [what-is-ho-system]
entry_points: [sidecar]
summary: >
  A record kept in a sibling folder outside a fork's working tree, so your own process files never mix into someone else's repository.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
sidecar

<!-- depth:2 -->
<!-- provenance: extracted -->
A record kept in a sibling folder outside a fork's working tree, so your own process files never mix into someone else's repository.

<!-- depth:3 -->
<!-- provenance: extracted -->
A record kept in a sibling directory outside a fork's working tree, separately
owned, so the practitioner's ho-process never enters the contribution's object database. The
pattern is the **sidecar directory**; the artifact is a **sidecar record**.

<!-- depth:4 -->
<!-- provenance: extracted -->
**What compresses: the Kamae chain, usually to zero.** An external contribution does not get a seed, system design, README, or overview.
**The upstream issue substitutes for all four** — it states the problem (seed), the
host codebase states the architecture (system design), the host README states scope,
and the PR's own bounded goal is the sequence. The supacode case ran two hos against
GitHub issue #442 with no Kamae documents; the ho frontmatter carries the
substitution:

```yaml
branch: osc11-per-pane-backgrounds
issue: https://github.com/supabitapp/supacode/issues/442
```

If a contribution grows past what an issue can anchor — multi-PR arcs, architectural
proposals — write the missing thinking as an RFC *in the host project's format*, not
as a Kamae document in their tree.

<!-- depth:5 -->
<!-- provenance: extracted -->
**What survives: the session discipline, intact.** From the case, kept without modification:

- **Document shape.** Frontmatter, Context, in-scope/out-of-scope, Think, Execute,
 Acceptance, Reflect. The ho-02 recovered from supacode is structurally
 indistinguishable from a home-project ho.
- **Planning before execution.** Think resolves the load-bearing facts before the
 agent prompt exists (ho-02's Think carries three "facts the executing agent must
 hold").
- **Escalation.** An explicit Escalation section: conditions under which the agent
 stops and surfaces rather than adapting (architectural assumption fails manual
 verification; input methods regress; a C accessor doesn't behave as documented).
- **Forbidden moves.** The out-of-scope list hardened into named prohibitions,
 including host-specific ones ("No `print()` or `os.Logger`. Use `SupaLogger`").
