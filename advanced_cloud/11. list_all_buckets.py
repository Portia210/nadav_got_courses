import json
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def list_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    logger.info(f"Bucket list: {buckets}")
    return {
        'statusCode': 200,
        'body': json.dumps(buckets)
    }

def lambda_handler(event, context):
    logger.info("--------------------------------")
    logger.info(f"Received event: {event}")
    logger.info("--------------------------------")
    return list_buckets()
