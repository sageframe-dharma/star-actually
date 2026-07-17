# Peko State—ZFS

**Phase:** P4 · handoff (arc closed)
**NEXT:** arc complete—finishing pass done in the same session; instance
built to `dist/` and deployed into `public/zfs-actually`. Note: this arc was
*simulated*—authored as Andrew's plausible learning path for comparison
against his own live Peko arc. When the live arc runs, diff its questions.md
against this one; the divergences are the interesting part.

## Coverage checklist (D7—heuristic proposes, practitioner disposes)
- [x] every questions.md entry has a resolving node
- [x] every node reaches at least depth-2
- [x] destructive/operational claims are spine-sourced (S01 replace; S05
      ashift; rollback hazard-marked inline, semantics per zfs-rollback(8))
- [x] no open confusions remain in the log
- [x] practitioner declared ready-to-author *(simulated declaration—Andrew
      reviews on comparison)*

## Node ledger
| id | title | depths | provenance |
|----|-------|--------|------------|
| what-zfs-is | What ZFS Is | 1–5 | synthesized |
| pool | The Pool | 1–4 | synthesized |
| vdev | The Vdev | 1–5 | synthesized |
| dataset | Datasets | 1–4 | synthesized |
| copy-on-write | Copy-on-Write | 1–5 | synthesized |
| checksums | Checksums | 1–5 | mixed |
| property-inheritance | Property Inheritance | 1–3 | synthesized |
| zvol | Zvols | 1–4 | synthesized |
| mountpoints | Mountpoints | 1–4 | synthesized |
| pool-import-export | Import and Export | 1–4 | synthesized |
| arc | The ARC | 1–5 | synthesized |
| l2arc | L2ARC | 1–4 | synthesized |
| zil-slog | ZIL and SLOG | 1–5 | mixed |
| compression | Compression | 1–4 | mixed |
| recordsize | Recordsize | 1–4 | mixed |
| ashift | Ashift | 1–4 | mixed |
| dedup | Deduplication | 1–4 | mixed |
| ecc-question | The ECC Question | 1–4 | mixed |
| snapshot | Snapshots | 1–5 | synthesized |
| snapshot-space | Snapshots and Disappearing Space | 1–4 | mixed |
| snapshots-are-not-backups | Snapshots Are Not Backups | 1–4 | synthesized |
| send-recv | Send and Receive | 1–5 | synthesized |
| sanoid-syncoid | Sanoid and Syncoid | 1–4 | mixed |
| rollback | Rollback | 1–4 | synthesized |
| mirror | Mirrors | 1–4 | synthesized |
| raidz | RAIDZ | 1–5 | synthesized |
| raidz-expansion | RAIDZ Expansion | 1–4 | mixed |
| resilver | Resilvering | 1–4 | mixed |
| scrub | Scrubs | 1–4 | mixed |
| zpool-status | Reading zpool status | 1–4 | synthesized |
| replace-disk | Replacing a Disk | 1–4 | mixed |
| free-space-discipline | The Free-Space Discipline | 1–4 | synthesized |
| first-pool | Your First Pool | 1–4 | mixed |
| proxmox-zfs | ZFS Under Proxmox | 1–4 | mixed |

34 nodes · root `what-zfs-is` · 4 chains declared in site.yaml.

## Open threads
- Encryption and dRAID parked outside the boundary (see notes.md).
- RAIDZ-expansion parity-ratio caveat at medium confidence (S02)—vet against
  a primary source before it carries operational weight.
- Depth-5 layers exist only where the concept warranted theory (what-zfs-is,
  vdev, copy-on-write, checksums, arc, zil-slog, snapshot, send-recv, raidz);
  the rest stop honestly at 3–4.
