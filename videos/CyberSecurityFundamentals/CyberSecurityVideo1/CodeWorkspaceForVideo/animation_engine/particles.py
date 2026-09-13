"""Request particle animation."""

import math
from PIL import Image, ImageDraw, ImageFilter

from .components import Component
from .layout import Rect


def ease(value: float) -> float:
    value = max(0.0, min(1.0, value))
    return value * value * (3.0 - 2.0 * value)


class Particle(Component):
    def __init__(self, source, target=None, start: float = 0.0, duration: float = 1.0, route=None, color=(185, 235, 255), radius: int = 4, glow: bool = True):
        super().__init__("Request particle", Rect(0, 0, radius * 2, radius * 2), start, True)
        self.source = source
        self.target = target
        self.route = route or [source, target]
        self.start = start
        self.duration = duration
        self.color = color
        self.radius = radius
        self.glow = glow

    def position(self, elapsed: float):
        progress = (elapsed - self.start) / self.duration
        if progress < 0 or progress > 1:
            return None
        progress = ease(progress)
        scaled = progress * (len(self.route) - 1)
        index = min(int(scaled), len(self.route) - 2)
        local = scaled - index
        start = self.route[index].output()
        end = self.route[index + 1].input()
        return (start[0] + (end[0] - start[0]) * local, start[1] + (end[1] - start[1]) * local)

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        position = self.position(elapsed)
        if position is None:
            return
        px, py = position
        if self.glow:
            glow = Image.new("RGBA", image.size, (0, 0, 0, 0))
            glow_draw = ImageDraw.Draw(glow)
            glow_draw.ellipse((px - 13, py - 13, px + 13, py + 13), fill=(*self.color, 65))
            image.alpha_composite(glow.filter(ImageFilter.GaussianBlur(7)))
        ImageDraw.Draw(image).ellipse((px - self.radius, py - self.radius, px + self.radius, py + self.radius), fill=(*self.color, 255))
