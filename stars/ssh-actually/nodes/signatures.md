---
id: signatures
title: Signatures
type: concept
requires: [key-pairs]
related: [fido2, hardware-security-keys, known-hosts]
entry_points: [what is a cryptographic signature, how does ssh prove identity, challenge response, how does the server verify me]
summary: >
  The challenge–sign–verify flow—proof of possession that never reveals the
  secret. The missing piece that makes key pairs usable.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Signatures

<!-- depth:2 -->
<!-- provenance: extracted -->
A **signature** is a cryptographic proof created with a private key that:

- proves possession of the private key
- proves the message was not altered
- does **not** reveal the private key

<!-- depth:3 -->
<!-- provenance: extracted -->
In SSH:

1. The server sends a challenge
2. Your client signs it
3. The server verifies the signature using your public key

If it verifies → access granted.

That's the whole authentication. No secret travels; only the proof does.

<!-- depth:4 -->
<!-- provenance: synthesized -->
Challenge–sign–verify is the one flow that repeats everywhere key-pair cryptography shows up:

- **Hardware security keys** run the same flow with the signing moved inside the device. The computer asks: *"Please sign this challenge."* The hardware responds: *"Here is a proof I signed it."* The secret never leaves the hardware—only the signature does.
- **FIDO2** brought the same shift to the web: the service verifies a *signature*, not a secret.
- **Agent forwarding** is this flow stretched across machines—the challenge travels back to your local agent for signing, and the signature travels forward.
- **Known hosts** is the same verification pointed the other way: the server proves *its* identity to you, and your client checks the proof against a stored fingerprint.

Once you can see the challenge and the signature in each of these, none of them is a new idea—just a new place to stand.

<!-- depth:5 -->
<!-- provenance: extracted -->
The full flow, as a picture:

```text
Client (has private key)              Server (has public key)
        │                                     │
        │◀── challenge: "prove you have ──────│
        │        the key"                     │
        │                                     │
   signs challenge with                       │
   private key                                │
        │                                     │
        │──── signature (proof) ─────────────▶│
        │                                     │
        │                          verifies signature
        │                          with public key
        │                                     │
        │◀── ✓ access granted ────────────────│
        │    (✗ denied if invalid)            │
```

**The private key NEVER travels over the network.** The server verifies the signature using your public key, but never sees your private key.

What a signature proves, stated fully: a specific secret exists, and the holder of that secret approved *this exact action*. That second half matters—a signature is bound to the challenge it signed, so it can't be replayed against a different one.
