import boto3
from botocore.exceptions import NoCredentialsError


def upload_to_s3(local_file_path, s3_folder_name, s3_file_name):
    bucket_name = ''
    # Initialize a session using DigitalOcean Spaces.
    s3 = boto3.client('s3',
                      aws_access_key_id='',
                      aws_secret_access_key='',
                      endpoint_url='')

    try:
        # Uploads the given file using a managed uploader, which will split up the
        # file if it's large and uploads parts in parallel.
        s3.upload_file(local_file_path, bucket_name, f'{s3_folder_name}/{s3_file_name}')

        print(f'File uploaded successfully to {bucket_name}/{s3_folder_name}/{s3_file_name}')
    except FileNotFoundError:
        print(f'The file {local_file_path} was not found.')
    except NoCredentialsError:
        print('Credentials not available.')


def download_from_s3(s3_folder_name, s3_file_name, local_file_path):
    bucket_name = 'staibucket'
    # Initialize a session using DigitalOcean Spaces.
    s3 = boto3.client('s3',
                      aws_access_key_id='',
                      aws_secret_access_key='',
                      endpoint_url='')

    try:
        # Download the file from S3
        s3.download_file(bucket_name, f'{s3_folder_name}/{s3_file_name}', local_file_path)
        print(f'File downloaded successfully to {local_file_path}')
    except NoCredentialsError:
        print('Credentials not available.') 
    except Exception as e:
        print(f'Error occurred: {str(e)}')
