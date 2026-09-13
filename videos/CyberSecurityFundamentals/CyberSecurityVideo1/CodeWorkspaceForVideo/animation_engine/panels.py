"""Reusable fixed discussion panel."""

from typing import Optional

from PIL import ImageDraw

from .canvas import BLUE, PANEL, WHITE
from .components import Component
from .layout import Rect
from .nodes import alpha_color
from .typography import font


class DiscussionPanel(Component):
    def __init__(self, title: str, bullets: list[str], x: float, y: float, width: float = 300, height: float = 200, reveals: Optional[list[float]] = None):
        super().__init__("Discussion panel", Rect(x, y, width, height), allow_overlap=True)
        self.title = title
        self.bullets = bullets
        self.reveals = reveals or [0.8 + index * 1.8 for index in range(len(bullets))]

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((self.x, self.y, self.bounds.right, self.bounds.bottom), radius=12, fill=PANEL, outline=(29, 75, 121), width=2)
        draw.text((self.x + 20, self.y + 20), self.title, font=font(19, True), fill=WHITE)
        for index, label in enumerate(self.bullets):
            opacity = max(0.0, min(1.0, (elapsed - self.reveals[index]) / 0.45))
            opacity = opacity * opacity * (3.0 - 2.0 * opacity)
            if opacity <= 0:
                continue
            y = self.y + 58 + index * 25
            draw.ellipse((self.x + 20, y + 5, self.x + 26, y + 11), fill=alpha_color(BLUE, opacity))
            draw.text((self.x + 36, y), label, font=font(13), fill=alpha_color(WHITE, opacity))
