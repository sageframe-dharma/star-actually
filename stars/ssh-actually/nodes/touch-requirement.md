---
id: touch-requirement
title: The Touch Requirement
type: definition
requires: [hardware-security-keys]
related: [presence-vs-identity, hardware-pin]
entry_points: [why do I have to touch my yubikey, what does the touch prove, hardware key flashing]
summary: >
  A physical press required before any cryptographic operation—proves a human
  is present and the action is intentional; makes automation impossible.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
The Touch Requirement

<!-- depth:2 -->
<!-- provenance: extracted -->
A **physical interaction** (pressing the key) required before cryptographic operations occur. This is about **control**, not identity.

<!-- depth:3 -->
<!-- provenance: extracted -->
Touch proves three things:

- A human is present
- The action is intentional
- Automation is impossible

Touch alone stops:

- Malware
- Remote attackers
- Background abuse

Nothing on your computer—no process, no script, no attacker with remote access—can produce a signature without a finger on the device. That is the entire point: the hardware key flashing at you is a request for a decision only a physically present human can make.

In practice you'll see it during authentication: the key flashes, you touch it, the signature is produced, login succeeds. If you ignore the flash, the operation simply times out—nothing was signed.
