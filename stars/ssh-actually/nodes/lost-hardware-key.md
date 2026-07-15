---
id: lost-hardware-key
title: Lost Hardware Key
type: scenario
requires: [resident-vs-non-resident]
related: [recovery-planning, blob, stub, managing-resident-credentials]
entry_points: [lost my yubikey, hardware key stolen what now, yubikey broke can I recover, locked out resident key]
summary: >
  The recovery playbook when the device is gone—why non-resident loss is an
  inconvenience and resident-without-backup is total lockout.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Lost Hardware Key

<!-- depth:2 -->
<!-- provenance: synthesized -->
The hardware key is gone—lost, stolen, or broken (a broken key is the same scenario as a lost one). What happens next depends entirely on one earlier decision: whether your keys were **non-resident** or **resident**, and whether you have a backup device.

<!-- depth:3 -->
<!-- provenance: extracted -->
**Non-resident keys:**

- **Risk:** Blobs are useless without hardware, but new key needed
- **Recovery:** Buy new hardware key, generate new keys, deploy to servers
- **Prevention:** Have a backup hardware key with separate keys

**Resident keys:**

- **Risk:** Total loss of access if only key
- **Recovery:** Requires out-of-band server access or recovery account
- **Prevention:** ALWAYS have a backup hardware key with duplicate resident keys

Hardware key breaks: same as lost key above. Prevention: have backup hardware key.

Related device-side dead ends worth knowing:

- **Forgot PIN**—cannot use the hardware key after limited attempts; the key locks/wipes after too many failures (usually 8 attempts). Store the PIN securely, have a backup hardware key.
- **Reached slot limit (resident keys)**—cannot create more resident keys. Delete old resident keys with `ykman fido credentials delete`; use non-resident keys for frequently-changing access.

<!-- depth:4 -->
<!-- provenance: synthesized -->
Why the asymmetry: a non-resident key's identity lives split between the device's master secret and the blob on your disk—losing the device destroys the pair, but *you still have working access to your servers through whatever other path exists*, and the recovery is mechanical: new device, new keys, redeploy. A resident key lives **only** inside the device. If that was your sole device and your sole access path, no file on any disk can bring it back—recovery is no longer a cryptographic question but an operational one (console access, a recovery account, a hosting provider's out-of-band door).

What about whoever *has* your key now? Physical possession alone is not authentication: FIDO2 operations are protected by the device's PIN, enforced in hardware with a small attempt budget before lockout—and the finder can't extract secrets from the device either. The realistic threat is not the stranger who found your key; it's your own lockout. That's why the prevention line repeats across every scenario here: **a second hardware key**—duplicate resident keys for server access, and backed-up blobs for non-resident ones. Deciding this *before* the loss is the whole content of recovery planning.
