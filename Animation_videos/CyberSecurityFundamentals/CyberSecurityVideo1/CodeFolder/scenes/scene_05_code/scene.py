"""Scene 5 composition: Integrity Breach.

Story:
A legitimate NEXA customer creates a ₹1,000 order.

The order reaches the service and is stored correctly.

Later, the value is unexpectedly modified to ₹100,000.

The scene explains integrity as protection against unauthorized
or unexpected modification of data.

The visual intentionally avoids showing an exploit payload.
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

from scenes.scene_05_code.config import (
    CORRUPTED_VALUE_REVEAL,
    DATABASE_RECT,
    DISCUSSION_REVEALS,
    MAIN_PANEL as MAIN_PANEL_VALUES,
    MODIFICATION_REVEAL,
    ORDER_RECT,
    ORDER_REVEAL,
    PANEL_TITLE,
    REQUEST_REVEAL,
    RESTORED_REVEAL,
    RIGHT_PANEL as RIGHT_PANEL_VALUES,
    SERVICE_RECT,
    TAKEAWAY,
    TAKEAWAY_REVEAL,
    USER_RECT,
    USER_REVEAL,
    VALIDATION_RECT,
    VALIDATION_REVEAL,
)


MAIN_PANEL = Rect(*MAIN_PANEL_VALUES)
RIGHT_PANEL = Rect(*RIGHT_PANEL_VALUES)

RED = (235, 70, 80)
GREEN = (75, 200, 130)
YELLOW = (235, 185, 75)


def alpha_color(color, opacity: float):
    return (*color, int(max(0.0, min(1.0, opacity)) * 255))


class SecurityBox(Component):
    """Technical system component."""

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
        return (self.x + self.width, self.y + self.height / 2)

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed, 0.55)

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        border = RED if active else BLUE

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=12,
            fill=alpha_color(PANEL, opacity),
            outline=alpha_color(border, opacity),
            width=2,
        )

        centered_text(
            draw,
            (
                self.x + 12,
                self.y + 20,
                self.bounds.right - 12,
                self.y + 62,
            ),
            self.label,
            font(18, True),
            alpha_color(WHITE, opacity),
        )

        if self.subtitle:
            centered_text(
                draw,
                (
                    self.x + 12,
                    self.y + 65,
                    self.bounds.right - 12,
                    self.bounds.bottom - 12,
                ),
                self.subtitle,
                font(13),
                alpha_color(MUTED, opacity),
            )


class OrderCard(Component):
    """Order record whose value can become corrupted."""

    def __init__(
        self,
        bounds: Rect,
        reveal: float,
    ):
        super().__init__(
            "OrderRecord",
            bounds,
            reveal=reveal,
        )

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed, 0.55)

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        corrupted = elapsed >= MODIFICATION_REVEAL
        restored = elapsed >= RESTORED_REVEAL

        if restored:
            border = GREEN
        elif corrupted:
            border = RED
        else:
            border = BLUE

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
            (self.x + 18, self.y + 12),
            "ORDER #48291",
            font=font(12, True),
            fill=alpha_color(BLUE, opacity),
        )

        draw.text(
            (self.x + 18, self.y + 38),
            "Amount",
            font=font(13),
            fill=alpha_color(MUTED, opacity),
        )

        if restored:
            amount = "₹1,000"
            amount_color = GREEN
        elif corrupted:
            amount = "₹100,000"
            amount_color = RED
        else:
            amount = "₹1,000"
            amount_color = WHITE

        draw.text(
            (self.x + 105, self.y + 34),
            amount,
            font=font(20, True),
            fill=alpha_color(amount_color, opacity),
        )

        if corrupted and not restored:
            draw.text(
                (self.x + 18, self.y + 67),
                "VALUE MODIFIED",
                font=font(11, True),
                fill=alpha_color(RED, opacity),
            )

        if restored:
            draw.text(
                (self.x + 18, self.y + 67),
                "INTEGRITY VERIFIED",
                font=font(11, True),
                fill=alpha_color(GREEN, opacity),
            )


class FlowArrow(Component):
    """Simple animated directional flow."""

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
            min(x1, x2) - 10,
            min(y1, y2) - 10,
            abs(x2 - x1) + 20,
            abs(y2 - y1) + 20,
        )

        super().__init__(
            name,
            bounds,
            reveal=reveal,
            allow_overlap=True,
        )

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


class ModificationIndicator(Component):
    """Shows that the stored value has been altered."""

    def __init__(self, bounds: Rect, reveal: float):
        super().__init__(
            "ModificationIndicator",
            bounds,
            reveal=reveal,
            allow_overlap=True,
        )

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed, 0.5)

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
                self.y + 5,
                self.bounds.right - 10,
                self.bounds.bottom - 5,
            ),
            "UNAUTHORIZED CHANGE",
            font(13, True),
            alpha_color(RED, opacity),
        )


class ValidationIndicator(Component):
    """Integrity validation result."""

    def __init__(self, bounds: Rect, reveal: float):
        super().__init__(
            "IntegrityValidation",
            bounds,
            reveal=reveal,
            allow_overlap=True,
        )

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed, 0.55)

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        corrupted = elapsed >= MODIFICATION_REVEAL
        restored = elapsed >= RESTORED_REVEAL

        if restored:
            border = GREEN
            label = "✓ INTEGRITY VERIFIED"
            sub = "EXPECTED VALUE: ₹1,000"
        elif corrupted:
            border = RED
            label = "✕ INTEGRITY CHECK FAILED"
            sub = "EXPECTED VALUE DOES NOT MATCH"
        else:
            border = BLUE
            label = "INTEGRITY CHECK"
            sub = "VERIFYING DATA"

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

        centered_text(
            draw,
            (
                self.x + 10,
                self.y + 12,
                self.bounds.right - 10,
                self.y + 39,
            ),
            label,
            font(14, True),
            alpha_color(border, opacity),
        )

        centered_text(
            draw,
            (
                self.x + 10,
                self.y + 42,
                self.bounds.right - 10,
                self.bounds.bottom - 8,
            ),
            sub,
            font(11),
            alpha_color(MUTED, opacity),
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
            (self.x + 18, self.y + 8),
            "TAKEAWAY",
            font=font(11, True),
            fill=alpha_color(BLUE, opacity),
        )

        draw.text(
            (self.x + 18, self.y + 27),
            TAKEAWAY,
            font=font(15, True),
            fill=alpha_color(WHITE, opacity),
        )


def build_scene():
    user = SecurityBox(
        "User",
        "CUSTOMER",
        Rect(*USER_RECT),
        USER_REVEAL,
        "Creates an order",
    )

    service = SecurityBox(
        "OrderService",
        "ORDER SERVICE",
        Rect(*SERVICE_RECT),
        REQUEST_REVEAL,
        "Processes order",
    )

    database = SecurityBox(
        "Database",
        "DATABASE",
        Rect(*DATABASE_RECT),
        ORDER_REVEAL,
        "Stores order state",
    )

    order = OrderCard(
        Rect(*ORDER_RECT),
        ORDER_REVEAL,
    )

    validation = ValidationIndicator(
        Rect(*VALIDATION_RECT),
        VALIDATION_REVEAL,
    )

    user_to_service = FlowArrow(
        "UserToService",
        (
            user.bounds.right,
            user.y + user.height / 2,
        ),
        (
            service.x,
            service.y + service.height / 2,
        ),
        REQUEST_REVEAL,
    )

    service_to_database = FlowArrow(
        "ServiceToDatabase",
        (
            service.bounds.right,
            service.y + service.height / 2,
        ),
        (
            database.x,
            database.y + database.height / 2,
        ),
        ORDER_REVEAL,
    )

    modification = ModificationIndicator(
        Rect(570, 145, 260, 38),
        MODIFICATION_REVEAL,
    )

    takeaway = Takeaway(
        Rect(
            MAIN_PANEL.x + 25,
            MAIN_PANEL.bottom - 82,
            MAIN_PANEL.width - 50,
            54,
        ),
        TAKEAWAY_REVEAL,
    )

    panel = DiscussionPanel(
        PANEL_TITLE,
        [
            "A legitimate order is created",
            "Stored value should not change unexpectedly",
            "An attacker modifies the data",
            "Integrity protects correctness and trust",
        ],
        RIGHT_PANEL.x,
        RIGHT_PANEL.y,
        RIGHT_PANEL.width,
        RIGHT_PANEL.height,
        DISCUSSION_REVEALS,
    )

    # Request particle travels through the legitimate path.
    particle = Particle(
        user,
        database,
        route=[user, service, database],
        start=REQUEST_REVEAL + 0.3,
        duration=3.2,
    )

    return (
        user,
        service,
        database,
        order,
        validation,
        user_to_service,
        service_to_database,
        modification,
        takeaway,
        panel,
        particle,
    )


def validate_scene(
    user,
    service,
    database,
    order,
    validation,
    user_to_service,
    service_to_database,
    modification,
    takeaway,
    panel,
):
    try:
        elements = [
            user,
            service,
            database,
            order,
            validation,
            modification,
            takeaway,
        ]

        validate_elements(elements, MAIN_PANEL)

        for element in elements:
            if element.bounds.overlaps(RIGHT_PANEL):
                raise LayoutError(
                    f"{element.name} overlaps the discussion panel"
                )

        assert_inside(user_to_service, MAIN_PANEL)
        assert_inside(service_to_database, MAIN_PANEL)

        if panel.bounds.overlaps(MAIN_PANEL):
            raise LayoutError(
                "discussion panel overlaps main animation panel"
            )

        if RIGHT_PANEL.right > CANVAS.width:
            raise LayoutError(
                "discussion panel exceeds canvas width"
            )

        if RIGHT_PANEL.bottom > CANVAS.height:
            raise LayoutError(
                "discussion panel exceeds canvas height"
            )

    except LayoutError as error:
        print("LAYOUT VALIDATION: FAILED")
        print(f"- {error}")
        raise SystemExit(1) from error

    print("LAYOUT VALIDATION: PASS")


def make_frame(
    canvas,
    user,
    service,
    database,
    order,
    validation,
    user_to_service,
    service_to_database,
    modification,
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
        "Security is not only about who can see data — it is also about whether the data stays correct.",
        font=font(14),
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
        "INTEGRITY",
        font=font(13, True),
        fill=BLUE,
    )

    # ------------------------------------------------------------------
    # Legitimate request path
    # ------------------------------------------------------------------

    user_to_service.draw(
        image,
        elapsed,
        active=False,
    )

    service_to_database.draw(
        image,
        elapsed,
        active=False,
    )

    if elapsed >= REQUEST_REVEAL:
        particle.draw(image, elapsed)

    # ------------------------------------------------------------------
    # System components
    # ------------------------------------------------------------------

    user.draw(
        image,
        elapsed,
        active=USER_REVEAL <= elapsed < REQUEST_REVEAL,
    )

    service.draw(
        image,
        elapsed,
        active=REQUEST_REVEAL <= elapsed < ORDER_REVEAL,
    )

    database.draw(
        image,
        elapsed,
        active=ORDER_REVEAL <= elapsed < MODIFICATION_REVEAL,
    )

    # ------------------------------------------------------------------
    # Order data
    # ------------------------------------------------------------------

    order.draw(
        image,
        elapsed,
        active=elapsed >= MODIFICATION_REVEAL,
    )

    # ------------------------------------------------------------------
    # Unauthorized modification
    # ------------------------------------------------------------------

    modification.draw(
        image,
        elapsed,
        active=elapsed >= MODIFICATION_REVEAL,
    )

    # ------------------------------------------------------------------
    # Integrity validation
    # ------------------------------------------------------------------

    validation.draw(
        image,
        elapsed,
        active=elapsed >= VALIDATION_REVEAL,
    )

    # ------------------------------------------------------------------
    # Final takeaway
    # ------------------------------------------------------------------

    takeaway.draw(
        image,
        elapsed,
    )

    # ------------------------------------------------------------------
    # Discussion panel
    # ------------------------------------------------------------------

    panel.draw(
        image,
        elapsed,
    )

    return image


def render_scene(output: Path):
    (
        user,
        service,
        database,
        order,
        validation,
        user_to_service,
        service_to_database,
        modification,
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
        user,
        service,
        database,
        order,
        validation,
        modification,
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
        user,
        service,
        database,
        order,
        validation,
        user_to_service,
        service_to_database,
        modification,
        takeaway,
        panel,
    )

    Renderer(CANVAS).render(
        lambda elapsed: make_frame(
            CANVAS,
            user,
            service,
            database,
            order,
            validation,
            user_to_service,
            service_to_database,
            modification,
            takeaway,
            panel,
            particle,
            elapsed,
        ),
        output,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Render Scene 5 - Integrity Breach"
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=(
            ROOT
            / "output"
            / "Cyber_Attack_X_FAANG_Video01_Scene05.mp4"
        ),
    )

    args = parser.parse_args()

    render_scene(args.output)


if __name__ == "__main__":
    main()