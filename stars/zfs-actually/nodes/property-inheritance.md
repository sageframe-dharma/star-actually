---
id: property-inheritance
title: Property Inheritance
type: definition
requires: [dataset]
related: [compression, recordsize, mountpoints]
entry_points:
  - how do zfs properties work
  - zfs set inherit
  - where do i set compression
  - property inheritance
summary: >
  Properties set on a dataset flow down its subtree until overridden—policy
  is written once at the right altitude, not per-dataset.
---
<!-- depth:1 -->
Property Inheritance
<!-- depth:2 -->
<!-- provenance: synthesized -->
Every dataset carries dozens of **properties**—compression, recordsize,
quota, mountpoint—and each one either was set *here* or is **inherited**
from the nearest ancestor that set it. You don't configure datasets; you
configure the *tree*, at the highest node where the policy is true, and let
it flow down.

The small actually: there's no global config file to hunt for. The pool's
root dataset *is* the global config, and every deviation is local, visible,
and attributed.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The three verbs:

- `zfs get compression tank/services/postgres`—read a property, and read
  its **SOURCE** column: `default`, `inherited from tank`, or `local`. The
  SOURCE column is the audit trail—it tells you *why* the value is what it
  is.
- `zfs set recordsize=16K tank/services/postgres`—override locally, from
  here down.
- `zfs inherit recordsize tank/services/postgres`—delete the local
  opinion; rejoin the ancestors.

The working pattern: set `compression=lz4` (and your snapshot-policy tags)
once near the top; override recordsize on the two datasets whose workloads
actually differ. A tree where every dataset sets everything locally is the
smell of configuration by copy-paste. One timing note: property changes
affect *new writes*—existing blocks keep the settings they were born under.
