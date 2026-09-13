"""Reusable animation event timeline."""

from dataclasses import dataclass

from PIL import ImageDraw

from .canvas import BLUE
from .components import Component
from .layout import Rect


@dataclass(frozen=True)
class Event:
    component: object
    start: float
    duration: float
    animation: str


class Timeline(Component):
    def __init__(self):
        super().__init__("Timeline", Rect(0, 0, 0, 0), allow_overlap=True)
        self.events = []

    def place(self, x: float, y: float, width: float, height: float = 12):
        self.bounds = Rect(x, y, width, height)
        return self

    def add(self, component, start: float, duration: float = 0.55, animation: str = "fade_in"):
        component.reveal = start
        self.events.append(Event(component, start, duration, animation))
        return component

    def active(self, elapsed: float):
        return [event for event in self.events if event.start <= elapsed <= event.start + event.duration]

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        draw = ImageDraw.Draw(image)
        x, y, width = self.x, self.y, self.width
        draw.line((x, y + 5, x + width, y + 5), fill=(33, 74, 112), width=2)
        progress = max(0.0, min(1.0, (elapsed - 0.8) / 7.2))
        draw.line((x, y + 5, x + width * progress, y + 5), fill=BLUE, width=3)
        for event in self.events:
            marker = x + width * max(0.0, min(1.0, (event.start - 0.8) / 7.2))
            color = BLUE if elapsed >= event.start else (33, 74, 112)
            draw.ellipse((marker - 4, y + 1, marker + 4, y + 9), fill=color)
