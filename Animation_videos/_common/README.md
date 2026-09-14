# Common Animation Package

Shared animation infrastructure for all videos. Video and scene code imports `_common.engine`; it is not copied into individual videos.

## SVG Icons

`IconNode` renders SVG assets at runtime with CairoSVG, preserving transparency and aspect ratio. Install Python dependencies with:

```bash
python3 -m pip install -r ../requirements.txt
```

On macOS with Homebrew, install the native Cairo runtime as well:

```bash
brew install cairo
```

The logical icon lookup order is:

```text
scene-specific assets -> video AssetFolder -> _common/assets
```

Run the standalone test from `Animation_videos/`:

```bash
python3 -m _common.tools.test_icon_system
```
