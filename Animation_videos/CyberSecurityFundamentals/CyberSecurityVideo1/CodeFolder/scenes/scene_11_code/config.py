"""Scene 11 layout and timing constants."""
SCENE_NAME = "scene_11"
SCENE_TITLE = "SO HOW BAD IS IT?"
MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 405)
TITLE_REVEAL = 0.4
IMPACT_REVEAL = 2.0
LIKELIHOOD_REVEAL = 5.0
RISK_REVEAL = 8.0
ESCALATION_REVEAL = 10.5
TAKEAWAY_REVEAL = 14.0
MATRIX_RECT = (90, 190, 420, 300)
IMPACT_RECT = (585, 200, 250, 95)
LIKELIHOOD_RECT = (585, 325, 250, 95)
RISK_RECT = (585, 450, 250, 45)
DISCUSSION_POINTS = [
    "Impact asks what happens if the attack succeeds",
    "Likelihood asks how plausible the event is",
    "Risk combines likelihood and impact",
    "High-impact systems need stronger controls",
]
DISCUSSION_REVEALS = [2.0, 5.0, 8.0, 11.0]
TAKEAWAY = "RISK = LIKELIHOOD × IMPACT"
