import argparse
import boto3
import auth
from functions import create_bucket, bucket_exists, delete_bucket, check_bucket_policy, create_bucket_policy

parser = argparse.ArgumentParser(description='Command Line TOOL for AWS')
parser.add_argument('-lb', '--list-buckets', action='store_true', help='list all S3 buckets')
parser.add_argument('-cb', '--create-bucket', action='store_true', help='checks and creates bucket if not exist')
parser.add_argument('-pb', '--policy-bucket', action='store_true', help='checks and creates policy for bucket')
parser.add_argument('-db', '--delete-bucket', action='store_true', help='deletes the bucket')
parser.add_argument('-bn', '--bucket-name', type=str, help='name of the bucket')
#parser.add_argument('-lb', '--list-buckets', action='store_true', help='list all S3 buckets')

args = parser.parse_args()
s3_client = auth.get_s3_client()

if not any(vars(args).values()):
    print("No arguments provided. See help for available options: python3 main.py -h")
    exit()

if args.list_buckets:
    response = s3_client.list_buckets()
    print('S3 Buckets on',s3_client.meta.region_name,':')
    for bucket in response['Buckets']:
        print(bucket['Name'])

if args.create_bucket: 
    if args.bucket_name:
        # Create bucket if it does not exist
        if not bucket_exists(s3_client,args.bucket_name):
            if create_bucket(s3_client,args.bucket_name):
                print(f"Bucket '{args.bucket_name}' created successfully!")
            else:
                print(f"Bucket '{args.bucket_name}' was not created successfully!")
        else:
            print(f"Bucket '{args.bucket_name}' already exists.")
    else:
        print("Error: Bucket name not specified.")

if args.policy_bucket:
    if not check_bucket_policy(s3_client, args.bucket_name): create_bucket_policy(s3_client, args.bucket_name)

if args.delete_bucket: 
    if not bucket_exists(s3_client, args.bucket_name): print ("Bucket -",args.bucket_name, "isn't available")
    else:
        if delete_bucket (s3_client, args.bucket_name): print("Bucket -",args.bucket_name, "successfully deleted")