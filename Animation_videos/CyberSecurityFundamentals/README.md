# Cyber Attack X FAANG Animation Workspace

This workspace separates reusable rendering infrastructure from video-specific and scene-specific composition.

```text
HLD_Video_Plan_Workspace/
├── videos/
│   ├── common/                 # Shared by every video series
│   │   ├── engine/
│   │   ├── assets/
│   │   └── asset_resolver.py
│   ├── tools/                  # Shared render commands
│   └── CyberSecurityFundamentals/
│       └── CyberSecurityVideo1/
│           └── CodeWorkspaceForVideo/
│               ├── video_config.py     # Video-wide canvas and theme
│               ├── reusable/           # Components shared by this video
│               ├── assets/             # Video-wide assets
│               └── scenes/
│                   └── scene_02/
│                       ├── code/       # Scene composition and timing
│                       ├── config.py    # Scene-specific settings
│                       ├── assets/      # Scene-only assets
│                       └── output/      # Scene-only renders
```

## Installation

Use Python 3.9+:

```bash
python3 -m pip install -r requirements.txt
```

Install FFmpeg separately and ensure `ffmpeg` is on `PATH`.

## Render Scene 2

From `HLD_Video_Plan_Workspace/`:

```bash
python3 -m videos.tools.render_scene \
	--video CyberSecurityVideo1 \
	--scene scene_02
```

Direct scene execution also works:

```bash
python3 videos/CyberSecurityFundamentals/CyberSecurityVideo1/CodeWorkspaceForVideo/scenes/scene_02/code/scene_02.py
```

Custom output:

```bash
python3 -m videos.tools.render_scene \
	--video CyberSecurityVideo1 \
	--scene scene_02 \
	--output output/test_scene.mp4
```

## Ownership Rules

- `videos/common/engine/` owns how components draw, animate, validate, and encode across all series.
- `videos/common/assets/` owns assets reusable across all videos and series.
- `CyberSecurityVideo1/CodeWorkspaceForVideo/video_config.py` owns video-wide canvas and theme settings.
- `CyberSecurityVideo1/CodeWorkspaceForVideo/reusable/` owns components shared only by that video.
- `CyberSecurityVideo1/CodeWorkspaceForVideo/assets/` owns assets shared by that video.
- `CyberSecurityVideo1/CodeWorkspaceForVideo/scenes/<scene>/` owns scene code, config, assets, and output.
- Parent creative source-of-truth files remain outside this coding workspace and are not modified by render code.

## Asset Resolution

Logical assets resolve in this order:

```text
scene assets -> video assets -> common assets
```

For icons, register the logical name in `videos/common/engine/icon_registry.py`. Place official or creator-supplied SVG/PNG files in the appropriate scope. Missing assets fall back to the generic node treatment; no brand artwork is fabricated by the engine.

## Adding A Video

1. Create `videos/<series>/<VideoName>/CodeWorkspaceForVideo/` with `video_config.py`, `reusable/`, `assets/`, and `scenes/`.
2. Create one directory per scene under `scenes/scene_nn/`, containing `code/`, `config.py`, `assets/`, and `output/`.
3. Keep scene code declarative: instantiate components, calculate layout, schedule timeline events, connect nodes, and provide a frame builder.
4. Reuse `common.engine.Renderer` and common validation rather than copying drawing or FFmpeg logic.
5. Render through `videos.tools.render_scene`.

Use Python for scene orchestration and rendering. C++ is not part of the default architecture; introduce it only after profiling demonstrates a specific performance bottleneck.
