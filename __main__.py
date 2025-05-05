"""An AWS Python Pulumi program"""
import pulumi
import pulumi_aws as aws
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.BucketV2('my-bucket')

# Create a DynamoDB table
table = aws.dynamodb.Table("my-table",
    attributes=[
        {
            "name": "id",
            "type": "S",
        }
    ],
    hash_key="id",
    billing_mode="PAY_PER_REQUEST"
)

pulumi.export('bucket_name', bucket.id)
pulumi.export("table_name", table.name)