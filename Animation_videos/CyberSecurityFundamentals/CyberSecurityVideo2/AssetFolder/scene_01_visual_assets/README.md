# Scene 01 Cinematic Visual Asset Pack v2

Use these as compositing layers with the existing official AWS SVG icons.

ICON TILES:
- cyan_tile.png -> Client
- purple_tile.png -> API Gateway
- orange_tile.png -> ECS
- blue_tile.png -> RDS
- red_tile.png -> Attacker

The tiles are intentionally icon-free. Place the official AWS SVG / actor
line icon centered on top of the tile.

PARTICLES:
- cyan_request.png
- cyan_sql.png
- red_attack.png
- red_impact.png

RINGS:
- orange_active_ring.png
- blue_active_ring.png
- red_active_ring.png

PANELS:
- purple_popup.png
- orange_popup.png
- blue_popup.png
- red_popup.png
- green_popup.png

ARROWS:
- cyan_flow_arrow.png
- orange_flow_arrow.png
- blue_flow_arrow.png
- red_flow_arrow.png

BACKGROUND:
- matched_cinematic_background.png

FONT:
Inter Regular / Medium / SemiBold / Bold.
Use Inter for all scene text. Prefer Inter SemiBold/Bold for headings and
Inter Regular/Medium for body/code. Do not mix random fonts.

COLOR IDENTITY:
Cyan = client/request
Purple = API Gateway
Orange = ECS
Blue = RDS
Red = attacker/impact
Green = defense

IMPORTANT:
These assets are intentionally separated into layers. Do not bake text,
icons, or arrows into one composite image. Python should animate each layer
independently for frame-by-frame control.
