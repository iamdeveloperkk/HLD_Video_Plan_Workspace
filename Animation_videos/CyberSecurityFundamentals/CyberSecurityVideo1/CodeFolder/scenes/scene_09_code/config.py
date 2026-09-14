"""Scene 9 layout and timing constants."""
SCENE_NAME = "scene_09"
SCENE_TITLE = "FINDING THE WEAKNESS"
MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 405)
TITLE_REVEAL = 0.4
REQUEST_REVEAL = 1.0
SERVICE_REVEAL = 3.0
WEAKNESS_REVEAL = 6.0
BOUNDARY_REVEAL = 8.4
TAKEAWAY_REVEAL = 13.8
REQUEST_RECT = (70, 245, 160, 100)
SERVICE_RECT = (315, 190, 260, 210)
DATA_RECT = (680, 245, 150, 100)
DISCUSSION_POINTS = [
    "A vulnerability is a weakness in a system",
    "Code, configuration, identity, or design can fail",
    "Reachability determines whether it matters",
    "The weakness becomes dangerous when exploitable",
]
DISCUSSION_REVEALS = [1.0, 3.0, 6.0, 9.0]
TAKEAWAY = "VULNERABILITY = WEAKNESS THAT CAN BE EXPLOITED"
