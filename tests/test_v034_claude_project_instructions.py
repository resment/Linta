import json
from pathlib import Path

from typer.testing import CliRunner

from linta.agent_access import configure_agent_access
from linta.claude_desktop import build_claude_project_instructions
from linta.cli import app
from linta.init_kb import init_knowledge_base
from linta.mcp_server import PRACTICAL_CONTEXT_TOOLS

runner = CliRunner()


def test_project_instructions_include_tools_boundary_and_path(tmp_path: Path) -> None:
    kb = tmp_path / "kb"
    init_knowledge_base(kb)

    instructions = build_claude_project_instructions(kb)

    assert kb.resolve().as_posix() in instructions.instructions
    for tool in PRACTICAL_CONTEXT_TOOLS:
        assert tool in instructions.instructions
    assert "ai_kb/raw" in instructions.instructions
    assert "Do not request or read" in instructions.instructions
    assert "ai_kb/wiki/source_cards" in instructions.instructions


def test_cli_project_instructions_json(tmp_path: Path) -> None:
    kb = tmp_path / "kb"
    init_knowledge_base(kb)

    result = runner.invoke(app, ["claude-desktop", "project-instructions", str(kb), "--json"])

    assert result.exit_code == 0, result.output
    payload = json.loads(result.output)
    assert payload["kb_root"] == kb.resolve().as_posix()
    assert payload["tools"] == list(PRACTICAL_CONTEXT_TOOLS)
    assert "ai_kb/raw" in payload["read_boundary"]
    assert "context_overview" in payload["recommended_first_prompt"]


def test_claude_status_reports_project_instructions(tmp_path: Path) -> None:
    kb = tmp_path / "kb"
    init_knowledge_base(kb)
    configure_agent_access(kb, primary_agent="hermes")

    json_result = runner.invoke(app, ["claude-desktop", "status", str(kb), "--json"])
    text_result = runner.invoke(app, ["claude-desktop", "status", str(kb)])

    assert json_result.exit_code == 0, json_result.output
    assert json.loads(json_result.output)["project_instructions_available"] is True
    assert text_result.exit_code == 0, text_result.output
    assert "project-instructions" in text_result.output
