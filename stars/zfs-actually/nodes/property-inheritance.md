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
  Settings flow downhill: set once on a parent dataset, every child follows
  until one is told otherwise. There is no central settings file—the tree
  is the settings.
---
<!-- depth:1 -->
Property Inheritance
<!-- depth:2 -->
<!-- provenance: synthesized -->
Everywhere else in your computing life, settings live in one central
place—a preferences screen, a control panel, a configuration file. ZFS
does it differently: every dataset carries its own **properties**—settings
like whether to squeeze its data, how much space it may use, where it
appears in your folders. And because datasets sit in a family tree, each
setting either was set *right here* or is **inherited** from the nearest
ancestor that set it. You set a rule once, at the highest point in the
tree where it's true, and everything below follows.

The payoff: there is no central settings file to hunt for. The top of the
tree *is* the settings, and every local exception is visible and signed—
you can always ask a dataset where a setting came from.
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
