---
id: slots
title: Slots
type: definition
requires: [hardware-keys-ssh, state]
related: [resident-keys, managing-resident-credentials]
entry_points: [what is a slot on a yubikey, how many keys fit on a hardware key, why are slots limited]
summary: >
  Small, protected storage locations inside the hardware key—intentionally
  scarce, because limiting stored secrets limits blast radius.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Slots

<!-- depth:2 -->
<!-- provenance: extracted -->
A **slot** is a **small, protected storage location inside a hardware security key** where state can live *without ever touching your computer*.

<!-- depth:3 -->
<!-- provenance: extracted -->
Slots exist because:

- secure hardware storage is expensive
- fewer stored secrets reduce attack surface
- limiting storage forces safer designs

Slots are **intentionally scarce**—typically 25–32 on current devices. This is a feature, not a shortcoming. If a hardware key allowed unlimited stored secrets:

- large-scale extraction would be more valuable
- loss or theft would be more damaging
- attacks would scale better

By limiting slots, hardware keys enforce minimal stored state, intentional key usage, and safer failure modes. Only **resident keys** consume slots—non-resident keys use none, which is exactly why they're unlimited.
