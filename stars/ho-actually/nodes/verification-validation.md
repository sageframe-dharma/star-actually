---
id: verification-validation
title: verification / validation
type: concept
requires: [what-is-ho-system]
related: [dogfood, graded-eval, interaction-test, smoke-test]
entry_points: [verification / validation]
summary: >
  The two halves of quality—verification asks whether it was built right, validation asks whether the right thing was built and whether it's any good.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
verification / validation

<!-- depth:2 -->
<!-- provenance: extracted -->
The two halves of quality—verification asks whether it was built right, validation asks whether the right thing was built and whether it's any good.

<!-- depth:3 -->
<!-- provenance: extracted -->
The two halves of quality. **Verification** asks _did we
build it right?_ (matches spec)—tests, lint, self-review, cross-agent review, human
architectural review. **Validation** asks _did we build the right thing, and is it good?_—the four modalities (smoke test, interaction test, eval, dogfood). A passing verification
stack is not validation.

<!-- depth:4 -->
<!-- provenance: extracted -->
**The Verification Stack.** Verification in the Ho System operates at five layers. Each layer catches different classes of problems. Used together, they form a comprehensive quality practice that scales from beginner to advanced practitioner.
