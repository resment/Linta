import os
import subprocess
import sys
from pathlib import Path
from tomllib import loads

from scripts.validate_example import validate_example

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_project_metadata_is_release_ready() -> None:
    metadata = loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    project = metadata["project"]

    assert project["name"] == "llm-wiki-kit"
    assert project["version"] == "0.1.0"
    assert project["requires-python"] == ">=3.11"
    assert "llm-wiki" in project["scripts"]
    assert "Homepage" in project["urls"]


def test_manifest_includes_public_assets() -> None:
    manifest = (REPO_ROOT / "MANIFEST.in").read_text(encoding="utf-8")
    metadata = loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert "README_CN.md" in manifest
    assert "recursive-include docs *.md" in manifest
    assert "recursive-include templates *.md" in manifest
    assert "recursive-include hermes *.md *.sh" in manifest
    assert "recursive-include examples *.md" in manifest
    assert "assets/hermes/skills/*/*.md" in metadata["tool"]["setuptools"]["package-data"][
        "llm_wiki_kit"
    ]


def test_readmes_and_roadmap_are_phase5_current() -> None:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    readme_cn = (REPO_ROOT / "README_CN.md").read_text(encoding="utf-8")
    roadmap = (REPO_ROOT / "ROADMAP.md").read_text(encoding="utf-8")

    assert "Phase 5" in readme
    assert "Phase 5" in readme_cn
    assert "Phase 5" in roadmap
    assert "No built-in LLM API calls" in roadmap


def test_product_knowledge_ops_example_validates() -> None:
    errors = validate_example(REPO_ROOT / "examples/product-knowledge-ops")

    assert errors == []


def test_module_entrypoint_help() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    result = subprocess.run(
        [sys.executable, "-m", "llm_wiki_kit", "--help"],
        cwd=REPO_ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0
    assert "Usage:" in result.stdout
    assert "hermes" in result.stdout
