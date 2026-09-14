"""Logical icon names mapped to creator-supplied asset locations."""

from pathlib import Path

from ..asset_resolver import AssetResolver

COMMON_ASSET_ROOT = Path(__file__).resolve().parents[1] / "assets"
ASSET_ROOTS = [COMMON_ASSET_ROOT]

ICONS = {
    "aws.api_gateway": "icons/aws/api_gateway.svg",
    "aws.aurora": "icons/aws/aurora.svg",
    "aws.certificate_manager": "icons/aws/certificate_manager.svg",
    "aws.cloudfront": "icons/aws/cloudfront.svg",
    "aws.cloudtrail": "icons/aws/cloudtrail.svg",
    "aws.cloudwatch": "icons/aws/cloudwatch.svg",
    "aws.cognito": "icons/aws/cognito.svg",
    "aws.dynamodb": "icons/aws/dynamodb.svg",
    "aws.ec2": "icons/aws/ec2.svg",
    "aws.ecs": "icons/aws/ecs.svg",
    "aws.eks": "icons/aws/eks.svg",
    "aws.elastic_load_balancing": "icons/aws/elastic_load_balancing.svg",
    "aws.elasticache": "icons/aws/elasticache.svg",
    "aws.eventbridge": "icons/aws/eventbridge.svg",
    "aws.guardduty": "icons/aws/guardduty.svg",
    "aws.iam": "icons/aws/iam.svg",
    "aws.kms": "icons/aws/kms.svg",
    "aws.lambda": "icons/aws/lambda.svg",
    "aws.network_firewall": "icons/aws/network_firewall.svg",
    "aws.rds": "icons/aws/rds.svg",
    "aws.route53": "icons/aws/route53.svg",
    "aws.s3": "icons/aws/s3.svg",
    "aws.secrets_manager": "icons/aws/secrets_manager.svg",
    "aws.security_hub": "icons/aws/security_hub.svg",
    "aws.shield": "icons/aws/shield.svg",
    "aws.sns": "icons/aws/sns.svg",
    "aws.sqs": "icons/aws/sqs.svg",
    "aws.vpc": "icons/aws/vpc.svg",
    "aws.waf": "icons/aws/waf.svg",
    "networking.internet": "icons/networking/internet.svg",
    "networking.internet_gateway": "icons/networking/internet_gateway.svg",
    "networking.nat_gateway": "icons/networking/nat_gateway.svg",
    "networking.router": "icons/networking/router.svg",
    "networking.vpc_boundary": "icons/networking/vpc_boundary.svg",
    "networking.public_subnet": "icons/networking/public_subnet.svg",
    "networking.private_subnet": "icons/networking/private_subnet.svg",
    "security.credentials": "icons/security/credentials.svg",
    "security.lock": "icons/security/lock.svg",
    "database.generic_database": "icons/database/generic_database.svg",
    "actors.user": "icons/actors/user.svg",
    "actors.client": "icons/actors/client.svg",
    "actors.mobile": "icons/actors/mobile.svg",
    "generic.user": "icons/actors/user.svg",
    "generic.attacker": "icons/actors/user.svg",
    "generic.database": "icons/database/generic_database.svg",
    "generic.firewall": "icons/security/lock.svg",
    "generic.server": "icons/generic/server.svg",
    "generic.service": "icons/generic/service.svg",
}


def configure_asset_roots(*roots: Path) -> None:
    global ASSET_ROOTS
    normalized = []
    for root in roots:
        root = Path(root)
        normalized.append(root.parent if root.name == "icons" else root)
    ASSET_ROOTS = normalized + [COMMON_ASSET_ROOT]


def resolve_icon(logical_name: str):
    relative_path = ICONS.get(logical_name)
    if not relative_path:
        return None
    return AssetResolver(ASSET_ROOTS).resolve(relative_path)
