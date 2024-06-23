import os
from flask import Flask, request, jsonify, send_file
import pandas as pd
import zipfile
# Import your data mapping code
from schema_generator.ai_schema_generator import AiSchemaGenerator
from s3uploader import upload_to_s3
from Kafka_config.kafka_config import publish_sms_to_kafka
import time
from s3downloader import download_files_from_s3
import pymongo
from bson import ObjectId
from io import BytesIO
import pandas as pd
from file_mapping import excute_file_mapping
import json
import csv
from database.mongoconnection2 import Mongoconnection
import time
from logzero import logger

obj_mongo = Mongoconnection()

def approve_file_schema_():
    file_schema_id = request.form['file_schema_id']
    start_time = time.time()
    file_schema_document = obj_mongo.get_file_schema_document(file_schema_id)
    obj_mongo.update_file_schema_document( "APPROVED", file_schema_id)

    obj_mongo.update_benchmark_schema(file_schema_document)
    file_status_document = obj_mongo.get_file_status_by_schema_id(file_schema_id)
    obj_mongo.update_file_status(file_status_document.get('_id'),"UPLOADED")
    end_time = time.time()
    logger.info(f"Time taken for approve_file_schema_: {end_time - start_time} seconds")
    # update_benchmark_data
    return ""


















    # # Check if the POST request has the file part
    # if 'input_file_name' not in request.form:
    #     return jsonify({'error': 'Missing file or filename parameter'}), 400

    # # Get the files from the request
    # filename = request.form['input_file_name']
    # schema_file = request.form['schema_file_name']
    # approval_flag =  request.form['approval_flag']

    # files, source_path = download_files_from_s3([filename])
    # schema,schema_path = download_files_from_s3([schema_file])

    
    # error_log_path = 'error_log.txt'
    # error_record_path = 'error_records.csv'
    # try:
    #     schema_content = pd.read_json(schema_path)
    # except ValueError as e:
    # # Print the error for investigation
    #     print(f"Error: {e}")
    
    # # Attempt to load with json.loads for more details
    # json_data = json.loads(schema_path)
    
    # print("schema_content", schema_content)
    # schema_config_path = "uploads/approved_schema.json"
    # selected_df = schema_content[['output_column', 'input_column']]
    # selected_df = selected_df.fillna('N/A')
    # print("selected_df", selected_df)

    # # Convert the selected DataFrame to a list of records and then to a dictionary
    # name_age_dict_list = selected_df.to_dict(orient='records')
    # name_age_dict = {record['Output Column Name']: record['Input Column Name'] if 'Input Column Name' in record else 'N/A' for record in name_age_dict_list}

    # # Convert the dictionary to JSON
    # schema_content = pd.Series(name_age_dict).to_json()
    # # Convert the JSON-like string to a JSON object
    # schema_content = json.loads(schema_content)

    # # # Print the JSON data
    # # schema_content = json.dumps(schema_content, indent=2)
    # print(type(schema_content))

    # if approval_flag =="True":
    #     output_df= excute_file_mapping(filename,file_type='org3_type3',exclude_id=False)

    #     output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.csv')
       
    #     output_df.to_csv(output_path, index=False)

    #     # Create a ZIP archive containing the processed files
    #     zip_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_files.zip')
    #     timestr = time.strftime("%Y%m%d%H%M%S")
    #     with zipfile.ZipFile(zip_path, 'w') as zip_file:
    #         zip_file.write(output_path, f'output_myorg_v1_{timestr}.csv')
    #         zip_file.write(error_log_path, f'errorlog_myorg_v1_{timestr}.txt')
    #         zip_file.write(error_record_path, f'errorrecords_myorg_v1_{timestr}.csv')
    #     #if zip_path != None:
    #         #publish_sms_to_kafka('success')

    #     # Specify the S3 bucket name, and desired S3 file name
    #     s3_file_name = 'mapping_files/processed_files.zip'

    #     # Upload the file to S3
    #     upload_to_s3(zip_path, s3_file_name)
    #     datainsert(schema_content,filename)


    #     # Return the ZIP file as an attachment in the response
    #     return send_file(zip_path, as_attachment=True, download_name='app_processed_files.zip')
    


    

