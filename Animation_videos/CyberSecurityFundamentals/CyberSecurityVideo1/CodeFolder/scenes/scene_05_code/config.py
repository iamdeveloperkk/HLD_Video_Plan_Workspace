"""Scene 5 layout and timing constants."""

SCENE_NAME = "scene_05"
SCENE_TITLE = "INTEGRITY BREACH"

MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 360)

# Timeline
TITLE_REVEAL = 0.4

USER_REVEAL = 1.0
REQUEST_REVEAL = 2.2
ORDER_REVEAL = 3.6
MODIFICATION_REVEAL = 6.4
CORRUPTED_VALUE_REVEAL = 8.0
VALIDATION_REVEAL = 10.4
RESTORED_REVEAL = 12.4
TAKEAWAY_REVEAL = 14.2

# Main visual layout
# Rect = (x, y, width, height)

USER_RECT = (65, 235, 145, 110)

SERVICE_RECT = (290, 220, 200, 140)

DATABASE_RECT = (555, 190, 270, 110)

ORDER_RECT = (555, 330, 270, 80)

VALIDATION_RECT = (290, 395, 200, 90)

# Right-side discussion panel
PANEL_TITLE = "INTEGRITY BREACH"

DISCUSSION_POINTS = [
    "A legitimate order is created",
    "Stored value should not change unexpectedly",
    "An attacker modifies the data",
    "Integrity protects correctness and trust",
]

DISCUSSION_REVEALS = [
    USER_REVEAL,
    ORDER_REVEAL,
    MODIFICATION_REVEAL,
    VALIDATION_REVEAL,
]

TAKEAWAY = "INTEGRITY = DATA CANNOT BE CHANGED UNAUTHORIZED"