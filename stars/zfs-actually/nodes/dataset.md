---
id: dataset
title: Datasets
type: concept
requires: [pool]
related: [zvol, property-inheritance, mountpoints, recordsize]
entry_points:
  - what is a dataset
  - dataset vs directory
  - dataset vs partition
  - how many datasets should i make
  - why separate datasets per service
summary: >
  Not folders and not partitions—nearly-free policy boundaries carved from
  the pool's shared space. The unit of properties, snapshots, and
  replication. Make many.
---
<!-- depth:1 -->
Datasets
<!-- depth:2 -->
<!-- provenance: synthesized -->
A **dataset** is a filesystem carved out of the pool—it mounts, it holds
files, it looks like a directory from the outside. The naive model says it's
either a fancy folder or a small partition. **Actually, a dataset is a policy
boundary**: it has no fixed size (all datasets share the pool's one
reservoir), costs almost nothing to create, and is the unit at which
everything interesting happens—properties, quotas, snapshots, replication.

The posture correction: on ext4 you'd make a directory; on ZFS you should
usually make a dataset. Make many.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The rule of thumb: **anything you might want to snapshot, replicate, quota,
or tune separately gets its own dataset.** A directory can't be snapshotted,
sent to another machine, or given its own recordsize; a dataset can.

This is why a service-deployment setup makes a separate dataset per service
rather than a folder per service: each service gets its own snapshot policy
(the database hourly, the media library weekly), its own replication
schedule, its own properties—and a restore of one service doesn't drag the
others backward in time with it.

Datasets nest into a tree (`tank/services/postgres`), and children inherit
properties from parents—so policy gets set once at the sensible level and
flows down. Creating one is instant: `zfs create tank/services/newthing`.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The boundaries that actually matter:

- **Dataset vs directory**—invisible day-to-day, decisive the day you need
  history: snapshots, sends, and rollbacks stop at dataset edges. The
  granularity you chose at creation is the granularity of your disaster
  recovery.
- **Dataset vs partition**—no fixed size is the liberation, but it cuts
  both ways: nothing stops one dataset from eating the pool. `quota` (ceiling)
  and `reservation` (guaranteed floor) reintroduce limits *as policy* where
  you actually want them, instead of as geometry everywhere.
- **Dataset vs zvol**—same carving, different face: a dataset presents a
  filesystem; a zvol presents a raw block device (what Proxmox gives VMs).

One warm-blooded warning: `zfs destroy` on a dataset takes its snapshots and
its children with it, and there is no undo. The cheapness of creation does
not extend to deletion.
