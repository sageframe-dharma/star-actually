---
id: zvol
title: Zvols
type: definition
requires: [dataset]
related: [proxmox-zfs, recordsize]
entry_points:
  - what is a zvol
  - zvol vs dataset
  - where are my vm disks
  - block device zfs
summary: >
  A dataset wearing a block-device face—pool-backed raw volumes with
  snapshots and send/recv, no filesystem-in-a-file. What Proxmox gives VMs.
---
<!-- depth:1 -->
Zvols
<!-- depth:2 -->
<!-- provenance: synthesized -->
A **zvol** is a dataset that presents as a raw block device instead of a
filesystem—a virtual disk carved from the pool, appearing at
`/dev/zvol/tank/...`. The naive hunt—"where's the file for my VM's disk?"—finds nothing because **there is no file**: no qcow2, no image format, no
filesystem-in-a-file. The consumer (a VM, iSCSI, swap) formats the block
device however it likes, and underneath it's still ZFS: checksummed,
snapshottable, sendable, thin by default.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Where you meet them: **Proxmox carves one zvol per VM disk** (that's why
`zfs list` on a Proxmox host shows `.../vm-103-disk-0` entries where you
expected files). The practical grammar: created with `zfs create -V 32G
tank/vm-disk`; snapshots and send/recv work exactly as for datasets—which
is how a VM disk gets hourly history and offsite replication with the same
machinery as everything else.

Two zvol-specific knobs worth knowing exist: **`volblocksize`** is the
recordsize question in block-device form—fixed at creation,
workload-matched (virtualizers set sane defaults); and **thin vs thick**
(`-s` for sparse) decides whether the pool promises the space up front or
lets you overcommit—overcommitted thin zvols on a filling pool are a
classic slow-motion incident.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The choice it creates: **zvol vs dataset-with-files.** A zvol hands the
guest a raw disk (native block semantics, guest-managed filesystem); a
dataset of qcow2 files hands the host visibility (files you can see, copy,
move with cp). Proxmox chose zvols for directness—one less filesystem
layer between guest write and pool. The double-CoW caveat travels with
either choice: a CoW guest filesystem (or qcow2) on CoW storage amplifies
writes; conventional guest filesystems (ext4/XFS) on zvols sidestep it.

Category-wise, this is the moment ZFS's self-description clicks: the pool
is a storage *reservoir*, and "filesystem" (dataset) vs "block device"
(zvol) are just two faces the same storage can wear—which is what "ZFS is
the whole stack, not a filesystem" cashes out to in daily life.
