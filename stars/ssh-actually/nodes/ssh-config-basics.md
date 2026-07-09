---
id: ssh-config-basics
title: SSH Config Basics
type: concept
requires: [what-ssh-is]
related: [identities-only, config-wildcards, host-aliases, first-key-setup]
entry_points: [what is ssh config, how to set up ~/.ssh/config, stop typing ssh flags, ssh nickname for server]
summary: >
  ~/.ssh/config as named connection instructions — Host, HostName, User, Port,
  IdentityFile — turning flag soup into `ssh myserver`.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
SSH Config Basics

<!-- depth:2 -->
<!-- provenance: extracted -->
`~/.ssh/config` is a **named set of connection instructions** — not a routing table for hostnames. Each block gives a nickname to a full set of connection details, so `ssh myserver` replaces a command line full of flags.

<!-- depth:3 -->
<!-- provenance: extracted -->
The basic structure:

```
Host nickname
    HostName actual-server.com
    User remote-username
    Port 2222
    IdentityFile ~/.ssh/specific_key
    IdentitiesOnly yes
```

The fields:

- `Host` — what you type: `ssh nickname`
- `HostName` — real address (DNS or IP)
- `User` — remote username (defaults to your local username)
- `Port` — SSH port (defaults to 22)
- `IdentityFile` — which key to use
- `IdentitiesOnly yes` — only try the specified keys

The before/after is the whole sales pitch. Without config:

```bash
ssh -i ~/.ssh/id_work_yk -p 2222 tyro@work-server.company.com
```

With config: `ssh work`. Short memorable names, the correct key always used, port and username remembered — and git operations against configured hosts just work.

<!-- depth:4 -->
<!-- provenance: synthesized -->
Three consequences follow from "named instructions, not a routing table":

- **Host is a label you control.** It doesn't have to match the real hostname — `HostName` handles that. This is what makes **host aliases** possible: two different names, two different keys, one actual server. Multi-account Git setups depend on it.
- **Blocks compose by pattern.** Wildcards (`Host 192.168.1.*`, `Host *`) let you set per-network keys and global defaults, with the most specific match winning.
- **`IdentitiesOnly` keeps SSH honest.** Without it, SSH may try every key you own — leaking which keys you hold and tripping "too many authentication failures." With it, each block presents exactly the key you named.

When the resolved behavior surprises you, ask SSH itself: `ssh -G hostname` prints every option as finally resolved — which config rules matched and what values won.
