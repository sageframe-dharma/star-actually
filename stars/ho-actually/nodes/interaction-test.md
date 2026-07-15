---
id: interaction-test
title: interaction test
type: definition
requires: []
related: [smoke-test]
entry_points: [interaction test]
summary: >
  A human at a real terminal checking that something works and feels right, not just that the code runs.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
interaction test

<!-- depth:2 -->
<!-- provenance: extracted -->
A human at a real terminal checking that something works and feels right, not just that the code runs.

<!-- depth:3 -->
<!-- provenance: extracted -->
A validation modality (b): a human, hands on a real terminal,
checking function _plus feel_—the UI/UX a smoke test structurally can't reach (the delta
between clean chosen input and a real human's messy TTY). Produces commits, no document—a
practice, not an artifact type.

<!-- depth:4 -->
<!-- provenance: extracted -->
**The Validation Layer.** The verification stack answers one question: **did we build it _right_?**—does the code match the spec. Every layer in Section 2 serves that question. It is only half of quality.

The other half is **validation**: **did we build the _right thing_, and is it _good_?** A system can pass every test, clear every linter, and survive cross-agent and human architectural review—and still be the wrong thing, or a right thing that is confusing, unpleasant, or useless in real hands. Verification cannot catch this, because verification measures conformance to a spec, and the spec itself is what validation interrogates.

This is Section 1's thesis extended. The research there—that humans overestimate AI-assisted work—was about correctness. It holds at least as strongly for goodness. An agent reporting "the feature works" is reporting that it ran; it is not reporting that the feature is _good_, because good is not a property the agent is positioned to judge. Validation is the antidote to overconfidence about goodness, exactly as verification is the antidote to overconfidence about correctness.
