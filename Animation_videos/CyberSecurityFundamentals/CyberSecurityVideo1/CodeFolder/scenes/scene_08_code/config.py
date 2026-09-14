"""Scene 8 layout and timing constants."""
SCENE_NAME = "scene_08"
SCENE_TITLE = "HOW DO THEY GET IN?"
MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 390)
TITLE_REVEAL = 0.4
CENTER_REVEAL = 1.0
PATH_REVEALS = [2.0, 4.0, 6.0, 8.0]
CONVERGE_REVEAL = 9.8
TAKEAWAY_REVEAL = 14.0
CENTER_RECT = (390, 270, 200, 115)
PATHS = [
    ("STOLEN CREDENTIALS", (65, 175, 190, 82)),
    ("EXPOSED ENDPOINT", (65, 400, 190, 82)),
    ("MALICIOUS INPUT", (645, 175, 190, 82)),
    ("MISCONFIGURATION", (645, 400, 190, 82)),
]
DISCUSSION_POINTS = [
    "Threats need a path to reach the system",
    "Credentials can become an entry path",
    "Exposed interfaces create reachable surfaces",
    "Weak configuration can open unintended paths",
]
DISCUSSION_REVEALS = [1.0, 2.0, 6.0, 8.0]
TAKEAWAY = "THREAT VECTOR = PATH TO THE TARGET"
