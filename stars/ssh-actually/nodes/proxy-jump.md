---
id: proxy-jump
title: ProxyJump
type: concept
requires: [ssh-config-basics]
related: [agent-forwarding, jump-host-config, trust-boundaries]
entry_points: [what is proxyjump, ssh -J, ssh through a jump host safely, proxyjump vs agent forwarding]
summary: >
  Route through an intermediate as a dumb TCP relay—it never sees your key,
  never talks to your agent, cannot act as you. The better answer to multi-hop.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
ProxyJump

<!-- depth:2 -->
<!-- provenance: extracted -->
An SSH feature that routes your connection through an intermediate server **without giving that server access to your agent**—the intermediate opens a TCP tunnel, and your client authenticates directly with the destination through it. The secure alternative to agent forwarding for multi-hop SSH.

<!-- depth:3 -->
<!-- provenance: extracted -->
On the command line:

```bash
ssh -J jumphost user@destination
```

Or in `~/.ssh/config`:

```
Host destination
    HostName 10.0.0.5
    User admin
    ProxyJump jumphost
```

How it works:

1. SSH opens a connection to the jump host
2. The jump host opens a **TCP tunnel** to the destination
3. Your SSH client authenticates **directly** with the destination through the tunnel
4. The jump host sees encrypted traffic—nothing else

The jump host never sees your key, never talks to your agent, cannot use your credentials. It is just a network relay.

<!-- depth:4 -->
<!-- provenance: extracted -->
ProxyJump is the third of three answers to "my key is on my laptop but I need to hop through a machine"—the other two being *copy the key to the intermediate* (don't) and *agent forwarding* (the key stays home but its power travels). The comparison:

| Feature                        | Agent Forwarding | ProxyJump |
| ------------------------------ | ---------------- | --------- |
| Key leaves laptop              | No               | No        |
| Intermediate can sign as you   | **Yes**          | No        |
| Requires trust in intermediate | **Yes**          | No        |
| Config complexity              | Low              | Low       |
| Works with hardware keys       | Partially        | **Yes**   |

When to use ProxyJump instead of forwarding: **almost always**. Especially any server you don't fully control, any multi-hop path through shared infrastructure, any cloud or work environment—and any time hardware keys are involved, because agent forwarding behavior with hardware keys varies and can be unreliable while ProxyJump works cleanly.

<!-- depth:5 -->
<!-- provenance: synthesized -->
What "just a network relay" actually buys you.

The tunnel carries a second, fully encrypted SSH connection—client to destination, end to end. The destination's authentication challenge travels through the jump host as ciphertext and is answered by *your local client*, so the cryptographic conversation has no party in the middle. There is nothing for the intermediate to steal (it never sees key material) and nothing for it to borrow (it never gets a channel to your agent, so it cannot ask for signatures the way a forwarding-enabled intermediate can).

That collapses the trust question. With agent forwarding, you must trust the intermediate with **the power to act as you**—anyone with root there can sign as you for the life of your session. With ProxyJump, the worst a hostile jump host can do is refuse to carry your traffic. Compromising it gets an attacker a view of encrypted bytes, not an identity.

This is also why hardware-backed keys and ProxyJump pair so well: the signing happens where it always does—between your local client and your device, touch and PIN included. No remote machine ever needs to talk to your agent or your hardware, so nothing about the hop changes the ceremony.

The design lesson generalizes: when a path must cross a machine you don't control, prefer the option that hands that machine **packets** over any option that hands it **authority**.
