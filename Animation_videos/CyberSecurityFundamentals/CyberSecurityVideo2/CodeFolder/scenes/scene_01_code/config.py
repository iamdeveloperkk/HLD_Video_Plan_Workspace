"""Scene 01 layout and timing constants."""
SCENE_NAME = "scene_01"
SCENE_TITLE = 'SQL Injection'
MAIN_PANEL = (35, 105, 875, 515)
RIGHT_PANEL = (930, 45, 300, 405)
TITLE_REVEAL = 0.4
TAKEAWAY_REVEAL = 14.0
DISCUSSION_POINTS = ['Application builds a database query', 'Untrusted input reaches the query layer', 'Query structure is altered', 'Database returns unintended data']
DISCUSSION_REVEALS = [1.0, 3.0, 6.0, 9.0]
TAKEAWAY = 'SQL INJECTION = INPUT CHANGES QUERY MEANING'

NODE_REVEALS = {
	"client": 1.0,
	"gateway": 2.4,
	"service": 3.8,
	"database": 5.2,
	"attacker": 8.2,
}

NODE_LAYOUT = {
	"client": (65, 255, 150, 105),
	"gateway": (275, 255, 170, 105),
	"service": (500, 255, 175, 105),
	"database": (735, 255, 150, 105),
	"attacker": (70, 430, 150, 85),
}
