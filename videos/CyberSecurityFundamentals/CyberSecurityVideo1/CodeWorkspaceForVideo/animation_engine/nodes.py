"""Generic technical node component."""

from typing import Optional

from PIL import ImageDraw

from .canvas import ACTIVE, BORDER, NODE_ACTIVE, NODE_FILL, WHITE, MUTED
from .components import Component
from .typography import centered_text, font


def alpha_color(color, alpha: float):
    return (*color, int(max(0.0, min(1.0, alpha)) * 255))


class Node(Component):
    def __init__(self, label: str, width: int = 140, height: int = 100, x: float = 0, y: float = 0, sequence: int = 0, reveal: float = 0.0, name: Optional[str] = None):
        super().__init__(name or label, bounds=__import__("animation_engine.layout", fromlist=["Rect"]).Rect(x, y, width, height), reveal=reveal)
        self.label = label
        self.sequence = sequence

    def input(self):
        return (self.x, self.y + self.height / 2)

    def output(self):
        return (self.x + self.width, self.y + self.height / 2)

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed)
        if opacity <= 0:
            return
        slide = (1.0 - opacity) * 16
        box = (self.x, self.y + slide, self.x + self.width, self.y + self.height + slide)
        draw = ImageDraw.Draw(image)
        fill = NODE_ACTIVE if active else NODE_FILL
        border = ACTIVE if active else BORDER
        draw.rounded_rectangle(box, radius=10, fill=alpha_color(fill, opacity), outline=alpha_color(border, opacity), width=2)
        draw.text((self.x + 13, self.y + 12 + slide), f"{self.sequence:02d}", font=font(12, True), fill=alpha_color(MUTED, opacity))
        centered_text(draw, (self.x + 8, self.y + 25 + slide, self.x + self.width - 8, self.y + self.height - 8 + slide), self.label, font(16, True), alpha_color(WHITE, opacity))
