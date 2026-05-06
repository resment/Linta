# Quickstart

```bash
pip install "linta @ git+https://github.com/resment/LLM-Wiki-Kit.git"
linta init ./SimonKnowledgeBase
```

For local development after cloning the repository, use:

```bash
pip install -e ".[dev]"
```

Create a raw source:

```bash
mkdir -p SimonKnowledgeBase/ai_kb/raw/meetings
cat > SimonKnowledgeBase/ai_kb/raw/meetings/2026-04-21_example.md <<'EOF'
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
linta manifest scan ./SimonKnowledgeBase
linta source-card create ./SimonKnowledgeBase ai_kb/raw/meetings/2026-04-21_example.md
linta prompt ingest ./SimonKnowledgeBase ai_kb/raw/meetings/2026-04-21_example.md
linta tags add ./SimonKnowledgeBase/ai_kb/wiki/source_cards/meetings__2026-04-21_example.source-card.md --tag project/example
linta index build ./SimonKnowledgeBase
linta lint ./SimonKnowledgeBase
```

Import an uploaded file:

```bash
linta raw import ./SimonKnowledgeBase ~/Downloads/uploaded.md --source-type docs
linta maintenance daily ./SimonKnowledgeBase
```

Export confirmed current pages:

```bash
linta export current ./SimonKnowledgeBase --single-file current_all.md
```

Create task context:

```bash
linta mini-kb create ./SimonKnowledgeBase --topic "Example Project" --purpose "Review prep"
```
