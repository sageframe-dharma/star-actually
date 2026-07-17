---
id: mountpoints
title: Mountpoints
type: concept
requires: [dataset]
related: [pool-import-export, property-inheritance]
entry_points:
  - zfs not in fstab
  - how do zfs mounts work
  - change mountpoint
  - where is zfs mount configured
summary: >
  ZFS mounts itself—the mountpoint is a property of the dataset, stored in
  the pool, traveling with the data. fstab isn't empty by accident.
---
<!-- depth:1 -->
Mountpoints
<!-- depth:2 -->
<!-- provenance: synthesized -->
You go looking for how your datasets mount, open /etc/fstab, and find
nothing. Decades of muscle memory say that file is the source of truth.
**Actually, ZFS mounts itself: the mountpoint is a *property of the
dataset*, stored inside the pool, inherited down the tree.** `zfs set
mountpoint=/srv/media tank/media` is the entire edit; at import, ZFS mounts
everything where its properties say it belongs.

The deeper shift: fstab describes storage *to the OS*. A ZFS pool carries
its own description—the configuration lives with the data, not with the
machine.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Working with it:

- `zfs get mountpoint tank/media`—see where and *why* (the SOURCE column:
  inherited or local). Default is inherited path-building: `tank/a/b`
  mounts at `/tank/a/b` until some ancestor overrides.
- `zfs set mountpoint=...`—takes effect immediately (it remounts), and
  children follow by inheritance.
- The escape hatches, for the cases the automation shouldn't own:
  `mountpoint=legacy` hands one dataset back to fstab/mount (useful when
  boot ordering or another system insists), and `canmount=off` makes a
  dataset a pure structural parent—a policy node in the tree with
  nothing mounted (the trick behind tidy hierarchies like
  `tank/services/*`).

The payoff scenario: move the disks to a new machine, `zpool import`, and
the entire mount layout arrives with them—nothing to reconstruct, no
fstab archaeology (see Import and Export).
<!-- depth:4 -->
<!-- provenance: synthesized -->
The one real collision to know about: **ZFS refuses to mount over a
non-empty directory.** If something wrote files at /srv/media while the
dataset wasn't mounted (a service that started too early, a restore to the
wrong layer), the next mount fails or the data hides underneath—the
classic "my files vanished" that's actually "my files are *under* the
mount." The `overlay` property and systemd ordering exist for this
boundary; the diagnostic habit is `zfs mount` + looking underneath before
assuming loss.

Against its neighbors: fstab still owns swap and non-ZFS filesystems;
`/etc/zfs/zpool.cache` (or its zgenhostid successor machinery) is just the
host remembering *which pools to import at boot*—not mount config. The
division of labor: the pool knows its layout; the host only knows which
pools are its.
