# Manage Obsidian Tags

Use Linta deterministic tag commands for Obsidian-readable Markdown tags.

Commands:

```bash
linta tags list <md_path>
linta tags add <md_path> --tag project/example --tag status/draft
linta tags set <md_path> --tag project/example --tag capability/review
linta prompt tag <kb_root> <md_path>
```

Rules:

- Do not modify `ai_kb/raw/`.
- Use the managed `linta-tags` block.
- Normalize tags to lowercase kebab-case.
- Prefer namespaces: `#project/...`, `#domain/...`, `#capability/...`, `#concept/...`, `#status/...`, `#type/...`.
- Run `linta lint <kb_root>` after writes when practical.

Output changed files, recommended tags, and human review notes.
