"""Scene 03 layout and timing constants."""
SCENE_NAME = "scene_03"
SCENE_TITLE = 'CSRF'
MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 405)
TITLE_REVEAL = 0.4
TAKEAWAY_REVEAL = 14.0
DISCUSSION_POINTS = ['Victim is already authenticated', 'A cross-site request is triggered', "Server sees the victim's session", 'CSRF defenses verify request intent']
DISCUSSION_REVEALS = [1.0, 3.0, 6.0, 9.0]
TAKEAWAY = 'CSRF = TRICKING AN AUTHENTICATED BROWSER INTO AN ACTION'
