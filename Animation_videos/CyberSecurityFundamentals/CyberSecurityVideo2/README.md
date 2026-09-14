# Video Project: Rate Limiting

## Video profile

- **Video title:** TBD
- **Topic:** Rate Limiting
- **Video type:** TBD
- **Target audience:** TBD
- **Objective:** TBD
- **Current status:** IDEA

## Production progress

| Stage | Status | Notes |
| --- | --- | --- |
| Idea | TODO | |
| Research | TODO | |
| Blueprint | TODO | |
| Script | TODO | |
| Storyboard | TODO | |
| Visual assets | TODO | |
| Voice/audio | TODO | |
| Editing | TODO | |
| Thumbnail | TODO | |
| Publishing | TODO | |
| Repurposing | TODO | |
| Analytics | TODO | |
| Learnings | TODO | |

## Project documents

- [Checklist](CHECKLIST.md)
- [Research](RESEARCH.md)
- [Blueprint](BLUEPRINT.md)
- [Script](SCRIPT.md)
- [Storyboard](STORYBOARD.md)
- [Visuals](VISUALS.md)
- [Publishing](PUBLISHING.md)
- [Analytics](ANALYTICS.md)

## Important decisions

| Decision | Rationale | Date |
| --- | --- | --- |
|  |  |  |

## Animation Workspace

Video 2 is scaffolded for seven independent scenes and uses the shared engine in `Animation_videos/_common`.

```text
CyberSecurityVideo2/
├── CodeFolder/
│   ├── video_config.py
│   └── scenes/
│       ├── scene_01_code/scene.py
│       ├── scene_02_code/scene.py
│       ├── scene_03_code/scene.py
│       ├── scene_04_code/scene.py
│       ├── scene_05_code/scene.py
│       ├── scene_06_code/scene.py
│       └── scene_07_code/scene.py
├── AssetFolder/
└── OutputFolder/
		├── scene_01_output/
		├── scene_02_output/
		├── scene_03_output/
		├── scene_04_output/
		├── scene_05_output/
		├── scene_06_output/
		└── scene_07_output/
```

Fill each scene's `scene.py` and `config.py`. Scene code should expose `render_scene(output)` and import reusable components from `_common.engine`.

Compile all seven scenes from `Animation_videos/`:

```bash
for scene in 01 02 03 04 05 06 07; do
	python3 -m py_compile \
		CyberSecurityFundamentals/CyberSecurityVideo2/CodeFolder/scenes/scene_${scene}_code/scene.py \
		CyberSecurityFundamentals/CyberSecurityVideo2/CodeFolder/scenes/scene_${scene}_code/config.py
done
```

Render an implemented scene:

```bash
python3 -m tools.render_scene \
	--series CyberSecurityFundamentals \
	--video CyberSecurityVideo2 \
	--scene scene_01
```

The renderer writes to the matching `OutputFolder/scene_01_output/` directory.

## External asset references

| Asset | Location or URL | License/usage notes |
| --- | --- | --- |
|  |  |  |

