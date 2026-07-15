---
id: passwords
title: Passwords
type: concept
requires: []
related: [one-time-codes, phishing-resistance, server-hardening, passphrases]
entry_points: [why are passwords weak, what is a shared secret, why replace passwords]
summary: >
  The shared-secret baseline—the server knows your secret, so the server can
  lose it. Everything else in modern authentication exists because of this flaw.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Passwords

<!-- depth:2 -->
<!-- provenance: extracted -->
A **password** is a shared secret known by you *and* the service. That single word—*shared*—is the whole problem: the server has to store something that can unlock your account, which means the server can lose it.

<!-- depth:3 -->
<!-- provenance: extracted -->
The problems, concretely:

- Passwords **can be stolen from servers**—every breach dump is a pile of shared secrets the server was holding.
- Passwords **can be reused**—one stolen password opens every account it was recycled into.
- Passwords **can be phished**—anything you type, you can be tricked into typing on the wrong site.
- Passwords **must be remembered**—which pushes people toward short, reused, guessable secrets.

One-time codes layer rotating secrets on top; they help, but the secret still lives on a server. The real fix is structural: replace shared secrets with key-pair cryptography, where the server verifies **signatures, not secrets**.

> Everything else in modern authentication exists because passwords are fundamentally weak.
