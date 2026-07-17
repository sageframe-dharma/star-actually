---
id: compression
title: Compression
type: concept
requires: [dataset]
related: [recordsize, dedup]
entry_points:
  - should i enable compression
  - is compression slow
  - lz4 zfs
  - zfs compression ratio
summary: >
  Squeezing data used to cost speed to save space. ZFS's method is so fast
  the trade runs backward—leave it on, and it often makes things faster.
---
<!-- depth:1 -->
Compression
<!-- depth:2 -->
<!-- provenance: extracted -->
The inherited belief: squeezing data to save space costs speed—a tax you
pay only when the space is worth it. **Actually, the method ZFS uses (named
LZ4) is so fast that the trade usually runs backward: squeezing the data
takes less time than writing and reading the extra unsqueezed bytes
would.** Compression frequently makes storage *faster*. It also gives up
quickly on data that won't squeeze (photos and video are already
compressed), so those cost you almost nothing. Leaving it on everywhere is
the official recommendation—"set compression=lz4 on your pools' root
datasets... unless you have a reason not to enable it" (OpenZFS docs).

Your decades-old instinct about slow compression was correct *when you
formed it*. The hardware moved; the instinct didn't.
<!-- depth:3 -->
<!-- provenance: synthesized -->
Operating it:

- Set once at the top (`zfs set compression=lz4 tank`), let inheritance
  carry it down. On current OpenZFS, `compression=on` means lz4 already.
- Check what it's buying: `zfs get compressratio tank/...`—text, logs,
  and databases commonly land 1.5–3×; already-compressed media sits at
  1.0× and cost you a rounding error to check.
- **zstd** is the deliberate upgrade: better ratios than lz4 for more CPU,
  tunable levels (`compression=zstd-3`). Worth it on datasets that are
  compressible, written moderately, and read a lot—archives, logs. lz4
  remains the right default reflex.

The temporal gotcha (same rule as every ZFS property): it applies to **newly
written blocks only**. Flipping it on rewrites nothing—old data stays
uncompressed until something rewrites it. Don't be puzzled by a 1.0× ratio
on a dataset that was full before you enabled it.
<!-- depth:4 -->
<!-- provenance: synthesized -->
Boundaries worth holding:

- **vs dedup**—the two get mentioned together as "space features" and
  deserve opposite reflexes: compression is nearly-free and default-on;
  dedup is a standing RAM tax and default-off. Compression also quietly
  captures much of what people hope dedup will give them (all those similar
  text blocks compress well) for none of the cost.
- **vs recordsize**—compression works per record, so larger records give
  the compressor more to chew on; a 1M-recordsize archive dataset
  compresses meaningfully better than the same bytes at 128K. The two knobs
  are teammates on archive-shaped data.
- **Where not to bother**—datasets that are purely already-compressed
  media *can* be set `compression=off` for tidiness, but the early-abort
  makes the savings mostly aesthetic. The reflex "off for performance" is
  the one to unlearn.
