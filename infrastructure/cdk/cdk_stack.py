from aws_cdk import (
    Stack,
    aws_s3,
    Duration,
    aws_iam,
    aws_lambda
)
from constructs import Construct

from os import path

class AwsCdkStack(Stack):
    def __init__(self, scope: Construct, id: str, environment=None, **kwargs)  -> None:
        super().__init__(scope, id, **kwargs)

        # create s3 bucket
        bucket = aws_s3.Bucket(
            self,
            f"{id}-bucket",
            bucket_name=f"{id}-bucket",
            public_read_access=False,
            block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
            versioned=True
        )

        # s3 lifecycle rules
        # expire old versions, current file won't be deleted
        bucket.add_lifecycle_rule(
            noncurrent_version_expiration=Duration.days(10),
            enabled=True
        )

        # expire files, current file will be deleted
        bucket.add_lifecycle_rule(
            expiration=Duration.days(30),
            enabled=True
        )

        # create lambda role
        lambda_role = aws_iam.Role(
            self,
            id=f"{id}-lambda-role",
            role_name=f"{id}-lambda-role",
            assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaRole"),
                aws_iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchLogsFullAccess")
            ]
        )

        # create lambda
        lambda = aws_lambda.Function(
            self,
            f"{id}-lambda",
            function_name=f"{id}-lambda",
            handler=app.handler,
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.from_asset(path.join(
                path.dirname(__file__), '..', 'application'
            )),
            memory_size=512,
            role=lambda_role,
            timeout=Duration.minutes(15),
            retry_attempts=0,
            environment={
                "DEPLOYMENT_ENV": environment
            }
        )

        # give lambda access to s3 bucket
        bucket.grant_read_write(lambda)