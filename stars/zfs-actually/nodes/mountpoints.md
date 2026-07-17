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
  Where a dataset appears in your folders is a setting stored on the
  dataset itself—the location travels with the data, not with the machine.
---
<!-- depth:1 -->
Mountpoints
<!-- depth:2 -->
<!-- provenance: synthesized -->
A **mountpoint** is where a piece of storage shows up in your folder tree—
the address at which its contents appear. On most systems, those addresses
live in a settings file on the machine (on Linux, `/etc/fstab`), and
people trained there go looking for it and find it empty. **Actually, ZFS
handles this itself: where a dataset appears is a setting stored *on the
dataset*, inside the pool.** One command changes it, and children follow
their parent unless told otherwise.

The deeper shift is worth pausing on: the machine's settings file
describes storage *to that machine*. A ZFS pool carries its own
description—so the layout travels with the data, not with the computer it
happens to be plugged into.
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
