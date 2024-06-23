import os
import logzero
from logzero import logger
from acord125_V2016_03.KEYVALUERESTRUCTURE import acord125_mapper
from acord130_V2013_09.acord_130_schema_mapper import acord130_mapper
from acord140_V2014_12.acord_140_schema_mapper import acord140_mapper
from acord141_V2016_03.acord_141_schema_mapper import acord141_mapper
from acord126_V2014_04.schema_json_mapper import acord126_mapper
from acord127_V2010_05.schema_mapper import acord127_mapper
from service_api.default_json_extractor import default_json
from service_api.textract import TEXTRACT
import time
from database.mongoDB_collection import MongoDBHandler
from aws_s3_bucket.s3downloader import download_from_s3
import traceback


obj_mongo = MongoDBHandler()
def convert_pdf(file_name):
    #create log file for logger
    log_file = "log.txt"
    logzero.logfile(log_file)
    try:        

        # Check if the POST request has the file part       
        file_status_id, file_status,benchmark_schema_id = obj_mongo.get_file_status_by_file_name(file_name)

        # update file status if it is equal to "UPLOADED"
        if file_status.upper() != "UPLOADED":
            return ''

        else:
            # Update file status "IN PROCESS" in database 
            obj_mongo.update_file_status(file_status_id,"IN PROCESS")

        # Get the file and file path from S3 bucket 
        file, file_path = download_from_s3(file_name)

        acord_form_name, stai_json_schema = obj_mongo.do_schema_already_exists(benchmark_schema_id)

        template = acord_form_name.replace(" ", "")
        print ("template: ", template)

        start_time = time.time()

        logger.info("New pdf document detected ...")
        logger.info("PDF to JSON conversion initialized ...")

        all_kvs,page_count,file_name = TEXTRACT.get_mapped_json(file_path,template)

        # print("output before JSON conversion ::::",all_kvs)
        if template == 'ACORD130(2013/09)':

            output_json = acord130_mapper(stai_json_schema,all_kvs,page_count,file_name)

            obj_mongo.update_output_json_in_ds_file_status(template,file,output_json)

            obj_mongo.update_file_status(file_status_id,"APPROVAL PENDING")

            end_time = time.time()

            print(f"time taken : {end_time-start_time}")

            logger.info(f"Time taken for conversion :: {end_time-start_time}")

            return output_json

        elif template == 'ACORD140(2014/12)':

            output_json = acord140_mapper(stai_json_schema,all_kvs,page_count,file_name)

            obj_mongo.update_output_json_in_ds_file_status(template,file,output_json)

            obj_mongo.update_file_status(file_status_id,"APPROVAL PENDING")

            end_time = time.time()

            print(f"time taken : {end_time-start_time}")

            logger.info(f"Time taken for conversion :: {end_time-start_time}")
           
            
            return output_json

        elif template == 'ACORD141(2016/03)':
            try:
                output_json = acord141_mapper(stai_json_schema,all_kvs,page_count,file_name)
                obj_mongo.update_output_json_in_ds_file_status(template,file,output_json)
                obj_mongo.update_file_status(file_status_id,"APPROVAL PENDING")
                print(file_name)
                end_time = time.time()
                logger.info(f"Time taken for conversion :: {end_time-start_time}")
                return output_json
            except Exception as e:
                print("Error occured ::",traceback.print_exc())


        elif template == 'ACORD126(2014/04)':

            output_json = acord126_mapper(stai_json_schema,all_kvs,file_name)

            obj_mongo.update_output_json_in_ds_file_status(template,file,output_json)

            obj_mongo.update_file_status(file_status_id,"APPROVAL PENDING")

            end_time = time.time()

            print(f"time taken : {end_time-start_time}")

            logger.info(f"Time taken for conversion :: {end_time-start_time}")
           
            
            return output_json

        elif template == 'ACORD125(2016/03)':

            output_json = acord125_mapper(stai_json_schema,all_kvs, file_name)
            
            obj_mongo.update_output_json_in_ds_file_status(template,file,output_json)

            obj_mongo.update_file_status(file_status_id,"APPROVAL PENDING")

            print(file_name)
            end_time = time.time()

            print(f"time taken : {end_time-start_time}")

            logger.info(f"Time taken for conversion :: {end_time-start_time}")
           
            
            return output_json
        
        elif template == 'ACORD127(2010/05)':

            output_json = acord127_mapper(stai_json_schema,all_kvs,page_count,file_name)

            obj_mongo.update_output_json_in_ds_file_status(template,file,output_json)

            obj_mongo.update_file_status(file_status_id,"APPROVAL PENDING")

            end_time = time.time()

            print(f"time taken : {end_time-start_time}")

            logger.info(f"Time taken for conversion :: {end_time-start_time}")
           
            
            return output_json

        else:

            output_json = default_json(all_kvs,page_count,file_name)

            obj_mongo.update_output_json_in_ds_file_status(template,file,output_json)

            obj_mongo.update_file_status(file_status_id,"APPROVAL PENDING")


            end_time = time.time()

            print(f"time taken : {end_time-start_time}")
            
            logger.info(f"Time taken for conversion :: {end_time-start_time}")
           

            return output_json

        # shutil.rmtree(upload_folder)

    except Exception as e:
        error_msg = f"An error occurred: {str(e)}"
       
        raise Exception(error_msg)