# Sources—ZFS

*The source ledger (D13): a research archive, not a publish queue. Excerpts
are the load-bearing text itself, so entries survive link rot.*

---

## S01 · OpenZFS man page—zpool-replace(8)
- **Tier:** spine
- **Locus:** https://openzfs.github.io/openzfs-docs/man/master/8/zpool-replace.8.html · accessed 2026-07-16
- **Excerpt:** > "This is equivalent to attaching new-device, waiting for it to resilver, and then detaching device." · "new-device is required if the pool is not redundant." · "Any in progress scrub will be canceled." · "The size of new-device must be greater than or equal to the minimum size of all the devices in a mirror or raidz configuration."
- **Why it mattered:** The exact semantics of the one command you run under stress—and the confirmation that replace is attach-resilver-detach, not a special mode.
- **Instance-relevant?:** yes → node `replace-disk`
- **Confidence:** high

## S02 · OpenZFS 2.3.0 release notes
- **Tier:** spine
- **Locus:** https://github.com/openzfs/zfs/releases/tag/zfs-2.3.0 · accessed 2026-07-16
- **Excerpt:** > "RAIDZ Expansion: Add new devices to an existing RAIDZ pool, increasing storage capacity without downtime." · "Fast Dedup: a major performance upgrade to the original OpenZFS deduplication functionality."
- **Why it mattered:** Kills the stale forum absolute "you can never grow a RAIDZ." Release is January 2025 (the fetch summary misread the year as 2024; the zfs-2.3.0 tag is 2025-01-13—flagged, not load-bearing). The old-data-keeps-old-parity-ratio caveat is not in the release notes themselves; carried at medium confidence from the feature's design discussion.
- **Instance-relevant?:** yes → node `raidz-expansion`
- **Confidence:** high (feature) / medium (caveat wording)

## S03 · jrs-s.net—"Will ZFS and non-ECC RAM kill your data?"
- **Tier:** web-found
- **Locus:** https://jrs-s.net/2015/02/03/will-zfs-and-non-ecc-ram-kill-your-data/ · accessed 2026-07-16
- **Excerpt:** > Matt Ahrens: "There's nothing special about ZFS that requires/encourages the use of ECC RAM more so than any other filesystem." · Article's conclusion: for a scrub to overwrite good data, bad RAM would effectively have to produce corrupted data that still matches its checksum—ZFS *mitigates* bad-RAM damage rather than amplifying it.
- **Why it mattered:** The scrub-of-death myth is the single loudest wrong claim in homelab ZFS discourse; this pins the correction to the co-creator's own words.
- **Instance-relevant?:** yes → node `ecc-question`
- **Confidence:** high (the quote is widely corroborated; the source is Jim Salter, a known ZFS writer)

## S04 · sanoid/syncoid README (Jim Salter)
- **Tier:** spine
- **Locus:** https://github.com/jimsalterjrs/sanoid · accessed 2026-07-16
- **Excerpt:** > "Sanoid is a policy-driven snapshot management tool for ZFS filesystems." · "Syncoid … facilitates the asynchronous incremental replication of ZFS filesystems."
- **Why it mattered:** Confirms the two-tools-two-primitives model: policy engine over snapshot/destroy; orchestrator over send/recv.
- **Instance-relevant?:** yes → node `sanoid-syncoid`
- **Confidence:** high

## S05 · OpenZFS docs—Performance and Tuning / Workload Tuning
- **Tier:** spine
- **Locus:** https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Workload%20Tuning.html · accessed 2026-07-16
- **Excerpt:** > ashift: "It is set at vdev creation and it is immutable." · "ZFS datasets use an internal recordsize of 128KB by default." · "Changing the recordsize on a dataset will only take effect for new files." · "Set recordsize=1M on datasets that are subject to sequential workloads." · dedup: "Each cached entry uses slightly more than 320 bytes of memory… If there is insufficient memory for the DDT to be cached in memory, each cache miss will require reading a random block from disk, resulting in poor performance." · "Set compression=lz4 on your pools' root datasets so that all datasets inherit it unless you have a reason not to enable it."
- **Why it mattered:** One page grounds four nodes: the ashift foundation-pour claim, the recordsize new-files-only trap, the dedup RAM tax arithmetic, and the lz4-by-default posture.
- **Instance-relevant?:** yes → nodes `ashift`, `recordsize`, `dedup`, `compression`
- **Confidence:** high

## S06 · OpenZFS man page—zpool-scrub(8)
- **Tier:** spine
- **Locus:** https://openzfs.github.io/openzfs-docs/man/master/8/zpool-scrub.8.html · accessed 2026-07-16
- **Excerpt:** > "A normal scrub examines all data in the specified pools and verifies each block's checksum." · "For replicated (mirror, raidz, or draid) devices, ZFS automatically repairs any damage discovered during the scrub." · "Resilvering only examines data that ZFS knows to be out of date… whereas scrubbing examines all data to discover silent errors due to hardware faults or disk failure."
- **Why it mattered:** The detection-vs-repair split in the project's own words—repair is conditional on replication; scrub-vs-resilver scope is explicit.
- **Instance-relevant?:** yes → nodes `scrub`, `resilver`, `checksums`
- **Confidence:** high

## S07 · Klara Systems—"When to use OpenZFS SLOG (and when to avoid it)"
- **Tier:** web-found
- **Locus:** https://klarasystems.com/articles/what-makes-a-good-time-to-use-openzfs-slog-and-when-should-you-avoid-it/ · accessed 2026-07-16
- **Excerpt:** > "regardless of whether or not you create a SLOG, each pool still has its own ZIL" · "On system startup, ZFS reads the ZIL and replays any pending transactions in order to commit those writes to disk." · "neither the ZIL nor the SLOG make a difference with pending asynchronous writes which are always stored in volatile RAM: if you don't have any applications that use synchronous writes, you don't need a SLOG"
- **Why it mattered:** Demolishes the SLOG-is-a-write-cache model with the three load-bearing facts: ZIL always exists, it's only read after a crash, and async writes never touch it. Klara employs core OpenZFS developers—high-quality web-found.
- **Instance-relevant?:** yes → node `zil-slog`
- **Confidence:** high

## S08 · Practitioner's homelab—Proxmox + ZFS + sanoid/syncoid in production
- **Tier:** operational
- **Locus:** practitioner's homelab (Proxmox Docker hosts, per-service ZFS datasets under /opt/services, sanoid snapshot policy + syncoid replication via the sageframe-docker-deploy skill; Kanyō in production on this substrate) · ongoing through 2026-07
- **Excerpt:** > A year of operating ZFS *through automation*—datasets created per service, snapshots taken and pruned on policy, replication running on schedule—without ever holding the model underneath. Every naive model in questions.md survived a year of successful operation, because working automation never tests your understanding.
- **Why it mattered:** This is the arc's origin (P0) and the instance's reader definition: the person whose ZFS works but isn't *theirs* yet.
- **Instance-relevant?:** yes → nodes `sanoid-syncoid`, `proxmox-zfs`, `dataset`
- **Confidence:** high (lived)

## S09 · Practitioner's homelab—the deleted-files-freed-nothing incident
- **Tier:** operational
- **Locus:** practitioner's homelab, a dataset under hourly sanoid policy · 2026 (recalled)
- **Excerpt:** > Cleared a large pile of rebuildable artifacts to reclaim space; `zfs list` barely moved. The space had migrated to the snapshot ledger instead of returning to the pool. First felt like a bug; it is the system keeping its promise.
- **Why it mattered:** The single best experiential teacher of what a snapshot *is*—the moment "snapshots are free" and "deleting frees space" collide and both models break at once.
- **Instance-relevant?:** yes → node `snapshot-space`
- **Confidence:** high (lived)
