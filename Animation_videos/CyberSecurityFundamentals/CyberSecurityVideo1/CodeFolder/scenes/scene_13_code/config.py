"""Scene 13 layout and timing constants."""
SCENE_NAME = "scene_13"
SCENE_TITLE = "THE INVESTIGATION CONTINUES"
MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 405)
TITLE_REVEAL = 0.4
CARD_REVEALS = [1.0, 2.4, 3.8, 5.2, 6.6, 8.0]
QUESTION_REVEAL = 10.2
SERIES_REVEAL = 13.0
CARDS = [
    ("SQL INJECTION", "Data-layer attack"),
    ("XSS", "Victim-browser attack"),
    ("CSRF", "Cross-site action"),
    ("DDoS", "Availability attack"),
    ("CREDENTIAL ATTACKS", "Identity abuse"),
    ("MITM / MALWARE", "Traffic / endpoint threats"),
]
DISCUSSION_POINTS = [
    "Each attack uses a different path and weakness",
    "The same security model helps analyze all of them",
    "Next episodes go deeper into attack mechanics",
]
DISCUSSION_REVEALS = [1.0, 5.2, 10.2]
TAKEAWAY = "NEXT: HOW THESE ATTACKS ACTUALLY WORK"
