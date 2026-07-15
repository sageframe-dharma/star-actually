---
id: identities-only
title: IdentitiesOnly
type: definition
requires: [ssh-config-basics]
related: [multiple-github-accounts, ssh-debugging, config-wildcards]
entry_points: [what does identitiesonly do, too many authentication failures, ssh tries wrong key]
summary: >
  Force SSH to present only the keys you named—prevents SSH trying every key
  you own and the "too many authentication failures" it causes.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
IdentitiesOnly

<!-- depth:2 -->
<!-- provenance: extracted -->
An SSH config option that forces SSH to use **only the identities explicitly listed**—the keys named in `IdentityFile`—instead of trying every key you have.

<!-- depth:3 -->
<!-- provenance: extracted -->
Without it, SSH offers your keys one after another until something works. Servers count each offered key as an authentication attempt, and once you own a handful of keys you start hitting **"too many authentication failures"** before the right key is ever tried.

Pair it with `IdentityFile` in any block where the key matters:

```
Host github.com
    IdentityFile ~/.ssh/id_github_yk
    IdentitiesOnly yes
```

Best practice—set it globally, so *every* connection presents only what you deliberately configured:

```
Host *
    IdentitiesOnly yes
```

The payoff: the correct key is always used, and fewer authentication failures. If a connection still picks a key you didn't expect, `ssh -G hostname` shows which config rules matched and what SSH actually resolved.
