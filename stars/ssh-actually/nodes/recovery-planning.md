---
id: recovery-planning
title: Recovery Planning
type: concept
requires: [key-pairs]
related: [lost-hardware-key, stolen-laptop, key-rotation, resident-vs-non-resident]
entry_points: [ssh backup strategy, do I need two yubikeys, how do I not lock myself out, test recovery process]
summary: >
  Always have a path back—the two-hardware-keys rule, blob backups,
  out-of-band access, and testing recovery before you need it.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Recovery Planning

<!-- depth:2 -->
<!-- provenance: synthesized -->
Every authentication setup should be built with its own failure in mind: keys get lost, disks die, passphrases and PINs get forgotten. Recovery planning means deciding—**before** anything breaks—how you will get back in. Security you can't recover from isn't strength; it's fragility with good cryptography.

<!-- depth:3 -->
<!-- provenance: extracted -->
The critical safety rules:

1. **Always have a recovery path**
   - Second hardware key with duplicate keys, OR
   - Disk-based backup key stored securely, OR
   - Out-of-band access to servers

2. **For resident keys: two hardware keys, always**
   - Primary key for daily use
   - Backup key stored safely with duplicate resident keys

3. **Blobs aren't secrets, but their loss is permanent**
   - Back them up
   - They can't be reverse-engineered
   - But losing them means generating new keys

4. **Test your recovery process before you need it**
   - Can you regenerate stubs?
   - Can you access servers with backup key?
   - Do you know your PIN?

For disk-based keys: always use strong passphrases (20+ characters), store the passphrase in a password manager, and back up private keys to encrypted storage. For hardware keys: store the backup key safely (not with the primary), test the backup regularly, and document your recovery process.

<!-- depth:4 -->
<!-- provenance: synthesized -->
Recovery planning is the practical face of a question that runs through the whole graph: **where does authentication state live, and what happens when that place is destroyed?**

- A **disk key**'s state is a file—its recovery story is backups (encrypted) plus the ability to revoke fast when the file falls into the wrong hands.
- A **non-resident hardware key** splits state between device and blob—its recovery story is blob backups plus an accepted cost of regenerating keys if the device dies.
- A **resident key** puts all state in the device—its recovery story *must* be a duplicate device, because nothing else can reconstruct it. This is why the resident-vs-non-resident choice is really a recovery-planning choice.

The supporting hygiene compounds here: **one key per purpose** (don't reuse keys across contexts—easier to revoke when needed), **regularly audit `authorized_keys` on servers** (remove old and unknown keys), and **name keys clearly** (makes revocation easier). Each of these turns a future emergency from an investigation into a checklist. And the untested plan is the one that fails: a backup key you've never authenticated with, a blob backup you've never restored, a PIN you *think* you remember—none of those are recovery paths yet. Test them while nothing is wrong.
