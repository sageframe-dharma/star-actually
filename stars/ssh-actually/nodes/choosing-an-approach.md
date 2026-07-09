---
id: choosing-an-approach
title: Choosing an Approach
type: concept
requires: [key-pairs]
related: [resident-vs-non-resident, hardware-keys-ssh, passphrases, first-key-setup]
entry_points: [which ssh key setup should I use, do I need a hardware key, disk key or hardware key, best ssh setup for github]
summary: >
  The decision guide: disk-based key with passphrase, hardware-backed resident,
  or hardware-backed non-resident — chosen by situation, not by maximalism.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Choosing an Approach

<!-- depth:2 -->
<!-- provenance: synthesized -->
There are three viable setups: a **disk-based key with a strong passphrase**, a **hardware-backed resident key**, and a **hardware-backed non-resident key**. Which one you want depends on your situation — how many servers, whether you already own a hardware key, how much recovery capability you need — not on reaching for the maximum.

<!-- depth:3 -->
<!-- provenance: extracted -->
If you're trying to decide what to do, start here.

### for ssh server access

```
Do you need to access servers?
│
├─ Yes, and I'm just getting started
│  → Use disk-based SSH keys with a strong passphrase
│
├─ Yes, and I want maximum security
│  → Use hardware-backed resident SSH keys
│
└─ Yes, and I manage dozens of servers
   → Use hardware-backed non-resident SSH keys
```

### for git hosting (github, gitlab, etc.)

```
Do you need to authenticate to Git services?
│
├─ Yes, and I already have a hardware key
│  → Use hardware-backed non-resident SSH keys
│     (Unlimited keys, better security)
│
├─ Yes, but I don't have a hardware key
│  → Use disk-based SSH keys with a strong passphrase
│     (Still much stronger than passwords)
│
└─ Yes, and I want the absolute strongest security
   → Get a hardware key and use non-resident keys
```

### quick recommendations by use case

| Situation                                     | Recommended Approach              | Why                                           |
| --------------------------------------------- | --------------------------------- | --------------------------------------------- |
| Personal laptop, accessing 1-2 servers        | Disk-based key with passphrase    | Simple, secure enough                         |
| Work laptop, accessing company infrastructure | Hardware-backed resident keys     | Best security, survives laptop wipes          |
| Developer using GitHub/GitLab daily           | Hardware-backed non-resident keys | Unlimited keys, no passwords ever             |
| System administrator, 20+ servers             | Hardware-backed resident keys     | Can't lose access, physical presence required |
| Learning SSH for the first time               | Disk-based key with passphrase    | Master the basics first                       |

<!-- depth:4 -->
<!-- provenance: synthesized -->
The pattern behind the trees:

- **Disk-based key with passphrase** is the answer when you're learning or when the footprint is small — one laptop, one or two servers. Simple, secure enough, and still much stronger than passwords. Master the basics first; the hardware setups make more sense once the disk-based model is familiar.
- **Hardware-backed resident keys** are the answer when losing access is the disaster you're designing against — company infrastructure, critical servers. Best security, survives laptop wipes, physical presence required. The cost: a scarce slot per key, and the obligation to keep a duplicate on a second device.
- **Hardware-backed non-resident keys** are the answer when keys multiply — git hosting, dozens of servers and services. Unlimited keys, no passwords ever. The cost: you must preserve the blob files.

Notice what the git tree assumes: if you already own a hardware key, non-resident is simply better for git hosting — there is no tradeoff to weigh there. The genuinely close call is **resident vs non-resident** for server access, and that decision surface has its own node.
