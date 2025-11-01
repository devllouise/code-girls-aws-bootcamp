import json
import boto3
import datetime

def lambda_handler(event, context):

    bucket_name = 'maira-lambda-s3-lab'

    s3 = boto3.client('s3')

    now = datetime.datetime.utcnow().isoformat()
    key = f"log-{now}.txt"

    content = "Função Lambda executada com sucesso!"

    s3.put_object(Bucket=bucket_name, Key=key, Body=content)

    return {
        "statusCode": 200,
        "body": json.dumps(f"Arquivo {key} criado no bucket {bucket_name}")
    }
