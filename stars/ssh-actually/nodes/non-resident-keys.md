---
id: non-resident-keys
title: Non-Resident SSH Keys
type: concept
requires: [hardware-keys-ssh, state]
related: [blob, resident-keys, hardware-key-setup-nonresident]
entry_points: [what is a non-resident key, where is my sk key stored, "the key isn't on the hardware?", unlimited hardware ssh keys]
summary: >
  The key that is stored nowhere — derived on demand inside the hardware from
  master secret plus blob; unlimited keys, but you must preserve the blob.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Non-Resident SSH Keys

<!-- depth:2 -->
<!-- provenance: extracted -->
A **non-resident SSH key** is a hardware-backed SSH key where the hardware key does not store the key's identity, does not remember the key exists, and the private key is **never stored anywhere — not on disk, not on the hardware**. Instead, the private key is **derived on demand** by the hardware key using a file called a blob.

<!-- depth:3 -->
<!-- provenance: extracted -->
The confusion usually comes from the phrase *"the key isn't stored on the hardware."* That's true — but incomplete. A non-resident key is **not stored** anywhere. Instead:

- the hardware key contains a **master secret**
- the blob (a non-secret, opaque file on disk) contains **key-specific metadata**
- the hardware key combines its internal master secret with the blob to **reconstruct the same private key every time**

This happens **only inside the hardware**, and only when authorized. The blob is not a private key — it is more like a **recipe card** the hardware key knows how to interpret. It cannot be used without the hardware, and cannot be reverse-engineered into a private key.

<!-- depth:4 -->
<!-- provenance: extracted -->
Properties:

- ✔ unlimited number of keys
- ✔ same cryptographic strength as resident keys
- ✔ private key never stored anywhere
- ❌ blob **must** be preserved
- ❌ losing the blob permanently destroys access
- ❌ hardware key cannot rediscover the key on its own

The contrast with the resident model is the whole decision: a **resident key** stores the key inside the hardware, consuming a scarce slot, and survives disk loss; a non-resident key consumes no slots — you can have as many as you like — but the blob on disk becomes state *you* are responsible for. Lose the hardware key alone and the blobs are useless to the thief; lose the blob and even *you* can't get the key back.

Best use: GitHub, GitLab, and other multi-service situations — places where you want many keys and re-registering a new public key is cheap.

<!-- depth:5 -->
<!-- provenance: extracted -->
The authentication flow:

```text
Client → Blob → Hardware Key → Signature → Server
```

Step-by-step:

1. SSH asks to authenticate
2. The client provides the blob
3. The hardware key uses its internal secret plus the blob
4. The private key is **derived temporarily**
5. A signature is produced
6. The private key is immediately discarded

At no point does the private key exist as a file. The blob is required every time.

The key insight:

> **Non-resident keys trade discoverability for scalability.**

You gain unlimited keys, zero stored private keys, and strong hardware enforcement. You accept responsibility for preserving the blob, with no recovery if it is lost.

The hardware key guarantees security. **You guarantee continuity.**
