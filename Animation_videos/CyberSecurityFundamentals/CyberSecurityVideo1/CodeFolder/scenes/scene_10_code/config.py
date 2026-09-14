"""Scene 10 layout and timing constants."""
SCENE_NAME = "scene_10"
SCENE_TITLE = "VULNERABILITY BECOMES AN ATTACK"
MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 405)
TITLE_REVEAL = 0.4
NORMAL_REVEAL = 1.0
BOUNDARY_REVEAL = 3.0
ATTACK_REVEAL = 5.4
EXPLOIT_REVEAL = 7.2
IMPACT_REVEAL = 10.0
TAKEAWAY_REVEAL = 14.0
CLIENT_RECT = (65, 250, 150, 100)
EDGE_RECT = (285, 225, 155, 150)
SERVICE_RECT = (520, 200, 200, 200)
DATA_RECT = (770, 250, 80, 100)
DISCUSSION_POINTS = [
    "The attacker sends a crafted request",
    "Security boundaries inspect the request",
    "A weakness lets the request cross a boundary",
    "The attack is the exploitation of that weakness",
]
DISCUSSION_REVEALS = [1.0, 3.0, 7.2, 10.0]
TAKEAWAY = "ATTACK = EXPLOITING A VULNERABILITY"
