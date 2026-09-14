"""Standalone runtime test for the shared SVG icon system."""

from pathlib import Path

from PIL import ImageDraw

from _common.engine.canvas import Canvas, PANEL, WHITE
from _common.engine.icon_node import IconNode
from _common.engine.icon_registry import configure_asset_roots
from _common.engine.renderer import Renderer
from _common.engine.layout import Rect
from _common.engine.typography import font


ROOT = Path(__file__).resolve().parents[1]
COMMON_ASSETS = ROOT / "assets"
VIDEO2_ASSETS = ROOT.parent / "CyberSecurityFundamentals" / "CyberSecurityVideo2" / "AssetFolder"
OUTPUT = Path("/tmp/common_icon_system_test.png")


def main() -> None:
    configure_asset_roots(VIDEO2_ASSETS, COMMON_ASSETS)
    canvas = Canvas(width=1280, height=720, fps=30, duration=1.0)
    image = Renderer(canvas).background()
    draw = ImageDraw.Draw(image)
    draw.text((50, 30), "COMMON SVG ICON SYSTEM TEST", font=font(26, True), fill=WHITE)

    icons = [
        ("aws.api_gateway", "API Gateway"),
        ("aws.ecs", "ECS"),
        ("aws.rds", "RDS"),
        ("aws.waf", "WAF"),
        ("aws.cloudfront", "CloudFront"),
        ("aws.iam", "IAM"),
        ("aws.sqs", "SQS"),
        ("generic.user", "User"),
        ("generic.database", "Database"),
    ]
    nodes = []
    for index, (logical_name, label) in enumerate(icons):
        column = index % 3
        row = index // 3
        node = IconNode(
            icon=logical_name,
            label=label,
            width=180,
            height=150,
            x=60 + column * 260,
            y=100 + row * 185,
            sequence=index + 1,
            reveal=0.0,
            icon_size=64,
        )
        if node.icon_path is None:
            raise RuntimeError(f"Missing registered icon asset: {logical_name}")
        node.draw(image, elapsed=1.0, active=index == 0)
        nodes.append(node)

    draw.text((50, 675), f"Rendered {len(nodes)} logical icons", font=font(16), fill=WHITE)
    image.convert("RGB").save(OUTPUT)
    print(f"ICON TEST PASS: {OUTPUT}")
    for node in nodes:
        print(f"{node.icon_name}: {node.icon_path}")


if __name__ == "__main__":
    main()
