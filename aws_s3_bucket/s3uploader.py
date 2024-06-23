import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(local_file_path, s3_file_name):
    bucket_name = 'staibucket'
    # Initialize a session using DigitalOcean Spaces.
    s3 = boto3.client('s3',
                      aws_access_key_id='',
                      aws_secret_access_key='',
                      endpoint_url='')

    try:
        # Uploads the given file using a managed uploader, which will split up the
        # file if it's large and uploads parts in parallel.
        s3.upload_file(local_file_path, bucket_name, s3_file_name)

        print(f'File uploaded successfully to {bucket_name}/{s3_file_name}')
    except FileNotFoundError:
        print(f'The file {local_file_path} was not found.')
    except NoCredentialsError:
        print('Credentials not available.')

# # Specify the local CSV file path, S3 bucket name, and desired S3 file name
# local_file_path = 'error_recordstest.csv'
# s3_file_name = 'analytics csv/error_recordstest.csv'

