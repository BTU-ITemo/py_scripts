import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def get_s3_client():
    ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    REGION_NAME = os.getenv('AWS_REGION_NAME')
    SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')
    
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY,
        region_name=REGION_NAME,
        aws_session_token=SESSION_TOKEN
    )
    
    return session.client('s3')
