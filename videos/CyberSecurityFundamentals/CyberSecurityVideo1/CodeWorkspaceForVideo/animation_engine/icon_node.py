"""Icon-backed node with a generic-node fallback."""

from pathlib import Path

from PIL import Image, ImageDraw

from .icon_registry import resolve_icon
from .layout import Rect
from .nodes import Node, alpha_color
from .canvas import ACTIVE, BORDER, NODE_ACTIVE, NODE_FILL, WHITE
from .typography import centered_text, font


class IconNode(Node):
    def __init__(self, icon: str, label: str, width: int = 145, height: int = 105, x: float = 0, y: float = 0, sequence: int = 0, reveal: float = 0.0, icon_size: int = 42):
        super().__init__(label, width, height, x, y, sequence, reveal)
        self.icon_name = icon
        self.icon_path = resolve_icon(icon)
        self.icon_size = icon_size

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        if self.icon_path is None or self.icon_path.suffix.lower() == ".svg":
            super().draw(image, elapsed, active)
            return
        opacity = self.opacity(elapsed)
        if opacity <= 0:
            return
        draw = ImageDraw.Draw(image)
        fill = NODE_ACTIVE if active else NODE_FILL
        border = ACTIVE if active else BORDER
        draw.rounded_rectangle((self.x, self.y, self.x + self.width, self.y + self.height), radius=10, fill=alpha_color(fill, opacity), outline=alpha_color(border, opacity), width=2)
        try:
            icon = Image.open(self.icon_path).convert("RGBA")
            icon.thumbnail((self.icon_size, self.icon_size), Image.Resampling.LANCZOS)
            icon_x = int(self.x + (self.width - icon.width) / 2)
            icon_y = int(self.y + 10)
            image.alpha_composite(icon, (icon_x, icon_y))
        except (OSError, ValueError):
            super().draw(image, elapsed, active)
            return
        centered_text(draw, (self.x + 8, self.y + 58, self.x + self.width - 8, self.y + self.height - 8), self.label, font(14, True), alpha_color(WHITE, opacity))
