---
id: stub
title: Stub
type: definition
requires: [resident-keys]
related: [blob, new-machine-setup, hardware-keys-ssh]
entry_points: [what is a stub file, ssh-keygen -K, regenerate ssh key files, deleted my sk key file]
summary: >
  The regenerable pointer — a small non-secret file that tells SSH which
  resident key to use. Delete it freely; regenerate anywhere with ssh-keygen -K.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Stub

<!-- depth:2 -->
<!-- provenance: extracted -->
A **small, non-secret local file** that tells SSH *which resident key to use*. It contains no private material, can be safely deleted, and can be regenerated on any machine. A stub is a **pointer**, not a dependency.

<!-- depth:3 -->
<!-- provenance: extracted -->
With a resident key, the hardware stores the private key and the key's identity; the computer stores **nothing essential**. The stub simply tells SSH which resident key to ask the hardware for.

Regenerate stubs on any machine:

```bash
ssh-keygen -K
```

This scans the hardware key for resident credentials and creates stub files in the current directory — move them to `~/.ssh/` afterward. Use it on a fresh machine, after accidentally deleting stub files, or when migrating to a new computer.

What loss means: a minor inconvenience only. Stub loss is five seconds of `ssh-keygen -K`. Compare the **blob** — the file a *non-resident* key depends on — whose loss is permanent. Both are non-secret and both are useless to a thief without the hardware; only the stub is regenerable. Backing up stubs is pointless — just regenerate.
