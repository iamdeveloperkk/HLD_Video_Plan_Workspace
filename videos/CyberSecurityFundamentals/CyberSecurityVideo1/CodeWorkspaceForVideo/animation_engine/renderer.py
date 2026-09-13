"""Frame compositor and raw-frame FFmpeg renderer."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

from .canvas import BG, BLUE, GRID, PANEL, WHITE, MUTED
from .typography import font


class Renderer:
    def __init__(self, canvas):
        self.canvas = canvas

    def background(self):
        image = Image.new("RGBA", (self.canvas.width, self.canvas.height), BG + (255,))
        draw = ImageDraw.Draw(image)
        for x in range(0, self.canvas.width, 32):
            draw.line((x, 0, x, self.canvas.height), fill=GRID, width=1)
        for y in range(0, self.canvas.height, 32):
            draw.line((0, y, self.canvas.width, y), fill=GRID, width=1)
        return image

    def render(self, frame_builder, output: Path) -> None:
        ffmpeg = shutil.which("ffmpeg")
        if not ffmpeg:
            raise SystemExit("FFmpeg was not found on PATH. Install FFmpeg, then run this script again.")
        output.parent.mkdir(parents=True, exist_ok=True)
        command = [ffmpeg, "-y", "-f", "rawvideo", "-vcodec", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{self.canvas.width}x{self.canvas.height}", "-r", str(self.canvas.fps), "-i", "-", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output)]
        process = subprocess.Popen(command, stdin=subprocess.PIPE)
        try:
            for frame_number in range(int(self.canvas.fps * self.canvas.duration)):
                elapsed = frame_number / self.canvas.fps
                frame = np.asarray(frame_builder(elapsed).convert("RGB"), dtype=np.uint8)
                process.stdin.write(frame.tobytes())
        except BrokenPipeError as error:
            raise RuntimeError("FFmpeg stopped while receiving frames") from error
        finally:
            if process.stdin:
                process.stdin.close()
        if process.wait() != 0:
            raise RuntimeError("FFmpeg failed to encode the video")
        print(f"OUTPUT: {output}")
