---
id: smoke-test
title: smoke test
type: definition
requires: []
related: [interaction-test]
entry_points: [smoke test]
summary: >
  An agent walking through the real feature to confirm it works—the floor other checks must clear, never the final word.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
smoke test

<!-- depth:2 -->
<!-- provenance: extracted -->
An agent walking through the real feature to confirm it works—the floor other checks must clear, never the final word.

<!-- depth:3 -->
<!-- provenance: extracted -->
A validation modality (a): the **agent** walks through the real _function_
(not a code/unit test) and confirms it works. Agent-run and therefore a _floor, never a
verdict_—"a passing smoke test is not validation; it's the floor a human interaction test
has to clear." Produces commits, no document—a practice, not an artifact type.

<!-- depth:4 -->
<!-- provenance: extracted -->
**The Validation Layer.** The verification stack answers one question: **did we build it _right_?**—does the code match the spec. Every layer in Section 2 serves that question. It is only half of quality.

The other half is **validation**: **did we build the _right thing_, and is it _good_?** A system can pass every test, clear every linter, and survive cross-agent and human architectural review—and still be the wrong thing, or a right thing that is confusing, unpleasant, or useless in real hands. Verification cannot catch this, because verification measures conformance to a spec, and the spec itself is what validation interrogates.

This is Section 1's thesis extended. The research there—that humans overestimate AI-assisted work—was about correctness. It holds at least as strongly for goodness. An agent reporting "the feature works" is reporting that it ran; it is not reporting that the feature is _good_, because good is not a property the agent is positioned to judge. Validation is the antidote to overconfidence about goodness, exactly as verification is the antidote to overconfidence about correctness.
