---
id: agent-forwarding
title: Agent Forwarding
type: concept
requires: [ssh-agents, key-pairs, ssh-config-basics]
related: [proxy-jump, trust-boundaries, hardware-keys-ssh]
entry_points: [ssh forwarding, forward agent, multi-hop ssh, ssh from server to server]
summary: >
  Let a remote server request signatures from your local SSH agent—convenient,
  and dangerous in a very specific way.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
Agent Forwarding

<!-- depth:2 -->
<!-- provenance: extracted -->
A feature that lets a remote server request signatures from the SSH agent running on your local machine—without copying the private key to that server.

<!-- depth:3 -->
<!-- provenance: extracted -->
You SSH from your laptop to Server A. From Server A, you need to SSH to Server B. Server B trusts your key—but your key is on your laptop, not on Server A.

With agent forwarding enabled, Server A sends the authentication challenge **back through the SSH connection** to your laptop. Your laptop's agent signs it, the signature travels back through Server A to Server B, and Server B grants access. The private key **never leaves your laptop**.

Why it's useful: one key, multiple hops, no private keys copied to servers, feels transparent.

Why it's dangerous: while you are connected with forwarding enabled, **anyone with root on Server A can use your agent**. They cannot steal the key—it never arrives. But they can ask your agent to sign things. Any things. Silently, for as long as your session is open.

<!-- depth:4 -->
<!-- provenance: synthesized -->
Agent forwarding is one of three answers to the same problem, and understanding it means seeing all three:

- **Copy your private key to Server A**—don't. The key now exists on two machines, and everyone with root on Server A can copy it. Multiplied attack surface, zero gain.
- **Agent forwarding**—the key stays home, but its *power* travels. Server A can't steal the key; it can *use* it, against any server that trusts you, for the duration of the session.
- **ProxyJump**—the intermediate becomes a dumb network relay. It never sees your key, never talks to your agent, cannot sign as you. This is almost always the better answer.

The decision hinges on one question: **do you trust the intermediate machine with the power to act as you?** Your own homelab, briefly—maybe. Shared infrastructure, cloud hosts, anything you don't fully control—no. Hardware keys tilt the answer further: forwarding behavior with hardware-backed keys varies and can be unreliable, while ProxyJump works cleanly.

<!-- depth:5 -->
<!-- provenance: extracted -->
The documented, intended behavior—not a vulnerability:

1. You SSH to Server A with agent forwarding enabled (`ForwardAgent yes` or `ssh -A`)
2. Server A needs to authenticate to Server B
3. Server A sends the challenge back through the SSH connection to your laptop
4. Your laptop's agent signs the challenge
5. The signature goes back to Server A → Server B
6. Server B grants access

> Agent forwarding does not give Server A your key. It gives Server A **access to your key's power** for the duration of your session.

The distinction matters. The key cannot be stolen. But it can be **used**—by anyone with root on the intermediate, against anything your key unlocks, without your knowledge.

When it's acceptable (rarely): you own all machines in the chain, you trust the intermediate completely, the session is short-lived, and you understand the risk. Enable per-host only:

```
Host trusted-server
    ForwardAgent yes
```

**Never enable `ForwardAgent yes` globally.**

The mental model: agent forwarding is handing someone your car keys through a window. They can't duplicate them, but they can drive anywhere until you take them back. ProxyJump is asking someone to open a gate—they open it, you drive through yourself, they never touch your keys.
