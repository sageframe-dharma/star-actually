---
id: modern-auth-landscape
title: The Modern Auth Landscape
type: concept
requires: [key-pairs, passwords]
related: [fido2, passkeys, mfa-strength-ladder, hardware-security-keys]
entry_points: [how do passkeys mfa and hardware keys fit together, map of modern authentication, how does ssh relate to webauthn, why do these all feel related]
summary: >
  The map — passwords, OTP, FIDO2/WebAuthn, passkeys, and hardware keys all
  converge on one idea: never give the server a secret it can lose. SSH did
  it first.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
The Modern Auth Landscape

<!-- depth:2 -->
<!-- provenance: extracted -->
The map of how passwords, MFA, FIDO, WebAuthn, passkeys, and hardware keys actually fit together. Everything modern converges on one idea:

> *Never give the server a secret it can lose.*

<!-- depth:3 -->
<!-- provenance: extracted -->
You do **not** need to be new to computers to be confused by this. The confusion exists because these technologies evolved **incrementally, not coherently** — independently, and never properly unified in documentation.

Modern authentication is built from **layers**, each solving a different problem:

1. **Identity** — who are you claiming to be?
2. **Proof** — how do you prove that claim?
3. **Transport** — how does that proof travel safely?
4. **Enforcement** — what limits abuse or theft?

Different technologies live at different layers; confusion happens when they get lumped together. How the pieces fit:

- **Passwords** → shared secrets (weak)
- **OTP** → layered defense (better)
- **FIDO2/WebAuthn** → cryptographic proof (strong)
- **Passkeys** → FIDO2 made usable
- **Hardware keys** → FIDO2 with physical enforcement
- **SSH** → cryptography before it was cool

<!-- depth:4 -->
<!-- provenance: extracted -->
The mental model to keep:

- **FIDO2** = the cryptographic foundation
- **WebAuthn** = how browsers use it
- **Passkeys** = user-friendly FIDO2
- **Hardware keys** = physical enforcement
- **SSH** = FIDO2 without the browser

Where SSH fits: SSH predates all of this. It has used key-pair cryptography since 1995; the web kept using passwords, then slowly caught up to where SSH already was — with different names and different contexts. SSH already knows the username and doesn't need discovery, so modern SSH simply reuses **FIDO2 hardware keys as signing devices**.

That single family tree — key-pair cryptography at the root, branching to SSH on one side and FIDO2 (WebAuthn → passkeys, hardware keys, `ed25519-sk`) on the other — explains the things that otherwise feel like coincidence:

- Why hardware SSH keys aren't a "new" technology — they're SSH and FIDO2 meeting in the middle
- Why the same YubiKey works for web logins *and* SSH
- Why touch + PIN feels similar whether you're logging into a website or authenticating to a server

The legacy branch — passwords, then OTP layered on top — is fundamentally weaker for one reason: the server stores secrets. The modern branch stores none; the server verifies **signatures, not secrets**.
