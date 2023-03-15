from aws_cdk import (
    Stack
)
from constructs import Construct

class {stack-name}(Stack):
    def __init__(self, scope: Construct, id: str, environment=None, **kwargs)  -> None:
        super().__init__(scope, id, **kwargs)