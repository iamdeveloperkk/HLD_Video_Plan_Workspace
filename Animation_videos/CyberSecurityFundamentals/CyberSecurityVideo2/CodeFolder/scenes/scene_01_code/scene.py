"""Scene 1: conceptual SQL injection flow through an HLD architecture."""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import ImageDraw

ROOT = Path(__file__).resolve().parents[5]
ANIMATION_ROOT = ROOT
SHARED_ROOT = ANIMATION_ROOT / "_common"
VIDEO_ROOT = ANIMATION_ROOT / "CyberSecurityFundamentals" / "CyberSecurityVideo2"
CODE_ROOT = VIDEO_ROOT / "CodeFolder"
for path in (ANIMATION_ROOT, CODE_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from _common.engine.arrows import Arrow
from _common.engine.canvas import BLUE, PANEL, WHITE, MUTED
from _common.engine.components import Component
from _common.engine.icon_node import IconNode
from _common.engine.icon_registry import configure_asset_roots
from _common.engine.layout import LayoutError, Rect, validate_elements
from _common.engine.nodes import alpha_color
from _common.engine.panels import DiscussionPanel
from _common.engine.particles import Particle
from _common.engine.renderer import Renderer
from _common.engine.typography import centered_text, font
from video_config import CANVAS
from scenes.scene_01_code.config import *


configure_asset_roots(VIDEO_ROOT / "AssetFolder", SHARED_ROOT / "assets")

MAIN_RECT = Rect(*MAIN_PANEL)
RIGHT_RECT = Rect(*RIGHT_PANEL)


class Takeaway(Component):
    def __init__(self):
        super().__init__("Takeaway", Rect(60, 528, 825, 54), reveal=TAKEAWAY_REVEAL, allow_overlap=True)

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed, 0.7)
        if opacity <= 0:
            return
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle(
            (self.x, self.y, self.bounds.right, self.bounds.bottom),
            radius=10,
            fill=alpha_color(PANEL, opacity),
            outline=alpha_color(BLUE, opacity),
            width=1,
        )
        draw.text((self.x + 18, self.y + 9), "TAKEAWAY", font=font(11, True), fill=alpha_color(BLUE, opacity))
        draw.text((self.x + 18, self.y + 27), TAKEAWAY, font=font(15, True), fill=alpha_color(WHITE, opacity))


def make_node(name: str, label: str, icon: str, subtitle: str) -> IconNode:
    x, y, width, height = NODE_LAYOUT[name]
    return IconNode(
        icon=icon,
        label=label,
        width=width,
        height=height,
        x=x,
        y=y,
        sequence=list(("client", "gateway", "service", "database", "attacker")).index(name) + 1,
        reveal=NODE_REVEALS[name],
        icon_size=52 if name != "attacker" else 44,
    )


def build_scene():
    client = make_node("client", "CLIENT", "actors.client", "user-controlled input")
    gateway = make_node("gateway", "API GATEWAY", "aws.api_gateway", "request entry point")
    service = make_node("service", "ECS SERVICE", "aws.ecs", "builds query")
    database = make_node("database", "RDS", "aws.rds", "stores data")
    attacker = make_node("attacker", "ATTACKER", "generic.attacker", "malicious request")

    nodes = [client, gateway, service, database, attacker]
    arrows = [
        Arrow(client, gateway, reveal=NODE_REVEALS["gateway"] - 0.35),
        Arrow(gateway, service, reveal=NODE_REVEALS["service"] - 0.35),
        Arrow(service, database, reveal=NODE_REVEALS["database"] - 0.35),
    ]
    normal_particle = Particle(client, database, route=[client, gateway, service, database], start=6.4, duration=3.0, color=(185, 235, 255))
    attack_particle = Particle(attacker, database, route=[attacker, gateway, service, database], start=9.2, duration=3.2, color=(235, 70, 80))
    discussion = DiscussionPanel(
        "SQL INJECTION",
        DISCUSSION_POINTS,
        RIGHT_RECT.x,
        RIGHT_RECT.y,
        RIGHT_RECT.width,
        RIGHT_RECT.height,
        DISCUSSION_REVEALS,
    )
    takeaway = Takeaway()
    return nodes, arrows, normal_particle, attack_particle, discussion, takeaway


def validate_scene(nodes, arrows, discussion, takeaway):
    try:
        validate_elements(nodes, MAIN_RECT)
        validate_elements([takeaway], MAIN_RECT)
        for arrow in arrows:
            if not MAIN_RECT.contains(arrow.bounds):
                raise LayoutError(f"{arrow.name} crosses the main panel")
        if discussion.bounds.overlaps(MAIN_RECT):
            raise LayoutError("discussion panel overlaps the main panel")
    except LayoutError as error:
        print("LAYOUT VALIDATION: FAILED")
        print(f"- {error}")
        raise SystemExit(1) from error
    print("LAYOUT VALIDATION: PASS")


def active_node_index(elapsed: float, start: float, duration: float, count: int):
    if elapsed < start or elapsed > start + duration:
        return None
    return min(count - 1, int(((elapsed - start) / duration) * (count - 1)))


def make_frame(elapsed: float):
    nodes, arrows, normal_particle, attack_particle, discussion, takeaway = build_scene()
    image = Renderer(CANVAS).background()
    draw = ImageDraw.Draw(image)
    draw.text((50, 35), SCENE_TITLE, font=font(26, True), fill=WHITE)
    draw.text((50, 70), "A request becomes dangerous when input changes query meaning.", font=font(16), fill=MUTED)
    draw.rounded_rectangle((MAIN_RECT.x, MAIN_RECT.y, MAIN_RECT.right, MAIN_RECT.bottom), radius=14, fill=PANEL, outline=(29, 75, 121), width=2)
    draw.text((MAIN_RECT.x + 25, MAIN_RECT.y + 22), "APPLICATION DATA PATH", font=font(13, True), fill=BLUE)

    for arrow in arrows:
        arrow.draw(image, elapsed)

    normal_particle.draw(image, elapsed)
    attack_particle.draw(image, elapsed)

    normal_active = active_node_index(elapsed, normal_particle.start, normal_particle.duration, 4)
    attack_active = active_node_index(elapsed, attack_particle.start, attack_particle.duration, 4)
    for index, node in enumerate(nodes):
        active = index == normal_active or (index > 0 and index - 1 == attack_active)
        node.draw(image, elapsed, active=active)

    if elapsed >= 6.0:
        draw.rounded_rectangle((300, 390, 700, 455), radius=10, fill=alpha_color((65, 35, 40), 0.92), outline=alpha_color((235, 70, 80), 0.95), width=2)
        centered_text(draw, (315, 398, 685, 425), "USER-CONTROLLED INPUT", font(16, True), WHITE)
        centered_text(draw, (315, 425, 685, 448), "query altered → unexpected database operation", font(13), WHITE)

    if elapsed >= 9.2:
        draw.text((70, 410), "MALICIOUS REQUEST", font=font(12, True), fill=(235, 70, 80))

    discussion.draw(image, elapsed)
    takeaway.draw(image, elapsed)
    return image


def render_scene(output: Path) -> None:
    nodes, arrows, _, _, discussion, takeaway = build_scene()
    validate_scene(nodes, arrows, discussion, takeaway)
    Renderer(CANVAS).render(make_frame, output)


if __name__ == "__main__":
    render_scene(Path("scene_output.mp4"))
