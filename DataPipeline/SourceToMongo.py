import pyodbc, time
from pymongo import MongoClient
from datetime import datetime
from decimal import Decimal
from Utils.Utils import convert_decimal

class SourceToMongo:
    def __init__(self):
        pass

    # def migrate_data(self, mongo_db, collection_name, rows, columns):
    #     t1=time.time()
    #     mongo_collection = mongo_db[collection_name]
    #     for row in rows:
    #         data_to_insert = {}
    #         for column, value in zip(columns, row):
    #             data_to_insert[column] = convert_decimal(value)
    #         #print('rows',row)
    #         mongo_collection.insert_one(data_to_insert)
    #     t2=time.time()
    #     print(f"Data from Source dumped inside collection database! Time taken for the process : {t2-t1}")

    def migrate_data(self, mongo_db, collection_name, rows, columns):
        t1 = time.time()
        mongo_collection = mongo_db[collection_name]
        bulk_data = []
        
        existing_ids = set(mongo_collection.distinct("QuoteID"))  # Fetch existing QuoteIds
        
        for row in rows:
            data_to_insert = {}
            quote_id = row[columns.index("QuoteID")]
            
            # Check if QuoteId already exists, if so, skip insertion
            if quote_id in existing_ids:
                continue
            
            for column, value in zip(columns, row):
                data_to_insert[column] = convert_decimal(value)
            bulk_data.append(data_to_insert)
            
            # Insert in batches of 1000 documents
            if len(bulk_data) == 1000:
                mongo_collection.insert_many(bulk_data)
                bulk_data = []
        
        # Insert remaining documents
        if bulk_data:
            mongo_collection.insert_many(bulk_data)
        
        t2 = time.time()
        print(f"Data from Source dumped inside collection database! Time taken for the process : {t2-t1}")

        
# class DataMigrator:
#     def __init__(self, sql_server_connection_string, mongo_connection_string):
#         self.sql_server_connection_string = sql_server_connection_string
#         self.mongo_connection_string = mongo_connection_string

#     def migrate_data(self, claim_sql_query, claim_id_column, related_tables, start_date, database_name, collection_name):
#         # Connect to SQL Server
#         sql_connection = pyodbc.connect(self.sql_server_connection_string)
#         sql_cursor = sql_connection.cursor()

#         # Connect to MongoDB
#         mongo_client = MongoClient(self.mongo_connection_string)
#         mongo_db = mongo_client[database_name]
#         mongo_collection = mongo_db[collection_name]

#         # Dictionary to hold data for each claim
#         data_dict = {}

#         # Retrieve data for each claim and related tables
#         sql_cursor.execute(claim_sql_query, start_date)
#         for row in sql_cursor.fetchall():
#             claim_id = row[claim_id_column]
#             claim_data = {}
#             for table_name, related_columns in related_tables.items():
#                 sql_query = f"SELECT {', '.join(related_columns)} FROM {table_name} WHERE {claim_id_column} = ?"
#                 sql_cursor.execute(sql_query, claim_id)
#                 columns = [column[0] for column in sql_cursor.description]
#                 table_data = []
#                 for row in sql_cursor.fetchall():
#                     row_dict = {}
#                     for column, value in zip(columns, row):
#                         if isinstance(value, Decimal):
#                             value = float(value)
#                         row_dict[column] = value
#                     table_data.append(row_dict)
#                 claim_data[table_name] = table_data
#             data_dict[claim_id] = claim_data

#         # Convert data_dict to JSON and insert into MongoDB
#         json_data = json.dumps(data_dict)
#         mongo_collection.insert_one({'claims_data': json_data})

#         # Close connections
#         sql_cursor.close()
#         sql_connection.close()
#         mongo_client.close()

# # Example usage:
# claim_sql_query = "SELECT DISTINCT ClaimID FROM ClaimTable WHERE DateCreatedOn >= ?"
# claim_id_column = 'ClaimID'
# related_tables = {
#     'ClaimTable': ['ClaimID', 'ClaimantName', 'ClaimAmount'],
#     'OtherTable': ['SomeColumn1', 'SomeColumn2']  # Add more related tables as needed
# }
# start_date = datetime(2024, 1, 1)
# database_name = 'your_mongodb_database'
# collection_name = 'your_mongodb_collection'

# data_migrator = DataMigrator(sql_connection_string, mongo_connection_string)
# data_migrator.migrate_data(claim_sql_query, claim_id_column, related_tables, start_date, database_name, collection_name)