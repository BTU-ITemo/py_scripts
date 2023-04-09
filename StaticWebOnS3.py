import argparse
import auth
import json
from dotenv import load_dotenv

load_dotenv()

# parse the command-line arguments
parser = argparse.ArgumentParser(description='Upload and host static website on S3 bucket')
parser.add_argument('-b', '--bucket-name', required=True, help='Name of the S3 bucket')
parser.add_argument('-i', '--index-file', default='index.html', help='Path to index.html file')
parser.add_argument('-e', '--error-file', default='error.html', help='Path to error.html file')
args = parser.parse_args()

# get the bucket name and file paths from the command-line arguments
bucket_name = args.bucket_name
index_file = args.index_file
error_file = args.error_file

# create an S3 client object
s3_client = auth.get_s3_client()

bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
}

bucket_policy = json.dumps(bucket_policy)

s3_client.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)

# upload the index.html file to the bucket
with open(index_file, 'rb') as f:
    s3_client.upload_fileobj(f, bucket_name, 'index.html', ExtraArgs={'ContentType': 'text/html'})

# upload the error.html file to the bucket
with open(error_file, 'rb') as f:
    s3_client.upload_fileobj(f, bucket_name, 'error.html', ExtraArgs={'ContentType': 'text/html'})

# configure the bucket to act as a static website
s3_client.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'}
    }
)

print(f"Static website uploaded and hosted at http://{bucket_name}.s3-website-{s3_client.meta.region_name}.amazonaws.com")
