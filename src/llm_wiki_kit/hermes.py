"""Optional Hermes skill installation."""

from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from importlib.resources import files
from pathlib import Path

DEFAULT_HERMES_SKILL_TARGET = Path.home() / ".hermes/skills/llm-wiki-kit"


@dataclass
class HermesInstallResult:
    """Result of a Hermes skill installation run."""

    target: Path
    dry_run: bool
    copied: list[Path] = field(default_factory=list)
    skipped: list[Path] = field(default_factory=list)


def install_skills(
    *,
    target: Path | None = None,
    dry_run: bool = False,
    force: bool = False,
) -> HermesInstallResult:
    """Install bundled Hermes skills into a target directory."""

    source_root = hermes_skills_root()
    destination_root = (target or DEFAULT_HERMES_SKILL_TARGET).expanduser().resolve()
    result = HermesInstallResult(target=destination_root, dry_run=dry_run)

    for source_skill in sorted(path for path in source_root.iterdir() if path.is_dir()):
        destination_skill = destination_root / source_skill.name
        if destination_skill.exists() and not force:
            result.skipped.append(destination_skill)
            continue
        result.copied.append(destination_skill)
        if dry_run:
            continue
        destination_root.mkdir(parents=True, exist_ok=True)
        if destination_skill.exists():
            shutil.rmtree(destination_skill)
        shutil.copytree(source_skill, destination_skill)

    return result


def hermes_skills_root() -> Path:
    """Return bundled Hermes skills from source checkout or installed package data."""

    repo_skills = Path(__file__).resolve().parents[2] / "hermes/skills"
    if repo_skills.exists():
        return repo_skills
    return Path(str(files("llm_wiki_kit") / "assets/hermes/skills"))
