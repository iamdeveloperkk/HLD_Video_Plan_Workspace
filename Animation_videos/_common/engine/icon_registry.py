"""Logical icon names mapped to creator-supplied asset locations."""

from pathlib import Path

COMMON_ASSET_ROOT = Path(__file__).resolve().parents[1] / "assets" / "icons"
ASSET_ROOTS = [COMMON_ASSET_ROOT]

ICONS = {
    "aws.sns": "aws/sns.svg",
    "aws.sqs": "aws/sqs.svg",
    "aws.lambda": "aws/lambda.svg",
    "aws.ecs": "aws/ecs.svg",
    "aws.s3": "aws/s3.svg",
    "aws.cloudfront": "aws/cloudfront.svg",
    "aws.waf": "aws/waf.svg",
    "aws.api_gateway": "aws/api_gateway.svg",
    "aws.dynamodb": "aws/dynamodb.svg",
    "kafka": "messaging/kafka.svg",
    "rabbitmq": "messaging/rabbitmq.svg",
    "redis": "databases/redis.svg",
    "postgres": "databases/postgres.svg",
    "mysql": "databases/mysql.svg",
    "docker": "infrastructure/docker.svg",
    "kubernetes": "infrastructure/kubernetes.svg",
    "generic.user": "generic/user.svg",
    "generic.attacker": "generic/attacker.svg",
    "generic.database": "generic/database.svg",
    "generic.firewall": "generic/firewall.svg",
    "generic.server": "generic/server.svg",
    "generic.service": "generic/service.svg",
}


def configure_asset_roots(*roots: Path) -> None:
    global ASSET_ROOTS
    ASSET_ROOTS = [Path(root) for root in roots] + [COMMON_ASSET_ROOT]


def resolve_icon(logical_name: str):
    relative_path = ICONS.get(logical_name)
    if not relative_path:
        return None
    for root in ASSET_ROOTS:
        path = root / relative_path
        if path.exists():
            return path
    return None
