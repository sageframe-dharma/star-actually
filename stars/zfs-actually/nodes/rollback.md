---
id: rollback
title: Rollback
type: procedure
requires: [snapshot]
related: [snapshot-space]
entry_points:
  - how to rollback a snapshot
  - undo rollback
  - roll forward zfs
  - restore old version
summary: >
  Not timeline navigation—demolition. Rolling back to Tuesday destroys
  everything after Tuesday, permanently. Clones and .zfs/snapshot are the
  gentle paths.
---
<!-- depth:1 -->
Rollback
<!-- depth:2 -->
<!-- provenance: synthesized -->
Other tools teach a seductive model of time travel: the timeline is a
scrubber bar—jump back to Tuesday, look around, jump forward again,
nothing lost. **Actually, `zfs rollback` is demolition, not navigation:
making Tuesday the present destroys everything after Tuesday**—all the
data since, and every later snapshot. Permanently. There is no jumping
forward again, because forward no longer exists.

⚠ **DESTRUCTIVE**—verify before running. The `-r` flag doesn't protect
later snapshots; it *confirms* their destruction (rollback to a non-latest
snapshot refuses to run without it—the refusal is the safety, the flag
disarms it). Semantics per zfs-rollback(8).
<!-- depth:3 -->
<!-- provenance: synthesized -->
The decision procedure, because the destructive verb is usually the wrong
one:

- **Want one file from the past?** Copy it out of the hidden
  `.zfs/snapshot/<name>/` directory. Nothing is destroyed; this is most
  restores.
- **Want to inspect or experiment with the past?** `zfs clone
  tank/ds@tuesday tank/ds-tuesday`—a writable branch sharing blocks,
  costing nearly nothing. Look around, take what you need, destroy the
  clone.
- **Certain the present is worthless?** That's rollback's one legitimate
  case: `zfs rollback tank/ds@tuesday`. Before running it, say out loud
  what dies: all data since Tuesday, and every snapshot after it (`-r` to
  acknowledge). If saying it caused hesitation, take a snapshot of *now*
  first—snapshots are free, and future-you may want to inspect the
  wreckage.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Why can't ZFS just roll forward? Because the timeline model was the wrong
metaphor: snapshots aren't positions on a scrubber bar; they're **pinned
pasts of a single advancing present**. Rollback doesn't move a cursor—it
grafts the present back onto an old state, and the CoW tree's "later" blocks
lose their referent. (A clone is exactly the have-it-both-ways answer: a
*second* present branched from the past, both alive simultaneously—ZFS
even lets you `zfs promote` the clone to swap which branch is the "real"
one, which is rollback's job done reversibly.)

The Proxmox comparison that caused the confusion, resolved: VM snapshot
trees keep *every* branch alive by design; ZFS keeps one live head per
dataset and any number of read-only pins. Same word, different geometry—and the geometry is the thing to remember when the word tempts you.
