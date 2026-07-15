---
id: config-wildcards
title: Config Patterns and Wildcards
type: concept
requires: [ssh-config-basics]
related: [jump-host-config, identities-only, host-aliases]
entry_points: [ssh config wildcards, different keys for different networks, Host * defaults, which config block wins]
summary: >
  Matching semantics—wildcards, per-network blocks, Host * global defaults,
  most-specific-match wins; plus the useful-options toolbox.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Config Patterns and Wildcards

<!-- depth:2 -->
<!-- provenance: extracted -->
`Host` lines in `~/.ssh/config` are **patterns**, not just names. Wildcards enable pattern matching, the **most specific match wins**, and `Host *` sets global defaults—the config is a matching system, not a flat list.

<!-- depth:3 -->
<!-- provenance: extracted -->
Different keys for different networks:

```
Host 192.168.1.*
    IdentityFile ~/.ssh/id_home

Host 10.0.*.*
    IdentityFile ~/.ssh/id_work_yk

Host *
    IdentitiesOnly yes
    ServerAliveInterval 60
```

How it works: the most specific match wins, wildcards group machines by pattern, and `Host *` carries the defaults you want everywhere (like `IdentitiesOnly yes`).

The useful-options toolbox, by concern:

```
Host myserver
    # Connection
    HostName server.com
    Port 2222
    User username

    # Authentication
    IdentityFile ~/.ssh/key
    IdentitiesOnly yes

    # Keep-alive (prevent disconnects)
    ServerAliveInterval 60
    ServerAliveCountMax 3

    # Forwarding
    ForwardAgent yes          # Forward ssh-agent (careful!)
    LocalForward 8080 localhost:80  # Port forwarding

    # Jump hosts
    ProxyJump bastion
```

When the result surprises you, ask SSH what it actually resolved:

```bash
ssh -G hostname
```

This shows all resolved options, which config rules matched, and the final values used—the fastest way to find out *which block won*.
