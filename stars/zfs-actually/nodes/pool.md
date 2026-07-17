---
id: pool
title: The Pool
type: concept
requires: [what-zfs-is]
related: [vdev, dataset, pool-import-export]
entry_points:
  - what is a zpool
  - what is a pool
  - pool vs dataset
  - how is a pool structured
  - is a pool a partition
summary: >
  All your disks, combined into one shared pot of storage—and the surprise
  inside the word: the pool itself keeps no spare copies.
---
<!-- depth:1 -->
The Pool
<!-- depth:2 -->
<!-- provenance: synthesized -->
The **pool** is what ZFS turns your disks into: one shared pot of storage
that the whole machine draws from. You hand ZFS the disks; it hands you
back a single supply of space. You never carve it up in advance, never
decide sizes ahead of time, never "resize" anything again—everything on the
machine simply shares the pot.

The surprise hiding inside the word: **the pool itself keeps no spare
copies of anything.** Protection against a dead disk lives one level down,
inside the small teams of disks the pool is built from (called *vdevs*—the
next idea to meet). That distinction is the difference between a safe setup
and a time bomb, which is why it gets its own page.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The containment hierarchy, once and cleanly:

- **Disks** are grouped into **vdevs** (a mirror pair, a RAIDZ set).
- **Vdevs** are striped together into the **pool**.
- **Datasets** carve the pool's one space into policy boundaries.

Day to day, the pool is mostly a health object: `zpool status` (is it whole),
`zpool list` (how full—watch that number), `zpool scrub` (verify it). You
create it once with `zpool create`, deliberately, and then live inside it via
`zfs` commands. Homelab reality: most machines want exactly one pool—split
pools only when the *physics* differ (an SSD pool for VMs, an HDD pool for
bulk), because separate pools don't share free space.
<!-- depth:4 -->
<!-- provenance: synthesized -->
What people conflate it with, and why each is wrong:

- **A partition**—partitions have fixed sizes; the pool's space is one
  fluid pot, and datasets take what they use.
- **A RAID array**—an mdraid array is one redundancy group; a pool is a
  *stripe across* redundancy groups (vdevs), with nothing between them. "Is
  the pool redundant?" is not actually a well-formed question—ask it of
  each vdev.
- **A machine's storage**—the pool isn't married to the host. Its entire
  self-description travels on the member disks; export it, move the disks,
  import it elsewhere, everything arrives.

Grows easily (add a vdev), shrinks reluctantly. Adding is one command;
removing has narrow support with real costs. Pools are built like
foundations: extension planned-for, subtraction painful.
