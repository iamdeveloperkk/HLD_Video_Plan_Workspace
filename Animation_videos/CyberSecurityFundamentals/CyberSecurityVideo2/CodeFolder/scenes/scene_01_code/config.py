"""
CyberSecurityVideo2 - Scene 01
SQL Injection

Single source of truth for:
- canvas
- timeline
- architecture geometry
- popup geometry
- colors
- text
- scene-local assets
"""

from pathlib import Path


# ---------------------------------------------------------------------------
# Canvas
# ---------------------------------------------------------------------------

WIDTH = 1280
HEIGHT = 720
FPS = 30
DURATION = 16.0


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 1230, 675)

ARCHITECTURE_Y = 330

NODES = {
    "client": {
        "x": 105,
        "y": 285,
        "width": 110,
        "height": 110,
    },
    "api": {
        "x": 315,
        "y": 285,
        "width": 110,
        "height": 110,
    },
    "ecs": {
        "x": 535,
        "y": 275,
        "width": 130,
        "height": 130,
    },
    "rds": {
        "x": 765,
        "y": 275,
        "width": 130,
        "height": 130,
    },
}


# ---------------------------------------------------------------------------
# Timeline
# ---------------------------------------------------------------------------

T_ARCHITECTURE = (0.0, 1.5)
T_NORMAL_REQUEST = (1.5, 2.0)

T_API = (2.0, 2.8)
T_ECS = (2.8, 3.7)
T_RDS = (3.7, 4.6)

T_ECS_ZOOM = (4.6, 7.0)
T_QUERY_TRAVEL = (7.0, 8.0)
T_NORMAL_DB = (8.0, 9.5)

T_RESET = (9.5, 10.5)

T_ATTACK_REQUEST = (10.5, 11.5)
T_MALICIOUS_ECS = (11.5, 13.0)
T_MALICIOUS_TRAVEL = (13.0, 14.0)
T_MALICIOUS_DB = (14.0, 15.2)

T_IMPACT = (15.2, 16.0)


# ---------------------------------------------------------------------------
# Popup geometry
#
# These are preferred sizes. Actual position is calculated from the
# active node and hard-clamped inside MAIN_PANEL.
# ---------------------------------------------------------------------------

POPUPS = {
    "api": {
        "width": 390,
        "height": 190,
        "preferred": "above",
        "offset_y": 18,
    },
    "ecs": {
        "width": 500,
        "height": 230,
        "preferred": "above",
        "offset_y": 18,
    },
    "rds": {
        "width": 500,
        "height": 230,
        "preferred": "above",
        "offset_y": 18,
    },
}


# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------

BACKGROUND_TOP = (5, 12, 28)
BACKGROUND_BOTTOM = (8, 20, 42)

WHITE = (235, 245, 255)
MUTED = (130, 157, 188)
DIM = (65, 84, 112)

CYAN = (54, 210, 255)
PURPLE = (170, 105, 255)
ORANGE = (255, 160, 65)
BLUE = (80, 150, 255)
RED = (255, 75, 90)
GREEN = (70, 225, 145)

PANEL_FILL = (10, 24, 48, 215)
PANEL_BORDER = (65, 105, 150, 150)

GRID = (32, 57, 88)


# ---------------------------------------------------------------------------
# Text
# ---------------------------------------------------------------------------

TITLE = "SQL INJECTION"

SUBTITLE = "HOW INPUT CAN CHANGE DATABASE BEHAVIOR"

NODE_LABELS = {
    "client": "CLIENT",
    "api": "API GATEWAY",
    "ecs": "ECS SERVICE",
    "rds": "RDS DATABASE",
}


# ---------------------------------------------------------------------------
# SQL
# ---------------------------------------------------------------------------

NORMAL_SQL = [
    "SELECT *",
    "FROM users",
    "WHERE id = ?",
]

MALICIOUS_SQL = [
    "SELECT *",
    "FROM users",
    "WHERE id = <unexpected input>",
]


# ---------------------------------------------------------------------------
# Discussion text
# ---------------------------------------------------------------------------

DISCUSSION = {
    "architecture": (
        "A request moves through multiple layers before reaching data."
    ),
    "normal_request": (
        "The application normally treats user input as data."
    ),
    "api": (
        "The API receives the request and forwards application input."
    ),
    "ecs": (
        "The service constructs the database operation."
    ),
    "rds": (
        "The database executes the resulting query."
    ),
    "ecs_zoom": (
        "The dangerous boundary appears when input influences query structure."
    ),
    "query_travel": (
        "The generated query is sent from the service to the database."
    ),
    "normal_db": (
        "The database evaluates the expected parameterized request."
    ),
    "reset": (
        "Now consider what happens when the input is no longer treated safely."
    ),
    "attack_request": (
        "An attacker introduces deliberately crafted input."
    ),
    "malicious_ecs": (
        "Unsafe query construction can change the intended database operation."
    ),
    "malicious_travel": (
        "The altered query reaches the database."
    ),
    "malicious_db": (
        "The database executes behavior that the application did not intend."
    ),
    "impact": (
        "A small input-validation mistake can become a data-security incident."
    ),
}


# ---------------------------------------------------------------------------
# Scene-local assets
# ---------------------------------------------------------------------------

ASSET_ROOT_NAME = "scene_01_reference_assets"

ASSETS = {
    "client": "icons/client.png",
    "api": "icons/api_gateway.png",
    "ecs": "icons/ecs.png",
    "rds": "icons/rds.png",
    "attacker": "icons/attacker.png",

    "blue_panel": "panels/blue_panel.png",
    "orange_panel": "panels/orange_large_panel.png",
    "purple_panel": "panels/purple_panel.png",
    "red_panel": "panels/red_panel.png",

    "cyan_particle": "particles/cyan_particle.png",
    "red_particle": "particles/red_particle.png",

    "blue_ring": "rings/blue_ring.png",
    "orange_ring": "rings/orange_ring.png",

    "cyan_arrow": "arrows/cyan_arrow.png",
    "orange_arrow": "arrows/orange_arrow.png",
    "red_arrow": "arrows/red_arrow.png",
}


# ---------------------------------------------------------------------------
# Timing helpers
# ---------------------------------------------------------------------------

TIMELINE = (
    ("architecture", *T_ARCHITECTURE),
    ("normal_request", *T_NORMAL_REQUEST),
    ("api", *T_API),
    ("ecs", *T_ECS),
    ("rds", *T_RDS),
    ("ecs_zoom", *T_ECS_ZOOM),
    ("query_travel", *T_QUERY_TRAVEL),
    ("normal_db", *T_NORMAL_DB),
    ("reset", *T_RESET),
    ("attack_request", *T_ATTACK_REQUEST),
    ("malicious_ecs", *T_MALICIOUS_ECS),
    ("malicious_travel", *T_MALICIOUS_TRAVEL),
    ("malicious_db", *T_MALICIOUS_DB),
    ("impact", *T_IMPACT),
)