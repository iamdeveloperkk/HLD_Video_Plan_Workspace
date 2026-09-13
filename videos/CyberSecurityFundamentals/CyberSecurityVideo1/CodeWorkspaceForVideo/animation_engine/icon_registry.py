"""Logical icon names mapped to creator-supplied asset locations."""

from pathlib import Path

ASSET_ROOT = Path(__file__).resolve().parents[1] / "assets" / "icons"

ICONS = {
    "aws.sns": ASSET_ROOT / "aws" / "sns.svg",
    "aws.sqs": ASSET_ROOT / "aws" / "sqs.svg",
    "aws.lambda": ASSET_ROOT / "aws" / "lambda.svg",
    "aws.ecs": ASSET_ROOT / "aws" / "ecs.svg",
    "aws.s3": ASSET_ROOT / "aws" / "s3.svg",
    "aws.cloudfront": ASSET_ROOT / "aws" / "cloudfront.svg",
    "aws.waf": ASSET_ROOT / "aws" / "waf.svg",
    "aws.api_gateway": ASSET_ROOT / "aws" / "api_gateway.svg",
    "aws.dynamodb": ASSET_ROOT / "aws" / "dynamodb.svg",
    "kafka": ASSET_ROOT / "messaging" / "kafka.svg",
    "rabbitmq": ASSET_ROOT / "messaging" / "rabbitmq.svg",
    "redis": ASSET_ROOT / "databases" / "redis.svg",
    "postgres": ASSET_ROOT / "databases" / "postgres.svg",
    "mysql": ASSET_ROOT / "databases" / "mysql.svg",
    "docker": ASSET_ROOT / "infrastructure" / "docker.svg",
    "kubernetes": ASSET_ROOT / "infrastructure" / "kubernetes.svg",
    "generic.user": ASSET_ROOT / "generic" / "user.svg",
    "generic.attacker": ASSET_ROOT / "generic" / "attacker.svg",
    "generic.database": ASSET_ROOT / "generic" / "database.svg",
    "generic.firewall": ASSET_ROOT / "generic" / "firewall.svg",
    "generic.server": ASSET_ROOT / "generic" / "server.svg",
    "generic.service": ASSET_ROOT / "generic" / "service.svg",
}


def resolve_icon(logical_name: str):
    path = ICONS.get(logical_name)
    return path if path and path.exists() else None
