---
id: blob
title: Blob
type: definition
requires: [non-resident-keys]
related: [stub, hardware-security-keys, key-pairs, recovery-planning]
entry_points: [blob file, sk key file, what is the file on disk for a hardware key]
summary: >
  The non-secret file on disk that a non-resident hardware key needs to
  reconstruct its private key. Not a secret—but lose it and the key is gone.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Blob

<!-- depth:2 -->
<!-- provenance: extracted -->
A **non-secret, opaque data file** stored on disk that identifies *which* key you are asking for and provides input material to the hardware key. It cannot be used without the hardware key, and cannot be reverse-engineered into a private key.

<!-- depth:3 -->
<!-- provenance: extracted -->
The blob is *not* a private key. It is more like a **recipe card** the hardware key knows how to interpret.

A non-resident key is not stored anywhere. The hardware key contains a master secret; the blob contains key-specific metadata; combined—only inside the hardware, only when authorized—they reconstruct the same private key every time. A signature is produced, and the derived key is immediately discarded. At no point does the private key exist as a file.

What this costs you: the blob **must** be preserved. Losing the blob permanently destroys access—the hardware key cannot rediscover the key on its own.

<!-- depth:4 -->
<!-- provenance: extracted -->
The blob is one half of the resident/non-resident tradeoff—its counterpart is the **stub**, the regenerable pointer file that resident keys use.

> **Non-resident keys trade discoverability for scalability.**

You gain unlimited keys, zero stored private keys, strong hardware enforcement. You accept responsibility for preserving the blob, with no recovery if it's lost. Blob loss is permanent; stub loss is five seconds of `ssh-keygen -K`.

The hardware key guarantees security. **You guarantee continuity.**
