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
  One shared reservoir of storage built from vdevs—not a big partition, and
  not where redundancy lives.
---
<!-- depth:1 -->
The Pool
<!-- depth:2 -->
<!-- provenance: synthesized -->
The naive model—*a pool is a big partition*—will let you operate for a
long time without being true. **Actually, a pool is a reservoir**: you hand
ZFS whole disks, arranged into vdevs, and get back one undifferentiated pot
of capacity that everything on top shares. Nothing inside a pool has a fixed
size—no partitioning, no pre-allocation, no "resize the volume" ever again.

The dangerous half of the correction: the pool is **not** where redundancy
lives. That's the vdev's job, one layer down—and the distinction is the
difference between a safe layout and a time bomb.
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
