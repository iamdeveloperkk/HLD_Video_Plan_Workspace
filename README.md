# HLD Video Plan Workspace

This repository is a Git-versioned YouTube Creator Operating System for technical HLD, LLD, and system-design educational videos. It preserves the research, decisions, production material, publication details, performance, and learnings for every video.

The governing principle is: **ideas are flexible; video production is standardized.**

Start Codex from this folder so it follows `AGENTS.md` and `MASTER_VIDEO_INSTRUCTIONS.md`.

```sh
cd ~/Documents/WorkSpaces/HLD_Video_Plan_Workspace
codex
```

## Structure

- `MASTER_VIDEO_INSTRUCTIONS.md` — permanent production SOP for every video.
- `research/topic-research/` — reusable research across topics.
- `videos/_template/` — the standardized project template.
- `videos/<video-slug>/` — one complete production record per video.
- `content/` — flexible ideas and the content calendar.
- `analytics/` and `channel/` — channel-level performance and long-term insights.

## Create a video workspace

Copy the template folder and replace `video-slug` with a short descriptive name:

```sh
cp -R videos/_template videos/video-slug
```

Then update the new folder's `README.md`, progress through `CHECKLIST.md`, and retain the work in Git.
