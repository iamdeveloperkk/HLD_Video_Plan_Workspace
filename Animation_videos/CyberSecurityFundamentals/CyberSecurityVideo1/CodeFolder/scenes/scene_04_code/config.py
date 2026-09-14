"""Scene 4 layout and timing constants."""

SCENE_NAME = "scene_04"
SCENE_TITLE = "CONFIDENTIALITY BREACH"

MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 360)

# Timeline
TITLE_REVEAL = 0.4

USER_A_REVEAL = 1.0
AUTH_REVEAL = 2.4
USER_B_REVEAL = 4.6
BREACH_REVEAL = 6.4
AUTHZ_REVEAL = 8.8
FIX_REVEAL = 11.8
TAKEAWAY_REVEAL = 14.2

# Main architecture
USER_A_RECT = (75, 235, 115, 100)
AUTH_RECT = (270, 235, 160, 100)
DATA_RECT = (505, 195, 310, 80)
USER_B_RECT = (505, 315, 310, 80)

# Right-side discussion panel
PANEL_TITLE = "CONFIDENTIALITY BREACH"

DISCUSSION_POINTS = [
    "User A is authenticated",
    "But User A requests User B's data",
    "Authentication ≠ Authorization",
    "Authorization must enforce ownership",
]

DISCUSSION_REVEALS = [
    USER_A_REVEAL,
    BREACH_REVEAL,
    AUTHZ_REVEAL,
    FIX_REVEAL,
]

TAKEAWAY = "AUTHENTICATED ≠ AUTHORIZED"