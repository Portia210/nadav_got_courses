import json
import boto3
import time

s3 = boto3.client("s3")
bucket = "lambda-files-bucket-nadav"

def handleEmptyPath():
    output = {}
    response = s3.list_objects(Bucket=bucket)
    if "Contents" in response:
        for content in response["Contents"]:
            curr_file_name = content["Key"]
            curr_response = s3.get_object(Bucket=bucket, Key=curr_file_name)
            output[curr_file_name] = curr_response['Body'].read().decode("utf-8")
    return {
        'statusCode': 200,
        'body': json.dumps(output)
    }
        
def handleCreate(event):
    data = json.loads(event["body"])
    file_name = data["key"]
    file_body = data["body"]
    s3.put_object(
        Bucket=bucket,
        Key=str(time.time()) + file_name,
        Body=file_body
    )
    return {
            'statusCode': 200,
            'body': json.dumps({"status": "Success"})
    }        

def lambda_handler(event, context):
    path = event["path"]
    http_method = event["httpMethod"]
    if path == "/":
        return handleEmptyPath()
    elif path == "/create":
        if http_method == "POST":
            return handleCreate(event)
    
    return {
        'statusCode': 404,
        'body': json.dumps({"Error": 'Unsupported Operation'})
    }
