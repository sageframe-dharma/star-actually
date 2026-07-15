---
id: passkeys
title: Passkeys
type: concept
requires: [fido2, webauthn]
related: [hardware-security-keys, trust-boundaries, mfa-strength-ladder]
entry_points: [what is a passkey, passkey vs password, passkey vs hardware key, who controls my passkeys]
summary: >
  User-friendly FIDO2—discoverable credentials, synced by platforms,
  phishing-resistant; the tradeoff is that the platform controls creation,
  sync, and recovery.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Passkeys

<!-- depth:2 -->
<!-- provenance: extracted -->
A **passkey** is a discoverable FIDO2 credential used for passwordless login—a public/private key pair created and managed via WebAuthn, stored securely on a device or platform (Apple, Google, Microsoft).

<!-- depth:3 -->
<!-- provenance: extracted -->
Key properties:

- Based on cryptographic key pairs—authentication is done by **signature, not by sharing secrets**
- No password required, ever
- **Phishing-resistant**—there is nothing to type on a fake site
- Often synced across your devices by the platform
- Typically unlocked by biometrics or a PIN

Passkeys are excellent for usability *and* security. They eliminate passwords entirely rather than layering defenses on top of them.

<!-- depth:4 -->
<!-- provenance: synthesized -->
The important distinction—and the tradeoff:

> Passkeys are **controlled by the service and platform**. You do not manage the raw keys directly.

The platform controls the experience: creation, syncing, recovery. That is exactly what makes passkeys easy to use and extremely secure—and it is also what ties your trust to the platform managing them. Where a disk-based SSH key is a file you custody yourself and a hardware key is a physical object you hold, a passkey's secret lives wherever the platform puts it, moves when the platform syncs it, and comes back (or doesn't) through the platform's recovery process.

Against hardware security keys, the split is clean: passkeys trade direct control for convenience; hardware keys trade convenience for **physical enforcement**—secrets that never leave the device, touch required, no platform in the loop. On the MFA strength ladder they sit adjacent, both far above anything code-based; which one is "better" depends on whether the thing you value is recoverability or custody.
