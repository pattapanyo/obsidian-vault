# Copilot instructions for this Obsidian vault

Purpose
- Provide concise, actionable guidance for Copilot-style assistants working with this repository (an Obsidian vault of notes about storytelling).

Build / test / lint
- Not an application repo: no build, test, or lint commands exist. There is no test runner here. Treat all files as content (Markdown).

High-level architecture (big picture)
- Root contents are an Obsidian vault: a mix of content and Obsidian config (.obsidian/).
- Primary content area: Storytelling/
  - index.md — master catalog (links + one-line summaries for each page)
  - log.md — append-only chronological log of changes and ingest actions
  - sources/ — raw source notes (one source per file; e.g., articles, scripts)
  - concepts/ — theories, techniques, structural tools (e.g., three-act)
  - entities/ — people and creative works (directors, films, authors)
  - synthesis/ — high-level comparisons and synthesized analyses
- Other: .obsidian/ (editor state/settings), .trash/ (removed notes), .GitHub/ (local assistant guidance in Storytelling).

Key conventions and rules (repo-specific)
- Filing protocol
  - sources/ → raw notes extracted from a single source
  - concepts/ → theory or technique pages
  - entities/ → bios, film pages, people
  - synthesis/ → comparative analyses and long-form syntheses
- Index and log
  - index.md: Update whenever a new page is added; include a one-line summary and a link (Obsidian style [[Page Name]]).
  - log.md: Append-only; every ingest or major edit gets a timestamped entry (use YYYY-MM-DD headings when appropriate).
- Links and citations
  - Use Obsidian-style links: [[Note Name]] (these are primary navigation and citation forms)
  - When answering queries, prefer citing internal pages (e.g., "See [[Three-Act Structure]]")
- Frontmatter and metadata
  - Pages should include YAML frontmatter with at least: tags, date, source_type (when applicable).
- Content style
  - High signal density: use concise bullet points and structured sections; avoid conversational fluff in canonical pages.
- Linting/health checks (operational tasks for assistants)
  - Flag orphan pages (no inbound links)
  - Flag contradictions between pages and suggest merges or clarifications
  - Suggest new pages for recurring but undefined terms

Assistant operational workflows (copied/adapted from Storytelling/.GitHub)
- Ingest workflow
  - Create a source page under sources/ with comprehensive notes
  - Update relevant concepts/ and entities/ pages based on the source
  - Add a one-line entry to index.md and append a timestamped note in log.md
- Query workflow
  - Answer with internal citations ([[Page Name]]) when possible
  - If the response is substantial, offer to file it as a new synthesis/ page
- Periodic lint workflow
  - Run the checks in "Linting/health checks" and output suggested fixes

Repository-specific files to be aware of
- Storytelling/.GitHub/copilot-instructions.md — local variant of these instructions; incorporated above.
- .obsidian/ — editor metadata; do not treat workspace files as canonical content when producing summaries (but respect vault settings like graph/links).

If you want adjustments: ask to add more examples (ingest-to-file flow, frontmatter template, or specific citation patterns).

## Mode Triggers
- If I start a prompt with "STORYBEAT:", act as a structuralist (focus on plot, pacing, and mechanics).
- If I start a prompt with "INTERNALITY:", act as a psychologist (focus on character depth, subtext, and theme).
- If I start a prompt with "LINT:", act as a strict librarian (focus on links and errors).

<system_reminder>
<sql_tables>Available tables: todos, todo_deps, inbox_entries</sql_tables>
</system_reminder>
