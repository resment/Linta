"""Run Linta as a module."""

from linta.cli import app


def main() -> None:
    """Execute the Typer application."""

    app()


if __name__ == "__main__":
    main()
