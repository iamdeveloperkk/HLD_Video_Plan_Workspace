"""Render a video scene through its common engine."""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ANIMATION_ROOT = Path(__file__).resolve().parents[2]


def load_scene(series: str, video: str, scene: str):
    video_root = ANIMATION_ROOT / series / video / "CodeFolder"
    scene_file = video_root / "scenes" / scene / "code" / "scene.py"
    if not scene_file.exists():
        scene_file = video_root / "scenes" / scene / "code" / f"{scene}.py"
    if not scene_file.exists():
        raise SystemExit(f"{series}/{video}/CodeFolder/scenes/{scene}")
    spec = importlib.util.spec_from_file_location(f"{series}.{video}.{scene}", scene_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description="Render one technical animation scene")
    parser.add_argument("--series", default="CyberSecurityFundamentals")
    parser.add_argument("--video", required=True)
    parser.add_argument("--scene", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    module = load_scene(args.series, args.video, args.scene)
    video_root = ANIMATION_ROOT / args.series / args.video
    output = args.output or video_root / "OutputFolder" / args.scene / f"{args.video}_{args.scene}.mp4"
    module.render_scene(output)


if __name__ == "__main__":
    main()
