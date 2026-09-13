"""Video-wide configuration and theme."""

from common.engine.canvas import Canvas

VIDEO_NAME = "cyber_attack_x_faang"
CANVAS = Canvas(width=1280, height=720, fps=30, duration=16.0)
THEME = {
    "background": (7, 16, 34),
    "primary": (229, 242, 255),
    "secondary": (135, 163, 194),
    "accent": (69, 166, 247),
}
