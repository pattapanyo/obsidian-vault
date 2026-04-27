# CLAUDE.md — LLM Wiki Schema

**Wiki:** Karpathy LLM Wiki  
**Location:** `LLM-Wiki/` inside your Obsidian vault  
**Interface:** Claude.ai chat (claude-sonnet-4-6) — no Claude Code  
**Workflow:** Paste-and-save. You paste sources into chat → Claude returns wiki pages → you save them to Obsidian manually.

---

## Directory Structure
LLM-Wiki/
├── CLAUDE.md          ← this file (schema + instructions for Claude)
├── index.md           ← master catalog of all wiki pages
├── log.md             ← append-only chronological record
├── sources/           ← summary pages for each ingested source
├── concepts/          ← concept pages (attention, tokenization, RLHF, etc.)
├── entities/          ← people, models, papers, orgs
└── synthesis/         ← comparisons, analyses, answers worth keeping

---

## Page Types

### `sources/` — one page per ingested source
- Frontmatter: `type: source`, `date:`, `url:` (if any), `tags:`
- Sections: Summary, Key Takeaways, Connections (links to concepts/entities)

### `concepts/` — one page per concept
- Frontmatter: `type: concept`, `tags:`
- Sections: Definition, How It Works, Why It Matters, Related Concepts, Sources

### `entities/` — people, models, papers, orgs
- Frontmatter: `type: entity`, `entity-kind: person|model|paper|org`, `tags:`
- Sections: Overview, Key Contributions, Related Concepts, Sources

### `synthesis/` — generated analyses, comparisons, answers
- Frontmatter: `type: synthesis`, `date:`, `tags:`
- These are valuable query answers filed back into the wiki

---

## Wikilink Conventions

- Always link to existing pages: `[[concepts/attention]]`, `[[entities/Andrej Karpathy]]`
- Use descriptive link text: `[[concepts/attention|attention mechanism]]`
- Never leave an important concept mentioned without a link

---

## Workflows

### Ingest
When given a source (article, paper, video transcript, gist):
1. Write a `sources/` page summarizing it
2. Update or create any `concepts/` pages it touches
3. Update or create any `entities/` pages (people, models, papers)
4. Return an updated `index.md` diff (new entries to add)
5. Return a `log.md` entry to append

### Query
When asked a question:
1. Answer with citations to wiki pages
2. If the answer is substantial, offer to file it as a `synthesis/` page

### Lint
When asked to lint:
- Flag orphan pages, missing cross-links, contradictions, stale claims
- Suggest new pages for concepts mentioned but not yet written

---

## Context Rule

### Every new session — always paste:
- The full contents of `index.md` (so Claude knows what exists)

### Before ingesting a source — also paste:
Any wiki pages the source is likely to touch. Use the index to identify them. Ask yourself:
- What concepts does this source explain or reference?
- What people, models, or papers does it mention?
- Does it contradict or extend anything already in the wiki?

Then paste those pages into the same message as the source.

### Example session opening:
Here's my index.md:
[paste index.md]
I want to ingest this source:
[paste source]
Relevant existing pages to update:
[paste concepts/attention.md]
[paste entities/Andrej Karpathy.md]

### What Claude can do with this context:
- Extend existing pages intelligently without repeating what's already there
- Flag contradictions between the new source and existing content
- Add cross-links that reference real existing content, not guesses
- Return updated versions of only the pages that changed

### What Claude cannot do:
- Read pages you didn't paste — the index gives names, not content
- Access your vault directly — you are the file system

---

## Log Format

Every log entry uses this prefix for parseability:

Operations: `ingest`, `query`, `synthesis`, `lint`

---

## Notes

- Raw sources are immutable — Claude reads them, never modifies them
- The wiki compiles knowledge once and keeps it current
- You (the human) curate sources and ask questions; Claude does the bookkeeping
- When in doubt, create a new page rather than cramming into an existing one