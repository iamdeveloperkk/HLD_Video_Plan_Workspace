"""Canvas configuration and color palette."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Canvas:
    width: int = 1280
    height: int = 720
    fps: int = 30
    duration: float = 16.0


BG = (7, 16, 34)
GRID = (15, 32, 57)
PANEL = (9, 23, 47)
NODE_FILL = (12, 35, 70)
NODE_ACTIVE = (16, 49, 91)
BORDER = (49, 133, 220)
ACTIVE = (108, 203, 255)
WHITE = (229, 242, 255)
MUTED = (135, 163, 194)
BLUE = (69, 166, 247)
