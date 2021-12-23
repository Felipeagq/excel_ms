import boto3 
from botocore.retries import bucket
from botocore.exceptions import ClientError
from botocore.config import Config
import logging
from dotenv import load_dotenv
import os
import requests


def s3_uploader(response,file):
    with open(file, 'rb') as f:
        print(file)
        files = {'file': (file, f)}
        http_response = requests.post(response['url'], data=response['fields'], files=files)
    # If successful, returns HTTP status code 204
    logging.info(f'File upload HTTP status code: {http_response.status_code}')
    print(http_response.url)
    return http_response.url