"""
Configuration for Cyber Attack X FAANG
Video 1 - Scene 01

Scene:
"The Night Something Goes Wrong"

This scene establishes the 02:13 AM production incident at NEXA.
"""

from pathlib import Path


# ---------------------------------------------------------------------------
# Scene identity
# ---------------------------------------------------------------------------

SCENE_NAME = "scene_01"
SCENE_TITLE = "The Night Something Goes Wrong"


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

WIDTH = 1280
HEIGHT = 720
FPS = 30

DURATION_SECONDS = 15

TOTAL_FRAMES = FPS * DURATION_SECONDS


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCENE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = SCENE_DIR / "assets"

OUTPUT_DIR = SCENE_DIR.parent.parent.parent / "OutputFolder" / f"{SCENE_NAME}_output"

OUTPUT_FILE = OUTPUT_DIR / "CyberSecurityVideo1_Scene01.mp4"


# ---------------------------------------------------------------------------
# Visual layout
# ---------------------------------------------------------------------------

# Main cinematic/animation area
MAIN_X = 35
MAIN_Y = 105
MAIN_WIDTH = 875
MAIN_HEIGHT = 515

# Right-side discussion panel
PANEL_X = 930
PANEL_Y = 45
PANEL_WIDTH = 305
PANEL_HEIGHT = 250


# ---------------------------------------------------------------------------
# Scene content
# ---------------------------------------------------------------------------

INCIDENT_TIME = "02:13 AM"

DISCUSSION_POINTS = [
    "PRODUCTION INCIDENT",
    "Traffic suddenly spikes",
    "Latency increasing",
    "Error rate climbing",
    "Something is wrong",
]


# ---------------------------------------------------------------------------
# Animation timing
# ---------------------------------------------------------------------------

METRIC_START = 2.0
STATUS_START = 4.0
PANEL_START = 1.0

TIMELINE_END = DURATION_SECONDS


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)