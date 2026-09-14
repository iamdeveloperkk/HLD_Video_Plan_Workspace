"""Scene 3 composition: What Are We Protecting?"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import ImageDraw


# ---------------------------------------------------------------------------
# Repository paths
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[6]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

SHARED_ROOT = ROOT / "Animation_videos"

if str(SHARED_ROOT) not in sys.path:
    sys.path.insert(0, str(SHARED_ROOT))

VIDEO_ROOT = (
    SHARED_ROOT
    / "CyberSecurityFundamentals"
    / "CyberSecurityVideo1"
    / "CodeFolder"
)

if str(VIDEO_ROOT) not in sys.path:
    sys.path.insert(0, str(VIDEO_ROOT))


# ---------------------------------------------------------------------------
# Common engine
# ---------------------------------------------------------------------------

from _common.engine.canvas import (
    BLUE,
    MUTED,
    PANEL,
    WHITE,
    ACTIVE,
    BORDER,
    NODE_FILL,
    NODE_ACTIVE,
)
from _common.engine.components import Component
from _common.engine.layout import (
    LayoutError,
    Rect,
    assert_inside,
    validate_elements,
)
from _common.engine.panels import DiscussionPanel
from _common.engine.renderer import Renderer
from _common.engine.typography import centered_text, font

from video_config import CANVAS

from scenes.scene_03_code.config import (
    SCENE_NAME,
    SCENE_TITLE,
    MAIN_PANEL,
    RIGHT_PANEL,
    ARCHITECTURE_SEPARATION,

    TITLE_REVEAL,

    CONFIDENTIALITY_REVEAL,
    INTEGRITY_REVEAL,
    AVAILABILITY_REVEAL,

    TAKEAWAY_REVEAL,

    CARD_WIDTH,
    CARD_HEIGHT,
    CARD_Y,
    CARD_GAP,
    CARD_X,

    CIA_SPECS,

    PANEL_TITLE,
    DISCUSSION_POINTS,
    DISCUSSION_REVEALS,

    TAKEAWAY,
)


MAIN_PANEL_RECT = Rect(*MAIN_PANEL)
RIGHT_PANEL_RECT = Rect(*RIGHT_PANEL)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def alpha_color(color, alpha: float):
    return (*color, int(max(0.0, min(1.0, alpha)) * 255))


# ---------------------------------------------------------------------------
# CIA Card
# ---------------------------------------------------------------------------

class CIACard(Component):
    """Animated CIA security objective card."""

    def __init__(
        self,
        key: str,
        x: float,
        y: float,
        reveal: float,
        subtitle: str,
        description: str,
        sequence: int,
    ):
        super().__init__(
            name=key,
            bounds=Rect(
                x,
                y,
                CARD_WIDTH,
                CARD_HEIGHT,
            ),
            reveal=reveal,
        )

        self.key = key
        self.subtitle = subtitle
        self.description = description
        self.sequence = sequence

    def draw(self, image, elapsed: float, active: bool = False) -> None:

        opacity = self.opacity(elapsed)

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        slide = (1.0 - opacity) * 20

        x = self.x
        y = self.y + slide

        right = x + self.width
        bottom = y + self.height

        fill = NODE_ACTIVE if active else NODE_FILL
        border = ACTIVE if active else BORDER

        # Card
        draw.rounded_rectangle(
            (x, y, right, bottom),
            radius=14,
            fill=alpha_color(fill, opacity),
            outline=alpha_color(border, opacity),
            width=2,
        )

        # Number
        draw.text(
            (x + 18, y + 16),
            f"{self.sequence:02d}",
            font=font(12, True),
            fill=alpha_color(MUTED, opacity),
        )

        # CIA title
        centered_text(
            draw,
            (
                x + 15,
                y + 48,
                right - 15,
                y + 92,
            ),
            self.key,
            font(18, True),
            alpha_color(WHITE, opacity),
        )

        # Question
        centered_text(
            draw,
            (
                x + 18,
                y + 105,
                right - 18,
                y + 145,
            ),
            self.subtitle,
            font(15),
            alpha_color(MUTED, opacity),
        )

        # Description divider
        draw.line(
            (
                x + 25,
                y + 158,
                right - 25,
                y + 158,
            ),
            fill=alpha_color(BORDER, opacity),
            width=1,
        )

        centered_text(
            draw,
            (
                x + 18,
                y + 170,
                right - 18,
                y + 215,
            ),
            self.description,
            font(14, True),
            alpha_color(BLUE, opacity),
        )


# ---------------------------------------------------------------------------
# Takeaway
# ---------------------------------------------------------------------------

class Takeaway(Component):
    """Final CIA takeaway."""

    def __init__(self, bounds: Rect, reveal: float):
        super().__init__(
            "Takeaway",
            bounds,
            reveal=reveal,
            allow_overlap=True,
        )

    def draw(self, image, elapsed: float, active: bool = False) -> None:

        opacity = self.opacity(elapsed, 0.7)

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        fill = (*PANEL, int(opacity * 255))
        outline = (*BLUE, int(opacity * 255))

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=8,
            fill=fill,
            outline=outline,
            width=1,
        )

        draw.text(
            (
                self.x + 18,
                self.y + 8,
            ),
            "SECURITY MODEL",
            font=font(11, True),
            fill=(*BLUE, int(opacity * 255)),
        )

        draw.text(
            (
                self.x + 18,
                self.y + 26,
            ),
            TAKEAWAY,
            font=font(16, True),
            fill=(*WHITE, int(opacity * 255)),
        )


# ---------------------------------------------------------------------------
# Build scene
# ---------------------------------------------------------------------------

def build_scene():

    cards = []

    for sequence, (key, spec) in enumerate(
        CIA_SPECS.items(),
        start=1,
    ):

        card = CIACard(
            key=key,
            x=CARD_X[sequence - 1],
            y=CARD_Y,
            reveal=spec["reveal"],
            subtitle=spec["subtitle"],
            description=spec["description"],
            sequence=sequence,
        )

        cards.append(card)

    takeaway = Takeaway(
        Rect(
            MAIN_PANEL_RECT.x + 25,
            MAIN_PANEL_RECT.y + 390,
            MAIN_PANEL_RECT.width - 50,
            54,
        ),
        TAKEAWAY_REVEAL,
    )

    panel = DiscussionPanel(
        PANEL_TITLE,
        DISCUSSION_POINTS,
        RIGHT_PANEL_RECT.x,
        RIGHT_PANEL_RECT.y,
        RIGHT_PANEL_RECT.width,
        RIGHT_PANEL_RECT.height,
        DISCUSSION_REVEALS,
    )

    return cards, takeaway, panel


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_scene(cards, takeaway, panel):

    try:

        validate_elements(
            cards + [takeaway],
            MAIN_PANEL_RECT,
        )

        for card in cards:

            if card.bounds.right > (
                RIGHT_PANEL_RECT.x - ARCHITECTURE_SEPARATION
            ):
                raise LayoutError(
                    f"{card.name} is too close to the discussion panel"
                )

        assert_inside(
            takeaway,
            MAIN_PANEL_RECT,
        )

        if panel.bounds.overlaps(MAIN_PANEL_RECT):
            raise LayoutError(
                "discussion panel overlaps main panel"
            )

    except LayoutError as error:

        print("LAYOUT VALIDATION: FAILED")
        print(f"- {error}")

        raise SystemExit(1) from error

    print("LAYOUT VALIDATION: PASS")


# ---------------------------------------------------------------------------
# Frame generation
# ---------------------------------------------------------------------------

def make_frame(
    canvas,
    cards,
    takeaway,
    panel,
    elapsed,
):

    renderer = Renderer(canvas)

    image = renderer.background()

    draw = ImageDraw.Draw(image)

    # -----------------------------------------------------------------------
    # Header
    # -----------------------------------------------------------------------

    draw.text(
        (50, 35),
        SCENE_TITLE,
        font=font(26, True),
        fill=WHITE,
    )

    draw.text(
        (50, 70),
        "Security starts with understanding what we need to protect.",
        font=font(16),
        fill=MUTED,
    )

    # -----------------------------------------------------------------------
    # Main panel
    # -----------------------------------------------------------------------

    draw.rounded_rectangle(
        (
            MAIN_PANEL_RECT.x,
            MAIN_PANEL_RECT.y,
            MAIN_PANEL_RECT.right,
            MAIN_PANEL_RECT.bottom,
        ),
        radius=14,
        fill=PANEL,
        outline=(29, 75, 121),
        width=2,
    )

    draw.text(
        (
            MAIN_PANEL_RECT.x + 25,
            MAIN_PANEL_RECT.y + 22,
        ),
        "THE SECURITY TRIAD",
        font=font(13, True),
        fill=BLUE,
    )

    # -----------------------------------------------------------------------
    # Cards
    # -----------------------------------------------------------------------

    active_card = None

    if elapsed >= CONFIDENTIALITY_REVEAL:
        active_card = 0

    if elapsed >= INTEGRITY_REVEAL:
        active_card = 1

    if elapsed >= AVAILABILITY_REVEAL:
        active_card = 2

    for index, card in enumerate(cards):

        card.draw(
            image,
            elapsed,
            active=(index == active_card),
        )

    # -----------------------------------------------------------------------
    # Takeaway
    # -----------------------------------------------------------------------

    takeaway.draw(
        image,
        elapsed,
    )

    # -----------------------------------------------------------------------
    # Right discussion panel
    # -----------------------------------------------------------------------

    panel.draw(
        image,
        elapsed,
    )

    return image


# ---------------------------------------------------------------------------
# Layout information
# ---------------------------------------------------------------------------

def print_layout(cards):

    print(
        f"main_panel: "
        f"x={MAIN_PANEL_RECT.x}, "
        f"y={MAIN_PANEL_RECT.y}, "
        f"w={MAIN_PANEL_RECT.width}, "
        f"h={MAIN_PANEL_RECT.height}"
    )

    print(
        f"right_panel: "
        f"x={RIGHT_PANEL_RECT.x}, "
        f"y={RIGHT_PANEL_RECT.y}, "
        f"w={RIGHT_PANEL_RECT.width}, "
        f"h={RIGHT_PANEL_RECT.height}"
    )

    for card in cards:

        print(
            f"{card.name}: "
            f"x={card.x:.2f}, "
            f"y={card.y:.2f}, "
            f"w={card.width}, "
            f"h={card.height}"
        )


# ---------------------------------------------------------------------------
# Shared CLI entry point
# ---------------------------------------------------------------------------

def render_scene(output: Path):

    cards, takeaway, panel = build_scene()

    print_layout(cards)

    validate_scene(
        cards,
        takeaway,
        panel,
    )

    Renderer(CANVAS).render(
        lambda elapsed: make_frame(
            CANVAS,
            cards,
            takeaway,
            panel,
            elapsed,
        ),
        output,
    )


# ---------------------------------------------------------------------------
# Direct execution
# ---------------------------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description="Render Scene 3 - What Are We Protecting?"
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=(
            ROOT
            / "CyberSecurityFundamentals"
            / "CyberSecurityVideo1"
            / "OutputFolder"
            / "scene_03_output"
            / "CyberSecurityVideo1_scene_03.mp4"
        ),
    )

    args = parser.parse_args()

    render_scene(args.output)


if __name__ == "__main__":
    main()