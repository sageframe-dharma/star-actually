---
created: 2026-07-03
status: complete
type: ho
project: star-actually
ho: ho-05
title: The Motion
builds-on: ho-04-the-look
---

# ho-05 — The Motion

**Goal:** the navigation model, alive. Keyboard-first movement, the journey rail, branch and one-keypress return, depth restoration — the invariant "getting lost is not possible" becomes running code.

## Scope

**In:** `assets/app.js` — the whole behavioral surface: journey state in `sessionStorage`, htmx event wiring, keyboard map (`+/−` depth, `↓` onward, `↑` back-with-depth-restore, `→` branch, `↩` return, `1–9` pick a neighbor, `/` ask, `?` help, `Esc` blur), rail rendering with branch return chip, rail-click recentering, deep-link `?d=N`.

**Out:** search behavior (ho-06 wires the prompt), any server anything.

## Decisions made here

- **The journey is a path plus a branch stack.** `path` records every visit `{id, depth, title}`; `branches` records departure indices. Return pops the stack, truncates the path to the departure point, and restores node *and* depth. Nested branches nest naturally.
- **Dialing depth edits the current visit rather than appending** — the rail shows where you are per node, not every dial you tried.
- **Keys defer to the reader's intent**: nothing fires while an input is focused (except `Esc` to blur and `↩` to submit); `Enter` on a focused link stays a click. The keyboard layer never fights the browser.
- **Programmatic navigations replace history; declarative link-clicks push it** (via `hx-push-url`). Browser back keeps working; the journey rail is the richer history, not a replacement for the browser's.

## Verification

`make verify` green (JS is smoke-covered per Kamae 2, not unit-covered); full keyboard walk of the exemplar graph in the built site: dial 1→5 on agent-forwarding, branch out, return, back-restores-depth. Budget check: file stays ≤ ~400 lines.
