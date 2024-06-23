import boto3
import os
from io import BytesIO
import pandas as pd
import logzero
from logzero import logger
from flask import  jsonify


# Specify your AWS credentials and S3 bucket information
aws_access_key_id = 'ARFB4'
aws_secret_access_key = 'G8LaCzzGat'
bucket_name = 'praai'
# file_names = ['file1.txt', 'file2.txt']  # List of file names you want to download
local_folder_path = 'local_folder/'  # The local folder where you want to save the downloaded files

def download_files_from_s3(file_name):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    file_contents = []

    
    object_key = f'mapping_files/{file_name}'
    # Construct the object key

    try:
    # Download the file from S3 into memory
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        file_content = response['Body'].read()
        logger.info(f"{file_name} file downloaded from {bucket_name} S3 bucket ")

        # Append the file content to the list
        file_contents.append((file_name, file_content))
    except Exception as e:
        logger.error(f"File not present in S3 bucket {str(e)}")
        return jsonify({'error': 'Missing file or filename parameter'}), 400


    return convert_to_dataframe(file_contents)

def convert_to_dataframe(file_contents):
    

    for file_name, file_content in file_contents:
        # Create a BytesIO object from the file content
        file_io = BytesIO(file_content)

        # Use pd.read_csv() or pd.read_excel() based on the file format
        if file_name.lower().endswith('.csv'):
            df = pd.read_csv(file_io)
            
        elif file_name.lower().endswith('.xlsx'):
            df = pd.read_excel(file_io, engine='openpyxl')
        elif file_name.lower().endswith('.json'):
            df = pd.read_json(file_io)
        else:
            logger.error("File no")
            raise ValueError(f"Unsupported file format: {file_name}")

        # Append the DataFrame to the list
        
        download_path = f'uploads/{file_name}'
        logger.info("file download in upload folder")
        df.to_csv(download_path, index=False)
    # dataframes = dataframes.to_csv(orient='records', lines=True)
    

    return df, download_path

