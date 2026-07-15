---
id: multiple-github-accounts
title: Multiple Accounts, One Service
type: scenario
requires: [git-ssh-authentication, host-aliases]
related: [username-trick, identities-only, key-naming]
entry_points: [two github accounts one machine, personal and work github ssh, wrong github account authenticating, git remote set-url alias]
summary: >
  The two-accounts trap—same host, same username, different keys—and the
  alias-based way out, including clone-URL changes and updating existing remotes.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Multiple Accounts, One Service

<!-- depth:2 -->
<!-- provenance: extracted -->
You have two GitHub accounts—personal and work—with one SSH key registered to each. Same hostname, same `git` username; SSH config matches on **Host**, so a single `Host github.com` block can only name one key. Whichever key it names, the other account breaks. You can't win—until you use **host aliases**.

<!-- depth:3 -->
<!-- provenance: extracted -->
Why it happens: when you run `git clone git@github.com:work-org/project.git`, SSH looks for a Host block matching `github.com`, finds one, and uses whatever key that block specifies. It does not know or care which GitHub account you mean. The only difference between your accounts is the key—but you've given SSH the same Host for both.

The solution—one alias per account, both pointing at the real hostname:

```
Host github-personal
    HostName github.com
    IdentityFile ~/.ssh/github_personal
    IdentitiesOnly yes

Host github-work
    HostName github.com
    IdentityFile ~/.ssh/github_work
    IdentitiesOnly yes
```

What changes in practice—clone URLs use the alias instead of `github.com`:

```bash
git clone git@github-personal:my-user/my-repo.git
git clone git@github-work:work-org/project.git
```

For repos you already have, update the remote:

```bash
git remote set-url origin git@github-personal:my-user/my-repo.git
git remote -v   # check the current remote
```

Test both identities:

```bash
ssh -T git@github-personal
# → Hi personal-user! You've been authenticated...

ssh -T git@github-work
# → Hi work-user! You've been authenticated...
```

If both return the correct username, the configuration is working.

<!-- depth:4 -->
<!-- provenance: synthesized -->
The fix is three ideas composing, each carrying one piece:

- **Identity comes from the key** (the `git@` username model)—that's *why* two accounts collide: nothing else in the connection distinguishes them.
- **Host is a label you control** (host aliases)—that's *how* you give SSH two different names for the same place, each bound to a different key.
- **`IdentitiesOnly yes`** in each block—that's what stops SSH from offering every key you own and letting the service accept whichever it recognizes first, which would quietly reintroduce the wrong-account problem.

GitHub never sees the alias—it only sees `github.com` and your key. This works the same for GitLab, Bitbucket, or any service where you have multiple accounts. And it's the strongest argument for naming keys by purpose: `github_personal` and `github_work` make the two blocks self-documenting; two files named `id_rsa` and `id_rsa2` do not.
