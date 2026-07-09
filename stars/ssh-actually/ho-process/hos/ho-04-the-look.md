---
created: 2026-07-03
status: complete
type: ho
project: star-actually
ho: ho-04
title: The Look
builds-on: ho-03-the-render
---

# ho-04 — The Look

**Goal:** classic 1996, gorgeous. The stylesheet that earns the seed's bar: dark screen, monospace grid, blinking cursor, content as the only interface — hostile to nothing, inviting like a good terminal.

## Scope

**In:** `assets/style.css` — the complete visual system. Monospace Web lineage: strict character grid, one accent, functional contrast only. Screen anatomy from Kamae 2 §2: journey rail, node head with type badge, depth gauge as lit cells, layer sections, neighborhood lists, persistent action bar, entry screen with blinking cursor. Reduced-motion respect. Terminal-width column.

**Out:** behavior (ho-05), search UI (ho-06).

## Decisions made here

- **Phosphor green as the single accent** on a near-black warm ground. SSH is a terminal subject; the green is earned, not nostalgic-kitsch. Dim gray for structure, off-white for prose. Type badges tint by node type, quietly.
- **System mono stack, zero webfonts.** The reader's own terminal font is the brand.
- **New layers announce themselves**: the deepest section fades in on arrival (respecting `prefers-reduced-motion`), so dialing deeper *feels* like revealing, not reloading.
- **Section labels in rule-lines** (`── onward ──`) via borders, not images. No icons anywhere.

## Verification

Build renders; visual pass over entry, node at each depth, help; no external requests in any emitted page (`grep -r "https\?://" dist --include="*.html"` finds only honest `<a href>`s).
