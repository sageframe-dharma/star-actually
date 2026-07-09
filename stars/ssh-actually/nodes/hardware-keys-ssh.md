---
id: hardware-keys-ssh
title: Hardware Keys for SSH
type: concept
requires: [hardware-security-keys, key-pairs]
related: [state, slots, agent-forwarding, choosing-an-approach]
entry_points: [ssh with a yubikey, what is ed25519-sk, why does hardware ssh feel weird, hardware backed ssh keys]
summary: >
  Hardware-backed SSH doesn't change the cryptography — it changes where
  authentication memory lives, splitting state between disk and device.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Hardware Keys for SSH

<!-- depth:2 -->
<!-- provenance: extracted -->
Hardware SSH keys don't change the cryptography. They change **where authentication memory lives**. Everything else follows from that.

<!-- depth:3 -->
<!-- provenance: extracted -->
Why hardware-backed SSH feels strange: with web auth, you visit a site, the browser handles everything, the key just "works." With SSH, there are files in `~/.ssh/`, some are called "blobs," others "stubs," terms like "resident" and "non-resident" appear, and it's not clear what goes where or why.

The confusion comes from one shift:

> **Hardware keys change *where authentication state lives*.**

Traditional SSH puts **all state on disk** — the private key file is the full secret, copyable, losable. Hardware-backed SSH **splits state** between your computer and the hardware key. That split is the entire design.

Mechanically, modern SSH simply reuses **FIDO2 hardware keys as signing devices** — the `ed25519-sk` key type uses FIDO2 as a signing oracle. SSH predates all of the modern web-auth machinery: it already uses key-pair cryptography, already knows the username, and does not need discovery. This is why SSH keys, WebAuthn, and passkeys feel related — they *are*.

<!-- depth:4 -->
<!-- provenance: extracted -->
Where state lives, side by side:

```text
Traditional SSH (disk-based key)

[ Your Computer ]
┌──────────────────────────┐
│ private_key (FULL SECRET)│  ← copyable
│ passphrase (optional)    │
└──────────────────────────┘

Hardware-backed SSH

[ Your Computer ]           [ Hardware Key ]
┌──────────────────┐       ┌────────────────┐
│ stub / handle    │──────▶│ slot (SECRET)  │
│ (no secret)      │       │ PIN / touch    │
└──────────────────┘       └────────────────┘
```

With the disk key: lose the file → access is gone; copy the file → attacker can authenticate. With the hardware key: the **secret never becomes a file**, the computer cannot authenticate alone, and physical presence is required every time.

Two concepts carry the whole model from here: **state** (anything that must be remembered for authentication to keep working) and **slots** (the scarce protected storage inside the device). The two kinds of hardware SSH key — resident and non-resident — are just two answers to "which side of the split holds the state?"

<!-- depth:5 -->
<!-- provenance: extracted -->
The takeaway:

> **Hardware-backed SSH is not about stronger math.**
> **It is about strictly controlling where state is allowed to exist.**

The cryptographic strength of an `ed25519-sk` key and a disk-based `ed25519` key is the same. What differs is the failure modes. A disk key's state is a file — so its threats are file threats: malware copies it, backups leak it, theft plus a weak passphrase compromises it. A hardware-backed key's secret lives where no copy operation exists — so its threats become physical ones: lose the device (recoverable, if you planned), or lose the non-secret file the device needs (recoverable or permanent, depending on key type).

Once you understand *state* and *slots*, everything else — resident keys, non-resident keys, stubs, blobs, PINs — becomes a detail, not a mystery.
