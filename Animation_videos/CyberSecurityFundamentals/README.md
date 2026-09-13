# Cyber Attack X FAANG Animation Workspace

This workspace separates reusable rendering infrastructure from video-specific and scene-specific composition.

```text
Animation_videos/
├── _common/                     # Shared by every video series
│   ├── engine/
│   ├── assets/
│   └── tools/render_scene.py
├── _template/
└── CyberSecurityFundamentals/
	└── CyberSecurityVideo1/
		├── CodeFolder/
		│   ├── video_config.py
		│   └── scenes/scene_02/
		│       ├── code/
		│       ├── config.py
		│       └── assets/
		├── AssetFolder/
		└── OutputFolder/scene_02/
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
python3 -m _common.tools.render_scene \
	--series CyberSecurityFundamentals \
	--video CyberSecurityVideo1 \
	--scene scene_02
```

Direct scene execution also works:

```bash
python3 CyberSecurityFundamentals/CyberSecurityVideo1/CodeFolder/scenes/scene_02/code/scene_02.py
```

Custom output:

```bash
python3 -m _common.tools.render_scene \
	--series CyberSecurityFundamentals \
	--video CyberSecurityVideo1 \
	--scene scene_02 \
	--output CyberSecurityFundamentals/CyberSecurityVideo1/OutputFolder/scene_02/test_scene.mp4
```

## Ownership Rules

- `_common/engine/` owns how components draw, animate, validate, and encode across all series.
- `_common/assets/` owns assets reusable across all videos and series.
- `CyberSecurityVideo1/CodeFolder/video_config.py` owns video-wide canvas and theme settings.
- `CyberSecurityVideo1/CodeFolder/reusable/` owns components shared only by that video.
- `CyberSecurityVideo1/AssetFolder/` owns assets shared by that video.
- `CyberSecurityVideo1/OutputFolder/<scene>/` owns generated scene output.
- Parent creative source-of-truth files remain outside this coding workspace and are not modified by render code.

## Asset Resolution

Logical assets resolve in this order:

```text
scene assets -> video assets -> common assets
```

For icons, register the logical name in `_common/engine/icon_registry.py`. Place official or creator-supplied SVG/PNG files in the appropriate scope. Missing assets fall back to the generic node treatment; no brand artwork is fabricated by the engine.

## Adding A Video

1. Copy `_template/` to `videos/<series>/<VideoName>/`.
2. Keep video code in `CodeFolder/`, shared video assets in `AssetFolder/`, and renders in `OutputFolder/`.
3. Create one directory per scene under `CodeFolder/scenes/scene_nn/`, containing `code/`, `config.py`, and scene-local `assets/`.
4. Keep scene code declarative: instantiate components, calculate layout, schedule timeline events, connect nodes, and provide a frame builder.
5. Reuse `_common.engine.Renderer` and common validation rather than copying drawing or FFmpeg logic.
6. Render through `_common.tools.render_scene`.

Use Python for scene orchestration and rendering. C++ is not part of the default architecture; introduce it only after profiling demonstrates a specific performance bottleneck.
