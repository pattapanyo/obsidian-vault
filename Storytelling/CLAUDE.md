# CLAUDE.md — Storytelling Wiki Schema

**Wiki:** Storytelling Wiki — Screenwriting & Film  
**Location:** `Storytelling/` inside your Obsidian vault  
**Interface:** Claude.ai chat — no Claude Code  
**Workflow:** Paste sources into chat → Claude returns wiki pages → save manually to Obsidian.

---

## Directory Structure
Storytelling/
├── CLAUDE.md          ← schema + instructions for Claude
├── index.md           ← master catalog of all wiki pages
├── log.md             ← append-only chronological record
├── sources/           ← one page per ingested source (book, article, film, lecture)
├── concepts/          ← structural tools, terms, techniques
├── entities/          ← writers, directors, films, books
└── synthesis/         ← comparisons, analyses, answers worth keeping

---

## Page Types

### `sources/` — one page per ingested source
- Frontmatter: `type: source`, `date:`, `url:` (if any), `tags:`
- Sections: Summary, Key Takeaways, Connections

### `concepts/` — one page per craft concept
- Frontmatter: `type: concept`, `tags:`
- Sections: Definition, How It Works, Why It Matters, Examples (films), Related Concepts, Sources

### `entities/` — writers, directors, films, books
- Frontmatter: `type: entity`, `entity-kind: person|film|book|org`, `tags:`
- Sections: Overview, Key Contributions, Related Concepts, Sources

### `synthesis/` — generated analyses, comparisons, answers
- Frontmatter: `type: synthesis`, `date:`, `tags:`
- File valuable query answers here so explorations compound

---

## Wikilink Conventions

- Always link to existing pages: `[[concepts/three-act-structure]]`
- Use descriptive link text: `[[concepts/three-act-structure|three-act structure]]`
- Never leave an important concept mentioned without a link

---

## Workflows

### Ingest
When given a source:
1. Write a `sources/` page
2. Update or create relevant `concepts/` pages
3. Update or create relevant `entities/` pages
4. Return new `index.md` entries to add
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
- The full contents of `index.md`

### Before ingesting a source — also paste:
Any wiki pages the source is likely to touch. Ask yourself:
- What concepts does this source explain or reference?
- What writers, directors, or films does it mention?
- Does it contradict or extend anything already in the wiki?

### Example session opening:

Here's my index.md:
[paste index.md]
I want to ingest this source:
[paste source]
Relevant existing pages to update:
[paste concepts/three-act-structure.md]

### What Claude can do with this context:
- Extend existing pages without repeating what's already there
- Flag contradictions between new source and existing content
- Return updated versions of only the pages that changed

### What Claude cannot do:
- Read pages you didn't paste
- Access your vault directly — you are the file system

---

## Log Format

[YYYY-MM-DD] operation | title

Operations: `ingest`, `query`, `synthesis`, `lint`