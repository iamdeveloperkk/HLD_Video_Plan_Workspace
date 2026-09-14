"""Scene 6 composition: Availability Attack.

Story:

    Normal traffic
        ↓
    Traffic suddenly increases
        ↓
    Queues grow
        ↓
    Latency increases
        ↓
    Service becomes unavailable
        ↓
    Defensive controls absorb/reject excess traffic
        ↓
    Service recovers

The scene demonstrates the availability dimension of the CIA triad
without teaching an operational DDoS recipe.
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

from scenes.scene_06_code.config import (
    DEFENSE_RECT,
    DEFENSE_REVEAL,
    EDGE_RECT,
    FAILURE_REVEAL,
    LATENCY_REVEAL,
    MAIN_PANEL as MAIN_PANEL_VALUES,
    NORMAL_TRAFFIC_REVEAL,
    PANEL_TITLE,
    QUEUE_RECT,
    QUEUE_REVEAL,
    RECOVERY_REVEAL,
    RIGHT_PANEL as RIGHT_PANEL_VALUES,
    SERVICE_RECT,
    SERVICE_REVEAL,
    TAKEAWAY,
    TAKEAWAY_REVEAL,
    TRAFFIC_SPIKE_REVEAL,
    USERS_RECT,
    USERS_REVEAL,
)


MAIN_PANEL = Rect(*MAIN_PANEL_VALUES)
RIGHT_PANEL = Rect(*RIGHT_PANEL_VALUES)

RED = (235, 70, 80)
GREEN = (75, 200, 130)
YELLOW = (235, 185, 75)


def alpha_color(color, opacity: float):
    return (*color, int(max(0.0, min(1.0, opacity)) * 255))


class FlowNode(Component):
    """Reusable node that is compatible with Particle routes."""

    def __init__(
        self,
        name: str,
        label: str,
        bounds: Rect,
        reveal: float,
        subtitle: str = "",
    ):
        super().__init__(
            name,
            bounds,
            reveal=reveal,
        )

        self.label = label
        self.subtitle = subtitle

    def input(self):
        return (
            self.x,
            self.y + self.height / 2,
        )

    def output(self):
        return (
            self.x + self.width,
            self.y + self.height / 2,
        )

    def draw(
        self,
        image,
        elapsed: float,
        active: bool = False,
    ) -> None:
        opacity = self.opacity(
            elapsed,
            0.55,
        )

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
            fill=alpha_color(
                PANEL,
                opacity,
            ),
            outline=alpha_color(
                border,
                opacity,
            ),
            width=2,
        )

        centered_text(
            draw,
            (
                self.x + 10,
                self.y + 18,
                self.bounds.right - 10,
                self.y + 58,
            ),
            self.label,
            font(17, True),
            alpha_color(
                WHITE,
                opacity,
            ),
        )

        if self.subtitle:
            centered_text(
                draw,
                (
                    self.x + 10,
                    self.y + 62,
                    self.bounds.right - 10,
                    self.bounds.bottom - 10,
                ),
                self.subtitle,
                font(12),
                alpha_color(
                    MUTED,
                    opacity,
                ),
            )


class FlowArrow(Component):
    """Directional connection between system components."""

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

    def draw(
        self,
        image,
        elapsed: float,
        active: bool = False,
    ) -> None:
        opacity = self.opacity(
            elapsed,
            0.45,
        )

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        color = RED if active else self.color

        x1, y1 = self.start
        x2, y2 = self.end

        draw.line(
            (
                x1,
                y1,
                x2,
                y2,
            ),
            fill=alpha_color(
                color,
                opacity,
            ),
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
            fill=alpha_color(
                color,
                opacity,
            ),
        )


class TrafficMeter(Component):
    """Shows traffic volume changing over time."""

    def __init__(
        self,
        bounds: Rect,
        reveal: float,
    ):
        super().__init__(
            "TrafficMeter",
            bounds,
            reveal=reveal,
            allow_overlap=True,
        )

    def draw(
        self,
        image,
        elapsed: float,
        active: bool = False,
    ) -> None:
        opacity = self.opacity(
            elapsed,
            0.5,
        )

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        if elapsed < TRAFFIC_SPIKE_REVEAL:
            value = "12K req/s"
            status = "NORMAL TRAFFIC"
            status_color = GREEN
            fill_ratio = 0.28

        elif elapsed < RECOVERY_REVEAL:
            value = "180K req/s"
            status = "TRAFFIC SPIKE"
            status_color = RED
            fill_ratio = 0.92

        else:
            value = "18K req/s"
            status = "TRAFFIC NORMALIZED"
            status_color = GREEN
            fill_ratio = 0.35

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=8,
            fill=alpha_color(
                PANEL,
                opacity,
            ),
            outline=alpha_color(
                BLUE,
                opacity,
            ),
            width=1,
        )

        draw.text(
            (
                self.x + 15,
                self.y + 8,
            ),
            "TRAFFIC",
            font=font(11, True),
            fill=alpha_color(
                MUTED,
                opacity,
            ),
        )

        draw.text(
            (
                self.x + 15,
                self.y + 27,
            ),
            value,
            font=font(19, True),
            fill=alpha_color(
                status_color,
                opacity,
            ),
        )

        bar_x = self.x + 15
        bar_y = self.y + 59
        bar_width = self.width - 30
        bar_height = 8

        draw.rounded_rectangle(
            (
                bar_x,
                bar_y,
                bar_x + bar_width,
                bar_y + bar_height,
            ),
            radius=4,
            fill=alpha_color(
                (35, 55, 75),
                opacity,
            ),
        )

        draw.rounded_rectangle(
            (
                bar_x,
                bar_y,
                bar_x + bar_width * fill_ratio,
                bar_y + bar_height,
            ),
            radius=4,
            fill=alpha_color(
                status_color,
                opacity,
            ),
        )

        draw.text(
            (
                self.x + 15,
                self.y + 73,
            ),
            status,
            font=font(10, True),
            fill=alpha_color(
                status_color,
                opacity,
            ),
        )


class QueueMeter(Component):
    """Visualizes growing request backlog."""

    def __init__(
        self,
        bounds: Rect,
        reveal: float,
    ):
        super().__init__(
            "QueueMeter",
            bounds,
            reveal=reveal,
            allow_overlap=True,
        )

    def draw(
        self,
        image,
        elapsed: float,
        active: bool = False,
    ) -> None:
        opacity = self.opacity(
            elapsed,
            0.5,
        )

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        if elapsed < TRAFFIC_SPIKE_REVEAL:
            count = 18
            color = GREEN
            status = "HEALTHY"

        elif elapsed < RECOVERY_REVEAL:
            count = min(
                950,
                int(
                    18
                    + max(
                        0,
                        elapsed - TRAFFIC_SPIKE_REVEAL,
                    )
                    * 180
                ),
            )
            color = RED
            status = "BACKLOG GROWING"

        else:
            count = 24
            color = GREEN
            status = "QUEUE CLEARING"

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=10,
            fill=alpha_color(
                PANEL,
                opacity,
            ),
            outline=alpha_color(
                color,
                opacity,
            ),
            width=2,
        )

        draw.text(
            (
                self.x + 15,
                self.y + 9,
            ),
            "REQUEST QUEUE",
            font=font(11, True),
            fill=alpha_color(
                MUTED,
                opacity,
            ),
        )

        draw.text(
            (
                self.x + 15,
                self.y + 29,
            ),
            f"{count:,}",
            font=font(20, True),
            fill=alpha_color(
                color,
                opacity,
            ),
        )

        draw.text(
            (
                self.x + 85,
                self.y + 34,
            ),
            status,
            font=font(10, True),
            fill=alpha_color(
                color,
                opacity,
            ),
        )


class ServiceStatus(Component):
    """Shows service health and latency."""

    def __init__(
        self,
        bounds: Rect,
        reveal: float,
    ):
        super().__init__(
            "ServiceStatus",
            bounds,
            reveal=reveal,
            allow_overlap=True,
        )

    def draw(
        self,
        image,
        elapsed: float,
        active: bool = False,
    ) -> None:
        opacity = self.opacity(
            elapsed,
            0.5,
        )

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        if elapsed < TRAFFIC_SPIKE_REVEAL:
            latency = "42 ms"
            status = "HEALTHY"
            status_color = GREEN

        elif elapsed < FAILURE_REVEAL:
            latency = "2.8 s"
            status = "DEGRADED"
            status_color = YELLOW

        elif elapsed < RECOVERY_REVEAL:
            latency = "TIMEOUT"
            status = "UNAVAILABLE"
            status_color = RED

        else:
            latency = "55 ms"
            status = "RECOVERED"
            status_color = GREEN

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=10,
            fill=alpha_color(
                PANEL,
                opacity,
            ),
            outline=alpha_color(
                status_color,
                opacity,
            ),
            width=2,
        )

        draw.text(
            (
                self.x + 15,
                self.y + 12,
            ),
            "SERVICE HEALTH",
            font=font(11, True),
            fill=alpha_color(
                MUTED,
                opacity,
            ),
        )

        draw.text(
            (
                self.x + 15,
                self.y + 34,
            ),
            latency,
            font=font(21, True),
            fill=alpha_color(
                status_color,
                opacity,
            ),
        )

        draw.text(
            (
                self.x + 15,
                self.y + 69,
            ),
            status,
            font=font(11, True),
            fill=alpha_color(
                status_color,
                opacity,
            ),
        )


class DefenseNode(Component):
    """Rate limiting / traffic protection layer."""

    def __init__(
        self,
        bounds: Rect,
        reveal: float,
    ):
        super().__init__(
            "Defense",
            bounds,
            reveal=reveal,
        )

    def input(self):
        return (
            self.x,
            self.y + self.height / 2,
        )

    def output(self):
        return (
            self.x + self.width,
            self.y + self.height / 2,
        )

    def draw(
        self,
        image,
        elapsed: float,
        active: bool = False,
    ) -> None:
        opacity = self.opacity(
            elapsed,
            0.55,
        )

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        if elapsed < RECOVERY_REVEAL:
            border = BLUE
            label = "RATE LIMIT"
            subtitle = "PROTECT"
        else:
            border = GREEN
            label = "RATE LIMIT"
            subtitle = "ACTIVE"

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=10,
            fill=alpha_color(
                PANEL,
                opacity,
            ),
            outline=alpha_color(
                border,
                opacity,
            ),
            width=2,
        )

        centered_text(
            draw,
            (
                self.x + 5,
                self.y + 20,
                self.bounds.right - 5,
                self.y + 55,
            ),
            label,
            font(13, True),
            alpha_color(
                WHITE,
                opacity,
            ),
        )

        centered_text(
            draw,
            (
                self.x + 5,
                self.y + 58,
                self.bounds.right - 5,
                self.bounds.bottom - 12,
            ),
            subtitle,
            font(12, True),
            alpha_color(
                border,
                opacity,
            ),
        )


class FailureBanner(Component):
    """Temporary availability failure indicator."""

    def __init__(
        self,
        bounds: Rect,
        reveal: float,
    ):
        super().__init__(
            "FailureBanner",
            bounds,
            reveal=reveal,
            allow_overlap=True,
        )

    def draw(
        self,
        image,
        elapsed: float,
        active: bool = False,
    ) -> None:
        opacity = self.opacity(
            elapsed,
            0.5,
        )

        if opacity <= 0:
            return

        draw = ImageDraw.Draw(image)

        if elapsed >= RECOVERY_REVEAL:
            border = GREEN
            text = "SERVICE RECOVERED"
        else:
            border = RED
            text = "SERVICE UNAVAILABLE"

        draw.rounded_rectangle(
            (
                self.x,
                self.y,
                self.bounds.right,
                self.bounds.bottom,
            ),
            radius=8,
            fill=alpha_color(
                PANEL,
                opacity,
            ),
            outline=alpha_color(
                border,
                opacity,
            ),
            width=2,
        )

        centered_text(
            draw,
            (
                self.x + 8,
                self.y + 6,
                self.bounds.right - 8,
                self.bounds.bottom - 6,
            ),
            text,
            font(13, True),
            alpha_color(
                border,
                opacity,
            ),
        )


class Takeaway(Component):
    """Final scene takeaway."""

    def __init__(
        self,
        bounds: Rect,
        reveal: float,
    ):
        super().__init__(
            "Takeaway",
            bounds,
            reveal=reveal,
            allow_overlap=True,
        )

    def draw(
        self,
        image,
        elapsed: float,
        active: bool = False,
    ) -> None:
        opacity = self.opacity(
            elapsed,
            0.7,
        )

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
            fill=alpha_color(
                PANEL,
                opacity,
            ),
            outline=alpha_color(
                BLUE,
                opacity,
            ),
            width=1,
        )

        draw.text(
            (
                self.x + 18,
                self.y + 8,
            ),
            "TAKEAWAY",
            font=font(11, True),
            fill=alpha_color(
                BLUE,
                opacity,
            ),
        )

        draw.text(
            (
                self.x + 18,
                self.y + 27,
            ),
            TAKEAWAY,
            font=font(16, True),
            fill=alpha_color(
                WHITE,
                opacity,
            ),
        )


def build_scene():
    users = FlowNode(
        "Users",
        "USERS",
        Rect(*USERS_RECT),
        USERS_REVEAL,
        "Requests arrive",
    )

    edge = FlowNode(
        "Edge",
        "EDGE / WAF",
        Rect(*EDGE_RECT),
        SERVICE_REVEAL,
        "Filters traffic",
    )

    service = FlowNode(
        "Service",
        "APPLICATION",
        Rect(*SERVICE_RECT),
        SERVICE_REVEAL,
        "Processes requests",
    )

    queue = QueueMeter(
        Rect(*QUEUE_RECT),
        QUEUE_REVEAL,
    )

    defense = DefenseNode(
        Rect(*DEFENSE_RECT),
        DEFENSE_REVEAL,
    )

    traffic = TrafficMeter(
        Rect(
            MAIN_PANEL.x + 30,
            MAIN_PANEL.y + 55,
            210,
            100,
        ),
        NORMAL_TRAFFIC_REVEAL,
    )

    service_status = ServiceStatus(
        Rect(
            520,
            145,
            190,
            65,
        ),
        LATENCY_REVEAL,
    )

    failure = FailureBanner(
        Rect(
            65,
            390,
            205,
            45,
        ),
        FAILURE_REVEAL,
    )

    user_to_edge = FlowArrow(
        "UserToEdge",
        users.output(),
        edge.input(),
        SERVICE_REVEAL,
    )

    edge_to_service = FlowArrow(
        "EdgeToService",
        edge.output(),
        service.input(),
        SERVICE_REVEAL,
    )

    # Normal request particle.
    normal_particle = Particle(
        users,
        service,
        route=[
            users,
            edge,
            service,
        ],
        start=NORMAL_TRAFFIC_REVEAL,
        duration=2.5,
    )

    # Excess traffic is visually represented by a second stream. It is not
    # an operational attack recipe; it simply communicates saturation.
    spike_particle = Particle(
        users,
        edge,
        route=[
            users,
            edge,
        ],
        start=TRAFFIC_SPIKE_REVEAL,
        duration=0.8,
    )

    takeaway = Takeaway(
        Rect(
            MAIN_PANEL.x + 25,
            MAIN_PANEL.bottom - 75,
            MAIN_PANEL.width - 50,
            50,
        ),
        TAKEAWAY_REVEAL,
    )

    panel = DiscussionPanel(
        PANEL_TITLE,
        [
            "Normal traffic keeps the system healthy",
            "A sudden flood consumes capacity",
            "Queues grow and latency increases",
            "Eventually users cannot reach the service",
        ],
        RIGHT_PANEL.x,
        RIGHT_PANEL.y,
        RIGHT_PANEL.width,
        RIGHT_PANEL.height,
        [
            USERS_REVEAL,
            TRAFFIC_SPIKE_REVEAL,
            QUEUE_REVEAL,
            FAILURE_REVEAL,
        ],
    )

    return (
        users,
        edge,
        service,
        queue,
        defense,
        traffic,
        service_status,
        failure,
        user_to_edge,
        edge_to_service,
        normal_particle,
        spike_particle,
        takeaway,
        panel,
    )


def validate_scene(
    users,
    edge,
    service,
    queue,
    defense,
    traffic,
    service_status,
    failure,
    user_to_edge,
    edge_to_service,
    takeaway,
    panel,
):
    try:
        elements = [
            users,
            edge,
            service,
            queue,
            defense,
            traffic,
            service_status,
            failure,
            takeaway,
        ]

        validate_elements(
            elements,
            MAIN_PANEL,
        )

        for element in elements:
            if element.bounds.overlaps(RIGHT_PANEL):
                raise LayoutError(
                    f"{element.name} overlaps the discussion panel"
                )

        assert_inside(
            user_to_edge,
            MAIN_PANEL,
        )

        assert_inside(
            edge_to_service,
            MAIN_PANEL,
        )

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
    users,
    edge,
    service,
    queue,
    defense,
    traffic,
    service_status,
    failure,
    user_to_edge,
    edge_to_service,
    normal_particle,
    spike_particle,
    takeaway,
    panel,
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
        "What happens when the system can no longer serve legitimate users?",
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
        (
            MAIN_PANEL.x + 25,
            MAIN_PANEL.y + 22,
        ),
        "AVAILABILITY",
        font=font(13, True),
        fill=BLUE,
    )

    # ------------------------------------------------------------------
    # Flow
    # ------------------------------------------------------------------

    user_to_edge.draw(
        image,
        elapsed,
        active=TRAFFIC_SPIKE_REVEAL <= elapsed < FAILURE_REVEAL,
    )

    edge_to_service.draw(
        image,
        elapsed,
        active=TRAFFIC_SPIKE_REVEAL <= elapsed < FAILURE_REVEAL,
    )

    # ------------------------------------------------------------------
    # Traffic
    # ------------------------------------------------------------------

    traffic.draw(
        image,
        elapsed,
    )

    # ------------------------------------------------------------------
    # Components
    # ------------------------------------------------------------------

    users.draw(
        image,
        elapsed,
        active=USERS_REVEAL <= elapsed < TRAFFIC_SPIKE_REVEAL,
    )

    edge.draw(
        image,
        elapsed,
        active=TRAFFIC_SPIKE_REVEAL <= elapsed < DEFENSE_REVEAL,
    )

    service.draw(
        image,
        elapsed,
        active=TRAFFIC_SPIKE_REVEAL <= elapsed < FAILURE_REVEAL,
    )

    # ------------------------------------------------------------------
    # Particles
    # ------------------------------------------------------------------

    if elapsed >= NORMAL_TRAFFIC_REVEAL:
        normal_particle.draw(
            image,
            elapsed,
        )

    if elapsed >= TRAFFIC_SPIKE_REVEAL:
        spike_particle.draw(
            image,
            elapsed,
        )

    # ------------------------------------------------------------------
    # Queue / service state
    # ------------------------------------------------------------------

    queue.draw(
        image,
        elapsed,
        active=elapsed >= QUEUE_REVEAL,
    )

    service_status.draw(
        image,
        elapsed,
        active=elapsed >= LATENCY_REVEAL,
    )

    # ------------------------------------------------------------------
    # Defense
    # ------------------------------------------------------------------

    defense.draw(
        image,
        elapsed,
        active=elapsed >= DEFENSE_REVEAL,
    )

    # ------------------------------------------------------------------
    # Failure
    # ------------------------------------------------------------------

    failure.draw(
        image,
        elapsed,
        active=elapsed >= FAILURE_REVEAL,
    )

    # ------------------------------------------------------------------
    # Takeaway
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
        users,
        edge,
        service,
        queue,
        defense,
        traffic,
        service_status,
        failure,
        user_to_edge,
        edge_to_service,
        normal_particle,
        spike_particle,
        takeaway,
        panel,
    ) = build_scene()

    print(
        f"main_panel: "
        f"x={MAIN_PANEL.x}, "
        f"y={MAIN_PANEL.y}, "
        f"w={MAIN_PANEL.width}, "
        f"h={MAIN_PANEL.height}"
    )

    print(
        f"right_panel: "
        f"x={RIGHT_PANEL.x}, "
        f"y={RIGHT_PANEL.y}, "
        f"w={RIGHT_PANEL.width}, "
        f"h={RIGHT_PANEL.height}"
    )

    for element in [
        users,
        edge,
        service,
        queue,
        defense,
        traffic,
        service_status,
        failure,
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
        users,
        edge,
        service,
        queue,
        defense,
        traffic,
        service_status,
        failure,
        user_to_edge,
        edge_to_service,
        takeaway,
        panel,
    )

    Renderer(CANVAS).render(
        lambda elapsed: make_frame(
            CANVAS,
            users,
            edge,
            service,
            queue,
            defense,
            traffic,
            service_status,
            failure,
            user_to_edge,
            edge_to_service,
            normal_particle,
            spike_particle,
            takeaway,
            panel,
            elapsed,
        ),
        output,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Render Scene 6 - Availability Attack"
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=(
            ROOT
            / "output"
            / "Cyber_Attack_X_FAANG_Video01_Scene06.mp4"
        ),
    )

    args = parser.parse_args()

    render_scene(args.output)


if __name__ == "__main__":
    main()