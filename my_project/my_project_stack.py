from aws_cdk import core
from aws_cdk import aws_s3 as s3


class MyProjectStack(cdk.Stareck):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        s3.Bucket(self, 'myBucket-juanarmond-cdk', bucket_name='myBucket-juanarmond-cdk')
