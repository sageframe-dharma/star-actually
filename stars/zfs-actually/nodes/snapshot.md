---
id: snapshot
title: Snapshots
type: concept
requires: [copy-on-write, dataset]
related: [snapshot-space, send-recv, rollback]
entry_points:
  - what is a snapshot
  - how do snapshots work
  - are snapshots free
  - why are snapshots instant
  - zfs snapshot cost
summary: >
  A snapshot copies nothing—it's a named pin on blocks that already exist.
  Free at creation; the cost arrives later, as the present diverges from the
  pinned past.
---
<!-- depth:1 -->
Snapshots
<!-- depth:2 -->
<!-- provenance: synthesized -->
The word "snapshot" sounds like a photograph—a captured duplicate of a
moment, costing what the data costs. **Actually, a ZFS snapshot copies
nothing.** Copy-on-write means the current state of a dataset is a tree of
blocks that were never going to be overwritten anyway; a snapshot is just a
named pointer to that tree, plus a promise: *don't garbage-collect these
blocks while I hold them.* Creation is instant and free at any size.

The cost is deferred, not absent: it accrues later, as the live dataset
diverges from the pinned past and the old blocks can't be freed.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Living with them:

- `zfs snapshot tank/services/postgres@before-upgrade`—the `@name` suffix
  is the whole syntax. Instant, safe, take one before anything risky.
- `zfs list -t snapshot` to see them; **`zfs list -o space`** to see what
  they're *costing* (the `USEDSNAP` column)—the number that explains the
  mystery in Snapshots and Disappearing Space.
- Read the past without commitment: every dataset hides a
  `.zfs/snapshot/<name>/` directory—the snapshot's contents, browsable
  read-only. Copy one file back out of last Tuesday without any rollback
  drama.
- At scale you don't take snapshots by hand; a policy tool (sanoid) takes
  hourlies/dailies/monthlies and prunes them. Snapshots are cheap; *keeping
  every snapshot forever* is how pools quietly fill.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The three relatives, kept distinct:

- **Rollback**—makes a snapshot the present again, by *destroying*
  everything since it. Demolition, not navigation (its node carries the
  warning).
- **Clone**—a writable dataset branched off a snapshot, sharing blocks.
  The nondestructive way to revisit or experiment with the past.
- **Send/receive**—a snapshot is also the unit of replication: sends ship
  exact snapshot states between pools.

And the confusion that owns its own node because it matters most:
**a snapshot is not a backup.** It's on the same disks, in the same pool,
behind the same mistakes. Versioning, not protection.
<!-- depth:5 -->
<!-- provenance: synthesized -->
The mechanism is just reference counting over the CoW tree. Live data and
every snapshot share all blocks they have in common; a block becomes free
only when the live tree *and* every snapshot referencing it have let go.
Which yields the accounting rule that explains all snapshot-space mysteries:
**a snapshot's `used` is only the space unique to it**—blocks held by it
and nothing else. A chain of hourly snapshots of slowly-changing data all
share almost everything; each shows a sliver of `used`, and destroying one
frees almost nothing because its neighbors still pin the same blocks.

This is also why snapshot *creation* can't be slow: there is no data path.
It's a bookkeeping entry—"this txg's root, keep it"—which is the same
reason snapshots are read-only and immutable: they aren't copies that could
drift; they're the actual past, still on disk, still checksummed, held by a
reference.
