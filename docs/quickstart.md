# Quickstart

```bash
pip install "linta @ git+https://github.com/resment/Linta.git"
linta init ./MyKnowledgeBase
```

For local development after cloning the repository, use:

```bash
pip install -e ".[dev]"
```

Create a raw source:

```bash
mkdir -p MyKnowledgeBase/ai_kb/raw/meetings
cat > MyKnowledgeBase/ai_kb/raw/meetings/2026-04-21_example.md <<'EOF'
---
date: 2026-04-21
type: meeting
project: Example Project
---

# Example meeting
EOF
```

Run deterministic tools:

```bash
linta manifest scan ./MyKnowledgeBase
linta source-card create ./MyKnowledgeBase ai_kb/raw/meetings/2026-04-21_example.md
linta prompt ingest ./MyKnowledgeBase ai_kb/raw/meetings/2026-04-21_example.md
linta tags add ./MyKnowledgeBase/ai_kb/wiki/source_cards/meetings__2026-04-21_example.source-card.md --tag project/example
linta index build ./MyKnowledgeBase
linta lint ./MyKnowledgeBase
```

Import an uploaded file:

```bash
linta raw import ./MyKnowledgeBase ~/Downloads/uploaded.md --source-type docs
linta maintenance daily ./MyKnowledgeBase
```

Export confirmed current pages:

```bash
linta export current ./MyKnowledgeBase --single-file current_all.md
```

Create task context:

```bash
linta mini-kb create ./MyKnowledgeBase --topic "Example Project" --purpose "Review prep"
```
