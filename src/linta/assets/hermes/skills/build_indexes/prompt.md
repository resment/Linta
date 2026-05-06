# Build Indexes

Build deterministic machine-readable indexes for an Linta knowledge base.

Commands:

```bash
linta lint <kb_root>
linta index build <kb_root>
```

Rules:

- Do not modify `ai_kb/raw/`.
- Treat `ai_kb/wiki/indexes/` as derived output.
- Use `--dry-run` first when the user asks for a preview.
- Report lint findings instead of hiding them.

Output index files written, lint findings, and human review notes.
