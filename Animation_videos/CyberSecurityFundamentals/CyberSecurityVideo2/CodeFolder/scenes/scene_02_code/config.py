"""Scene 02 layout and timing constants."""
SCENE_NAME = "scene_02"
SCENE_TITLE = 'Cross-Site Scripting'
MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 405)
TITLE_REVEAL = 0.4
TAKEAWAY_REVEAL = 14.0
DISCUSSION_POINTS = ['Attacker-controlled content reaches a page', 'Browser interprets unsafe content', "Code runs in the victim's browser context", 'Output encoding and CSP reduce exposure']
DISCUSSION_REVEALS = [1.0, 3.0, 6.0, 9.0]
TAKEAWAY = 'XSS = UNTRUSTED CONTENT EXECUTES IN A BROWSER CONTEXT'
