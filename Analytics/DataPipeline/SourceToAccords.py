import pyodbc
from pymongo import MongoClient
from decimal import Decimal
from logzero import logger
import logging
import time,csv,json
from Mapping.ManualMapping2 import ManualMapping
import pandas as pd
import numpy as np
import config
from datetime import datetime
from Utils.Utils import Util
from SourceToMongo import SourceToMongo

class SqlConnect:

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.mongo_uri = config.mongodb_uri
        self.mongo_db = config.db
        self.mongo_db_stage0=config.db_stage0
        self.status_collection_name='MigrationStatus'
        self.status_pipeline='PipelineStatus'
        self.util=Util()
        self.sourcetomongo=SourceToMongo()

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
        logger.info(f"Connection with mongoDB server on {config.mongodb_uri} successful")
        self.mongo_db_instance = self.mongo_client[self.mongo_db]
        self.mongo_db_instance_stage0=self.mongo_client[self.mongo_db_stage0]

    def get_latest_timestamp(self, collection):
        latest_record = collection.find_one(sort=[("CreatedDateTime", -1)])
        if latest_record:
            return latest_record['CreatedDateTime']
        else:
            # If collection is empty, return a default timestamp
            return datetime.min

    def update_migration_status(self, status):
        progress_collection = self.mongo_db_instance[self.status_collection_name]
        progress_collection.update_one({}, {'$set': {'Status': status}}, upsert=True)

    def run_query(self, table_names=None):
        #to update migration status in mongodb to in progress         
        status="In Progress"
        self.update_migration_status(status)
        logger.info(f"Migration status :{status}")

        start_time = time.time()

        self.util.update_pipeline_status('In Process',0,self.status_pipeline,self.mongo_db_instance)
        if table_names is None:
            table_names = ['dbo.tblQuotes']  # Default table name if not provided

        for table_name in table_names:

            logger.info(f"Running  query on {table_name}")

            #stage 0

            query = f"SELECT * FROM {table_name}"
            file_name = table_name.split('.')[1]

            latest_timestamp = self.get_latest_timestamp(self.mongo_db_instance['Quote'])
            latest_timestamp = datetime(2024, 2, 1)
            print(latest_timestamp) 
            # Execute the query
            #self.sql_cursor.execute(query)
            self.sql_cursor.execute(f"SELECT * FROM {table_name} WHERE DateCreated > ?", latest_timestamp)
            #new_records = self.sql_cursor.fetchall()

            # Fetch all rows from the last executed statement
            rows = self.sql_cursor.fetchall()
            logger.info(f"fetched data from {table_name} successfully")
            # Get column names
            column_names = [column[0] for column in self.sql_cursor.description]            
            for i in range(1,7):
                self.util.update_pipeline_status('Queued',f'{i}',self.status_pipeline,self.mongo_db_instance)
            self.util.update_pipeline_status('In Process','0',self.status_pipeline,self.mongo_db_instance)
            time.sleep(15)

            self.sourcetomongo.migrate_data(self.mongo_db_instance_stage0, self.mongo_db_stage0, rows, column_names)
            self.util.update_pipeline_status('Completed','0',self.status_pipeline,self.mongo_db_instance)
            self.util.update_pipeline_status('In Process','1',self.status_pipeline,self.mongo_db_instance)
            self.util.update_pipeline_status('Queued','2',self.status_pipeline,self.mongo_db_instance)
            time.sleep(15)

            #print('column names : \n',column_names)

            map_csv=ManualMapping(column_names,rows,self.mongo_db_instance)
            map_csv.mapandcreatecsvs()
            self.util.update_pipeline_status('Completed','5',self.status_pipeline,self.mongo_db_instance)
            time.sleep(15)
            self.util.update_pipeline_status('Completed','6',self.status_pipeline,self.mongo_db_instance)            
            #to update migration status in mongodb         
            status="Completed"
            self.update_migration_status(status)
            logger.info(f"Migration status :{status}")
            #logger.info(f"Inserted data into {file_name} collection successfully!")

        end_time = time.time()  # Record end time   
        elapsed_time = end_time - start_time
        logger.info(f"Time taken for the entire flow: {elapsed_time:.2f} seconds")
        self.logger.info(f"Time taken for the entire flow: {elapsed_time:.2f} seconds")

    def close_connections(self):
        self.sql_cursor.close()
        self.sql_conn.close()
        self.mongo_client.close()
