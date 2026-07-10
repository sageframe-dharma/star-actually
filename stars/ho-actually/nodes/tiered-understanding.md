---
id: tiered-understanding
title: tiered understanding
type: concept
requires: []
related: [what-is-ho-system]
entry_points: [tiered understanding]
summary: >
  Naming honestly how well you grasp something, on a three-step scale from use-it-blindly to could-rebuild-it.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
tiered understanding

<!-- depth:2 -->
<!-- provenance: extracted -->
Naming honestly how well you grasp something, on a three-step scale from use-it-blindly to could-rebuild-it.

<!-- depth:3 -->
<!-- provenance: extracted -->
Calibrated comprehension in three declared tiers: Tier 1 Black Box
(use without investigating), Tier 2 Functional (configure, troubleshoot, explain — the
default target), Tier 3 Deep (could redesign). Declaring tiers honestly is a core skill;
tiers are declared in shu, self-assigned in ha, internalized in ri.

<!-- depth:4 -->
<!-- provenance: extracted -->
**The Three Tiers in Detail.** ### Tier 1 — Black Box

**Definition:** The learner uses this component without understanding its internals. They know the inputs, the outputs, and the invocation pattern. They trust that it works.

**What Tier 1 looks like in practice:**

- "I call `model(frame)` and get detections back. I don't know how YOLO's neural network identifies objects."
- "I run `ffmpeg -i input -c:v libx264 output` and get a compressed video. I don't know how H.264 encoding works."
- "I use `collections.deque(maxlen=N)` as a ring buffer. I don't know how deque is implemented internally."

**What Tier 1 is NOT:**

- It's not "I've heard of it." Tier 1 requires functional usage — you can invoke it, you can read its output, you can pass it the right inputs.
- It's not "I'm confused by it." If you can't use it at all, you don't have Tier 1 — you have a prerequisite gap.

**When Tier 1 is appropriate:**

- Dependencies and libraries you consume but don't modify
- Infrastructure components you configure but don't build (Docker, CI/CD, CDN)
- Algorithms and protocols you use through standard interfaces
- Anything where the investment to reach Tier 2 doesn't pay off for the current work

**The honest self-assessment test:** "If this component broke in a way I've never seen before, I would need help." That's Tier 1, and that's fine.
