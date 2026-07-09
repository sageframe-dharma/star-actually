<!-- DRAFT — your story, your voice. Edit freely. Live URLs assume production at
     star-actually.sageframe.net/ssh-actually/ (subdir model) — confirm the domain. -->

# SSH, Actually

**The one that started it all.**

I wanted to learn SSH. Not the eight million ways the internet explains SSH — the
key-exchange diagrams, the RFC cosplay, the fourteen-tab Stack Overflow spelunk. I
wanted to know how to *actually use it*. What to type, why, and what's really
happening when I do.

So I wrote it up the way I'd want it told to me — plain language, no
throat-clearing. And then I wanted *more*. The why under the how. The connections.
The deep end — on demand, when **I** got curious, not dumped on me up front.

There wasn't a thing that did that. So I built one. **SSH, Actually** was born.

The name is a wink at the htmx crowd's deadpan house line — *"htmx, actually"* — the
answer to every over-engineered stack. Same energy: build the simple thing that
respects how people actually work, and let it be enough.

## The idea, in one breath

Documentation is organized around *products*. Learning is organized around
*questions*. So you land on a term, get the plain version, and if you're curious
you **dial deeper** — definition → how you use it → how it connects → the theory —
and you stop the second the itch is scratched. Nothing dumped up front. That's the
whole trick, and it's not a gimmick: [curiosity is a gap you can see and close on
your own terms](https://doi.org/10.1037/0033-2909.116.1.75).

Fully static. Terminal aesthetic. One small file of readable JavaScript, htmx
vendored, no framework, no tracking, no cookie banner apologizing for itself. A
love letter to the early web, when a hyperlinked document was a revelation and
nobody had figured out how to ruin it yet.

**→ Read it live: [ssh, actually](https://star-actually.sageframe.net/ssh-actually/)**

## About this repo

This is the **original text, archived** — where SSH, Actually was first written,
and the full build record behind it (`guide/`, `nodes/`, `ho-process/`). The live
site is regenerated from here. Things out in the world link to this repo, so it
stays put. Consider it the OG.

## Roll your own

SSH, Actually isn't special — it's an *instance*. It runs on a domain-blind engine,
**[`*, Actually` / star-actually](https://github.com/sageframe-no-kaji/star-actually)**,
that weaves depth-layered markdown into a navigable static site. The engine never
knows the subject: you hand it `nodes/` + a `site.yaml`, and it builds.

Which means anything with a shape — a glossary, a manual, a body of hard-won
knowledge you're tired of explaining the same way twice — can become a
`*, Actually`. The asterisk is a glob for a reason.

## Or don't — I'll make one for you

Genuinely: if there's a subject you wish existed like this, don't sweat the tooling.
**Tell me what it is, why it itches, and send me your content** —
[atmarcus@gmail.com](mailto:atmarcus@gmail.com) — and I'll build you your own
`*, Actually`. Not a funnel. I just want more of these in the world.

## Licensing

Two licenses, deliberately. **Code** is [MIT](LICENSE). **Content** — the guide and
the authored nodes — is [CC BY-ND 4.0](LICENSE-CONTENT): read it, share it, use it
commercially; don't publish altered versions. Attribution: **Andrew T Marcus**,
linking here.

## Author

**Andrew T. Marcus** (Cambridge, Massachusetts) — systems designer, author of the
[Ho System](https://github.com/sageframe-no-kaji/ho-system). This exists because SSH
was needlessly confusing, the docs assumed too much, and the fix for
badly-structured knowledge isn't a better document — it's a better *structure*.
