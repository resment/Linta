"""Run llm-wiki-kit as a module."""

from llm_wiki_kit.cli import app


def main() -> None:
    """Execute the Typer application."""

    app()


if __name__ == "__main__":
    main()
