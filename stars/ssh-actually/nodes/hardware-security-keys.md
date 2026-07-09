---
id: hardware-security-keys
title: Hardware Security Keys
type: concept
requires: [key-pairs, fido2]
related: [trust-boundaries, hardware-keys-ssh, passkeys, touch-requirement]
entry_points: [what is a yubikey, what does a hardware security key do, how does a security key work, can a yubikey be copied]
summary: >
  A physically enforced boundary where secrets can be used but never stolen —
  a cryptographic co-processor, not a USB password.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Hardware Security Keys

<!-- depth:2 -->
<!-- provenance: extracted -->
A small physical device whose entire purpose is to **hold cryptographic power in a place software cannot reach**. It is not "extra authentication." It is **moving trust out of your computer and into a physical object**.

<!-- depth:3 -->
<!-- provenance: extracted -->
A hardware security key can do four things, and understanding them dissolves most of the mystery:

**1. Generate cryptographic secrets.** A cryptographic secret is a large random number that is mathematically infeasible to guess. When a hardware key generates one, the secret is created **inside the hardware** — the operating system never sees it, it is never written to disk, it cannot be copied. You cannot steal what never existed outside the device.

**2. Store secrets securely.** Storage that cannot be read, copied, or dumped — even by the computer it's plugged into. Secrets live in tamper-resistant memory, there is no command to "export" them, and physical extraction is extremely difficult and usually destructive. The hardware key does **not** "encrypt files." It simply **refuses to give secrets away**.

**3. Require touch and/or PIN.** This is about **control**, not identity — a physical press proves a human is present, and a device-enforced PIN limits who can ask.

**4. Sign data without exposing secrets.** The computer asks: *"Please sign this challenge."* The hardware responds: *"Here is a proof I signed it."* At no point does the computer get the private key, any reusable secret, or any material it could steal.

Examples: YubiKey, SoloKey, Nitrokey. They are not "USB passwords." They are **cryptographic co-processors**.

<!-- depth:4 -->
<!-- provenance: extracted -->
Why the device exists at all: key-pair cryptography is strong, but there's still a vulnerability — **where the secret lives**. Traditional SSH keys live on disk. That means malware can copy them, disk theft exposes them, and backups contain them. Passphrases help, but they're brute-forceable offline. Hardware security keys solve this by changing the rules entirely: the secret never exists anywhere software can reach.

Because the underlying trick is generic — sign challenges without releasing the secret — one device can act as several things at once:

- an **MFA device** (second factor for logins)
- a **passkey holder** (storing discoverable FIDO2 credentials)
- an **SSH authenticator** (signing SSH challenges, no private keys on disk)
- a **smart card** (on models that support it)

All of these rely on the same three guarantees: hardware isolation, non-exportable secrets, signature-based authentication.

<!-- depth:5 -->
<!-- provenance: extracted -->
The signature is the core magic. A **signature** is a mathematical proof that a specific secret exists and that the holder of that secret approved *this exact action*. Crucially, the secret never leaves the hardware — only the signature does.

In key-pair terms:

- Public key → shared with servers
- Private key → locked inside hardware
- Signature → proof created *by* the hardware

The mental model to keep. A hardware security key is not:

- A password manager
- A magic dongle
- A second password

It is:

> **A physically enforced boundary where secrets can be used but never stolen.**

Everything else — SSH, passkeys, PINs, touch — is just different ways of *asking* that boundary to prove something. Once you see it this way, the rest stops being obtuse.
