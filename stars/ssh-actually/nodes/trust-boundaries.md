---
id: trust-boundaries
title: Trust Boundaries
type: concept
requires: [key-pairs]
related: [passphrases, hardware-security-keys, agent-forwarding, state]
entry_points: [where does my ssh key live, who can steal my key, where do secrets live, what am I trusting]
summary: >
  Where the secret lives determines who you must trust — disk trusts your OS,
  hardware trusts a physical object, forwarding lends trust away.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Trust Boundaries

<!-- depth:2 -->
<!-- provenance: synthesized -->
A **trust boundary** is the line around the place your secret lives. Everything inside the line can use — or lose — the secret; everything outside must ask. Where you draw the line decides who you are trusting: a key on disk trusts your entire operating system; a key in hardware trusts one physical object.

<!-- depth:3 -->
<!-- provenance: synthesized -->
The question "how secure is my SSH setup?" is really "where does the secret live?" — and there are only a few answers:

**On disk (traditional keys).** The private key is a file. Malware can copy it, disk theft exposes it, backups contain it. A passphrase helps, but it's brute-forceable offline. The boundary is your whole OS: anything that can read your files is inside it.

**On disk, dressed up (macOS Keychain).** macOS stores passphrases in Keychain, unlocks them via Touch ID, auto-loads keys into the agent. It *feels* like hardware security; it is actually disk-based security plus OS trust. The private key still lives on disk — the boundary hasn't moved, it's just better furnished.

**In hardware.** The secret is created inside the device, never written to disk, and cannot be copied. The boundary shrinks to a physical object you can hold.

**Lent away (agent forwarding).** The key stays home, but a remote machine can request signatures from your agent — the boundary temporarily extends to include a machine you may not control.

<!-- depth:4 -->
<!-- provenance: extracted -->
The core mental model, side by side:

| | Disk-based key | Non-resident (hardware) | Resident (hardware) |
| --- | --- | --- | --- |
| On disk | Private key (**SECRET**, copyable) | Blob file (not secret) | Stub file (not secret) |
| In hardware | — | Master secret (not copyable) | Private key in slot (not copyable) |
| Security level | Medium | High | High |
| Recovery | Restore from backup | Restore blob from backup | Regenerate stub |
| Vulnerability | Disk theft + weak passphrase = compromise | Lose blob = lose access; hardware theft alone OK | Lose hardware = lose access |

> **Hardware keys don't change the cryptography — they change where secrets can exist.**

Traditional SSH keys live on disk, and passphrases help but are brute-forceable offline. Hardware security keys solve this by changing the rules entirely: moving trust out of your computer and into a physical object. What must be remembered for authentication to keep working — the **state** — can't be eliminated; you can only choose where it lives.
