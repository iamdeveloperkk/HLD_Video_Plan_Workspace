"""Template scene composition entry point."""

from pathlib import Path


def render_scene(output: Path) -> None:
    raise NotImplementedError("Define the scene composition and call the common Renderer")
