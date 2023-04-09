import argparse
import boto3
import auth

parser = argparse.ArgumentParser(description='Command Line TOOL for AWS')
parser.add_argument('-lb', '--list-buckets', action='store_true', help='list all S3 buckets')
parser.add_argument('-cb', '--create-bucket', action='store_true', help='checks and creates bucket if not exist')
parser.add_argument('-bn', '--bucket-name', type=str, help='name of the bucket')
#parser.add_argument('-lb', '--list-buckets', action='store_true', help='list all S3 buckets')

args = parser.parse_args()
s3_client = auth.get_s3_client()

if not any(vars(args).values()):
    print("No arguments provided. See help for available options: python3 main.py -h")
    exit()

if args.list_buckets:
    response = s3_client.list_buckets()
    print('S3 Buckets on {}:') # rogor gamoviyvanot regionis saxeli env-dan??
    for bucket in response['Buckets']:
        print(bucket['Name'])

if args.create_bucket: 
    if args.bucket_name:
        # Check if bucket exists
        bucket_exists = True
        try:
            s3_client.head_bucket(Bucket=args.bucket_name)
        except:
            bucket_exists = False

        # Create bucket if it does not exist
        if not bucket_exists:
            location = {'LocationConstraint': s3_client.meta.region_name}
            response = s3_client.create_bucket(
                Bucket=args.bucket_name,
                CreateBucketConfiguration=location)
            status_code = response["ResponseMetadata"]["HTTPStatusCode"]
            if status_code == 200:
                print(f"Bucket '{args.bucket_name}' created successfully!")
            else:
                print(f"Bucket '{args.bucket_name}' was not created successfully!")
        else:
            print(f"Bucket '{args.bucket_name}' already exists.")
    else:
        print("Error: Bucket name not specified.")
