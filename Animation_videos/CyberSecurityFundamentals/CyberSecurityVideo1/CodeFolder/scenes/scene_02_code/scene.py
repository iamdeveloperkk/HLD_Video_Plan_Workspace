"""Scene 2 composition: The Big-Tech Architecture."""

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
VIDEO_ROOT = SHARED_ROOT / "CyberSecurityFundamentals" / "CyberSecurityVideo1" / "CodeFolder"
if str(VIDEO_ROOT) not in sys.path:
    sys.path.insert(0, str(VIDEO_ROOT))

from PIL import ImageDraw

from _common.engine.arrows import Arrow
from _common.engine.canvas import BLUE, Canvas, PANEL, WHITE, MUTED
from _common.engine.components import Component
from _common.engine.icon_node import IconNode
from _common.engine.icon_registry import configure_asset_roots
from _common.engine.layout import LayoutError, Rect, assert_inside, validate_elements
from _common.engine.nodes import Node
from _common.engine.panels import DiscussionPanel
from _common.engine.particles import Particle
from _common.engine.renderer import Renderer
from _common.engine.timeline import Timeline
from _common.engine.typography import font
from video_config import CANVAS
from scenes.scene_02_code.config import ARCHITECTURE_SEPARATION, MAIN_PANEL as MAIN_PANEL_VALUES, NODE_REVEALS, RIGHT_PANEL as RIGHT_PANEL_VALUES


MAIN_PANEL = Rect(*MAIN_PANEL_VALUES)
RIGHT_PANEL = Rect(*RIGHT_PANEL_VALUES)
NODE_SPECS = [
    ("USERS", 135, NODE_REVEALS["USERS"], "generic.user", IconNode),
    ("CDN / WAF", 145, NODE_REVEALS["CDN / WAF"], None, Node),
    ("API GATEWAY", 155, NODE_REVEALS["API GATEWAY"], "aws.api_gateway", IconNode),
    ("SERVICES", 135, NODE_REVEALS["SERVICES"], None, Node),
    ("DATABASE", 135, NODE_REVEALS["DATABASE"], "generic.database", IconNode),
]

SCENE_ROOT = VIDEO_ROOT / "scenes" / "scene_02_code"
configure_asset_roots(SCENE_ROOT / "assets" / "icons", VIDEO_ROOT.parent / "AssetFolder" / "icons")


class Takeaway(Component):
    def __init__(self, bounds: Rect, reveal: float):
        super().__init__("Takeaway", bounds, reveal=reveal, allow_overlap=True)

    def draw(self, image, elapsed: float, active: bool = False) -> None:
        opacity = self.opacity(elapsed, 0.8)
        if opacity <= 0:
            return
        draw = ImageDraw.Draw(image)
        fill = (*PANEL, int(opacity * 255))
        outline = (*BLUE, int(opacity * 255))
        draw.rounded_rectangle((self.x, self.y, self.bounds.right, self.bounds.bottom), radius=8, fill=fill, outline=outline, width=1)
        draw.text((self.x + 18, self.y + 9), "TAKEAWAY", font=font(11, True), fill=(*BLUE, int(opacity * 255)))
        draw.text((self.x + 18, self.y + 26), "SECURITY BOUNDARIES EXIST AT EVERY STEP", font=font(16, True), fill=(*WHITE, int(opacity * 255)))


def build_scene():
    side_padding = 30
    available_width = MAIN_PANEL.width - side_padding * 2
    total_node_width = sum(spec[1] for spec in NODE_SPECS)
    number_of_gaps = len(NODE_SPECS) - 1
    gap = (available_width - total_node_width) / number_of_gaps
    if not 20 <= gap <= 30:
        raise LayoutError(f"calculated gap {gap:.2f}px is outside the 20-30px range")

    nodes = []
    current_x = MAIN_PANEL.x + side_padding
    node_y = MAIN_PANEL.y + 167
    for sequence, (label, width, reveal, icon, node_type) in enumerate(NODE_SPECS, start=1):
        kwargs = dict(width=width, height=105, x=current_x, y=node_y, sequence=sequence, reveal=reveal)
        node = node_type(icon=icon, label=label, **kwargs) if node_type is IconNode else node_type(label=label, **kwargs)
        nodes.append(node)
        current_x += width + gap

    arrows = [Arrow(nodes[index], nodes[index + 1], reveal=NODE_SPECS[index + 1][2] - 0.55) for index in range(len(nodes) - 1)]
    timeline = Timeline().place(MAIN_PANEL.x + 35, MAIN_PANEL.bottom - 38, MAIN_PANEL.width - 70)
    for node in nodes:
        timeline.add(node, node.reveal, 0.55, "fade_in")
    takeaway = Takeaway(Rect(MAIN_PANEL.x + 25, MAIN_PANEL.y + 390, MAIN_PANEL.width - 50, 54), 9.4)
    panel = DiscussionPanel(
        "THE SYSTEM",
        ["Users generate requests", "Edge layer filters traffic", "Gateway routes requests", "Services execute logic", "Database stores state"],
        RIGHT_PANEL.x,
        RIGHT_PANEL.y,
        RIGHT_PANEL.width,
        RIGHT_PANEL.height,
        [0.8, 2.6, 4.4, 6.2, 8.0],
    )
    particle = Particle(nodes[0], nodes[-1], route=nodes, start=8.65, duration=5.2)
    return nodes, arrows, timeline, takeaway, panel, particle, gap, available_width, total_node_width, number_of_gaps


def validate_scene(nodes, arrows, timeline, takeaway, panel):
    try:
        validate_elements(nodes + [takeaway], MAIN_PANEL)
        for node in nodes:
            if node.bounds.right > RIGHT_PANEL.x - ARCHITECTURE_SEPARATION:
                raise LayoutError(f"{node.name} is too close to the discussion panel")
        for arrow in arrows:
            assert_inside(arrow, MAIN_PANEL)
        assert_inside(timeline, MAIN_PANEL)
        if panel.bounds.overlaps(MAIN_PANEL):
            raise LayoutError("discussion panel overlaps architecture panel")
    except LayoutError as error:
        print("LAYOUT VALIDATION: FAILED")
        print(f"- {error}")
        raise SystemExit(1) from error
    print("LAYOUT VALIDATION: PASS")


def print_layout(nodes, gap, available_width, total_node_width, number_of_gaps):
    print(f"available_width: {available_width:.2f}px")
    print(f"node_width_total: {total_node_width:.2f}px")
    print(f"number_of_gaps: {number_of_gaps}")
    print(f"gap: {gap:.2f}px")
    for node in nodes:
        print(f"{node.label}: x={node.x:.2f}, y={node.y:.2f}, w={node.width}, h={node.height}")


def make_frame(canvas, nodes, arrows, timeline, takeaway, panel, particle, elapsed):
    renderer = Renderer(canvas)
    image = renderer.background()
    draw = ImageDraw.Draw(image)
    draw.text((50, 35), "NEXA SECURITY ARCHITECTURE", font=font(26, True), fill=WHITE)
    draw.text((50, 70), "Every request crosses multiple security boundaries.", font=font(16), fill=MUTED)
    draw.rounded_rectangle((MAIN_PANEL.x, MAIN_PANEL.y, MAIN_PANEL.right, MAIN_PANEL.bottom), radius=14, fill=PANEL, outline=(29, 75, 121), width=2)
    draw.text((MAIN_PANEL.x + 25, MAIN_PANEL.y + 22), "REQUEST PATH", font=font(13, True), fill=BLUE)
    for index, arrow in enumerate(arrows):
        arrow.draw(image, elapsed)
    particle.draw(image, elapsed)
    active_index = None
    if elapsed >= particle.start:
        particle_progress = min(1.0, max(0.0, (elapsed - particle.start) / particle.duration))
        active_index = min(len(nodes) - 1, int(particle_progress * (len(nodes) - 1)))
    for node_index, node in enumerate(nodes):
        active = active_index == node_index
        node.draw(image, elapsed, active=active)
    timeline.draw(image, elapsed)
    takeaway.draw(image, elapsed)
    panel.draw(image, elapsed)
    return image


def render_scene(output: Path):
    canvas = CANVAS
    nodes, arrows, timeline, takeaway, panel, particle, gap, available_width, total_node_width, number_of_gaps = build_scene()
    print_layout(nodes, gap, available_width, total_node_width, number_of_gaps)
    validate_scene(nodes, arrows, timeline, takeaway, panel)
    Renderer(canvas).render(lambda elapsed: make_frame(canvas, nodes, arrows, timeline, takeaway, panel, particle, elapsed), output)


def main():
    parser = argparse.ArgumentParser(description="Render Scene 2 - The Big-Tech Architecture")
    parser.add_argument("--output", type=Path, default=ROOT / "output" / "Cyber_Attack_X_FAANG_Video01_Scene02.mp4")
    args = parser.parse_args()
    render_scene(args.output)


if __name__ == "__main__":
    main()
