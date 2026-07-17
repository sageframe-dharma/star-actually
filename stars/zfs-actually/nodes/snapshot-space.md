---
id: snapshot-space
title: Snapshots and Disappearing Space
type: troubleshooting
requires: [snapshot]
related: [free-space-discipline, sanoid-syncoid]
entry_points:
  - deleted files but no space freed
  - zfs delete not freeing space
  - where did my space go
  - usedbysnapshots
  - pool full but datasets small
summary: >
  You deleted the files and the space didn't come back—because snapshots
  still reference them. The space moved ledgers; it didn't free.
---
<!-- depth:1 -->
Snapshots and Disappearing Space
<!-- depth:2 -->
<!-- provenance: extracted -->
The lived version: you clear 100GB of artifacts to free space, run
`zfs list`, and almost nothing came back. Forty years of filesystems said
deleting frees space. **Actually, deletion only frees blocks that nothing
references—and every snapshot taken while those files existed still
references them.** The space didn't leak; it moved from the dataset's ledger
to the snapshots' ledger. Deleting files in the present cannot unpin the
past. *(Operational source: the practitioner's own hourly-snapshot dataset
doing exactly this.)*
<!-- depth:3 -->
<!-- provenance: synthesized -->
The diagnostic, in order:

1. `zfs list -o space tank/...`—read `USEDDS` (the live dataset) vs
   `USEDSNAP` (held by snapshots). A big `USEDSNAP` is this exact
   situation.
2. `zfs list -t snapshot -o name,used,creation tank/...`—see who's
   holding. Remember each snapshot's `used` shows only *unique* space, so a
   chain can collectively hold far more than the column suggests.
3. To reclaim: destroy the snapshots that span the deletion. Dry-run first—`zfs destroy -nv tank/ds@old1%old8` (a range, with `-n` showing what
   would free without doing it).

⚠ **Destructive**—`zfs destroy` of snapshots is permanent, and under a
policy tool it's also usually *wrong*: sanoid will keep pruning on schedule
anyway. Adjust the retention policy, not individual snapshots—hand-culling
what a policy engine manages is how you end up with neither the space nor
the history.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The two intuitions this scenario finally reconciles: "snapshots are free"
(true—at creation) and "deleting frees space" (true—absent references).
Snapshot cost is **divergence**: churn-heavy datasets (databases, build
dirs, VM disks) under hourly retention accumulate held space fast; static
media barely accrues any. Which means retention policy is a *per-dataset*
decision—the databases might warrant aggressive hourlies pruned in days,
the media library weekly snapshots kept for months. One-size retention is
how the pool fills.

The graduating insight: `USEDSNAP` isn't waste—it's the storage price of
your history, itemized. The question is never "how do I make it zero" but
"is this history worth this rent," dataset by dataset.
