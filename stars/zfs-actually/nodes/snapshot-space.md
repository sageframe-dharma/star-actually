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
  You deleted the files and the free space barely moved—because snapshots
  are still holding those files. The space changed owners; it didn't come
  back.
---
<!-- depth:1 -->
Snapshots and Disappearing Space
<!-- depth:2 -->
<!-- provenance: extracted -->
The lived version: you delete a hundred gigabytes of junk to free up room,
check the free space—and almost nothing came back. A lifetime of computers
said deleting frees space. **Actually, deleting a file only frees its space
if *nothing else is still holding it*—and every snapshot taken while those
files existed is still holding them.** That's what a snapshot is: a promise
that a past moment won't be thrown away. The space didn't leak; its
ownership moved from your live files to the snapshots. Deleting things in
the present cannot un-keep the past. *(Operational source: the
practitioner's own hourly-snapshot dataset doing exactly this.)*
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
