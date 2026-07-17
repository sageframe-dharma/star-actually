---
id: recordsize
title: Recordsize
type: concept
requires: [dataset]
related: [compression, zvol, proxmox-zfs]
entry_points:
  - what is recordsize
  - recordsize vs block size
  - recordsize for database
  - recordsize 1m
  - zfs tuning
summary: >
  The size of the chunks ZFS stores files in—adjustable per dataset. It
  matters when programs change small pieces inside huge files, and changing
  it only affects files written afterward.
---
<!-- depth:1 -->
Recordsize
<!-- depth:2 -->
<!-- provenance: extracted -->
ZFS stores each file in chunks, and **recordsize** is the setting that says
how big those chunks may get—adjustable for each dataset, with a default
of 128 kilobytes ("ZFS datasets use an internal recordsize of 128KB by
default"—OpenZFS docs). It's a ceiling, not a straitjacket: small files
simply use smaller chunks; nothing gets padded.

The mix-up to avoid: this is *not* about the disk's hardware. Recordsize is
a choice you make per dataset, changeable anytime; the hardware story is a
different setting (ashift, one page over) with very different rules.
<!-- depth:3 -->
<!-- provenance: extracted -->
When it matters: **applications doing small random I/O inside large files.**
A database updating a 16K page inside a 50GB file under 128K records forces
ZFS to read and copy-on-write 128K to change 16K—an 8× amplification on
every hot-path write. Match the record to the I/O grain:

- `recordsize=16K` for MySQL/InnoDB data files; ~`32K` (or the 128K
  default) works well for PostgreSQL (OpenZFS docs).
- `recordsize=1M` for sequential, whole-file workloads—media, backups,
  archives ("Set recordsize=1M on datasets that are subject to sequential
  workloads"). Fewer, bigger blocks: less metadata, better compression.
- Everything else: leave the 128K default alone. It's a good default.

The trap that catches everyone: "Changing the recordsize on a dataset will
only take effect for new files" (OpenZFS docs). Tuning a dataset full of
existing data changes nothing until the files are rewritten—copy them in
again or accept the status quo.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Its neighborhood:

- **vs ashift**—the pair that shares one mental slot. Ashift is the
  *physical* floor (the sector size a vdev assumes, immutable); recordsize
  is the *logical* ceiling (per dataset, changeable anytime). Foundation
  and furniture.
- **vs volblocksize**—zvols don't have files, so they get a fixed block
  size instead (`volblocksize`, set at zvol creation, *not* changeable)—the same workload-matching question Proxmox answers for you with its
  defaults when it carves VM disks.
- **vs compression**—records are the unit compression chews; bigger
  records compress better. On archive datasets, `recordsize=1M` +
  zstd is the classic pairing.

The meta-lesson it teaches: ZFS default settings are chosen for the general
case and are usually right; the knobs exist for the two datasets on your
pool whose workload you can actually name.
