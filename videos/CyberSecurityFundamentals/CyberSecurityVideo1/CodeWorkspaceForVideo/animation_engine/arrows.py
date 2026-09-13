"""Connection-point-based arrows."""

import math
from PIL import ImageDraw

from .canvas import BLUE
from .components import Component
from .nodes import alpha_color


class Arrow(Component):
    def __init__(self, start_component, end_component, reveal: float = 0.0, curved: bool = False):
        self.start_component = start_component
        self.end_component = end_component
        self.curved = curved
        super().__init__(f"Arrow {start_component.name} to {end_component.name}", self._bounds(), reveal, True)

    def _bounds(self):
        start = self.start_component.output()
        end = self.end_component.input()
        return __import__("animation_engine.layout", fromlist=["Rect"]).Rect(min(start[0], end[0]), min(start[1], end[1]) - 8, abs(end[0] - start[0]), abs(end[1] - start[1]) + 16)

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = max(0.0, min(1.0, (elapsed - self.reveal) / 0.5))
        if opacity <= 0:
            return
        start = self.start_component.output()
        end = self.end_component.input()
        draw = ImageDraw.Draw(image)
        color = alpha_color(BLUE, opacity)
        draw.line((*start, *end), fill=color, width=2)
        angle = math.atan2(end[1] - start[1], end[0] - start[0])
        size = 8
        left = (end[0] - size * math.cos(angle - math.pi / 6), end[1] - size * math.sin(angle - math.pi / 6))
        right = (end[0] - size * math.cos(angle + math.pi / 6), end[1] - size * math.sin(angle + math.pi / 6))
        draw.polygon((end, left, right), fill=color)
