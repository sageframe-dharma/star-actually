---
id: what-a-filesystem-is
title: What a Filesystem Is
type: concept
requires: []
related: [filesystem-history, filesystem-landscape]
entry_points:
  - what is a filesystem
  - what does a filesystem do
  - filesystem basics
  - what does formatting mean
  - i know nothing about storage
summary: >
  The absolute ground floor: a disk stores only numbered blocks and has no
  idea what a file is—the filesystem is the ledger that invents files,
  names, and folders on top of them.
---
<!-- depth:1 -->
What a Filesystem Is
<!-- depth:2 -->
<!-- provenance: synthesized -->
Everyone has saved a file. It feels like the file goes "onto the disk"—a
thing, placed in a place. But a disk—a hard drive, an SSD, a USB stick—
offers nothing so friendly. It stores only **blocks**: millions of small,
numbered, same-sized slots that each hold some bytes. A disk has no idea
what a file is. It can do exactly two things: read slot number so-and-so,
and write slot number so-and-so.

A **filesystem** is the bookkeeping software that turns those anonymous
slots into the world you actually use: files with names and sizes, folders
inside folders, a record of who is allowed to read what.

So the correction worth carrying from here on: your files are not really
"on the disk." **The disk holds only blocks; the *files* live in the
ledger.** Lose the ledger and every block is still there—and means
nothing.
<!-- depth:3 -->
<!-- provenance: synthesized -->
You have been using filesystems for years without naming them:

- **"Formatting" a drive** means writing a fresh, empty ledger onto it.
  Nothing about the hardware changes—the drive just gets a new, blank
  book of records.
- Every device picked a ledger design: USB sticks usually carry **FAT32**
  or **exFAT**, Windows uses **NTFS**, Macs use **APFS**, Linux most often
  uses **ext4**. When a Mac can't write to a Windows drive, that isn't a
  hardware problem—the two systems keep their records differently, and
  one side can't read the other's book.
- "The format erased my files" means: new ledger, old entries gone. The
  blocks underneath often still hold the old bytes for a while—which is
  exactly what data-recovery tools go digging for.
<!-- depth:4 -->
<!-- provenance: synthesized -->
The words that get tangled together, untangled:

- **The disk** is hardware. It holds blocks. That is all it does.
- **A partition** is a fenced-off region of a disk—a way to split one
  physical disk into sections, each of which gets its own filesystem.
- **The filesystem** is the ledger written inside a partition (or a whole
  disk): the software layer that invents files.
- **The operating system** is the reader and writer of that ledger—it
  contains the code that understands each format.

Stacked in order: **disk → partition → filesystem → files**. Each layer
adds meaning the layer below doesn't have. Almost everything in storage
that seems confusing becomes clear the moment you ask "which layer is this
about?"—and ZFS, where this site is headed, is interesting precisely
because it redraws these layer boundaries.
<!-- depth:5 -->
<!-- provenance: synthesized -->
Every filesystem ever built is a set of answers to the same four problems:

1. **Allocation** — which blocks are free, and which belong to which file?
2. **Naming** — how does `/photos/cat.jpg` become a list of block numbers?
3. **Consistency** — what happens if the power dies *while the ledger is
   half-updated*? A ledger that lies is worse than no ledger.
4. **Speed** — disks are slow and memory is fast; what gets cached, and
   when is it safe to say "done"?

Different filesystems are different trade-offs among the four. And the
*history* of filesystems—the next node—is mostly the history of problem 3:
each generation discovered a new way the ledger could end up wrong, and
built a new defense. The most recent generation, the one ZFS opened, added
a fifth problem the first four decades quietly ignored: **what if the disk
itself lies?**
