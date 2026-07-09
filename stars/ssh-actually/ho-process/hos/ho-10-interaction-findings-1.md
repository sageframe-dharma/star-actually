---
created: 2026-07-04
status: complete
type: ho
project: star-actually
ho: ho-10
title: Interaction Findings, Round One
builds-on: ho-08-integration-and-smoke
---

# ho-10 — Interaction Findings, Round One

**Goal:** the practitioner's first interaction test produced findings; findings become hos, not patches. This ho lands the characterized ones and records the open one.

## Findings addressed

1. **The depth dial was inverted.** The seed (Kamae 1 §3, §7) is explicit: *"you dial down: the definition appears."* Depth is water — deeper is down, `−`. ho-05 implemented `+` as reveal, misreading "add a layer" for "descend." Fixed: `−` (and `_`) descends into the node, `+` (and `=`) surfaces; on-screen affordances, action bar, and help all re-worded to the dial metaphor.
2. **Search had no visible way back.** `/` always worked but nothing said so, and the action-bar hint looked clickable while being dead text. Fixed: the `/ search` hint is now a real link to the entry screen; movement hints stay keyboard-only (mouse users have the in-content links).
3. **First arrival gave no orientation.** The rail was empty until the second node, so the top of the screen offered nothing to stand on. Fixed: a single visit renders as the start of a path, with a dim note that the path grows as you move.
4. **Light theme.** Deferred in Kamae 2 as "reader themes"; the practitioner asked. Landed as `prefers-color-scheme` auto-follow — a paper variant with the green kept legible. Dark remains the canonical identity; no toggle yet (a toggle is a preference-persistence question, not a stylesheet question).

## Finding still open

5. **"Some wayfinding issue I can't quite figure out."** Not yet characterized. Suspects, in order: no zoomed-out graph view (deliberately cut from MVP); onward/lateral distinction too subtle in the neighborhood lists; rail semantics. Waiting on the practitioner catching it in the act. Becomes its own ho when named.

## Verification

`make verify` green; rebuild + smoke walk re-run clean; keyboard walk of the new dial direction.
