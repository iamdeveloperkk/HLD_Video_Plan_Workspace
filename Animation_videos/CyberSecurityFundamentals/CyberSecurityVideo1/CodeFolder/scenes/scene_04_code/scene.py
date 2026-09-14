"""Scene 4 composition: Confidentiality Breach.

Story:
A legitimate user is authenticated, but an authorization failure allows
that user to access another user's private data.

The scene intentionally avoids showing a real exploit payload. The focus is
the security mental model:

    Authentication -> Who are you?
    Authorization  -> What are you allowed to access?
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

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


from PIL import ImageDraw

from _common.engine.canvas import BLUE, PANEL, WHITE, MUTED
from _common.engine.components import Component
from _common.engine.layout import LayoutError, Rect, assert_inside, validate_elements
from _common.engine.panels import DiscussionPanel
from _common.engine.particles import Particle
from _common.engine.renderer import Renderer
from _common.engine.typography import centered_text, font

from video_config import CANVAS

from scenes.scene_04_code.config import (
    AUTH_REVEAL,
    AUTH_RECT,
    AUTHZ_REVEAL,
    BREACH_REVEAL,
    DATA_RECT,
    FIX_REVEAL,
    MAIN_PANEL as MAIN_PANEL_VALUES,
    PANEL_TITLE,
    RIGHT_PANEL as RIGHT_PANEL_VALUES,
    TAKEAWAY,
    TAKEAWAY_REVEAL,
    USER_A_RECT,
    USER_A_REVEAL,
    USER_B_RECT,
    USER_B_REVEAL,
)

RED = (235, 70, 80)

MAIN_PANEL = Rect(*MAIN_PANEL_VALUES)
RIGHT_PANEL = Rect(*RIGHT_PANEL_VALUES)


def alpha_color(color, opacity: float):
    return (*color, int(max(0.0, min(1.0, opacity)) * 255))


class SecurityBox(Component):
    """Simple scene-specific security component."""

    def __init__(
        self,
        name: str,
        label: str,
        bounds: Rect,
        reveal: float,
        subtitle: str = "",
    ):
        super().__init__(name, bounds, reveal=reveal)
        self.label = label
        self.subtitle = subtitle

    def input(self):
        return (self.x, self.y + self.height / 2)

    def output(self):
        return (self.bounds.right, self.y + self.height / 2)

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed, 0.55)

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        fill = PANEL
        border = RED if active else BLUE

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=12,
            fill=alpha_color(fill, opacity),
            outline=alpha_color(border, opacity),
            width=2,
        )

        centered_text(
            draw,
            (
                self.x + 12,
                self.y + 22,
                self.bounds.right - 12,
                self.y + 65,
            ),
            self.label,
            font(19, True),
            alpha_color(WHITE, opacity),
        )

        if self.subtitle:
            centered_text(
                draw,
                (
                    self.x + 12,
                    self.y + 67,
                    self.bounds.right - 12,
                    self.bounds.bottom - 12,
                ),
                self.subtitle,
                font(13),
                alpha_color(MUTED, opacity),
            )


class DataRecord(Component):
    """Represents private user data."""

    def __init__(
        self,
        name: str,
        label: str,
        owner: str,
        bounds: Rect,
        reveal: float,
        compromised: bool = False,
    ):
        super().__init__(name, bounds, reveal=reveal)
        self.label = label
        self.owner = owner
        self.compromised = compromised

    def input(self):
        return (self.x, self.y + self.height / 2)

    def output(self):
        return (self.bounds.right, self.y + self.height / 2)

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed, 0.55)

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        border = RED if self.compromised or active else BLUE

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=10,
            fill=alpha_color(PANEL, opacity),
            outline=alpha_color(border, opacity),
            width=2,
        )

        draw.text(
            (self.x + 18, self.y + 13),
            self.owner,
            font=font(12, True),
            fill=alpha_color(BLUE, opacity),
        )

        draw.text(
            (self.x + 18, self.y + 36),
            self.label,
            font=font(15, True),
            fill=alpha_color(WHITE, opacity),
        )


class FlowArrow(Component):
    """Animated request/data flow arrow."""

    def __init__(
        self,
        name: str,
        start: tuple[float, float],
        end: tuple[float, float],
        reveal: float,
        color=BLUE,
    ):
        x1, y1 = start
        x2, y2 = end

        bounds = Rect(
            min(x1, x2) - 8,
            min(y1, y2) - 8,
            abs(x2 - x1) + 16,
            abs(y2 - y1) + 16,
        )

        super().__init__(name, bounds, reveal=reveal)

        self.start = start
        self.end = end
        self.color = color

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed, 0.45)

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        color = RED if active else self.color

        x1, y1 = self.start
        x2, y2 = self.end

        draw.line(
            (x1, y1, x2, y2),
            fill=alpha_color(color, opacity),
            width=3,
        )

        # Arrow head
        if x2 >= x1:
            points = [
                (x2, y2),
                (x2 - 12, y2 - 7),
                (x2 - 12, y2 + 7),
            ]
        else:
            points = [
                (x2, y2),
                (x2 + 12, y2 - 7),
                (x2 + 12, y2 + 7),
            ]

        draw.polygon(
            points,
            fill=alpha_color(color, opacity),
        )


class BreachBanner(Component):
    """Displays the confidentiality failure."""

    def __init__(self, bounds: Rect, reveal: float):
        super().__init__(
            "BreachBanner",
            bounds,
            reveal=reveal,
            allow_overlap=True,
        )

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed, 0.6)

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=8,
            fill=alpha_color((60, 18, 25), opacity),
            outline=alpha_color(RED, opacity),
            width=2,
        )

        centered_text(
            draw,
            (
                self.x + 10,
                self.y + 7,
                self.bounds.right - 10,
                self.bounds.bottom - 7,
            ),
            "UNAUTHORIZED DATA ACCESS",
            font(14, True),
            alpha_color(RED, opacity),
        )


class Takeaway(Component):
    """Final scene takeaway."""

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

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=8,
            fill=alpha_color(PANEL, opacity),
            outline=alpha_color(BLUE, opacity),
            width=1,
        )

        draw.text(
            (self.x + 18, self.y + 9),
            "TAKEAWAY",
            font=font(11, True),
            fill=alpha_color(BLUE, opacity),
        )

        draw.text(
            (self.x + 18, self.y + 27),
            TAKEAWAY,
            font=font(17, True),
            fill=alpha_color(WHITE, opacity),
        )


def build_scene():
    user_a = SecurityBox(
        "UserA",
        "USER A",
        Rect(*USER_A_RECT),
        USER_A_REVEAL,
        "Authenticated user",
    )

    auth = SecurityBox(
        "Authentication",
        "AUTHENTICATION",
        Rect(*AUTH_RECT),
        AUTH_REVEAL,
        "Identity verified",
    )

    user_b_data = DataRecord(
        "UserBData",
        "PRIVATE DATA",
        "USER B",
        Rect(*USER_B_RECT),
        USER_B_REVEAL,
    )

    user_a_data = DataRecord(
        "UserAData",
        "PRIVATE DATA",
        "USER A",
        Rect(*DATA_RECT),
        USER_B_REVEAL,
    )

    # Legitimate authentication flow.
    auth_arrow = FlowArrow(
        "AuthenticationFlow",
        (
            user_a.bounds.right,
            user_a.y + user_a.height / 2,
        ),
        (
            auth.x,
            auth.y + auth.height / 2,
        ),
        AUTH_REVEAL,
    )

    # Data access path appears later.
    data_arrow = FlowArrow(
        "DataAccessFlow",
        (
            auth.bounds.right,
            auth.y + auth.height / 2,
        ),
        (
            user_b_data.x,
            user_b_data.y + user_b_data.height / 2,
        ),
        BREACH_REVEAL,
        color=RED,
    )

    breach = BreachBanner(
        Rect(505, 420, 310, 45),
        BREACH_REVEAL,
    )

    takeaway = Takeaway(
        Rect(
            MAIN_PANEL.x + 25,
            MAIN_PANEL.bottom - 92,
            MAIN_PANEL.width - 50,
            60,
        ),
        TAKEAWAY_REVEAL,
    )

    panel = DiscussionPanel(
        PANEL_TITLE,
        [
            "User A is authenticated",
            "But User A requests User B's data",
            "Authentication ≠ Authorization",
            "Authorization must enforce ownership",
        ],
        RIGHT_PANEL.x,
        RIGHT_PANEL.y,
        RIGHT_PANEL.width,
        RIGHT_PANEL.height,
        [
            USER_A_REVEAL,
            BREACH_REVEAL,
            AUTHZ_REVEAL,
            FIX_REVEAL,
        ],
    )

    # The particle intentionally represents a legitimate request that reaches
    # the wrong data object because authorization is missing/broken.
    particle = Particle(
        user_a,
        user_b_data,
        route=[user_a, auth, user_b_data],
        start=BREACH_REVEAL,
        duration=3.2,
    )

    return (
        user_a,
        auth,
        user_a_data,
        user_b_data,
        auth_arrow,
        data_arrow,
        breach,
        takeaway,
        panel,
        particle,
    )


def validate_scene(
    user_a,
    auth,
    user_a_data,
    user_b_data,
    auth_arrow,
    data_arrow,
    breach,
    takeaway,
    panel,
):
    try:
        elements = [
            user_a,
            auth,
            user_a_data,
            user_b_data,
            breach,
            takeaway,
        ]

        validate_elements(elements, MAIN_PANEL)

        for element in elements:
            if element.bounds.overlaps(RIGHT_PANEL):
                raise LayoutError(
                    f"{element.name} overlaps the discussion panel"
                )

        assert_inside(auth_arrow, MAIN_PANEL)
        assert_inside(data_arrow, MAIN_PANEL)

        if panel.bounds.overlaps(MAIN_PANEL):
            raise LayoutError(
                "discussion panel overlaps main animation panel"
            )

        if RIGHT_PANEL.right > CANVAS.width:
            raise LayoutError("discussion panel exceeds canvas width")

        if RIGHT_PANEL.bottom > CANVAS.height:
            raise LayoutError("discussion panel exceeds canvas height")

    except LayoutError as error:
        print("LAYOUT VALIDATION: FAILED")
        print(f"- {error}")
        raise SystemExit(1) from error

    print("LAYOUT VALIDATION: PASS")


def make_frame(
    canvas,
    user_a,
    auth,
    user_a_data,
    user_b_data,
    auth_arrow,
    data_arrow,
    breach,
    takeaway,
    panel,
    particle,
    elapsed,
):
    renderer = Renderer(canvas)
    image = renderer.background()
    draw = ImageDraw.Draw(image)

    # ------------------------------------------------------------------
    # Header
    # ------------------------------------------------------------------

    draw.text(
        (50, 35),
        "NEXA SECURITY INCIDENT",
        font=font(26, True),
        fill=WHITE,
    )

    draw.text(
        (50, 70),
        "A legitimate user should only see the data they are authorized to access.",
        font=font(15),
        fill=MUTED,
    )

    # ------------------------------------------------------------------
    # Main panel
    # ------------------------------------------------------------------

    draw.rounded_rectangle(
        (
            MAIN_PANEL.x,
            MAIN_PANEL.y,
            MAIN_PANEL.right,
            MAIN_PANEL.bottom,
        ),
        radius=14,
        fill=PANEL,
        outline=(29, 75, 121),
        width=2,
    )

    draw.text(
        (MAIN_PANEL.x + 25, MAIN_PANEL.y + 22),
        "CONFIDENTIALITY",
        font=font(13, True),
        fill=BLUE,
    )

    # ------------------------------------------------------------------
    # Data objects
    # ------------------------------------------------------------------

    user_a_data.draw(
        image,
        elapsed,
        active=False,
    )

    user_b_data.draw(
        image,
        elapsed,
        active=elapsed >= BREACH_REVEAL,
    )

    # ------------------------------------------------------------------
    # Flow
    # ------------------------------------------------------------------

    auth_arrow.draw(
        image,
        elapsed,
        active=AUTH_REVEAL <= elapsed < BREACH_REVEAL,
    )

    data_arrow.draw(
        image,
        elapsed,
        active=elapsed >= BREACH_REVEAL,
    )

    # ------------------------------------------------------------------
    # Core nodes
    # ------------------------------------------------------------------

    user_a.draw(
        image,
        elapsed,
        active=USER_A_REVEAL <= elapsed < AUTH_REVEAL,
    )

    auth.draw(
        image,
        elapsed,
        active=AUTH_REVEAL <= elapsed < AUTHZ_REVEAL,
    )

    # ------------------------------------------------------------------
    # Breach state
    # ------------------------------------------------------------------

    if elapsed >= BREACH_REVEAL:
        particle.draw(image, elapsed)

    breach.draw(
        image,
        elapsed,
        active=elapsed >= BREACH_REVEAL,
    )

    # ------------------------------------------------------------------
    # Final takeaway
    # ------------------------------------------------------------------

    takeaway.draw(image, elapsed)

    # ------------------------------------------------------------------
    # Discussion panel
    # ------------------------------------------------------------------

    panel.draw(image, elapsed)

    return image


def render_scene(output: Path):
    (
        user_a,
        auth,
        user_a_data,
        user_b_data,
        auth_arrow,
        data_arrow,
        breach,
        takeaway,
        panel,
        particle,
    ) = build_scene()

    print(
        f"main_panel: "
        f"x={MAIN_PANEL.x}, y={MAIN_PANEL.y}, "
        f"w={MAIN_PANEL.width}, h={MAIN_PANEL.height}"
    )

    print(
        f"right_panel: "
        f"x={RIGHT_PANEL.x}, y={RIGHT_PANEL.y}, "
        f"w={RIGHT_PANEL.width}, h={RIGHT_PANEL.height}"
    )

    for element in [
        user_a,
        auth,
        user_a_data,
        user_b_data,
        breach,
        takeaway,
    ]:
        print(
            f"{element.name}: "
            f"x={element.x:.2f}, "
            f"y={element.y:.2f}, "
            f"w={element.width}, "
            f"h={element.height}"
        )

    validate_scene(
        user_a,
        auth,
        user_a_data,
        user_b_data,
        auth_arrow,
        data_arrow,
        breach,
        takeaway,
        panel,
    )

    canvas = CANVAS

    Renderer(canvas).render(
        lambda elapsed: make_frame(
            canvas,
            user_a,
            auth,
            user_a_data,
            user_b_data,
            auth_arrow,
            data_arrow,
            breach,
            takeaway,
            panel,
            particle,
            elapsed,
        ),
        output,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Render Scene 4 - Confidentiality Breach"
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=(
            ROOT
            / "output"
            / "Cyber_Attack_X_FAANG_Video01_Scene04.mp4"
        ),
    )

    args = parser.parse_args()

    render_scene(args.output)


if __name__ == "__main__":
    main()