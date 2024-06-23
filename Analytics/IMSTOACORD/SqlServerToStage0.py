from decimal import Decimal
import pyodbc
from pymongo import MongoClient
import config
from decimal import Decimal
from logzero import logger
import logging
import time,csv,json
from ManualMapping2 import ManualMapping
import pandas as pd
import numpy as np
import config


class SqlConnect:

    def __init__(self, server, database, username, password, mongo_uri, mongo_db):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.status_collection_name='MigrationStatus'
            

        # Logger setup
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Create a file handler and set the formatter
        log_file_path = 'logger.txt'
        fh = logging.FileHandler(log_file_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(fh)

        # Create the SQL Server connection
        conn_str = (
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            r'SERVER='+self.server+';'
            r'DATABASE='+self.database+';'
            r'UID='+self.username+';'
            r'PWD='+self.password+';'
        )
        self.sql_conn = pyodbc.connect(conn_str)
        logger.info("Connection with sql server successful")
        self.sql_cursor = self.sql_conn.cursor()

        # Create the MongoDB connection
        self.mongo_client = MongoClient(self.mongo_uri)
        logger.info("Connection with mongoDB server successful")
        self.mongo_db_instance = self.mongo_client[self.mongo_db]

    def update_status(self, status):
        progress_collection = self.mongo_db_instance[self.status_collection_name]
        progress_collection.update_one({}, {'$set': {'Status': status}}, upsert=True)

    def run_query(self, table_names=None):
        #to update migration status in mongodb to in progress         
        status="In Progress"
        self.update_status(status)
        logger.info(f"Migration status :{status}")

        start_time = time.time()
        if table_names is None:
            table_names = ['dbo.tblQuotes']  # Default table name if not provided
        #print('table names : ',table_names)
        for table_name in table_names:
            logger.info(f"Runnig  query on {table_name}")
            query = f"SELECT * FROM {table_name}"
            file_name = table_name.split('.')[1]

            # Execute the query
            self.sql_cursor.execute(query)

            # Fetch all rows from the last executed statement
            rows = self.sql_cursor.fetchall()
            logger.info(f"fetched data from {table_name} successfully")
            # Get column names
            column_names = [column[0] for column in self.sql_cursor.description]
            #print('column names : \n',column_names)

            map_csv=ManualMapping(column_names,rows,self.mongo_db_instance)
            map_csv.mapandcreatecsvs()

            #to update migration status in mongodb         
            status="Completed"
            self.update_status(status)
            logger.info(f"Migration status :{status}")
            
            logger.info(f"Inserted data into {file_name} collection successfully!")

        end_time = time.time()  # Record end time
        elapsed_time = end_time - start_time
        logger.info(f"Time taken for the entire flow: {elapsed_time:.2f} seconds")
        self.logger.info(f"Time taken for the entire flow: {elapsed_time:.2f} seconds")

    def close_connections(self):
        self.sql_cursor.close()
        self.sql_conn.close()
        self.mongo_client.close()


# if __name__ == "__main__":
#     obj = SqlConnect(
#        server='10.130.205.31',
#         database='IMS_Base',
#         username='ims_kmg_dev',
#         password='the5.Guide.jested.a.fact.fools.the1.vestibule',
#         mongo_uri=config.mongodb_uri, 
#         mongo_db=config.database_name
#     )

#     obj.run_query(['dbo.tblQuotes'])
#     # obj.run_query()
#     obj.close_connections()