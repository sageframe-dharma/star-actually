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
  A frozen moment of a dataset that copies nothing—it just keeps the past
  from being thrown away. Free to take; the cost arrives slowly, as the
  present drifts from the moment you kept.
---
<!-- depth:1 -->
Snapshots
<!-- depth:2 -->
<!-- provenance: synthesized -->
A **snapshot** freezes a dataset at a moment in time, so you can look at—
or return to—exactly how things were. The word sounds like a photograph: a
duplicate, costing what the data costs. **Actually, a ZFS snapshot copies
nothing.** Because ZFS never writes over existing data anyway, everything
the dataset looked like a moment ago is *already sitting on disk*. A
snapshot is just a name attached to that moment, plus a promise: *don't
throw any of this away while I'm holding it.* Taking one is instant and
free, no matter how much data is involved.

The cost is deferred, not absent: it builds up slowly, as the live data
drifts away from the kept moment and the old pieces can't be thrown out.
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
