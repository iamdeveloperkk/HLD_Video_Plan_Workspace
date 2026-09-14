"""Scene 3 layout and timing constants."""

SCENE_NAME = "scene_03"
SCENE_TITLE = "WHAT ARE WE PROTECTING?"


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 330)

ARCHITECTURE_SEPARATION = 50


# ---------------------------------------------------------------------------
# Scene timing
# ---------------------------------------------------------------------------

TITLE_REVEAL = 0.4

CONFIDENTIALITY_REVEAL = 2.4
INTEGRITY_REVEAL = 6.2
AVAILABILITY_REVEAL = 10.0

TAKEAWAY_REVEAL = 14.0


# ---------------------------------------------------------------------------
# CIA cards
# ---------------------------------------------------------------------------

CARD_WIDTH = 245
CARD_HEIGHT = 230

CARD_Y = 220

CARD_GAP = 25

CARD_X = (
    65,
    65 + CARD_WIDTH + CARD_GAP,
    65 + (CARD_WIDTH + CARD_GAP) * 2,
)


CIA_SPECS = {
    "CONFIDENTIALITY": {
        "subtitle": "Who can see the data?",
        "description": "Prevent unauthorized access",
        "reveal": CONFIDENTIALITY_REVEAL,
    },
    "INTEGRITY": {
        "subtitle": "Can someone change it?",
        "description": "Prevent unauthorized changes",
        "reveal": INTEGRITY_REVEAL,
    },
    "AVAILABILITY": {
        "subtitle": "Can users access it?",
        "description": "Keep systems usable",
        "reveal": AVAILABILITY_REVEAL,
    },
}


# ---------------------------------------------------------------------------
# Discussion panel
# ---------------------------------------------------------------------------

PANEL_TITLE = "WHAT ARE WE PROTECTING?"

DISCUSSION_POINTS = [
    "Confidentiality → unauthorized access",
    "Integrity → unauthorized changes",
    "Availability → system remains usable",
]

DISCUSSION_REVEALS = [
    CONFIDENTIALITY_REVEAL,
    INTEGRITY_REVEAL,
    AVAILABILITY_REVEAL,
]


# ---------------------------------------------------------------------------
# Takeaway
# ---------------------------------------------------------------------------

TAKEAWAY = "SECURITY = PROTECTING ALL THREE"