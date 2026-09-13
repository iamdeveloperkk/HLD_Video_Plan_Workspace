"""Base visual components."""

from dataclasses import dataclass
from typing import Optional

from .layout import Rect
from .typography import font


@dataclass
class Component:
    name: str
    bounds: Rect
    reveal: float = 0.0
    allow_overlap: bool = False

    @property
    def x(self):
        return self.bounds.x

    @property
    def y(self):
        return self.bounds.y

    @property
    def width(self):
        return self.bounds.width

    @property
    def height(self):
        return self.bounds.height

    def opacity(self, elapsed: float, duration: float = 0.55) -> float:
        value = (elapsed - self.reveal) / duration
        value = max(0.0, min(1.0, value))
        return value * value * (3.0 - 2.0 * value)

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        raise NotImplementedError


@dataclass
class Panel(Component):
    title: Optional[str] = None


@dataclass
class TextNode(Component):
    text: str = ""
    size: int = 16
    fill: tuple[int, int, int] = (229, 242, 255)

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        if elapsed < self.reveal:
            return
        from PIL import ImageDraw
        ImageDraw.Draw(image).text((self.x, self.y), self.text, font=font(self.size), fill=self.fill)
