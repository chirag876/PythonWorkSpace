import json
from pymongo import MongoClient
from logzero import logger
from bson import ObjectId


class MongoDBHandler:
    def __init__(self):
        with open("database/mongo_config.json", 'r') as file:
            # Load the JSON data from the file
            config = json.load(file)
        
        # Define all mongo configurations
        self.client =  MongoClient(config['mongo_connection_string'])
        self.db = self.client[config['database_name']]
        self.pdf_record_collection = self.db[config['pdf_records_collection_name']]
        self.acord_form_collection = self.db[config['acord_form_collection_name']]
        self.ds_file_status_collection = self.db[config['ds_file_status_collection_name']]


    def check_record_exists(self,text):
        logger.info("Checking if record already exists ....")
        serff_tracking_numbers = self.pdf_record_collection.distinct("SERFF Tracking #")

        # Check if any of the SERFF Tracking # values are present in the string
        for tracking_number in serff_tracking_numbers:
            # print("tracking number :",tracking_number)
            if tracking_number in text:
                # print(f"Document with SERFF Tracking # {tracking_number} already exists.")
                logger.info(f"Document with SERFF Tracking # {tracking_number} already exists.")
                return tracking_number
    
    def insert_json_data(self, json_data):
            logger.info("Inserting data into MongoDB ...")
            try:
                result = self.pdf_record_collection.insert_one(json_data)
                logger.info(f'Data inserted successfully into MongoDB with id {result.inserted_id}')
                return (f"Document inserted with SERFF Tracking #: {json_data.get('SERFF Tracking #')}, ObjectId: {result.inserted_id}")
            except Exception as e:
                logger.error('Failed to insert data into MongoDB', err=e)
    
    def get_stai_json_schema_by_form_name(self,read_acord_form_name):
        
        # Get the file schema doucument using acord_form_name
        document = self.acord_form_collection.find_one({"AcordFormDisplayName": read_acord_form_name})
        stai_json_schema = document.get("StaiJsonSchema")
        return stai_json_schema
    
    def get_file_status_by_file_name(self,input_file_name):

        if input_file_name is None:
            return      

        # Query the collections
        query = {"input_file_name": input_file_name}
        file_status_document = self.ds_file_status_collection.find_one(query)
        print(file_status_document.get('_id'),file_status_document.get('status'))
        return file_status_document.get('_id'),file_status_document.get('status'),file_status_document.get('benchmark_schema_id')
    
    def update_file_status(self,file_id, file_status):
        filter_query = {'_id': file_id}

        update_query = {'$set': {'status': file_status}}
        logger.info("update file_status in mongo Collection")
        # Update the document
        result = self.ds_file_status_collection.update_one(filter_query, update_query)

    def do_schema_already_exists(self, benchmark_schema_id):
        object_id = ObjectId(benchmark_schema_id)
        
        # Get the file schema doucument using id 
        acord_form_schema_document = self.acord_form_collection.find_one({"_id":object_id })

        acord_form_name = acord_form_schema_document.get("AcordFormDisplayName")
        stai_json_schema = acord_form_schema_document.get("StaiJsonSchema")
        stai_json_schema = json.loads(stai_json_schema)
        return acord_form_name, stai_json_schema

    def update_output_json_in_ds_file_status(self,template,file_name,json_data):
        
        print("file_name ::",file_name)
        query = {'input_file_name':file_name}


        # update_query = {"$set":{"output":json_data}}
        update_data = {
                    "$push": {
                        "output": {
                            template: json_data
                        }                        
                    }
                }

        self.ds_file_status_collection.update_one(query,update_data)
        logger.info(f"{file_name}  updated with output JSON.")
        


         
         
                