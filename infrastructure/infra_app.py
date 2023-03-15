#!/usr/bin/env python3
from aws_cdk import App, Environment
from cdk.cdk_stack import AwsCdkStack

app = App()

# dev
AwsCdkStack(
    app,
    "dev-{repo-name}",
    environment="dev",
    env=Environment(
        account={aws-account-number},
        region="us-east-1"
    )
)

# stg
AwsCdkStack(
    app,
    "stg-{repo-name}",
    environment="stg",
    env=Environment(
        account={aws-account-number},
        region="us-east-1"
    )
)

# prod
AwsCdkStack(
    app,
    "prd-{repo-name}",
    environment="prd",
    env=Environment(
        account={aws-account-number},
        region="us-east-1"
    )
)

app.synth()
