import boto3
import os
from io import BytesIO
import pandas as pd
import logzero
from logzero import logger
from flask import  jsonify
from botocore.exceptions import NoCredentialsError

# Specify your AWS credentials and S3 bucket information
aws_access_key_id = ''
aws_secret_access_key = ''
bucket_name = 'staibucket'
# file_names = ['file1.txt', 'file2.txt']  # List of file names you want to download
local_folder_path = 'input'  # The local folder where you want to save the downloaded files

def download_from_s3(s3_file_name):
    s3_folder_name = "pydatascanner"
    local_file_path = 'upload/'

    bucket_name = 'staibucket'
    # Initialize a session using DigitalOcean Spaces.
    s3 = boto3.client('s3',
                      aws_access_key_id='',
                      aws_secret_access_key='',
                      endpoint_url='')
    
    local_file_path = local_file_path +s3_file_name 

    try:
        # Download the file from S3
        s3.download_file(bucket_name, f'{s3_folder_name}/{s3_file_name}', local_file_path)
        print(f'File downloaded successfully to {local_file_path}')
        return s3_file_name, local_file_path
    except NoCredentialsError:
        print('Credentials not available.')
    except Exception as e:
        print(f'Error occurred: {str(e)}')
