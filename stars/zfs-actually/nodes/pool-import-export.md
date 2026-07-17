---
id: pool-import-export
title: Import and Export
type: concept
requires: [pool]
related: [mountpoints, send-recv]
entry_points:
  - move pool to new machine
  - zpool import
  - motherboard died is my data safe
  - where is pool config stored
summary: >
  The pool's entire self-description lives on its member disks—any machine
  with OpenZFS can import them and get everything, mounts included. Data was
  never married to the machine.
---
<!-- depth:1 -->
Import and Export
<!-- depth:2 -->
<!-- provenance: synthesized -->
The fear comes from RAID history: array configuration lives in a controller
or an OS file, and when *that* dies, the disks become a puzzle. **Actually,
a ZFS pool's entire self-description—vdev layout, properties, dataset
tree, mountpoints—lives on the member disks themselves, as labels.** A
dead motherboard is a hardware errand, not a data event: move the disks to
any machine running OpenZFS, `zpool import tank`, and everything arrives—including where it all mounts.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The verbs:

- **`zpool export tank`**—the polite handoff: unmount, flush, mark
  released. Do this before planned moves.
- **`zpool import`**—with no arguments, it *scans* attached disks and
  reports every importable pool it finds; then `zpool import tank` takes
  one. After an unplanned death there's no export on record, so the new
  machine asks for `-f` (force)—that's the expected flow after a
  hardware failure, not a danger sign by itself.
- The disks don't even need the same names, ports, or order—ZFS
  identifies members by label, not location. (This is also why building
  pools against `/dev/disk/by-id` is kindness to future-you: the *display*
  stays legible.)

⚠ The one sharp edge: importing a pool on two machines **at once** (shared
disk shelves, iSCSI, VM passthrough mistakes) corrupts it—the `-f` flag
can override the "looks active elsewhere" warning, so make sure "elsewhere"
is actually dead before forcing.
<!-- depth:4 -->
<!-- provenance: synthesized -->
What this dissolves, and what it doesn't:

- **vs mdadm.conf / hardware RAID controllers**—the horror story this
  node exists to retire: proprietary metadata married to a controller
  model. ZFS's on-disk labels make pools *portable by construction*, across
  machines and even across OSes (a FreeBSD pool imports on Linux, feature
  flags permitting—check `zpool upgrade -v` compatibility when hopping).
- **vs send/recv**—import/export moves *the pool itself* (no copying, no
  second storage); send/recv *copies datasets* between pools. Migration
  vs replication.
- **What still lives on the host**—almost nothing: which pools to import
  at boot (the cachefile machinery), and any keys for encrypted datasets.
  The honest disaster checklist for a homelab is therefore short: the
  disks, the keys, and the offsite replica. Everything else is
  reconstructable by `zpool import` on fresh metal.
