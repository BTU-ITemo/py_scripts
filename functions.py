import json

def bucket_exists(s3_client, bucket_name):

    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except:
        return False

def create_bucket(s3_client, bucket_name):
    location = {'LocationConstraint': s3_client.meta.region_name}
    response = s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration=location)
    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code == 200:
        return True
    return False

def delete_bucket(s3_client, bucket_name):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket.html
    response = s3_client.delete_bucket(Bucket=bucket_name)
    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code == 204:
        return True
    return False

def check_bucket_policy(s3_client, bucket_name):
    """
    Checks if a bucket has a policy attached to it.

    Args:
    bucket_name (str): The name of the S3 bucket to check.

    Returns:
    bool: True if the bucket has a policy, False otherwise.
    """
    
    try:
        response = s3_client.get_bucket_policy(Bucket=bucket_name)
        print(f"The bucket '{bucket_name}' already has a policy attached to it.")
        print(f"The policy content is: {response['Policy']}")
        return True
    except:
        return False

def create_bucket_policy(s3_client, bucket_name):
    """
    Creates a bucket policy that makes all files under the /dev and /test prefixes/folders publicly accessible.

    Args:
    bucket_name (str): The name of the S3 bucket to create the policy for.
    """
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:GetObject"
                ],
                "Resource": [
                    f"arn:aws:s3:::{bucket_name}/dev/*",
                    f"arn:aws:s3:::{bucket_name}/test/*"
                ]
            }
        ]
    }
    s3_client.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))
    print(f"Policy created for the bucket '{bucket_name}'.")

