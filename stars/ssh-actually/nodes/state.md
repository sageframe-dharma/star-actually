---
id: state
title: State
type: definition
requires: [hardware-keys-ssh]
related: [slots, trust-boundaries, resident-vs-non-resident]
entry_points: [what is authentication state, what must be remembered for ssh to work, where does auth state live]
summary: >
  Anything that must be remembered for authentication to keep working—lose it
  and auth fails, copy it and auth can be stolen.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
State

<!-- depth:2 -->
<!-- provenance: extracted -->
**State** is *anything that must be remembered* for authentication to keep working. If the required state is lost, authentication fails. If the state is copied, authentication can be stolen.

<!-- depth:3 -->
<!-- provenance: extracted -->
Examples of state:

- a private SSH key file on disk
- a password stored by a service
- a cryptographic secret stored inside hardware

You cannot eliminate state—you can only **choose where it lives**.

That choice is the entire design space. Traditional SSH puts all state on disk. Hardware-backed SSH splits state between your computer and the hardware key. Resident and non-resident keys are two different answers to the same question: which side of that split remembers the key?
