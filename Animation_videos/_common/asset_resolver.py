"""Resolve assets from scene, video, then common scope."""

from pathlib import Path
from typing import Iterable, Optional


class AssetResolver:
    def __init__(self, roots: Iterable[Path]):
        self.roots = [Path(root) for root in roots]

    def resolve(self, relative_path: str) -> Optional[Path]:
        for root in self.roots:
            candidate = root / relative_path
            if candidate.exists():
                return candidate
        return None


def default_resolver(common_root: Path, video_root: Optional[Path] = None, scene_root: Optional[Path] = None) -> AssetResolver:
    roots = []
    if scene_root:
        roots.append(Path(scene_root))
    if video_root:
        roots.append(Path(video_root))
    roots.append(Path(common_root))
    return AssetResolver(roots)
