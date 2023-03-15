#!/usr/bin/env python3
from aws_cdk import App, Environment
from cdk.cdk_stack import {stack-name}

app = App()

# dev
{stack_name}(
    app,
    "dev-{repo-name}",
    environment="dev",
    env=Environment(
        account={aws-account-number},
        region="us-east-1"
    )
)

# stg
{stack_name}(
    app,
    "stg-{repo-name}",
    environment="stg",
    env=Environment(
        account={aws-account-number},
        region="us-east-1"
    )
)

# prod
{stack_name}(
    app,
    "prd-{repo-name}",
    environment="prd",
    env=Environment(
        account={aws-account-number},
        region="us-east-1"
    )
)

app.synth()
