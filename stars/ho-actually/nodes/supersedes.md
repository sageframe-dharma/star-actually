---
id: supersedes
title: supersedes
type: procedure
requires: []
related: [kamae]
entry_points: [supersedes]
summary: >
  Names exactly what a newer document overtakes; the older one keeps a pointer back, and nothing is erased.
---

<!-- depth:1 -->
<!-- provenance: extracted -->
supersedes

<!-- depth:2 -->
<!-- provenance: extracted -->
Names exactly what a newer document overtakes; the older one keeps a pointer back, and nothing is erased.

<!-- depth:3 -->
<!-- provenance: extracted -->
Frontmatter field (and body discipline) naming exactly what an artifact
overtakes — section-precise for Kamae addenda, decision-precise for hos. Supersession links
are **bidirectional**: the new document names what it supersedes, the older carries a pointer
back. The supersession is part of the record, never hidden in an edit.

<!-- depth:4 -->
<!-- provenance: extracted -->
**The Forward-Only Principle.** Closed hos stay closed. When evidence surfaces that an earlier ho's work was incomplete, wrong, or has been overtaken by what the project now knows, the response is a new ho in the current build slot — not a reopening, rewrite, or retroactive edit of the earlier one.

The earlier ho is a historical record of what was known and decided at the time. The new ho is the response to what is known now. Both are kept. The timeline reads as a sequence of honest positions, each correct for its moment, with later hos visibly responding to earlier ones.

This is the same logic as Rule 1 ("Numbers are permanent") applied to content rather than addresses. Rule 1 protects the address space; forward-only protects the record. Together they make the arc trustworthy as history: numbers don't get recycled, and conclusions don't get silently revised.

What forward-only rules out:

- Editing a closed ho's findings, scope, or deliverables to reflect later understanding.
- "Reopening" a ho to do additional work under its old number.
- Marking closed hos as failed or invalid in retrospect — they were correct given what was known.

What forward-only enables: […]

<!-- depth:5 -->
<!-- provenance: extracted -->
**How the readership knows what supersedes what.** Three links, all mandatory, so the chain is navigable from any entry point:

1. **The addendum → parent:** the `supersedes:` field plus quoted original text.
2. **The parent → addendum:** a reader's note at the top of the frozen parent naming
 each addendum and one line on what it supersedes. Sharibako kamae-2 carries
 exactly this (`superseded-in-part-by:` frontmatter list + a "Reader's note" block),
 with the body "preserved as-authored to record what was decided when." The parent
 edit is one of the narrow legitimate touches to a frozen document — it changes
 navigation, not what the document said.
3. **Downstream consumers → addendum:** hos that build on the revised decision cite
 the addendum in `builds-on:` alongside the parent (sharibako ho-03 cites kamae-2,
 2.1, and 2.2). A ho that cites only kamae-2 is declaring it predates — or is
 unaware of — the revision; tooling can flag the latter.

These three links are this document's instance of the framework-wide
**bidirectional-supersession** rule (ho-structure §3.5, merge-decisions D7): whichever
document a reader lands on — parent, addendum, or downstream ho — they can reach the
others. The parent → addendum reader's note (link 2) is the backward half the general
rule makes mandatory for every living document; it is not a courtesy specific to
addenda, and because the parent is frozen, adding it is one of the narrow legitimate
touches to a frozen document.
