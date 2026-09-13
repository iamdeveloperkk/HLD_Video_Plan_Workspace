# Cyber Attack X FAANG Animation Workspace

Reusable Python animation engine for clean technical architecture explainers. Scene 2 demonstrates generic `Node`, real-technology `IconNode`, computed layout, arrows, one routed request particle, a fixed discussion panel, and a reusable timeline.

## Installation

Use Python 3.9+ and install the Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Install FFmpeg separately and ensure `ffmpeg` is on `PATH`.

## Render Scene 2

From `CodeWorkspaceForVideo/`:

```bash
python3 scenes/video_01/scene_02/scene_02.py
```

Use a custom output path when needed:

```bash
python3 scenes/video_01/scene_02/scene_02.py --output output/scene02.mp4
```

The renderer validates layout before opening FFmpeg. Failed validation prints `LAYOUT VALIDATION: FAILED` and exits without rendering. A successful render prints `LAYOUT VALIDATION: PASS` and writes `output/Cyber_Attack_X_FAANG_Video01_Scene02.mp4`.

## Engine Structure

- `animation_engine/canvas.py` - resolution, FPS, duration, and visual palette.
- `animation_engine/layout.py` - `Rect`, safe-area checks, overlap checks, and text/icon overflow checks.
- `animation_engine/components.py` - base `Component`, `Panel`, and `TextNode` contracts.
- `animation_engine/nodes.py` - generic technical nodes with connection points.
- `animation_engine/icon_node.py` - icon-backed nodes with generic fallback.
- `animation_engine/icon_registry.py` - logical icon names mapped to creator-supplied assets.
- `animation_engine/arrows.py` - connection-point arrows.
- `animation_engine/particles.py` - eased particles following a component route.
- `animation_engine/timeline.py` - animation events and timeline visual.
- `animation_engine/panels.py` - fixed progressive discussion panel.
- `animation_engine/renderer.py` - raw RGB frame pipe to FFmpeg.

## Icons

Place official or creator-supplied SVG/PNG files under `assets/icons/`, then register them in `animation_engine/icon_registry.py`. Scenes use logical names such as `aws.api_gateway` or `generic.database`. Missing assets, and SVG assets when no SVG rasterizer is installed, gracefully fall back to the generic node style.

## Creating A Scene

Create a folder under `scenes/video_01/`, instantiate components, calculate positions from available space, connect nodes with `Arrow`, schedule reveals with `Timeline`, validate the scene, and pass a frame builder to `Renderer`. Keep scene code focused on what exists, where it belongs, and when it appears; drawing and encoding belong to the engine.
