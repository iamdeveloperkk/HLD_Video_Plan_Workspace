"""
CyberSecurityVideo2 - Scene 01
SQL Injection

PIL-based deterministic compositor.

Design:
    Background
      ↓
    Parametric Architecture
      ↓
    Active particles / packets
      ↓
    Exclusive popup / detail view
      ↓
    Right HUD

Scene-specific assets are STRICTLY loaded from:
    CyberSecurityVideo2/AssetFolder/scene_01_reference_assets/

No common-asset fallback is permitted.
"""

from __future__ import annotations

import math
import subprocess
from pathlib import Path
from typing import Optional

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import config


# ============================================================================
# Paths
# ============================================================================

SCENE_DIR = Path(__file__).resolve().parent

# scene_01_code
#   parents[0] = scene_01_code
#   parents[1] = scenes
#   parents[2] = CodeFolder
#   parents[3] = CyberSecurityVideo2
VIDEO_ROOT = SCENE_DIR.parents[2]

ASSET_ROOT = (
    VIDEO_ROOT
    / "AssetFolder"
    / config.ASSET_ROOT_NAME
).resolve()


# ============================================================================
# Strict asset loading
# ============================================================================

_IMAGE_CACHE: dict[str, Image.Image] = {}


def load_scene_asset(relative_path: str) -> Image.Image:
    """
    Strictly load an asset from Scene 01's reference asset directory.

    No fallback is allowed.
    """

    path = (ASSET_ROOT / relative_path).resolve()

    try:
        path.relative_to(ASSET_ROOT)
    except ValueError as exc:
        raise RuntimeError(
            f"Scene asset escapes Scene 01 asset root: {relative_path}"
        ) from exc

    if not path.is_file():
        raise FileNotFoundError(
            f"Required Scene 01 asset is missing:\n{path}"
        )

    key = str(path)

    if key not in _IMAGE_CACHE:
        with Image.open(path) as image:
            _IMAGE_CACHE[key] = image.convert("RGBA").copy()

    return _IMAGE_CACHE[key].copy()


def validate_assets() -> None:
    """
    Fail before rendering if any required scene asset is missing.
    """

    for logical_name, relative_path in config.ASSETS.items():
        load_scene_asset(relative_path)


# ============================================================================
# Fonts
# ============================================================================

def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = []

    if bold:
        candidates.extend([
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf",
        ])
    else:
        candidates.extend([
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/System/Library/Fonts/Supplemental/Helvetica.ttf",
        ])

    candidates.extend([
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ])

    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)

    return ImageFont.load_default()


FONT_SMALL = load_font(16)
FONT_BODY = load_font(20)
FONT_BODY_BOLD = load_font(20, True)
FONT_LABEL = load_font(15, True)
FONT_TITLE = load_font(26, True)
FONT_SQL = load_font(18)
FONT_SQL_BOLD = load_font(18, True)


# ============================================================================
# Math helpers
# ============================================================================

def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def smoothstep(value: float) -> float:
    value = clamp(value, 0.0, 1.0)
    return value * value * (3.0 - 2.0 * value)


def ease_out_cubic(value: float) -> float:
    value = clamp(value, 0.0, 1.0)
    return 1.0 - (1.0 - value) ** 3


def local_progress(
    t: float,
    start: float,
    end: float,
) -> float:
    if end <= start:
        return 1.0
    return clamp((t - start) / (end - start), 0.0, 1.0)


# ============================================================================
# State machine
# ============================================================================

def scene_state(t: float) -> str:
    """
    The ONLY timeline authority.
    """

    for state, start, end in config.TIMELINE:
        if start <= t < end:
            return state

    return "impact"


def state_window(state: str) -> tuple[float, float]:
    for name, start, end in config.TIMELINE:
        if name == state:
            return start, end

    return config.T_IMPACT


def state_progress(t: float, state: str) -> float:
    start, end = state_window(state)
    return local_progress(t, start, end)


# ============================================================================
# Geometry
# ============================================================================

def node_rect(name: str) -> tuple[float, float, float, float]:
    n = config.NODES[name]
    return (
        n["x"],
        n["y"],
        n["x"] + n["width"],
        n["y"] + n["height"],
    )


def node_center(name: str) -> tuple[float, float]:
    x1, y1, x2, y2 = node_rect(name)
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def node_top(name: str) -> float:
    return node_rect(name)[1]


def node_bottom(name: str) -> float:
    return node_rect(name)[3]


def node_left(name: str) -> float:
    return node_rect(name)[0]


def node_right(name: str) -> float:
    return node_rect(name)[2]


def lerp_point(
    a: tuple[float, float],
    b: tuple[float, float],
    amount: float,
) -> tuple[float, float]:
    return (
        a[0] + (b[0] - a[0]) * amount,
        a[1] + (b[1] - a[1]) * amount,
    )


# ============================================================================
# Background
# ============================================================================

def draw_background(frame: Image.Image) -> None:
    pixels = frame.load()

    for y in range(config.HEIGHT):
        ratio = y / max(1, config.HEIGHT - 1)

        color = tuple(
            int(
                config.BACKGROUND_TOP[i]
                * (1.0 - ratio)
                + config.BACKGROUND_BOTTOM[i]
                * ratio
            )
            for i in range(3)
        )

        for x in range(config.WIDTH):
            pixels[x, y] = (*color, 255)

    draw = ImageDraw.Draw(frame, "RGBA")

    left, top, right, bottom = config.MAIN_PANEL

    grid_step = 45

    for x in range(left, right, grid_step):
        draw.line(
            (x, top, x, bottom),
            fill=(*config.GRID, 55),
            width=1,
        )

    for y in range(top, bottom, grid_step):
        draw.line(
            (left, y, right, y),
            fill=(*config.GRID, 45),
            width=1,
        )


# ============================================================================
# Glow
# ============================================================================

def draw_glow(
    frame: Image.Image,
    center: tuple[float, float],
    radius: int,
    color: tuple[int, int, int],
    alpha: int = 100,
) -> None:

    size = radius * 2

    glow = Image.new(
        "RGBA",
        (size, size),
        (0, 0, 0, 0),
    )

    draw = ImageDraw.Draw(glow, "RGBA")

    draw.ellipse(
        (radius // 2, radius // 2, radius * 3 // 2, radius * 3 // 2),
        fill=(*color, alpha),
    )

    glow = glow.filter(ImageFilter.GaussianBlur(radius // 2))

    frame.alpha_composite(
        glow,
        (
            int(center[0] - radius),
            int(center[1] - radius),
        ),
    )


# ============================================================================
# Asset scaling
# ============================================================================

def fit_asset(
    image: Image.Image,
    width: int,
    height: int,
) -> Image.Image:

    result = image.copy()
    result.thumbnail((width, height), Image.Resampling.LANCZOS)
    return result


def paste_center(
    frame: Image.Image,
    image: Image.Image,
    center: tuple[float, float],
    width: int,
    height: int,
    opacity: float = 1.0,
    scale: float = 1.0,
) -> None:

    target_w = max(1, int(width * scale))
    target_h = max(1, int(height * scale))

    image = fit_asset(image, target_w, target_h)

    if opacity < 1.0:
        alpha = image.getchannel("A")
        alpha = alpha.point(
            lambda p: int(p * clamp(opacity, 0.0, 1.0))
        )
        image.putalpha(alpha)

    x = int(center[0] - image.width / 2)
    y = int(center[1] - image.height / 2)

    frame.alpha_composite(image, (x, y))


# ============================================================================
# Architecture
# ============================================================================

NODE_COLORS = {
    "client": config.CYAN,
    "api": config.PURPLE,
    "ecs": config.ORANGE,
    "rds": config.BLUE,
}


def draw_connection(
    frame: Image.Image,
    source: str,
    target: str,
    alpha: int = 150,
) -> None:

    draw = ImageDraw.Draw(frame, "RGBA")

    a = node_center(source)
    b = node_center(target)

    draw.line(
        (a[0], a[1], b[0], b[1]),
        fill=(*config.MUTED, alpha),
        width=2,
    )


def draw_arrow_head(
    frame: Image.Image,
    point: tuple[float, float],
    direction: tuple[float, float],
    color: tuple[int, int, int],
    alpha: int,
) -> None:

    draw = ImageDraw.Draw(frame, "RGBA")

    dx, dy = direction
    length = math.hypot(dx, dy)

    if length < 0.001:
        return

    dx /= length
    dy /= length

    px = -dy
    py = dx

    size = 8

    p1 = point
    p2 = (
        point[0] - dx * size + px * size * 0.55,
        point[1] - dy * size + py * size * 0.55,
    )
    p3 = (
        point[0] - dx * size - px * size * 0.55,
        point[1] - dy * size - py * size * 0.55,
    )

    draw.polygon(
        [p1, p2, p3],
        fill=(*color, alpha),
    )


def draw_network_arrow(
    frame: Image.Image,
    source: str,
    target: str,
    color: tuple[int, int, int],
    alpha: int = 190,
) -> None:

    draw = ImageDraw.Draw(frame, "RGBA")

    a = node_center(source)
    b = node_center(target)

    draw.line(
        (a[0], a[1], b[0], b[1]),
        fill=(*color, alpha),
        width=3,
    )

    direction = (
        b[0] - a[0],
        b[1] - a[1],
    )

    draw_arrow_head(
        frame,
        b,
        direction,
        color,
        alpha,
    )


def draw_arrival_pulse(
    frame: Image.Image,
    node: str,
    color: tuple[int, int, int],
    progress: float,
) -> None:
    """Show a short expanding reception pulse at a node."""
    pulse = clamp(progress / 0.42, 0.0, 1.0)
    radius = 34 + int(58 * ease_out_cubic(pulse))
    draw = ImageDraw.Draw(frame, "RGBA")
    draw.ellipse(
        (
            node_center(node)[0] - radius,
            node_center(node)[1] - radius,
            node_center(node)[0] + radius,
            node_center(node)[1] + radius,
        ),
        outline=(*color, int(190 * (1.0 - pulse))),
        width=3,
    )


def draw_active_ring(
    frame: Image.Image,
    node: str,
    color: tuple[int, int, int],
    intensity: float,
    node_scale: float = 1.0,
) -> None:

    image_name = (
        "blue_ring"
        if node == "rds"
        else "orange_ring"
    )

    image = load_scene_asset(config.ASSETS[image_name])

    cx, cy = node_center(node)
    node_config = config.NODES[node]
    rendered_icon = fit_asset(
        load_scene_asset(config.ASSETS[node]),
        max(1, int(node_config["width"] * node_scale)),
        max(1, int(node_config["height"] * node_scale)),
    )
    ring_width = rendered_icon.width + 34
    ring_height = rendered_icon.height + 28

    draw_glow(
        frame,
        (cx, cy),
        120,
        color,
        int(80 * intensity),
    )

    paste_center(
        frame,
        image,
        (cx, cy),
        ring_width,
        ring_height,
        opacity=intensity,
        scale=1.0 + 0.04 * intensity,
    )


def draw_architecture(
    frame: Image.Image,
    active_node: Optional[str] = None,
    dim_opacity: float = 0.40,
    scale_active: bool = True,
    reveal_progress: Optional[float] = None,
) -> None:
    """
    ONE architecture renderer.

    State-specific visual emphasis is supplied through parameters.
    """

    connections = (
        ("client", "api"),
        ("api", "ecs"),
        ("ecs", "rds"),
    )

    for connection_index, (source, target) in enumerate(connections):
        alpha = 190

        if active_node:
            if source != active_node and target != active_node:
                alpha = 60

        if reveal_progress is None:
            draw_connection(frame, source, target, alpha)
            continue

        connection_progress = clamp(
            (reveal_progress - 0.20 - connection_index * 0.24) / 0.24,
            0.0,
            1.0,
        )
        if connection_progress <= 0.0:
            continue
        start = node_center(source)
        end = lerp_point(node_center(source), node_center(target), smoothstep(connection_progress))
        ImageDraw.Draw(frame, "RGBA").line(
            (*start, *end),
            fill=(*config.MUTED, alpha),
            width=2,
        )

    for name in ("client", "api", "ecs", "rds"):
        active = name == active_node

        opacity = 1.0 if active or active_node is None else dim_opacity
        if reveal_progress is not None:
            node_index = ("client", "api", "ecs", "rds").index(name)
            opacity *= clamp(
                (reveal_progress - node_index * 0.22) / 0.32,
                0.0,
                1.0,
            )

        scale = 1.0

        if active and scale_active:
            scale = 1.06

        color = NODE_COLORS[name]

        if active:
            draw_glow(
                frame,
                node_center(name),
                115,
                color,
                120,
            )

            draw_active_ring(
                frame,
                name,
                color,
                1.0,
                node_scale=scale,
            )

        image = load_scene_asset(
            config.ASSETS[name]
        )

        n = config.NODES[name]

        paste_center(
            frame,
            image,
            node_center(name),
            n["width"],
            n["height"],
            opacity=opacity,
            scale=scale,
        )

        draw = ImageDraw.Draw(frame, "RGBA")

        label = config.NODE_LABELS[name]

        bbox = draw.textbbox(
            (0, 0),
            label,
            font=FONT_LABEL,
        )

        label_w = bbox[2] - bbox[0]

        draw.text(
            (
                node_center(name)[0] - label_w / 2,
                n["y"] + n["height"] + 10,
            ),
            label,
            fill=(
                *config.WHITE,
                int(255 * opacity),
            ),
            font=FONT_LABEL,
        )


# ============================================================================
# Particles
# ============================================================================

def draw_particle_between(
    frame: Image.Image,
    source: str,
    target: str,
    progress: float,
    malicious: bool = False,
) -> None:

    progress = ease_out_cubic(progress)

    a = node_center(source)
    b = node_center(target)

    point = lerp_point(a, b, progress)

    color = config.RED if malicious else config.CYAN

    draw_glow(
        frame,
        point,
        50,
        color,
        120,
    )

    draw = ImageDraw.Draw(frame, "RGBA")

    draw.ellipse(
        (
            point[0] - 7,
            point[1] - 7,
            point[0] + 7,
            point[1] + 7,
        ),
        fill=(*color, 255),
    )

    for i in range(1, 6):
        trail_progress = clamp(
            progress - i * 0.025,
            0.0,
            1.0,
        )

        trail = lerp_point(
            a,
            b,
            trail_progress,
        )

        radius = max(2, 7 - i)

        draw.ellipse(
            (
                trail[0] - radius,
                trail[1] - radius,
                trail[0] + radius,
                trail[1] + radius,
            ),
            fill=(*color, max(20, 120 - i * 18)),
        )


# ============================================================================
# Popup geometry
# ============================================================================

def popup_rect_for_node(
    node: str,
    width: int,
    height: int,
) -> tuple[int, int, int, int]:

    cx, _ = node_center(node)

    panel_left, panel_top, panel_right, panel_bottom = config.MAIN_PANEL

    preferred_x = int(cx - width / 2)
    preferred_y = int(node_top(node) - height - 32)

    x = clamp(
        preferred_x,
        panel_left + 15,
        panel_right - width - 15,
    )

    y = clamp(
        preferred_y,
        panel_top + 15,
        panel_bottom - height - 15,
    )

    return (
        int(x),
        int(y),
        int(x + width),
        int(y + height),
    )


def draw_tether(
    frame: Image.Image,
    popup_rect: tuple[int, int, int, int],
    node: str,
    color: tuple[int, int, int],
    alpha: int,
) -> None:

    draw = ImageDraw.Draw(frame, "RGBA")

    x1, y1, x2, y2 = popup_rect

    popup_center_x = (x1 + x2) / 2
    popup_bottom = y2

    nx, ny = node_center(node)
    node_top_y = node_top(node)

    draw.line(
        (
            popup_center_x,
            popup_bottom,
            nx,
            node_top_y,
        ),
        fill=(*color, alpha),
        width=2,
    )


# ============================================================================
# Popup rendering
# ============================================================================

def wrap_text_to_width(
    text: str,
    text_font: ImageFont.ImageFont,
    max_width: int,
) -> list[str]:
    """Wrap text by measured font width while preserving explicit newlines."""
    draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    wrapped: list[str] = []

    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            wrapped.append("")
            continue

        current = ""
        for word in words:
            candidate = f"{current} {word}" if current else word
            if draw.textbbox((0, 0), candidate, font=text_font)[2] <= max_width:
                current = candidate
                continue

            if current:
                wrapped.append(current)
                current = ""

            # Split a single overlong token so no glyph can cross the region.
            for character in word:
                candidate = f"{current}{character}"
                if draw.textbbox((0, 0), candidate, font=text_font)[2] > max_width and current:
                    wrapped.append(current)
                    current = character
                else:
                    current = candidate

        if current:
            wrapped.append(current)

    return wrapped


def draw_wrapped_text(
    target: Image.Image,
    text: str,
    box: tuple[int, int, int, int],
    text_font: ImageFont.ImageFont,
    fill: tuple[int, int, int, int],
    line_gap: int = 6,
) -> int:
    """Draw wrapped text inside a hard rectangular content boundary."""
    x1, y1, x2, y2 = box
    lines = wrap_text_to_width(text, text_font, max(1, x2 - x1))
    draw = ImageDraw.Draw(target, "RGBA")
    line_height = text_font.getbbox("Ag")[3] - text_font.getbbox("Ag")[1] + line_gap
    visible_lines = max(0, (y2 - y1 + line_gap) // line_height)

    for index, line in enumerate(lines[:visible_lines]):
        draw.text((x1, y1 + index * line_height), line, font=text_font, fill=fill)

    return min(len(lines), visible_lines) * line_height

def popup_alpha(local_t: float) -> float:
    enter = smoothstep(
        clamp(local_t / 0.18, 0.0, 1.0)
    )

    exit_start = 0.72

    if local_t <= exit_start:
        return enter

    exit_progress = clamp(
        (local_t - exit_start) / (1.0 - exit_start),
        0.0,
        1.0,
    )

    return enter * (1.0 - smoothstep(exit_progress))


def draw_glass_popup(
    frame: Image.Image,
    node: str,
    title: str,
    lines: list[str],
    color: tuple[int, int, int],
    local_t: float,
    width: int,
    height: int,
) -> None:

    alpha_factor = popup_alpha(local_t)

    if alpha_factor <= 0.001:
        return

    x1, y1, x2, y2 = popup_rect_for_node(
        node,
        width,
        height,
    )

    # Small vertical emergence.
    travel = int(
        (1.0 - ease_out_cubic(
            clamp(local_t / 0.2, 0.0, 1.0)
        )) * 18
    )

    y1 += travel
    y2 += travel

    # Hard safety assertion.
    assert x1 >= config.MAIN_PANEL[0]
    assert x2 <= config.MAIN_PANEL[2]
    assert y1 >= config.MAIN_PANEL[1]
    assert y2 <= config.MAIN_PANEL[3]

    draw_tether(
        frame,
        (x1, y1, x2, y2),
        node,
        color,
        int(110 * alpha_factor),
    )

    popup = Image.new(
        "RGBA",
        (x2 - x1, y2 - y1),
        (0, 0, 0, 0),
    )

    popup_draw = ImageDraw.Draw(
        popup,
        "RGBA",
    )

    popup_draw.rounded_rectangle(
        (
            1,
            1,
            popup.width - 2,
            popup.height - 2,
        ),
        radius=18,
        fill=(*config.PANEL_FILL[:3], int(225 * alpha_factor)),
        outline=(*color, int(170 * alpha_factor)),
        width=2,
    )

    # Header accent.
    popup_draw.rounded_rectangle(
        (
            0,
            0,
            popup.width,
            7,
        ),
        radius=4,
        fill=(*color, int(210 * alpha_factor)),
    )

    padding_x = 28
    content_left = padding_x
    content_right = popup.width - padding_x
    title_box = (content_left, 22, content_right, 54)
    draw_wrapped_text(
        popup,
        title,
        title_box,
        FONT_BODY_BOLD,
        (*config.WHITE, int(255 * alpha_factor)),
        line_gap=2,
    )

    popup_draw.line(
        (content_left, 62, content_right, 62),
        fill=(*color, int(150 * alpha_factor)),
        width=1,
    )

    body_text = "\n".join(lines)
    body_box = (content_left, 78, content_right, popup.height - 20)
    draw_wrapped_text(
        popup,
        body_text,
        body_box,
        FONT_BODY,
        (*config.MUTED, int(235 * alpha_factor)),
        line_gap=7,
    )

    frame.alpha_composite(
        popup,
        (x1, y1),
    )


def render_exclusive_popup_layer(
    frame: Image.Image,
    state: str,
    t: float,
) -> None:
    """
    Exclusive popup mutex.

    Only api / ecs / rds can produce a popup.
    """

    if state not in ("api", "ecs", "rds"):
        return

    progress = state_progress(t, state)

    if state == "api":
        draw_glass_popup(
            frame,
            "api",
            "API REQUEST",
            [
                "GET /users?id=42",
                "Input enters the service boundary",
                "Application logic processes the request",
            ],
            config.PURPLE,
            progress,
            config.POPUPS["api"]["width"],
            config.POPUPS["api"]["height"],
        )

    elif state == "ecs":
        draw_glass_popup(
            frame,
            "ecs",
            "APPLICATION SERVICE",
            [
                "User input reaches application code",
                "Service prepares a database operation",
                "The query boundary is approaching",
            ],
            config.ORANGE,
            progress,
            config.POPUPS["ecs"]["width"],
            config.POPUPS["ecs"]["height"],
        )

    elif state == "rds":
        draw_glass_popup(
            frame,
            "rds",
            "DATABASE",
            [
                "Query arrives at RDS",
                "Database evaluates the request",
                "Expected result is returned",
            ],
            config.BLUE,
            progress,
            config.POPUPS["rds"]["width"],
            config.POPUPS["rds"]["height"],
        )


# ============================================================================
# ECS zoom
# ============================================================================

def draw_sql_box(
    frame: Image.Image,
    x: int,
    y: int,
    width: int,
    height: int,
    title: str,
    sql_lines: list[str],
    color: tuple[int, int, int],
    alpha: int = 235,
    reveal: float = 1.0,
) -> None:

    draw = ImageDraw.Draw(frame, "RGBA")

    draw.rounded_rectangle(
        (x, y, x + width, y + height),
        radius=18,
        fill=(*config.PANEL_FILL[:3], alpha),
        outline=(*color, min(alpha, 190)),
        width=2,
    )

    draw.text(
        (x + 20, y + 17),
        title,
        fill=(*color, alpha),
        font=FONT_BODY_BOLD,
    )

    yy = y + 62

    visible_lines = min(
        len(sql_lines),
        max(0, int(reveal * (len(sql_lines) + 1))),
    )

    for line_index, line in enumerate(sql_lines[:visible_lines]):
        line_reveal = clamp(reveal * (len(sql_lines) + 1) - line_index, 0.0, 1.0)
        visible_characters = max(1, int(len(line) * line_reveal))
        line_color = config.RED if "unexpected input" in line else config.WHITE
        draw.text(
            (x + 22, yy),
            line[:visible_characters],
            fill=(*line_color, int(alpha * line_reveal)),
            font=FONT_SQL,
        )
        yy += 31


def draw_ecs_zoom(
    frame: Image.Image,
    t: float,
) -> None:

    progress = state_progress(
        t,
        "ecs_zoom",
    )

    focus = smoothstep(progress)

    # Dim architecture except ECS.
    draw_architecture(
        frame,
        active_node="ecs",
        dim_opacity=0.16 + 0.20 * (1.0 - focus),
        scale_active=True,
    )

    # Focus overlay.
    overlay = Image.new(
        "RGBA",
        (config.WIDTH, config.HEIGHT),
        (0, 0, 0, int(90 * focus)),
    )

    frame.alpha_composite(overlay)

    ecs_center = node_center("ecs")

    draw_glow(
        frame,
        ecs_center,
        180,
        config.ORANGE,
        int(130 * focus),
    )

    # Detail view emerges from ECS.
    start_x = 365
    start_y = 165

    scale = 0.82 + 0.18 * ease_out_cubic(
        clamp(progress / 0.55, 0.0, 1.0)
    )

    width = int(500 * scale)
    height = int(250 * scale)

    x = int(
        ecs_center[0]
        - width / 2
    )

    y = int(
        start_y
        + (1.0 - focus) * 80
    )

    draw_sql_box(
        frame,
        x,
        y,
        width,
        height,
        "QUERY CONSTRUCTION",
        config.NORMAL_SQL,
        config.ORANGE,
        int(235 * focus),
        reveal=clamp(progress / 0.72, 0.0, 1.0),
    )

    draw = ImageDraw.Draw(frame, "RGBA")

    draw.text(
        (x + 20, y + height - 42),
        "INPUT → QUERY STRUCTURE",
        fill=(*config.MUTED, int(220 * focus)),
        font=FONT_SMALL,
    )


# ============================================================================
# Database execution
# ============================================================================

def draw_database_execution(
    frame: Image.Image,
    t: float,
    malicious: bool = False,
) -> None:

    state = "malicious_db" if malicious else "normal_db"

    progress = state_progress(
        t,
        state,
    )

    draw_architecture(
        frame,
        active_node="rds",
        dim_opacity=0.30,
    )

    color = config.RED if malicious else config.BLUE

    draw_glow(
        frame,
        node_center("rds"),
        150,
        color,
        130,
    )

    x = 545
    y = 150
    width = 350
    height = 265

    title = (
        "UNINTENDED DB EXECUTION"
        if malicious
        else "DATABASE EXECUTION"
    )

    sql = (
        config.MALICIOUS_SQL
        if malicious
        else config.NORMAL_SQL
    )

    draw_sql_box(
        frame,
        x,
        y,
        width,
        height,
        title,
        sql,
        color,
        235,
    )

    draw = ImageDraw.Draw(frame, "RGBA")

    rows = [
        ("users", "id", "42"),
        ("users", "name", "user_record"),
        ("users", "status", "active"),
    ]

    yy = y + 150

    for index, row in enumerate(rows):
        reveal = clamp(
            progress * 4.0 - index * 0.7,
            0.0,
            1.0,
        )

        if reveal <= 0:
            continue

        text = f"{row[0]:<10} {row[1]:<10} {row[2]}"

        draw.text(
            (x + 22, yy),
            text,
            fill=(
                *(
                    config.RED
                    if malicious
                    else config.GREEN
                ),
                int(220 * reveal),
            ),
            font=FONT_SMALL,
        )

        yy += 26


# ============================================================================
# Attack
# ============================================================================

def draw_attacker(
    frame: Image.Image,
    t: float,
) -> None:

    progress = state_progress(
        t,
        "attack_request",
    )

    image = load_scene_asset(
        config.ASSETS["attacker"]
    )

    start = (
        95,
        560,
    )

    end = (
        node_center("client")[0],
        node_center("client")[1],
    )

    point = lerp_point(
        start,
        end,
        ease_out_cubic(progress),
    )

    draw_glow(
        frame,
        point,
        75,
        config.RED,
        140,
    )

    paste_center(
        frame,
        image,
        point,
        120,
        120,
        opacity=1.0,
        scale=1.0,
    )


# ============================================================================
# Right panel
# ============================================================================

def draw_right_panel(
    frame: Image.Image,
    state: str,
) -> None:

    draw = ImageDraw.Draw(
        frame,
        "RGBA",
    )

    x1, y1, x2, y2 = config.RIGHT_PANEL

    draw.rounded_rectangle(
        (x1, y1, x2, y2),
        radius=20,
        fill=(*config.PANEL_FILL[:3], 205),
        outline=(*config.PANEL_BORDER[:3], 150),
        width=2,
    )

    draw.text(
        (x1 + 20, y1 + 20),
        config.TITLE,
        fill=(*config.WHITE, 255),
        font=FONT_TITLE,
    )

    draw_wrapped_text(
        frame,
        config.SUBTITLE,
        (x1 + 20, y1 + 58, x2 - 20, y1 + 104),
        FONT_SMALL,
        (*config.MUTED, 230),
        line_gap=2,
    )

    draw.line(
        (
            x1 + 20,
            y1 + 112,
            x2 - 20,
            y1 + 112,
        ),
        fill=(*config.PANEL_BORDER[:3], 130),
        width=1,
    )

    text = config.DISCUSSION.get(
        state,
        "",
    )

    y = y1 + 142

    words = text.split()
    lines = []
    current = ""

    for word in words:
        candidate = (
            f"{current} {word}"
            if current
            else word
        )

        bbox = draw.textbbox(
            (0, 0),
            candidate,
            font=FONT_BODY,
        )

        if bbox[2] - bbox[0] > (x2 - x1 - 40):
            lines.append(current)
            current = word
        else:
            current = candidate

    if current:
        lines.append(current)

    for line in lines:
        draw.text(
            (x1 + 20, y),
            line,
            fill=(*config.MUTED, 235),
            font=FONT_BODY,
        )
        y += 31


# ============================================================================
# State-specific effects
# ============================================================================

def render_state(
    frame: Image.Image,
    state: str,
    t: float,
) -> None:

    if state == "architecture":
        p = state_progress(t, state)

        draw_architecture(
            frame,
            active_node=None,
            dim_opacity=0.8,
            scale_active=False,
            reveal_progress=p,
        )

        if p > 0.56:
            draw_particle_between(
                frame,
                "api",
                "ecs",
                clamp((p - 0.56) / 0.44, 0.0, 1.0),
            )

    elif state == "normal_request":
        draw_architecture(
            frame,
            active_node="client",
            dim_opacity=0.50,
        )

        draw_network_arrow(
            frame,
            "client",
            "api",
            config.CYAN,
        )

        draw_particle_between(
            frame,
            "client",
            "api",
            state_progress(t, state),
        )

    elif state == "api":
        draw_architecture(
            frame,
            active_node="api",
            dim_opacity=0.38,
        )

        draw_network_arrow(
            frame,
            "client",
            "api",
            config.CYAN,
        )

        draw_arrival_pulse(frame, "api", config.CYAN, state_progress(t, state))

        render_exclusive_popup_layer(
            frame,
            state,
            t,
        )

    elif state == "ecs":
        draw_architecture(
            frame,
            active_node="ecs",
            dim_opacity=0.38,
        )

        draw_network_arrow(
            frame,
            "api",
            "ecs",
            config.CYAN,
        )

        draw_arrival_pulse(frame, "ecs", config.ORANGE, state_progress(t, state))

        render_exclusive_popup_layer(
            frame,
            state,
            t,
        )

    elif state == "rds":
        draw_architecture(
            frame,
            active_node="rds",
            dim_opacity=0.38,
        )

        draw_network_arrow(
            frame,
            "ecs",
            "rds",
            config.CYAN,
        )

        draw_arrival_pulse(frame, "rds", config.BLUE, state_progress(t, state))

        render_exclusive_popup_layer(
            frame,
            state,
            t,
        )

    elif state == "ecs_zoom":
        draw_ecs_zoom(
            frame,
            t,
        )

    elif state == "query_travel":
        draw_architecture(
            frame,
            active_node="rds",
            dim_opacity=0.35,
        )

        draw_network_arrow(
            frame,
            "ecs",
            "rds",
            config.ORANGE,
        )

        draw_particle_between(
            frame,
            "ecs",
            "rds",
            state_progress(t, state),
        )

        draw_arrival_pulse(frame, "rds", config.BLUE, state_progress(t, state) - 0.58)

    elif state == "normal_db":
        draw_database_execution(
            frame,
            t,
            malicious=False,
        )

    elif state == "reset":
        draw_architecture(
            frame,
            active_node=None,
            dim_opacity=0.85,
            scale_active=False,
        )

    elif state == "attack_request":
        draw_architecture(
            frame,
            active_node="client",
            dim_opacity=0.35,
        )

        draw_attacker(
            frame,
            t,
        )

    elif state == "malicious_ecs":
        draw_architecture(
            frame,
            active_node="ecs",
            dim_opacity=0.30,
        )

        draw_particle_between(
            frame,
            "client",
            "ecs",
            state_progress(t, state),
            malicious=True,
        )

        draw_arrival_pulse(frame, "ecs", config.RED, state_progress(t, state))

    elif state == "malicious_travel":
        draw_architecture(
            frame,
            active_node="rds",
            dim_opacity=0.28,
        )

        draw_network_arrow(
            frame,
            "ecs",
            "rds",
            config.RED,
            alpha=220,
        )

        draw_particle_between(
            frame,
            "ecs",
            "rds",
            state_progress(t, state),
            malicious=True,
        )

        draw_arrival_pulse(frame, "rds", config.RED, state_progress(t, state) - 0.58)

    elif state == "malicious_db":
        draw_database_execution(
            frame,
            t,
            malicious=True,
        )

    elif state == "impact":
        draw_architecture(
            frame,
            active_node="rds",
            dim_opacity=0.22,
        )

        draw_glow(
            frame,
            node_center("rds"),
            190,
            config.RED,
            170,
        )

        impact_progress = state_progress(t, state)
        draw_arrival_pulse(frame, "rds", config.RED, impact_progress * 0.45)

        draw = ImageDraw.Draw(
            frame,
            "RGBA",
        )

        draw.rounded_rectangle(
            (
                470,
                475,
                895,
                560,
            ),
            radius=16,
            fill=(45, 8, 18, 225),
            outline=(*config.RED, 190),
            width=2,
        )

        draw.text(
            (500, 495),
            "UNINTENDED DATABASE BEHAVIOR",
            fill=(*config.RED, 255),
            font=FONT_BODY_BOLD,
        )

        rows_y = 585
        draw.text(
            (500, rows_y),
            "AFFECTED ROWS  42   43   44   ...",
            fill=(*config.RED, int(255 * clamp(impact_progress * 2.5, 0.0, 1.0))),
            font=FONT_SMALL,
        )
        draw.text(
            (760, rows_y),
            "SECURITY ALERT",
            fill=(*config.WHITE, int(255 * clamp((impact_progress - 0.35) * 2.5, 0.0, 1.0))),
            font=FONT_SMALL,
        )


# ============================================================================
# Header
# ============================================================================

def draw_header(frame: Image.Image) -> None:

    draw = ImageDraw.Draw(
        frame,
        "RGBA",
    )

    draw.text(
        (45, 48),
        config.TITLE,
        fill=(*config.WHITE, 255),
        font=FONT_TITLE,
    )

    draw.text(
        (45, 78),
        config.SUBTITLE,
        fill=(*config.MUTED, 220),
        font=FONT_SMALL,
    )


# ============================================================================
# Frame
# ============================================================================

def make_frame(t: float) -> Image.Image:

    t = clamp(
        t,
        0.0,
        config.DURATION - 1.0 / config.FPS,
    )

    state = scene_state(t)

    frame = Image.new(
        "RGBA",
        (config.WIDTH, config.HEIGHT),
        (0, 0, 0, 255),
    )

    draw_background(frame)

    draw_header(frame)

    render_state(
        frame,
        state,
        t,
    )

    draw_right_panel(
        frame,
        state,
    )

    return frame.convert("RGB")


# ============================================================================
# Render
# ============================================================================

def render_scene(output) -> None:
    """
    Render the complete Scene 01 MP4.

    The function intentionally validates every required asset before
    generating any frames.
    """

    validate_assets()

    output = Path(output)

    if output.suffix.lower() != ".mp4":
        output.mkdir(
            parents=True,
            exist_ok=True,
        )

        output = (
            output
            / "CyberSecurityVideo2_scene_01.mp4"
        )
    else:
        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    temp_dir = (
        output.parent
        / f".{output.stem}_frames"
    )

    temp_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    try:
        total_frames = int(
            config.DURATION * config.FPS
        )

        for frame_index in range(total_frames):
            t = frame_index / config.FPS

            frame = make_frame(t)

            frame.save(
                temp_dir / f"frame_{frame_index:05d}.png",
                "PNG",
            )

        command = [
            "ffmpeg",
            "-y",
            "-framerate",
            str(config.FPS),
            "-i",
            str(temp_dir / "frame_%05d.png"),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-movflags",
            "+faststart",
            str(output),
        ]

        subprocess.run(
            command,
            check=True,
        )

    finally:
        for frame_file in temp_dir.glob("*.png"):
            frame_file.unlink(missing_ok=True)

        temp_dir.rmdir()