# # Import necessary libraries
# from pymongo import MongoClient  # MongoDB client library
# import csv  # Library for reading and writing CSV files
import json  # Library for working with JSON data
from bson import ObjectId
import app_level as app_level
import copy
import pandas as pd
 
from pymongo import MongoClient 
from logzero import logger
import copy


class Mongoconnection:

    def __init__(self) -> None:
        with open("database/mongo_config.json", 'r') as file:
            # Load the JSON data from the file
            config = json.load(file)
        
        
        self.client =  MongoClient(config['mongo_connection_string'])
        self.db = self.client[config['database_name']]
        self.benchmark_schema_collection = self.db[config['benchmark_schema_collection_name']]
        self.benchmark_data_collection = self.db[config['benchmark_data_collection_name']]
        self.file_status_collection = self.db[config['file_status_collection_name']]
        self.file_schema_collection = self.db[config['file_schema_collection_name']]

            

    def get_file_schema_rules(self, file_id):
        # client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")  # replace with your MongoDB connection string
        
        # # Select the database and collection
        # db = client["datapulse0"]
        # collection = db["file_schema"]

        # Query the collection based on the file name
        # document = collection.find_one({"file_type": file_type})
        document = self.file_schema_collection.find_one({"_id": file_id})

        # Print or use the retrieved document
        if document:
            logger.info("Get schema rules")
            rules = document['rules']
            return rules
        else:
            return None




    def get_file_schema_document(self, file_id):
        # client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")  # replace with your MongoDB connection string

        # # Select the database and collection
        # db = client["datapulse0"]
        # collection = db["file_schema"]
        
        object_id = ObjectId(file_id)

        # Query the collection based on the file name
        document = self.file_schema_collection.find_one({"_id": object_id})
    
        # Print or use the retrieved document
        if document:
            return document
        
        else:
            return None


    def insert_file_schema(self, schema_content):
        

        # Convert the JSON string to a Python dictionary
        schema_dict = json.loads(schema_content)
        
        #filtered_data = [doc for doc in schema_dict['rules'] if doc['input_column'] != "" and doc['output_column'] != ""]


        # Connect to MongoDB
        # client = MongoClient('mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/')

        # # Access the database
        # mydatabase = client["datapulse0"]

        # # Access the collection of the database
        # mycollection = mydatabase['file_schema']


        # Insert the dictionary into the collection
        result = self.file_schema_collection.insert_one(schema_dict)
        logger.info("schema file inserted into MongoDb")    
        return result.inserted_id

        

    def get_benchmark_schema_and_benchmark_data(self,benchmark_schema_id):
        
        if benchmark_schema_id is None:
            return      

        # Connect to MongoDB
        # client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")

        # # Select the database and collection
        # db = client["datapulse0"]
        # benchmark_schema_collection = db["benchmark_schema"]
        # benchmark_data_collection = db['benchmark_data']

        # Query the collections
        # query = {"benchmark_name": "msig_premium_template"}
        query = {"_id": ObjectId(benchmark_schema_id)}
        benchmark_schema_documents = self.benchmark_schema_collection.find_one(query)
        query_for_benchmark_data = {"benchmark_schema_id": benchmark_schema_id}
        benchmark_data_documents = self.benchmark_data_collection.find(query_for_benchmark_data)    
        # Convert MongoDB documents to pandas DataFrames
        benchmark_df = pd.DataFrame(list(benchmark_data_documents))
        
        # Convert list of dictionaries to JSON
        # schema_config_documents = json.dumps(schema_config_documents, default=str, indent=2)
        logger.info("get main schema config and main benchmark")
        return benchmark_df, benchmark_schema_documents


    def get_file_status_by_file_name(self,input_file_name):

        if input_file_name is None:
            return      

        # Connect to MongoDB
        # client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")

        # # Select the database and collection
        # db = client["datapulse0"]
        # file_status_collection = db["file_status"]
        
        # Query the collections
        query = {"input_file_name": input_file_name}
        file_status_document = self.file_status_collection.find_one(query)
        print(file_status_document.get('_id'),file_status_document.get('status'))
        return file_status_document.get('_id'),file_status_document.get('status'),file_status_document.get('benchmark_schema_id')


    def get_file_status_by_schema_id(self, file_schema_id):

        if file_schema_id is None:
            return      

        # Connect to MongoDB
        # client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")

        # # Select the database and collection
        # db = client["datapulse0"]
        # file_status_collection = db["file_status"]
        
        # Query the collections
        query = {"file_schema_id": file_schema_id}
        file_status_document = self.file_status_collection.find_one(query)

        return file_status_document


    def update_schema_id_in_file_status_collection(self,file_id, file_schema_id):
        # client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")
        # # Select the database and collection
        # db = client["datapulse0"]
        # update_file_status_collection = db["file_status"]
        filter_query = {'_id': file_id}
        update_query = {'$set': {'file_schema_id': str(file_schema_id)}}
        logger.info("update schema_id in file_status collection")
        # Update the document
        result = self.file_status_collection.update_one(filter_query, update_query)
    


    def update_file_status(self,file_id, file_status):
        # client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")
        # # Select the database and collection
        # db = client["datapulse0"]
        # update_file_status_collection = db["file_status"]

        filter_query = {'_id': file_id}

        update_query = {'$set': {'status': file_status}}
        logger.info("update file_status in mongo Collection")
        # Update the document
        result = self.file_status_collection.update_one(filter_query, update_query)
    

    def update_outputs_name(self,file_status_id, file_name, input_file_timestamp ):
        
        # client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")
        # # Select the database and collection
        # db = client["datapulse0"]
        # update_file_status_collection = db["file_status"]

        filter_query = {'_id': file_status_id}

        update_input = {'$set': {'input_file_name': file_name[0]+'__input_' + input_file_timestamp[1] } }
        update_schema = {'$set': {'schema_file_name': file_name[0]+'__schema_' + input_file_timestamp[1]} }
        update_outputs = {'$set': {'output_file_name': file_name[0]+'__output_' + input_file_timestamp[1] } }
        update_log_outputs = {'$set': {'log_file_name': file_name[0]+'__log_' + input_file_timestamp[1] } }

        # Update the document
        self.file_status_collection.update_one(filter_query, update_input)
        self.file_status_collection.update_one(filter_query, update_schema)
        self.file_status_collection.update_one(filter_query, update_outputs)
        self.file_status_collection.update_one(filter_query, update_log_outputs)
        logger.info("update outputs name in mongoDb")

    def update_file_schema_document(self,updated_approval_status, file_id):
       
        
        # client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")
        # # Select the database and collection
        # db = client["datapulse0"]
        update_file_status_collection = self.file_schema_collection
        
        
        object_id = ObjectId(file_id)


        filter_query = {'_id': object_id}
        update_query = {'$set': {'mapping_approval_status': updated_approval_status}}

        try:
            # update_file_status_collection = self.file_status_collection
            # Update the document
            result = update_file_status_collection.update_one(filter_query, update_query)
            
        
        except Exception as e:
            print("Update failed:", e)


    def update_benchmark_schema(self, file_schema_document):
        
        file_schema_document_rules = file_schema_document['rules']
        # Fetch the document from the collection
        benchmark_schema_id = file_schema_document.get('benchmark_schema_id')
        benchmark_schema_query = {"_id": ObjectId(benchmark_schema_id)}
        benchmark_schema_document = self.benchmark_schema_collection.find_one(benchmark_schema_query)
        benchmark_schema_document_schema = benchmark_schema_document['schema']

        # Assuming 'update_benchmark_schema' is a dictionary with columns as keys
        columns = [key for key in benchmark_schema_document_schema.keys()]

        new_schema = copy.deepcopy(benchmark_schema_document_schema)
        
        # Iterate over all columns in the document
        for column in columns:
            existing_values_set = set()  # Initialize the set here

            # Check if the column is present in the document
            if column in benchmark_schema_document_schema:
                existing_values = benchmark_schema_document_schema[column]
                if not isinstance(existing_values, list):
                    existing_values = [existing_values]
                

                # Iterate over new rules and append to existing values
                for rule in file_schema_document_rules:
                    # Check if the rule is not already present in existing_values
                    if rule not in existing_values:
                        if column == rule['output_column']:
                            if rule['input_column'] != "":
                                existing_values.append(rule['input_column'].strip())   
                            existing_values = list(map(str.upper, existing_values))                             
                            existing_values_set = set(existing_values)
                            new_schema[column] = list(existing_values_set)


        # Update the document in MongoDB with the modified array for the column        
        self.benchmark_schema_collection.update_one(
            {'_id': benchmark_schema_id},
            {'$set':{"schema": new_schema}}
        )
            # else:
            #     # If the column is not present, add a new array with the rules
            #     # Update the document in MongoDB with a new array for the column
            #     self.benchmark_schema_collection.update_one(
            #         {'_id': benchmark_schema_document_id},
            #         {'$set': {column: file_schema_document_rules}}
            #     )


    def update_benchmark_data(self,output_file_path):

        # Connect to the MongoDB server
        # client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")    
        # # Select the database and collection
        # db = client["datapulse0"]
        # update_benchmark_data_collection = db["benchmark_data"]
        output_file_df = pd.read_csv(output_file_path)
        top_rows = self.get_top_rows_with_max_non_empty_cells(output_file_df)

        # Assuming self.benchmark_data_collection is already initialized and points to your collection
        collection = self.benchmark_data_collection

        for _, top_row in top_rows.iterrows():
            benchmark_schema_query = {"benchmark_schema_id": "656f157517416ff12d4761fb"}
            document = collection.find_one(benchmark_schema_query)  # Assuming you want to find one document per top row
            # print(document.get('benchmark_schema_id'))
            if document:
                for column in top_row.index:
                    if column in document.keys():
                        document[column] = top_row[column]
                    if document['benchmark_schema_id'] ==None:
                        document['benchmark_schema_id']= "656f157517416ff12d4761fb"

             # Remove _id if it's nan
            if document['_id']:
                del document['_id']



            # Update the document in the collection
            result = collection.insert_one(document)

            # else:
            #     # If no existing document found, you might want to insert a new one
                # new_document = top_row.to_dict()
                # result = collection.insert_one(new_document)
            #     print(f"Inserted new document ID: {result.inserted_id}")

        print("Documents updated/inserted successfully.")

    def get_top_rows_with_max_non_empty_cells(self, csv_file, top_n=5):
        df = csv_file.copy()
        df['non_empty_count'] = df.apply(lambda row: row.count(), axis=1)
        df['empty_count'] = df.apply(lambda row: row.isna().sum(), axis=1)
        top_rows = df.nlargest(top_n, 'non_empty_count')
        columns_to_drop = ['non_empty_count', 'empty_count']
        top_rows = top_rows.drop(columns=columns_to_drop)
        return top_rows

   