---
id: resident-vs-non-resident
title: Resident vs Non-Resident
type: concept
requires: [resident-keys, non-resident-keys]
related: [choosing-an-approach, state, slots, recovery-planning]
entry_points: [resident or non-resident, which hardware key type should I use, resident vs non-resident comparison, blob vs stub]
summary: >
  The decision surface — permanence vs scalability. Resident trades slots for
  survivability; non-resident trades blob custody for unlimited keys. State
  survivability, not strength.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Resident vs Non-Resident

<!-- depth:2 -->
<!-- provenance: extracted -->
Both are hardware-backed SSH keys with the **same cryptographic strength**. The difference is what the hardware remembers: a **resident key** is generated and stored entirely inside the device; a **non-resident key** is derived on demand from a **blob** file on disk. Resident vs non-resident is about **state survivability**, not strength.

<!-- depth:3 -->
<!-- provenance: extracted -->
The critical summary:

| Feature          | Non-Resident | Resident |
| ---------------- | ------------ | -------- |
| Secrets on disk  | ❌           | ❌       |
| Blob required    | ✔            | ❌       |
| Stub regenerable | N/A\*        | ✔        |
| Uses slots       | ❌           | ✔        |
| Unlimited        | ✔            | ❌       |
| Disk loss safe   | ❌           | ✔        |
| Best use         | GitHub       | Servers  |

\*Non-resident keys use blobs (required, not regenerable), not stubs. Only resident keys have stubs, which can be regenerated on any machine.

Neither puts a secret on disk. The question is which *non-secret* file sits there — a blob you must preserve, or a stub you can throw away — and whether the key consumes a scarce hardware slot.

<!-- depth:4 -->
<!-- provenance: extracted -->
The two tradeoffs are mirror images:

> **Resident keys trade scalability for permanence.**
> **Non-resident keys trade discoverability for scalability.**

Choose by situation:

| Situation                        | Use this              |
| -------------------------------- | --------------------- |
| Access to 1–5 critical servers   | **Resident keys**     |
| Access to GitHub/GitLab only     | **Non-resident keys** |
| Access to 10+ servers/services   | **Non-resident keys** |
| Need maximum recovery capability | **Resident keys**     |

Why the table falls this way: resident keys survive disk loss and work on fresh machines with nothing but the hardware — ideal for critical infrastructure and long-lived access, where recovery matters more than quantity — but each one consumes a slot, and slots are intentionally scarce. Non-resident keys are unlimited and use no slots, but you accept responsibility for preserving the blob, with no recovery if it's lost.

The failure modes mirror too. Lose the *disk*: resident keys are fine (regenerate stubs), non-resident keys die with their blobs unless you backed them up. Lose the *hardware*: both are gone — which is why the recovery plan (a backup hardware key, or backed-up blobs plus a new device) matters no matter which side you choose.
