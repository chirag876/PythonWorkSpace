from flask import request, jsonify, send_file
import zipfile
from s3uploader import upload_to_s3
from s3downloader import download_files_from_s3
import pymongo
from file_mapping import excute_file_mapping
from schema_generator.ai_schema_generator import AiSchemaGenerator
import logzero
from logzero import logger,logfile
import app_level as app_level
from database.mongoconnection2 import Mongoconnection
import time
import json

obj_mongo = Mongoconnection()

def read_input_file(app): 
    log_file = "log.txt"
    # error_file = "error.txt"  
    logzero.logfile(log_file)
    try:
        # Check if the POST request has the file part
        if 'source' not in request.form:
            logger.error('error Missing file or filename parameter')
            return jsonify({'error': 'Missing file or filename parameter'}), 400

        # Get the files from the request
        file_name = request.form['source'] 
        logger.info(f'{file_name} received' )
        file_status_id, file_status,benchmark_schema_id = obj_mongo.get_file_status_by_file_name(file_name)

        if benchmark_schema_id is None:
            benchmark_schema_id = "62"
        else:
            obj_mongo.update_file_status(file_status_id,"IN PROCESS") #File status will be IN PROCESS only if benchmark_schema_id is not None

        if file_status.upper() != "UPLOADED":
            return ''

        obj_ai_schema_generator = AiSchemaGenerator()
        file_list = [file_name]
        file, file_path_n_name = download_files_from_s3(file_list[0])
        

        # Extract file_type from input filename
        extract_file_name_static_part = file_name.split("__")
        input_file_timestamp = extract_file_name_static_part[1].split("_")

        # Check weather schema exists or not
        input_headers = file.columns
        input_headers = list(map(str.upper, input_headers))   
        schema_found, file_schema = do_schema_already_exists(input_headers)

        # file_schema = None
        if file_schema is None:
            if benchmark_schema_id is not None:
                # Run your data mapping code with the uploaded files
                schema_df = obj_ai_schema_generator.generate_schema(file_path_n_name, benchmark_schema_id)
                logger.info("Schema file Generated")
                
                # print("schema:", schema_df)
                with open('schema_test.json', 'w') as file:
                    file.write(schema_df)
                # insert file_schema collection in mongo db
                file_schema_id = obj_mongo.insert_file_schema(schema_df)           
                obj_mongo.update_schema_id_in_file_status_collection(file_status_id, file_schema_id)
                obj_mongo.update_outputs_name(file_status_id,extract_file_name_static_part, input_file_timestamp )
                obj_mongo.update_file_status(file_status_id,"APPROVAL PENDING")
                
                return ""
            else:
                return ""
        else:
            start_time =time.time()
            # update_file_status(file_status_id,"IN PROCESS")
            file_schema_id = file_schema['_id']
            obj_mongo.update_schema_id_in_file_status_collection(file_status_id, file_schema_id)
            # create_output_file(app, source_path,file_name,file_type,filetime,error_log_path,error_record_path)  
            schema_file_path, output_file_path  = excute_file_mapping(file_path_n_name, file_schema_id, exclude_id=True)
           
            # file_status_update_file_status()
            # s3_file_name = 'mapping_files/schema.json'
            # schema_path = os.path.join(app.config['UPLOAD_FOLDER'], 'schema.json')
            obj_mongo.update_file_status(file_status_id,"COMPLETED")
            obj_mongo.update_benchmark_data(output_file_path)
            end_time = time.time()
            logger.info(f"output gernaration time {end_time - start_time} senconds")
            return create_output_zip_file(schema_file_path,extract_file_name_static_part[0],output_file_path, input_file_timestamp)

    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        obj_mongo.update_file_status(file_status_id,"COMPLETED")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    


def do_schema_already_exists(input_fields):
    with open("database/mongo_config.json", 'r') as file:
        # Load the JSON data from the file
        config = json.load(file)

    if input_fields is None:
        return

    # input_fields = ["mga","first_name","middle_name","last_name","addressline1","addressline2","city","state","country"]
    input_fields_set = set(input_fields)
   
    # Connect to MongoDB
    client = pymongo.MongoClient(config['mongo_connection_string'])
    db = client[config['database_name']]   
    collection = db[config['file_schema_collection_name']]
    
    # Find a single document in the collection based on the file_id
    # document = collection.find_one({"file_type": file_type})
    # print("document", document)
    #get all fields from db
    documents = collection.find()
    logger.info("matching the input header with exisiting schema")
    
    for document in documents:
        if document.get('mapping_approval_status') == "APPROVED":
            document_fields = document.get('fields')  # Use get() to handle None
            if document_fields is not None:
                existing_fields_set = set(document_fields)
                try:
                    if existing_fields_set == input_fields_set:
                        return True, document
                except Exception as e:
                    logger.error(f'An error occurred: {str(e)}')
                    return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    
    return False, None

        

def create_output_zip_file(schema_file_path,extract_file_name_static_part,output_file_path, input_file_timestamp2):

    input_file_timestamp2 = input_file_timestamp2[1].split('.')[0]

    logger.info("Store Output file and schema file in processed_files")
        # Create a ZIP archive containing the processed files
    output_file_name = f'{extract_file_name_static_part}__output_{input_file_timestamp2}.zip'
    zip_path = 'outputs/'+output_file_name
    log_file_path = "log.txt"
    log_error_file_path = "error.txt" 
    error_record_csv = "error_record_csv.csv"

    with zipfile.ZipFile(zip_path, 'w') as zip_file:        
        zip_file.write(schema_file_path, f'{extract_file_name_static_part}__schema_{input_file_timestamp2}.json')
        zip_file.write(output_file_path, f'{extract_file_name_static_part}__output_{input_file_timestamp2}.csv')
        zip_file.write(log_file_path, f'{extract_file_name_static_part}__log_{input_file_timestamp2}.txt')
        zip_file.write(log_error_file_path, f'{extract_file_name_static_part}__log_error_{input_file_timestamp2}.txt')
        zip_file.write(error_record_csv, f'{extract_file_name_static_part}__error_record_csv_{input_file_timestamp2}.csv')
       
    # if zip_path != None:
    #     publish_sms_to_kafka('exist',filetime)

    # Specify the S3 bucket name, and desired S3 file name
    s3_file_name = "mapping_files/"+output_file_name

    # Upload the file to S3
    upload_to_s3(zip_path, s3_file_name)
    app_level.output_json = None
    logzero.logfile(log_file_path, mode='w')
    return send_file(zip_path, as_attachment=True, download_name=output_file_name)

# def create_output_file(app, source_path,file_name,file_type,filetime,error_log_path,error_record_path):
    
#     schema_df, output_df = excute_file_mapping(source_path, file_type, exclude_id=True)
           
#     # Save the output files to the upload folder
#     output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.csv')
#     schema_path = os.path.join(app.config['UPLOAD_FOLDER'], 'schema.json')

#     output_df.to_csv(output_path, index=False)

#     # Create a ZIP archive containing the processed files
#     zip_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_files.zip')

#     with zipfile.ZipFile(zip_path, 'w') as zip_file:
#         zip_file.write(output_path, f'output_{file_type}_{filetime}.csv')
#         zip_file.write(schema_path, f'schema_{file_type}_{filetime}.json')
#         zip_file.write(error_log_path, f'errorlog_{file_type}_{filetime}.txt')
#         zip_file.write(error_record_path, f'errorrecords_{file_type}_{filetime}.csv')
#     # if zip_path != None:
#     #     publish_sms_to_kafka('exist',filetime)

#     # Specify the S3 bucket name, and desired S3 file name
#     s3_file_name = 'mapping_files/processed_files.zip'   

#     # Upload the file to S3
#     upload_to_s3(zip_path, s3_file_name)

#     # Return the ZIP file as an attachment in the response
#     return send_file(zip_path, as_attachment=True, download_name='processed_files.zip')

# def insert_file_schema(schema):
#     insert_file_schema(schema)




    




