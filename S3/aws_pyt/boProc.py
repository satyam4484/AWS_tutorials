import boto3
import json


client = boto3.client('s3')

# bucket_response = client.list_buckets()
# if 'Buckets' in bucket_response:
#     for bucket in bucket_response['Buckets']:
#         print(bucket['Name'])

BUCKET_NAME='s3-tutorial-satyam'
print("uplaoding file to s3")
client.upload_file('/Users/satyamsingh/Desktop/satyam/aws_tutorials/dummy.txt',BUCKET_NAME,'dev/testing/dummy.txt')
print("file uploaded to s3")