"""Layout regions and validation primitives."""

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Rect:
    x: float
    y: float
    width: float
    height: float

    @property
    def right(self) -> float:
        return self.x + self.width

    @property
    def bottom(self) -> float:
        return self.y + self.height

    def contains(self, other: "Rect") -> bool:
        return other.x >= self.x and other.y >= self.y and other.right <= self.right and other.bottom <= self.bottom

    def overlaps(self, other: "Rect") -> bool:
        return self.x < other.right and self.right > other.x and self.y < other.bottom and self.bottom > other.y


class LayoutError(ValueError):
    pass


def assert_inside(element, region: Rect) -> None:
    if not region.contains(element.bounds):
        raise LayoutError(f"{element.name} crosses {region}")


def assert_no_overlap(first, second) -> None:
    if first.bounds.overlaps(second.bounds):
        raise LayoutError(f"{first.name} overlaps {second.name}")


def assert_no_overlap_with_region(element, region: Rect) -> None:
    if element.bounds.overlaps(region):
        raise LayoutError(f"{element.name} enters forbidden region")


def validate_elements(elements: Iterable, safe_area: Rect, forbidden_regions: Iterable[Rect] = ()) -> None:
    elements = list(elements)
    for element in elements:
        assert_inside(element, safe_area)
        label = getattr(element, "label", None)
        if label is not None and len(label) * 8 + 16 > element.bounds.width:
            raise LayoutError(f"{element.name} label overflows its bounds")
        icon_size = getattr(element, "icon_size", None)
        if icon_size is not None and icon_size > element.bounds.width:
            raise LayoutError(f"{element.name} icon overflows its bounds")
        for region in forbidden_regions:
            assert_no_overlap_with_region(element, region)
    for index, first in enumerate(elements):
        for second in elements[index + 1:]:
            if getattr(first, "allow_overlap", False) or getattr(second, "allow_overlap", False):
                continue
            assert_no_overlap(first, second)
