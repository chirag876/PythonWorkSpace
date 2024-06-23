# # # Import necessary libraries
# # from pymongo import MongoClient  # MongoDB client library
# # import csv  # Library for reading and writing CSV files
# import json
# from pickle import NONE  # Library for working with JSON data
# from bson import ObjectId
# import app_level as app_level
# import copy
# import pandas as pd
 
# from pymongo import MongoClient 
# from logzero import logger
# import uuid 




# def get_file_schema_rules(file_id):
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")  # replace with your MongoDB connection string
    
#     # Select the database and collection
#     db = client["datapulse0"]
#     collection = db["file_schema"]

#     # Query the collection based on the file name
#     # document = collection.find_one({"file_type": file_type})
#     document = collection.find_one({"_id": file_id})

#     # Print or use the retrieved document
#     if document:
#         logger.info("Get schema rules")
#         rules = document['rules']
#         return rules
#     else:
#         return None




# def get_file_schema_document(file_id):
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")  # replace with your MongoDB connection string

#     # Select the database and collection
#     db = client["datapulse0"]
#     collection = db["file_schema"]
    
#     object_id = ObjectId(file_id)

#     # Query the collection based on the file name
#     document = collection.find_one({"_id": object_id})
   
#     # Print or use the retrieved document
#     if document:
#         return document
    
#     else:
#         return None


# def insert_file_schema(schema_content):
    

#     # Convert the JSON string to a Python dictionary
#     schema_dict = json.loads(schema_content)
    
#     #filtered_data = [doc for doc in schema_dict['rules'] if doc['input_column'] != "" and doc['output_column'] != ""]


#     # Connect to MongoDB
#     client = MongoClient('mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/')

#     # Access the database
#     mydatabase = client["datapulse0"]

#     # Access the collection of the database
#     mycollection = mydatabase['file_schema']


#     # Insert the dictionary into the collection
#     result = mycollection.insert_one(schema_dict)
#     logger.info("schema file inserted into MongoDb")    
#     return result.inserted_id

    

# def get_benchmark_schema_and_benchmark_data(benchmark_schema_id = None):

#     if benchmark_schema_id == None:
#         return

#     # Connect to MongoDB
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")

#     # Select the database and collection
#     db = client["datapulse0"]
#     benchmark_schema_collection = db["benchmark_schema"]
#     benchmark_data_collection = db['benchmark_data']

#     # Query the collections
#     benchmark_schema_documents = benchmark_schema_collection.find({}, {'_id': 0})
#     query = {"benchmark_schema_id": benchmark_schema_id}
#     benchmark_data_documents = benchmark_data_collection.find(query)    
#     # Convert MongoDB documents to pandas DataFrames
#     benchmark_df = pd.DataFrame(list(benchmark_data_documents))
#     benchmark_schema_documents = [doc for doc in benchmark_schema_documents]
#     # Convert list of dictionaries to JSON
#     # schema_config_documents = json.dumps(schema_config_documents, default=str, indent=2)
#     # print(type(schema_config_documents), schema_config_documents)
#     logger.info("get main schema config and main benchmark")
#     return benchmark_df, benchmark_schema_documents[0]


# def get_file_status(input_file_name):
#     # Connect to MongoDB
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")

#     # Select the database and collection
#     db = client["datapulse0"]
#     file_status_collection = db["file_status"]
    
#     # Query the collections
#     query = {"input_file_name": input_file_name}
#     file_status_document = file_status_collection.find_one(query)
#     return file_status_document.get('_id'),file_status_document.get('status'),file_status_document.get('benchmark_schema_id')

# def get_file_status_by_schema_id(schema_id):
#     # Connect to MongoDB
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")

#     # Select the database and collection
#     db = client["datapulse0"]
#     file_status_collection = db["file_status"]
    
#     # Query the collections
#     query = {"file_schema_id": schema_id}
#     file_status_document = file_status_collection.find_one(query)

#     return file_status_document


# def update_schema_id_in_file_status_collection(file_id, file_schema_id):
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")
#     # Select the database and collection
#     db = client["datapulse0"]
#     update_file_status_collection = db["file_status"]
#     filter_query = {'_id': file_id}
#     update_query = {'$set': {'file_schema_id': str(file_schema_id)}}
#     logger.info("update schema_id in file_status collection")
#     # Update the document
#     result = update_file_status_collection.update_one(filter_query, update_query)
  


# def update_file_status(file_id, file_status):
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")
#     # Select the database and collection
#     db = client["datapulse0"]
#     update_file_status_collection = db["file_status"]

#     filter_query = {'_id': file_id}

#     update_query = {'$set': {'status': file_status}}
#     logger.info("update file_status in mongo Collection")
#     # Update the document
#     result = update_file_status_collection.update_one(filter_query, update_query)
   

# def update_outputs_name(file_status_id,file_name, input_file_timestamp ):
    
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")
#     # Select the database and collection
#     db = client["datapulse0"]
#     update_file_status_collection = db["file_status"]

#     filter_query = {'_id': file_status_id}

#     update_input = {'$set': {'input_file_name': file_name[0]+'__input_' + input_file_timestamp[1] } }
#     update_schema = {'$set': {'schema_file_name': file_name[0]+'__schema_' + input_file_timestamp[1]} }
#     update_outputs = {'$set': {'output_file_name': file_name[0]+'__output_' + input_file_timestamp[1] } }

#     # Update the document
#     update_file_status_collection.update_one(filter_query, update_input)
#     update_file_status_collection.update_one(filter_query, update_schema)
#     update_file_status_collection.update_one(filter_query, update_outputs)
#     logger.info("update outputs name in mongoDb")

# def update_file_schema_document(updated_approval_status, file_id):
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")
#     # Select the database and collection
#     db = client["datapulse0"]
#     update_file_status_collection = db["file_schema"]
    
#     object_id = ObjectId(file_id)

#     filter_query = {'_id': object_id}
#     update_query = {'$set': {'mapping_approval_status': updated_approval_status}}

#     try:
#         # Update the document
#         result = update_file_status_collection.update_one(filter_query, update_query)
       
#     except Exception as e:
#         print("Update failed:", e)


# def update_benchmark_schema(file_schema_document):

#     # Connect to the MongoDB server
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")    
#     # Select the database and collection
#     db = client["datapulse0"]
#     # Query the collections
#     benchmark_schema_id = file_schema_document.get('benchmark_schema_id')
    
#     benchmark_schema_collection = db["benchmark_schema"]
#     benchmark_schema_query = {"benchmark_schema_id": benchmark_schema_id}
    
#     # Fetch the document from the collection
#     benchmark_schema_document = benchmark_schema_collection.find(benchmark_schema_query)
#     benchmark_schema_document = benchmark_schema_document[0]
#     #Get Rules from file_schema
#     file_schema_document_rules = file_schema_document['rules'] 
    
#     # Assuming 'update_benchmark_schema' is a dictionary with columns as keys
#     columns = [key for key in benchmark_schema_document.keys() if key != '_id']
#     # Iterate over all columns in the document
#     for column in columns:
#         existing_values_set = set()  # Initialize the set here

#         # Check if the column is present in the document
#         if column in benchmark_schema_document:
#             existing_values = benchmark_schema_document[column]
#             if not isinstance(existing_values, list):
#                 existing_values = [existing_values]
               

#             # Iterate over new rules and append to existing values
#             for rule in file_schema_document_rules:
#                 # Check if the rule is not already present in existing_values
#                 if rule not in existing_values:
#                     if column == rule['output_column']:
#                         existing_values.append(rule['input_column'].strip())
                        
#                         existing_values_set = set(existing_values)

#             # Update the document in MongoDB with the modified array for the column
#             benchmark_schema_collection.update_one(
#                 {'_id': benchmark_schema_document['_id']},
#                 {'$set': {column: list(existing_values_set)}}
#             )
#         else:
#             # If the column is not present, add a new array with the rules
#             # Update the document in MongoDB with a new array for the column
#             benchmark_schema_collection.update_one(
#                 {'_id': benchmark_schema_document['_id']},
#                 {'$set': {column: file_schema_document_rules}}
#             )


# def update_benchmark_data(output_file_path):

#     # Connect to the MongoDB server
#     client = MongoClient("mongodb+srv://Project0:Diagnostics11@cluster0.w9m3hlk.mongodb.net/")    
#     # Select the database and collection
#     db = client["datapulse0"]
#     update_benchmark_data_collection = db["benchmark_data"]
#     output_file_df = pd.read_csv(output_file_path)
#     output_columns = output_file_df.columns
#     document = update_benchmark_data_collection.find_one({})
#     if document:
#         keys = document.keys()
#         for k in keys:
#             for column in output_columns:
#                 if k == column:
#                     document[k] = output_file_df[column]

# def get_top_rows_with_max_non_empty_cells(csv_file, top_n=5):
#     # Read the Excel file into a pandas DataFrame
#     df = pd.read_excel(csv_file)

#     # Exclude the header and count the non-empty and empty cells in each row
#     df['non_empty_count'] = df.apply(lambda row: row.count(), axis=1)
#     df['empty_count'] = df.apply(lambda row: row.isna().sum(), axis=1)

#     # Find the top rows with the maximum number of non-empty cells
#     top_rows = df.nlargest(top_n, 'non_empty_count')

#     # Drop additional columns from the result
#     columns_to_drop = ['non_empty_count', 'empty_count']
#     top_rows = top_rows.drop(columns=columns_to_drop)

#     return top_rows
    
    
