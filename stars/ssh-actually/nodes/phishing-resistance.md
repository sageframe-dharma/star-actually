---
id: phishing-resistance
title: Phishing Resistance
type: concept
requires: [passwords]
related: [fido2, webauthn, git-ssh-authentication, hardware-security-keys]
entry_points: [what does phishing resistant mean, why can't ssh keys be phished, can 2fa codes be phished, phishing proof login]
summary: >
  Why cryptographic auth defeats phishing — nothing to type, nothing to
  replay; the authenticator verifies the service before signing. The thread
  tying SSH, FIDO2, and hardware keys together.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Phishing Resistance

<!-- depth:2 -->
<!-- provenance: synthesized -->
An authentication method is **phishing-resistant** when tricking you onto a fake site gains the attacker nothing — because there is no secret to type, nothing that travels can be captured and replayed, and the authentication simply doesn't happen with the wrong service.

<!-- depth:3 -->
<!-- provenance: synthesized -->
Phishing works on anything typed. A password typed on a convincing fake site is captured whole. A one-time code is no better in the moment that matters: codes are **phishable and replayable** — an attacker who tricks you into entering one can immediately use it, live, against the real service.

Cryptographic authentication removes the raw material:

- **Git over SSH**: no passwords ever transmitted, no credentials to steal from the service's servers — phishing-resistant because *you're not typing anything*.
- **WebAuthn**: phishing-resistant *by design* — the browser and authenticator perform the exchange; there is no code for a fake page to ask you for.
- **Hardware security keys**: phishing is ineffective because *the device verifies the service before signing anything*. Point it at the wrong site and it refuses — no user vigilance required.

<!-- depth:4 -->
<!-- provenance: synthesized -->
Phishing resistance is the lateral thread running through everything signature-based, and it falls out of one structural fact rather than any anti-phishing feature:

> The server verifies **signatures, not secrets** — so no secret is ever entered, transmitted, or stored where it can be stolen.

This is what the MFA strength ladder is actually measuring at its cliff edge. Every code-based rung — email link, SMS, TOTP, enterprise tokens — leaves a human typing something an attacker can relay in real time; each rung just shrinks the window. The signature-based rungs — WebAuthn, passkeys, hardware keys — close the window entirely. Phishing doesn't get *harder*; it stops working, because the human is no longer the channel the proof travels through.

SSH had this property from the start: key-pair authentication never sends anything reusable, which is why SSH keys can't be phished the way passwords can. FIDO2 brought the same shape to the web, and hardware keys add the final piece — an authenticator that checks *who is asking* before it signs. Same cryptography, same immunity, three decades apart.
