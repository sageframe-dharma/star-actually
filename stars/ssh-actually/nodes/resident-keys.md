---
id: resident-keys
title: Resident SSH Keys
type: concept
requires: [hardware-keys-ssh, state]
related: [stub, slots, non-resident-keys, hardware-key-setup-resident]
entry_points: [what is a resident key, ssh key that survives a wiped laptop, discoverable credential ssh, -O resident meaning]
summary: >
  The key the hardware remembers—generated and stored entirely inside the
  device, discoverable, survives disk loss; the cost is a scarce slot.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Resident SSH Keys

<!-- depth:2 -->
<!-- provenance: extracted -->
A **resident SSH key** is a hardware-backed SSH key where the hardware device stores the key's identity, remembers the key exists, and the private key is **generated and stored entirely inside the hardware**. The private key never exists as a file, never needs to be reconstructed from disk data, and lives permanently inside the hardware key.

<!-- depth:3 -->
<!-- provenance: extracted -->
With a resident key, the hardware stores the private key *and* the key's identity. The computer stores **nothing essential**—only a **stub**, a small non-secret pointer file that tells SSH which resident key to use. The hardware key already knows *which* key you mean and *how* to use it. No reconstruction is required.

The practical consequences: if you have the hardware key,

- the SSH key **cannot be lost**
- no files are required to recover access
- stubs can be regenerated anywhere, on any machine, with `ssh-keygen -K`

A wiped laptop, a stolen disk, a fresh machine—none of it matters. Plug in the hardware key, regenerate the stubs, and you're back.

<!-- depth:4 -->
<!-- provenance: extracted -->
Properties:

- ✔ survives disk loss
- ✔ works on fresh machines
- ✔ discoverable by the hardware key
- ✔ no blob required
- ❌ limited by available hardware slots

The tradeoff is intentional:

> **Resident keys trade scalability for permanence.**

The mirror image of non-resident keys, which trade the other way—unlimited keys, but a blob on disk you must preserve. A resident key consumes one of the device's intentionally scarce slots (typically 25–32 total); in exchange, the state that matters lives entirely in the hardware, where it cannot be lost with a disk.

Resident keys are ideal for:

- critical infrastructure
- long-lived access
- situations where recovery matters more than quantity

One discipline comes with them: because the key exists *only* in that one physical device, losing the device without a backup means total lockout. Resident keys and a **second hardware key with duplicate credentials** go together.

<!-- depth:5 -->
<!-- provenance: extracted -->
The authentication flow:

```text
Client → Hardware Key → Signature → Server
```

Step-by-step:

1. SSH requests authentication
2. The hardware key recognizes the resident key
3. User presence (touch / PIN) is confirmed
4. The private key signs the challenge internally
5. The signature is returned
6. The private key never leaves the hardware

Compare the non-resident flow—`Client → Blob → Hardware Key → Signature → Server`—and notice what's missing here: the required disk file. That is what "discoverable" means mechanically: the device can enumerate its own resident credentials, which is why `ssh-keygen -K` can rebuild your stub files from nothing but the plugged-in key. The stub is required by SSH at connection time, but it is *derived* state, not *essential* state—deleting it costs you five seconds, not a key.

Side by side:

```text
NON-RESIDENT                    RESIDENT
════════════                    ════════
- Unlimited keys                - Limited by slots
- Blob must be preserved        - Stub is regenerable
- Blob loss = permanent         - Disk loss = recoverable
```
