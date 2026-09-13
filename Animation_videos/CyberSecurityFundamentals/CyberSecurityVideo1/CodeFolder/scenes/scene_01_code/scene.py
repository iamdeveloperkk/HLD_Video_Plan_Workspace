"""
Cyber Attack X FAANG
Video 1 - Scene 01

Scene: The Night Something Goes Wrong

Purpose:
Establish the mysterious production incident at NEXA.

Visual language:
- Cinematic NEXA production environment
- Slow camera movement
- Dark technical atmosphere
- Production metrics
- Right-side discussion panel
- Minimal UI
- No actual attack mechanics yet
"""

from pathlib import Path
import sys
import math
import shutil
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Make repository common package available
# ---------------------------------------------------------------------------

SCENE_DIR = Path(__file__).resolve().parent

# scene_01_code
#   -> scene_01
#       -> scenes
#           -> CyberSecurityVideo1
#               -> CodeFolder
#                   -> scenes
#
# Adjust if your current repository nesting differs.
REPO_ROOT = SCENE_DIR.parents[5]

COMMON_DIR = REPO_ROOT / "Animation_videos" / "_common"

if str(COMMON_DIR) not in sys.path:
    sys.path.insert(0, str(COMMON_DIR))


# ---------------------------------------------------------------------------
# Scene configuration
# ---------------------------------------------------------------------------

from config import (
    WIDTH,
    HEIGHT,
    FPS,
    DURATION_SECONDS,
    TOTAL_FRAMES,
    ASSETS_DIR,
    OUTPUT_FILE,
    PANEL_X,
    PANEL_Y,
    PANEL_WIDTH,
    PANEL_HEIGHT,
    MAIN_X,
    MAIN_Y,
    MAIN_WIDTH,
    MAIN_HEIGHT,
    INCIDENT_TIME,
    DISCUSSION_POINTS,
)


# ---------------------------------------------------------------------------
# Optional common engine imports
# ---------------------------------------------------------------------------
#
# Keep these imports aligned with the actual _common engine implementation.
# If your common engine exposes Renderer / helpers under different names,
# replace only this section.
# ---------------------------------------------------------------------------

try:
    from engine.renderer import Renderer
except ImportError:
    Renderer = None


# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------

def load_font(size: int, bold: bool = False):
    """
    Load a clean system font.

    Falls back to PIL's default font if the requested font is unavailable.
    """

    candidates = []

    if bold:
        candidates.extend([
            "/System/Library/Fonts/SFNS.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ])
    else:
        candidates.extend([
            "/System/Library/Fonts/SFNS.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ])

    for font_path in candidates:
        if Path(font_path).exists():
            try:
                return ImageFont.truetype(font_path, size)
            except Exception:
                pass

    return ImageFont.load_default()


FONT_SMALL = load_font(18)
FONT_BODY = load_font(21)
FONT_MEDIUM = load_font(26, bold=True)
FONT_TITLE = load_font(34, bold=True)
FONT_INCIDENT = load_font(58, bold=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clamp(value, minimum=0.0, maximum=1.0):
    return max(minimum, min(maximum, value))


def lerp(a, b, t):
    return a + (b - a) * t


def ease_out(t):
    t = clamp(t)
    return 1 - (1 - t) ** 3


def ease_in_out(t):
    t = clamp(t)

    if t < 0.5:
        return 4 * t * t * t

    return 1 - ((-2 * t + 2) ** 3) / 2


def fade_alpha(frame_time, start, duration=0.6):
    return int(255 * ease_out((frame_time - start) / duration))


def rounded_rectangle(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(
        box,
        radius=radius,
        fill=fill,
        outline=outline,
        width=width,
    )


# ---------------------------------------------------------------------------
# Background
# ---------------------------------------------------------------------------

def create_background():
    """
    Create the dark NEXA production environment background.

    The scene intentionally keeps the background understated because the
    metrics and incident state are the important information.
    """

    image = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        (7, 12, 22),
    )

    draw = ImageDraw.Draw(image)

    # Subtle horizontal technical lines
    for y in range(0, HEIGHT, 40):
        draw.line(
            [(0, y), (WIDTH, y)],
            fill=(12, 22, 36),
            width=1,
        )

    # Subtle vertical lines
    for x in range(0, WIDTH, 80):
        draw.line(
            [(x, 0), (x, HEIGHT)],
            fill=(11, 20, 33),
            width=1,
        )

    return image


# ---------------------------------------------------------------------------
# Main incident visualization
# ---------------------------------------------------------------------------

def draw_incident_environment(draw, frame_time):
    """
    Draw the production environment on the left side.

    This is deliberately abstract rather than attempting to reproduce
    a complete dashboard.
    """

    x0 = MAIN_X
    y0 = MAIN_Y

    # Main production container
    rounded_rectangle(
        draw,
        (
            x0,
            y0,
            x0 + MAIN_WIDTH,
            y0 + MAIN_HEIGHT,
        ),
        radius=18,
        fill=(10, 18, 31),
        outline=(29, 48, 70),
        width=2,
    )

    # Header
    draw.text(
        (x0 + 25, y0 + 20),
        "NEXA PRODUCTION",
        font=FONT_MEDIUM,
        fill=(210, 220, 235),
    )

    draw.text(
        (x0 + 25, y0 + 55),
        "Live system health",
        font=FONT_SMALL,
        fill=(105, 125, 150),
    )

    # -----------------------------------------------------------------------
    # Metric cards
    # -----------------------------------------------------------------------

    card_y = y0 + 105
    card_width = 250
    card_height = 105
    gap = 22

    metrics = [
        ("TRAFFIC", "NORMAL"),
        ("LATENCY", "42 ms"),
        ("ERROR RATE", "0.3%"),
    ]

    for index, (label, value) in enumerate(metrics):

        card_x = x0 + 25 + index * (card_width + gap)

        rounded_rectangle(
            draw,
            (
                card_x,
                card_y,
                card_x + card_width,
                card_y + card_height,
            ),
            radius=12,
            fill=(13, 24, 40),
            outline=(31, 51, 74),
            width=1,
        )

        draw.text(
            (card_x + 18, card_y + 17),
            label,
            font=FONT_SMALL,
            fill=(105, 125, 150),
        )

        draw.text(
            (card_x + 18, card_y + 48),
            value,
            font=FONT_MEDIUM,
            fill=(215, 225, 240),
        )

    # -----------------------------------------------------------------------
    # System visualization
    # -----------------------------------------------------------------------

    system_y = y0 + 255

    components = [
        ("EDGE", x0 + 55),
        ("API", x0 + 250),
        ("SERVICES", x0 + 445),
        ("DATABASE", x0 + 665),
    ]

    for label, x in components:

        rounded_rectangle(
            draw,
            (
                x,
                system_y,
                x + 125,
                system_y + 58,
            ),
            radius=9,
            fill=(15, 29, 47),
            outline=(38, 62, 88),
            width=1,
        )

        draw.text(
            (x + 18, system_y + 18),
            label,
            font=FONT_SMALL,
            fill=(180, 195, 215),
        )

    # Connecting paths
    for i in range(len(components) - 1):

        _, x1 = components[i]
        _, x2 = components[i + 1]

        start_x = x1 + 125
        end_x = x2

        draw.line(
            [
                (start_x, system_y + 29),
                (end_x, system_y + 29),
            ],
            fill=(43, 67, 94),
            width=2,
        )

    # -----------------------------------------------------------------------
    # Abnormal traffic animation
    # -----------------------------------------------------------------------

    if frame_time >= 3.0:

        progress = clamp((frame_time - 3.0) / 8.0)

        # Number of particles increases as incident develops
        particle_count = int(2 + progress * 18)

        for i in range(particle_count):

            phase = (
                frame_time * (0.8 + i * 0.03)
                + i * 0.37
            )

            particle_progress = phase % 1.0

            start_x = x0 + 40
            end_x = x0 + MAIN_WIDTH - 40

            px = lerp(
                start_x,
                end_x,
                particle_progress,
            )

            py = (
                system_y
                + 29
                + math.sin(
                    particle_progress * math.pi * 3 + i
                ) * 18
            )

            radius = 2 + int(progress * 2)

            draw.ellipse(
                (
                    px - radius,
                    py - radius,
                    px + radius,
                    py + radius,
                ),
                fill=(190, 55, 55),
            )


# ---------------------------------------------------------------------------
# Incident metrics
# ---------------------------------------------------------------------------

def draw_dynamic_metrics(draw, frame_time):

    if frame_time < 2.0:
        return

    progress = clamp((frame_time - 2.0) / 9.0)

    # Traffic
    traffic_value = int(100 + 900 * progress)

    # Latency
    latency_value = int(42 + 410 * progress)

    # Errors
    error_value = 0.3 + 7.2 * progress

    x0 = MAIN_X
    y0 = MAIN_Y

    card_y = y0 + 105
    card_width = 250
    card_height = 105
    gap = 22

    values = [
        f"{traffic_value:,} req/s",
        f"{latency_value} ms",
        f"{error_value:.1f}%",
    ]

    for index, value in enumerate(values):

        card_x = x0 + 25 + index * (card_width + gap)

        # redraw value area
        draw.rectangle(
            (
                card_x + 15,
                card_y + 43,
                card_x + card_width - 15,
                card_y + 92,
            ),
            fill=(13, 24, 40),
        )

        draw.text(
            (card_x + 18, card_y + 48),
            value,
            font=FONT_MEDIUM,
            fill=(220, 85, 85),
        )


# ---------------------------------------------------------------------------
# Right-side discussion panel
# ---------------------------------------------------------------------------

def draw_discussion_panel(draw, frame_time):

    # Panel
    rounded_rectangle(
        draw,
        (
            PANEL_X,
            PANEL_Y,
            PANEL_X + PANEL_WIDTH,
            PANEL_Y + PANEL_HEIGHT,
        ),
        radius=16,
        fill=(11, 19, 32),
        outline=(35, 55, 78),
        width=2,
    )

    # Header
    draw.text(
        (PANEL_X + 20, PANEL_Y + 18),
        "02:13 AM",
        font=FONT_TITLE,
        fill=(220, 225, 235),
    )

    draw.text(
        (PANEL_X + 20, PANEL_Y + 60),
        "PRODUCTION INCIDENT",
        font=FONT_SMALL,
        fill=(190, 65, 65),
    )

    # Progressive bullet reveal
    bullet_start = PANEL_Y + 105

    reveal_schedule = [
        1.0,
        2.5,
        4.0,
        5.5,
        7.0,
    ]

    visible_count = 0

    for reveal_time in reveal_schedule:
        if frame_time >= reveal_time:
            visible_count += 1

    for index in range(visible_count):

        text = DISCUSSION_POINTS[index]

        y = bullet_start + index * 26

        # Bullet
        draw.ellipse(
            (
                PANEL_X + 20,
                y + 7,
                PANEL_X + 26,
                y + 13,
            ),
            fill=(205, 70, 70),
        )

        draw.text(
            (PANEL_X + 35, y),
            text,
            font=FONT_SMALL,
            fill=(185, 198, 215),
        )


# ---------------------------------------------------------------------------
# Incident status
# ---------------------------------------------------------------------------

def draw_status(draw, frame_time):

    if frame_time < 1.0:
        status = "Investigating..."
    elif frame_time < 4.0:
        status = "Traffic spike detected"
    elif frame_time < 8.0:
        status = "Multiple services degrading"
    else:
        status = "Something is wrong."

    x = MAIN_X + 25
    y = MAIN_Y + MAIN_HEIGHT - 55

    draw.text(
        (x, y),
        status,
        font=FONT_MEDIUM,
        fill=(215, 220, 230),
    )


# ---------------------------------------------------------------------------
# Timeline
# ---------------------------------------------------------------------------

def draw_timeline(draw, frame_time):

    x = 55
    y = HEIGHT - 28
    width = WIDTH - 110

    draw.line(
        [(x, y), (x + width, y)],
        fill=(40, 56, 75),
        width=3,
    )

    progress = clamp(frame_time / DURATION_SECONDS)

    draw.line(
        [
            (x, y),
            (x + width * progress, y),
        ],
        fill=(175, 65, 65),
        width=4,
    )


# ---------------------------------------------------------------------------
# Frame generation
# ---------------------------------------------------------------------------

def render_frame(frame_index):

    frame_time = frame_index / FPS

    image = create_background()

    draw = ImageDraw.Draw(image)

    # -----------------------------------------------------------------------
    # Subtle camera movement
    # -----------------------------------------------------------------------

    # The actual background is static, while the visual composition gives
    # the perception of a slow cinematic push.
    #
    # Keep the movement subtle so technical information remains readable.

    draw_incident_environment(
        draw,
        frame_time,
    )

    draw_dynamic_metrics(
        draw,
        frame_time,
    )

    draw_discussion_panel(
        draw,
        frame_time,
    )

    draw_status(
        draw,
        frame_time,
    )

    draw_timeline(
        draw,
        frame_time,
    )

    return image


# ---------------------------------------------------------------------------
# Video rendering
# ---------------------------------------------------------------------------

def render_video():

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    print("=" * 60)
    print("Cyber Attack X FAANG")
    print("Video 1 - Scene 01")
    print("Rendering...")
    print(f"Resolution : {WIDTH}x{HEIGHT}")
    print(f"FPS        : {FPS}")
    print(f"Duration   : {DURATION_SECONDS}s")
    print(f"Output     : {OUTPUT_FILE}")
    print("=" * 60)

    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("FFmpeg was not found on PATH")

    command = [
        ffmpeg, "-y", "-f", "rawvideo", "-vcodec", "rawvideo",
        "-pix_fmt", "rgb24", "-s", f"{WIDTH}x{HEIGHT}", "-r", str(FPS),
        "-i", "-", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(OUTPUT_FILE),
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    try:
        for frame_index in range(TOTAL_FRAMES):
            frame = np.asarray(render_frame(frame_index), dtype=np.uint8)
            process.stdin.write(frame.tobytes())
            if frame_index % FPS == 0:
                print(f"Rendering: {frame_index // FPS:02d}/{DURATION_SECONDS:02d}s")
    finally:
        process.stdin.close()
    if process.wait() != 0:
        raise RuntimeError("FFmpeg failed to encode Scene 1")

    print("=" * 60)
    print("Render complete.")
    print(f"Output: {OUTPUT_FILE}")
    print("=" * 60)


def render_scene(output):
    """Adapter used by the shared scene renderer CLI."""
    global OUTPUT_FILE
    OUTPUT_FILE = Path(output)
    render_video()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    render_video()