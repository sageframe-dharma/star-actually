---
id: jump-host-config
title: Configuring Jump Hosts
type: procedure
requires: [proxy-jump, ssh-config-basics]
related: [config-wildcards, agent-forwarding]
entry_points: [configure a bastion in ssh config, proxyjump config example, ssh through bastion automatically]
summary: >
  The bastion pattern in ~/.ssh/config—ProxyJump blocks, wildcarded
  environment groups, transparent ssh prod-db1 through a bastion.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Configuring Jump Hosts

<!-- depth:2 -->
<!-- provenance: extracted -->
Encoding the bastion path in `~/.ssh/config` with `ProxyJump`, so SSH routes through the intermediate automatically—you type `ssh production-db` and the hop just happens, no flags.

<!-- depth:3 -->
<!-- provenance: extracted -->
The basic pattern—one block for the destination, one for the bastion it rides through:

```
Host production-db
    HostName 10.0.1.50
    User dbadmin
    ProxyJump bastion

Host bastion
    HostName bastion.company.com
    User tyro
    IdentityFile ~/.ssh/id_work
```

Connect with `ssh production-db`—SSH automatically connects through bastion.

At scale, combine `ProxyJump` with wildcards to define whole environments at once:

```
Host bastion
    HostName bastion.company.com
    User sysadmin
    IdentityFile ~/.ssh/prod_yk

Host prod-*
    ProxyJump bastion
    User admin
    IdentityFile ~/.ssh/prod_yk
    IdentitiesOnly yes

Host prod-db1
    HostName 10.0.1.10

Host prod-web1
    HostName 10.0.1.20

Host staging-*
    User admin
    IdentityFile ~/.ssh/staging
    IdentitiesOnly yes

Host staging-web1
    HostName staging.company.com
    Port 2222
```

Usage:

```bash
ssh prod-db1      # Automatically goes through bastion
ssh prod-web1     # Automatically goes through bastion
ssh staging-web1  # Direct connection, different key
```

Every `prod-*` host inherits the jump, the user, and the key from the wildcard block; the per-host blocks only carry what differs (the address). Staging gets its own key and no bastion—the pattern boundaries *are* the environment boundaries.
