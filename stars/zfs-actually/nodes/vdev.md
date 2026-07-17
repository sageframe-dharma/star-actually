---
id: vdev
title: The Vdev
type: concept
requires: [pool]
related: [mirror, raidz, ashift, resilver]
entry_points:
  - what is a vdev
  - where does redundancy live
  - can i lose a vdev
  - is my pool safe
  - single disk vdev
summary: >
  The small team of disks that back each other up—where protection actually
  lives, and therefore where failure actually lives. Lose one whole team,
  lose the whole pool.
---
<!-- depth:1 -->
The Vdev
<!-- depth:2 -->
<!-- provenance: synthesized -->
From above, the pool looks like one undivided pot of storage. Underneath,
ZFS never treats your disks as one big group. It binds them into small
teams, and each team backs itself up. That team is a **vdev** ("virtual
device"). A team might be two disks keeping identical copies (a *mirror*),
a group of disks sharing recovery math so any one can die (*RAIDZ*), or—
dangerously—one lone disk backing up nothing. A pool is built by joining
teams together.

Here is the sentence this entire site most wants you to hold: **spare
copies exist only *inside* each team, never between teams—so losing any
one whole team loses the whole pool.** Not damaged. Gone. The pool spread
everyone's data across all its teams, so a dead team is a bite out of
everything.
<!-- depth:3 -->
<!-- provenance: synthesized -->
This is why the classic homelab move—"the pool's getting full, I'll just
add this spare disk"—is a trap. `zpool add tank /dev/sdX` with a bare disk
welds a redundancy-less vdev into your pool of mirrors, permanently. Now that
one consumer drive can take down everything, and the two mirrors you paid for
protect nothing. The pool is exactly as strong as its weakest vdev.

Audit your real layout in ten seconds: `zpool status` indents the truth—vdevs (`mirror-0`, `raidz1-0`) at one level, member disks under them. A disk
sitting at vdev indentation with no group above it *is* a single-disk vdev.
If you find one under data you care about, that's a rebuild-the-pool
conversation, not a someday conversation.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The vdev is where every serious layout question actually lives:

- **Mirrors vs RAIDZ** is a per-vdev choice (and don't mix types under one
  pool without a reason).
- **Performance** scales with vdev *count*, not disk count—the pool
  stripes across vdevs, so six disks as three mirrors substantially
  out-IOPS six disks as one RAIDZ2.
- **A resilver** is a vdev event: one vdev rebuilding a member while the
  others carry on.
- **Growth** happens vdev-wise: add a vdev, or swap every disk in one vdev
  for bigger ones. (RAIDZ widening exists now—see RAIDZ Expansion—but
  the vdev remains the unit you plan around.)

Special vdev classes exist (log, cache, spare, special)—supporting cast,
not data vdevs; the log and cache ones have their own nodes.
<!-- depth:5 -->
<!-- provenance: synthesized -->
Why did ZFS put redundancy *inside* the stripe instead of across the whole
pool, when whole-pool parity sounds safer? Because the vdev boundary is what
keeps redundancy **composable and repairable**:

- Each vdev handles its own failures locally—a resilver touches one vdev's
  disks, not the whole pool.
- Vdevs of different shapes, ages, and sizes can join one pool over the
  years; a global parity scheme would have to be re-solved on every change.
- The allocator balances new writes across vdevs by free space and load—striping is a *placement policy*, cheap and adaptive, while redundancy
  stays a *structural property*, local and stable.

The cost of that composability is the brutal rule at depth 2: the pool
stripes with no parity of its own, so vdev survival is pool survival. ZFS
chose "redundancy is local, loss is total" over "redundancy is global,
everything is coupled"—and it expects you to know it chose that.
