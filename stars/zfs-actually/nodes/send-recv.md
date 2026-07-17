---
id: send-recv
title: Send and Receive
type: concept
requires: [snapshot]
related: [sanoid-syncoid, snapshots-are-not-backups, pool-import-export]
entry_points:
  - what is zfs send
  - zfs send vs rsync
  - incremental replication
  - how to copy a dataset to another machine
summary: >
  Not rsync with extra steps—a serialized exact snapshot state, with
  incrementals diffed by block birth-time. rsync approximates sameness; recv
  is sameness.
---
<!-- depth:1 -->
Send and Receive
<!-- depth:2 -->
<!-- provenance: synthesized -->
The naive slot for "replication tool" is rsync-shaped: walk the tree,
compare, copy what changed. **Actually, `zfs send` serializes a snapshot—an exact, block-level, point-in-time state of a dataset—into a stream,
and `zfs recv` reconstructs it perfectly on any pool**: every file,
property, and the snapshot itself. No walking, no comparing, no "mostly the
same." rsync approximates sameness file-by-file over a live, shifting
target; recv *is* sameness, of a frozen moment.
<!-- depth:3 -->
<!-- provenance: synthesized -->
The shape of use:

- Full: `zfs send tank/ds@snap | ssh backup zfs recv vault/ds`—a stream
  through a pipe, composable with ssh (this is where your SSH keys earn
  their keep).
- **Incremental** is the daily workhorse: `zfs send -i @yesterday @today`
  ships only the blocks born between the two snapshots. Cost scales with
  churn, not dataset size—a 10TB dataset that changed 2GB sends 2GB.
- Interrupted transfers resume (`-t` with a receive token)—relevant the
  first time a multi-TB initial send meets a flaky link.
- Nobody types this on schedule; syncoid wraps the whole dance. But run it
  by hand once—the pipe makes the architecture legible.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The load-bearing constraint: **incrementals require a common snapshot on
both sides.** The shared snapshot is the reference point the diff is
computed against; destroy the last common one (say, by hand-pruning
snapshots the replication depended on) and incremental replication is over—next send starts from zero. This single fact explains most real-world
replication breakage, and it's why retention policy and replication schedule
have to be designed *together* (sanoid's job, syncoid's job—one config).

Boundaries: send/recv moves *datasets between pools*; moving *whole pools
between machines* is import/export, no copying at all. And the
tape-archive temptation—piping sends into files for cold storage—is
brittle (one flipped bit invalidates a whole stream, and incrementals chain);
streams are transport, a live receiving pool is storage.
<!-- depth:5 -->
<!-- provenance: synthesized -->
Why incrementals are cheap to *compute*, not just to ship: every block in
ZFS records the transaction group of its birth. A snapshot is a txg
boundary; "what changed between @a and @b" is answered by descending the
block tree and pruning any subtree whose birth-txg is older than @a—whole unchanged branches are skipped at the pointer level, without reading
the data below them. The diff falls out of the CoW bookkeeping that was
happening anyway. rsync must *discover* differences by inspection;
ZFS already knows, structurally, which is why an incremental over ten
million unchanged files costs approximately nothing.

The stream's exactness also transfers what file-level tools can't see—holes in sparse files, every property, dataset structure (`-R` for
recursive trees)—and encrypted datasets can travel *raw*: replicated
without ever being decrypted, so the backup target holds ciphertext it
cannot read. Try expressing that in rsync.
