import boto3
from datetime import datetime
import os


def upload_to_s3(local_file, bucket_name, s3_key):

    
    s3 = boto3.client('s3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION')   
   )

    s3.upload_file(local_file, bucket_name, s3_key)
    print(f"✅ Uploaded {local_file} to s3://{bucket_name}/{s3_key}")

def upload_to_s3_main():

    local_file = "data/reddit_top_posts.csv"
    bucket_name = "random-files-for-me"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    s3_key = f"reddit/reddit_top_posts_{timestamp}.csv"

    upload_to_s3(local_file, bucket_name, s3_key)