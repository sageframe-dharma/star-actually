---
id: host-aliases
title: Host Aliases
type: concept
requires: [ssh-config-basics]
related: [username-trick, multiple-github-accounts, config-wildcards]
entry_points: [ssh host alias, host vs hostname ssh config, can host be a made-up name, nickname for ssh server]
summary: >
  Host is a label you control, HostName is where the connection goes — SSH
  config as named connection instructions, not a hostname routing table.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Host Aliases

<!-- depth:2 -->
<!-- provenance: extracted -->
In SSH config, `Host` is a **nickname** and `HostName` is the **actual address**. They don't have to match. A host alias is a Host name you invent — it connects wherever its `HostName` says.

<!-- depth:3 -->
<!-- provenance: extracted -->
An alias block looks like any other config block — the only trick is that the label is made up:

```
Host github-personal
    HostName github.com
    IdentityFile ~/.ssh/github_personal
    IdentitiesOnly yes
```

Connecting with `ssh github-personal` — or a git URL like `git@github-personal:my-user/my-repo.git` — still reaches `github.com`; that's what `HostName` handles. But SSH matched the block by the alias you typed, so it presents the key *that block* names.

The service never sees the alias. It only sees the `HostName` you connected to and the key you presented. The alias exists purely on your machine, in your config.

<!-- depth:4 -->
<!-- provenance: extracted -->
The mental model: SSH config is not a routing table for hostnames. It is a **named set of connection instructions**. The Host name is whatever you want it to be. The HostName is where the connection actually goes.

Once you see Host as a **label you control** rather than a hostname you must match, multi-identity SSH stops being confusing. You're just giving SSH different names for different ways of reaching the same place — which is exactly what solves the multiple-accounts-on-one-service problem: same hostname, same username, different keys, distinguished only by which alias you typed.
