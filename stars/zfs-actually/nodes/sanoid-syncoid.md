---
id: sanoid-syncoid
title: Sanoid and Syncoid
type: concept
requires: [snapshot, send-recv]
related: [snapshot-space, proxmox-zfs]
entry_points:
  - what is sanoid
  - what is syncoid
  - automated zfs snapshots
  - zfs backup automation
  - snapshot policy
summary: >
  Not a backup daemon—two thin tools: sanoid is policy over
  snapshot/destroy, syncoid is orchestration over send/recv. Judgment on top
  of primitives you can run by hand.
---
<!-- depth:1 -->
Sanoid and Syncoid
<!-- depth:2 -->
<!-- provenance: extracted -->
Configured once, together, in one file, they blur into a single mental
object: "the backup system." **Actually, they're two separate, thin tools
wrapping two ZFS primitives you can run by hand.** "Sanoid is a
policy-driven snapshot management tool" (its README)—a scheduler over
`zfs snapshot` and `zfs destroy`: take hourlies/dailies/monthlies, prune on
retention. Syncoid "facilitates the asynchronous incremental replication of
ZFS filesystems"—an orchestrator over `zfs send | zfs recv`: find the
common snapshot, ship the increment, retry sanely.

Neither adds storage machinery. It's cron-shaped judgment on top of
snapshots—which is why understanding snapshots and send/recv *is*
understanding these tools.
<!-- depth:3 -->
<!-- provenance: extracted -->
The working setup (the practitioner's homelab runs exactly this shape):
`/etc/sanoid/sanoid.conf` assigns each dataset a template—
```
[tank/services/postgres]
  use_template = production   # hourlies pruned in days; frequent history
[tank/media]
  use_template = archive      # weekly, kept for months; slow history
```
—and a timer runs `sanoid --cron`. Separately, a scheduled
`syncoid --recursive tank/services backup-host:vault/services` replicates.
Two decisions worth making deliberately rather than by default: retention
*per dataset* (churn-heavy data accrues snapshot rent fast—see Snapshots
and Disappearing Space), and replication cadence per dataset (how much
history are you willing to lose—that's your real RPO, in systems terms:
the age of the newest copy elsewhere when disaster hits).
<!-- depth:4 -->
<!-- provenance: synthesized -->
The relationship that bites when misunderstood: **sanoid's pruning and
syncoid's incrementals share the snapshot chain.** Incremental replication
needs a common snapshot on both ends; a retention policy that destroys it
forces the next replication to start from zero. Design retention and
replication as one system (syncoid's own sync snapshots exist to hold the
reference point)—and treat hand-deleting snapshots under a policy engine
as off-limits; change the policy instead.

Automation's quiet cost, named once: a year of these tools working
flawlessly is a year of never being forced to learn what they do—the
naive models survive *because* nothing fails. Run the primitives by hand
once (`zfs snapshot`, `zfs send -i ... | zfs recv`), and the config file
stops being an incantation. Then let the robots have it back.
