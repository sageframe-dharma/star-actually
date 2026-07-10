---
id: graded-eval
title: eval (graded eval)
type: definition
requires: []
related: [smoke-test]
entry_points: [eval]
summary: >
  A human-graded check of output quality — correctness, clarity, judgment — where a pass/fail machine won't do.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
eval (graded eval)

<!-- depth:2 -->
<!-- provenance: extracted -->
A human-graded check of output quality — correctness, clarity, judgment — where a pass/fail machine won't do.

<!-- depth:3 -->
<!-- provenance: extracted -->
A validation modality (c): a human-graded pass on _output quality_
— correctness, clarity, judgment — that needs discernment rather than a pass/fail robot.
Produces a graded-eval record (a `type: eval-handoff` + `type: eval-results` pair). What
earlier drafts mislabeled a "smoke test."

<!-- depth:4 -->
<!-- provenance: extracted -->
**The Validation Layer.** The verification stack answers one question: **did we build it _right_?** — does the code match the spec. Every layer in Section 2 serves that question. It is only half of quality.

The other half is **validation**: **did we build the _right thing_, and is it _good_?** A system can pass every test, clear every linter, and survive cross-agent and human architectural review — and still be the wrong thing, or a right thing that is confusing, unpleasant, or useless in real hands. Verification cannot catch this, because verification measures conformance to a spec, and the spec itself is what validation interrogates.

This is Section 1's thesis extended. The research there — that humans overestimate AI-assisted work — was about correctness. It holds at least as strongly for goodness. An agent reporting "the feature works" is reporting that it ran; it is not reporting that the feature is _good_, because good is not a property the agent is positioned to judge. Validation is the antidote to overconfidence about goodness, exactly as verification is the antidote to overconfidence about correctness.

<!-- depth:5 -->
<!-- provenance: extracted -->
**Eval (graded eval) *(canonical-provisional — adopt on 2nd use)*.** **Purpose:** a graded pass on *output quality* — correctness, clarity, judgment — the
validation modality that needs human discernment rather than a pass/fail robot (2.7 §3). A
regression floor plus a new-capability set, with a grader/observer split and a corpus-delta
check. Two paired documents in practice: a self-contained *handoff* framing the pass, and a
*results* document recording graded outcomes.
**Frontmatter:** `type: eval-handoff`, `type: eval-results`.
**Location / instances:** shodo main arc and Subproject-A; the instances carry the historical
`smoke-handoff` / `smoke-results` tokens — new instances use `eval-handoff` / `eval-results`
(the `smoke-` token is dropped, as `smoke-sidequest-` was). Produced by the project-local
`ho-smoke-collaborator` skill — a promotion candidate, re-scoped to the validation modalities
it serves (IDEA-004); it self-describes as "a sibling to the Kamae authoring skills: it feeds
Kamae 5's Reflect phase without writing it."

> **Name correction (D19).** This entry is what earlier drafts mislabeled a "smoke test." In
> the validation layer (2.7 §3) the *smoke test* is the agent-run function check — a
> *practice*, not an artifact — while this human-graded output-quality pass is the **eval**.
