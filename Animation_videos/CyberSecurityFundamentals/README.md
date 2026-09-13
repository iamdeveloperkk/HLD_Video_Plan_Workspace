# Cyber Attack X FAANG Animation Workspace

This workspace separates reusable rendering infrastructure from video-specific and scene-specific composition.

```text
Animation_videos/
├── _common/                     # Shared by every video series
│   ├── engine/
│   ├── assets/
│   └── tools/
│       └── render_scene.py
├── _template/
└── CyberSecurityFundamentals/
	└── CyberSecurityVideo1/
		├── CodeFolder/
		│   ├── video_config.py
		│   └── scenes/scene_02_code/
		│       ├── scene.py
		│       ├── config.py
		│       └── assets/
		├── AssetFolder/
		└── OutputFolder/scene_02_output/
```

## Scene Files To Fill

For every new scene, create a folder using the explicit code suffix:

```text
CyberSecurityVideo1/
├── CodeFolder/
│   ├── video_config.py             # Video-wide canvas and theme
│   └── scenes/
│       └── scene_03_code/
│           ├── scene.py           # Scene composition and rendering entry point
│           ├── config.py          # Scene-specific timing, layout, and constants
│           └── assets/             # Optional scene-only assets
│               ├── icons/
│               ├── diagrams/
│               ├── backgrounds/
│               └── audio/
├── AssetFolder/                   # Assets shared by the whole video
│   ├── icons/
│   ├── diagrams/
│   ├── backgrounds/
│   └── audio/
└── OutputFolder/
	└── scene_03_output/           # Generated files; do not place source code here
```

Fill these files for a scene:

1. `scene.py`: build the scene, use `_common.engine`, and expose `render_scene(output)` for the shared CLI.
2. `config.py`: keep scene-only values such as dimensions, timing, labels, panel positions, and asset constants.
3. `assets/`: add only assets unique to that scene. Put video-wide assets in the video `AssetFolder/` instead.
4. `video_config.py`: edit this only when the entire video needs a different canvas, FPS, duration, or theme.

Do not copy `_common/` into a video. Do not put generated MP4 files in `CodeFolder`.

## Installation

Use Python 3.9+:

```bash
python3 -m pip install -r requirements.txt
```

Install FFmpeg separately and ensure `ffmpeg` is on `PATH`.

## Compile And Render From Command Line

Run these commands from `Animation_videos/`:

Compile one scene without rendering:

```bash
python3 -m py_compile \
	CyberSecurityFundamentals/CyberSecurityVideo1/CodeFolder/scenes/scene_01_code/scene.py \
	CyberSecurityFundamentals/CyberSecurityVideo1/CodeFolder/scenes/scene_01_code/config.py
```

Compile all shared and Video 1 Python files:

```bash
python3 -m compileall -q \
	_common \
	tools \
	CyberSecurityFundamentals/CyberSecurityVideo1/CodeFolder
```

Render Scene 1:

```bash
python3 -m tools.render_scene \
	--series CyberSecurityFundamentals \
	--video CyberSecurityVideo1 \
	--scene scene_01
```

Render Scene 2:

```bash
python3 -m tools.render_scene \
	--series CyberSecurityFundamentals \
	--video CyberSecurityVideo1 \
	--scene scene_02
```

The logical scene name maps automatically:

```text
scene_01 -> CodeFolder/scenes/scene_01_code/scene.py
scene_01 -> OutputFolder/scene_01_output/

scene_02 -> CodeFolder/scenes/scene_02_code/scene.py
scene_02 -> OutputFolder/scene_02_output/
```

Expected outputs:

```text
CyberSecurityVideo1/OutputFolder/scene_01_output/CyberSecurityVideo1_scene_01.mp4
CyberSecurityVideo1/OutputFolder/scene_02_output/CyberSecurityVideo1_scene_02.mp4
```

The renderer validates and loads the scene before encoding. A successful scene should print `LAYOUT VALIDATION: PASS` when the scene implements layout validation, followed by an `OUTPUT` or `Output` path.

Direct scene execution also works:

```bash
python3 CyberSecurityFundamentals/CyberSecurityVideo1/CodeFolder/scenes/scene_02_code/scene.py
```

Custom output:

```bash
python3 -m tools.render_scene \
	--series CyberSecurityFundamentals \
	--video CyberSecurityVideo1 \
	--scene scene_02 \
	--output CyberSecurityFundamentals/CyberSecurityVideo1/OutputFolder/scene_02_output/test_scene.mp4
```

## Ownership Rules

- `_common/engine/` owns how components draw, animate, validate, and encode across all series.
- `_common/assets/` owns assets reusable across all videos and series.
- `CyberSecurityVideo1/CodeFolder/video_config.py` owns video-wide canvas and theme settings.
- `CyberSecurityVideo1/CodeFolder/reusable/` owns components shared only by that video.
- `CyberSecurityVideo1/AssetFolder/` owns assets shared by that video.
- `CyberSecurityVideo1/CodeFolder/scenes/<scene>_code/` owns scene implementation and local assets.
- `CyberSecurityVideo1/OutputFolder/<scene>_output/` owns generated scene output.
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
3. Create one directory per scene under `CodeFolder/scenes/scene_nn_code/`, containing `scene.py`, optional `config.py`, and optional scene assets.
4. Keep scene code declarative: instantiate components, calculate layout, schedule timeline events, connect nodes, and provide a frame builder.
5. Reuse `_common.engine.Renderer` and common validation rather than copying drawing or FFmpeg logic.
6. Render through `tools.render_scene`.

Use Python for scene orchestration and rendering. C++ is not part of the default architecture; introduce it only after profiling demonstrates a specific performance bottleneck.
