"""Scene 12 layout and timing constants."""
SCENE_NAME = "scene_12"
SCENE_TITLE = "BIG-TECH SECURITY IS LAYERS"
MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 405)
TITLE_REVEAL = 0.4
LAYER_REVEALS = [1.0, 2.2, 3.4, 4.6, 5.8, 7.0, 8.2, 9.4]
ATTACK_REVEAL = 11.0
TAKEAWAY_REVEAL = 14.0
LAYERS = [
    "EDGE / CDN",
    "WAF",
    "API GATEWAY",
    "AUTHENTICATION",
    "AUTHORIZATION",
    "RATE LIMITING",
    "SERVICES",
    "DATA + AUDIT",
]
DISCUSSION_POINTS = [
    "No single control should carry the whole system",
    "Each layer reduces a different class of risk",
    "Controls can detect, block, limit, or recover",
    "Defense in depth assumes something will fail",
]
DISCUSSION_REVEALS = [1.0, 4.6, 8.2, 11.0]
TAKEAWAY = "DEFENSE IN DEPTH = MULTIPLE SECURITY LAYERS"
