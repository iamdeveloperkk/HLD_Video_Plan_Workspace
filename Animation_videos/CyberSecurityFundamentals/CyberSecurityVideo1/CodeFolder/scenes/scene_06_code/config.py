"""Scene 6 layout and timing constants."""

SCENE_NAME = "scene_06"
SCENE_TITLE = "AVAILABILITY ATTACK"

MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 390)

# Timeline
TITLE_REVEAL = 0.4

USERS_REVEAL = 1.0
SERVICE_REVEAL = 2.2
NORMAL_TRAFFIC_REVEAL = 3.2
TRAFFIC_SPIKE_REVEAL = 5.2
QUEUE_REVEAL = 6.8
LATENCY_REVEAL = 8.2
FAILURE_REVEAL = 9.8
DEFENSE_REVEAL = 11.4
RECOVERY_REVEAL = 13.2
TAKEAWAY_REVEAL = 14.5

# Main visual layout
USERS_RECT = (65, 235, 145, 110)
EDGE_RECT = (275, 220, 175, 140)
SERVICE_RECT = (520, 220, 190, 140)
QUEUE_RECT = (520, 395, 190, 75)
DEFENSE_RECT = (745, 220, 110, 140)

# Right-side discussion panel
PANEL_TITLE = "AVAILABILITY"

DISCUSSION_POINTS = [
    "Normal traffic keeps the system healthy",
    "A sudden flood consumes capacity",
    "Queues grow and latency increases",
    "Eventually users cannot reach the service",
]

DISCUSSION_REVEALS = [
    USERS_REVEAL,
    TRAFFIC_SPIKE_REVEAL,
    QUEUE_REVEAL,
    FAILURE_REVEAL,
]

TAKEAWAY = "AVAILABILITY = SYSTEM REMAINS USABLE"