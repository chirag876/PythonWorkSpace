import os, json
import pandas as pd
import re,csv,config,time
import numpy as np
from UploadCsvToBlob import CsvToBlob
from bson.decimal128 import Decimal128
import decimal
from UploadCsvToBlob import CsvToBlob
from Utils.Utils import Util, convert_decimal
from AccordsToCsv import AccordsToCSV

class ManualMapping:
    def __init__(self,column_names, rows, mongo_instance) -> None:
        self.column_names = column_names
        self.mongo_instance=mongo_instance
        self.rows=rows
        self.util=Util()
        self.status_pipeline='PipelineStatus'
        self.get_csv=AccordsToCSV(self.mongo_instance)

    def read_config(self,filename):
        with open(filename, 'r') as file:
            config_data = json.load(file)
        return config_data

    def mapandcreatecsvs(self):
        
        config_folder=config.sourcetostage0configs
       
        config_labels=[i.split('.')[0] for i in os.listdir(config_folder)]
        
        rows=np.array(self.rows)
        
        df=pd.DataFrame(rows,columns=self.column_names)
        
        for config_label in config_labels:   
            
            t1=time.time()         
            matching_count=0
            updated_columns = pd.DataFrame()
            config_data=os.path.join(config_folder,f"{config_label}.json")
            with open(config_data, 'r') as f:
                config_data = json.load(f)
                for key, aliases in config_data.items():
                    if not aliases:  # If aliases list is empty, add an empty column
                        updated_columns[key] = pd.Series(dtype=df.dtypes.get(key, 'object'))
                    else:
                        for alias in aliases:
                            if alias in df.columns:
                                matching_count+=1

                                updated_columns[key]=df[alias]
                                break  # Break the loop after finding the first match
                    if key not in updated_columns.columns:  # If key not added, add empty column
                        updated_columns[key] = pd.Series(dtype=df.dtypes.get(key, 'object'))
            print(f"Matching alias count :{matching_count}")

            df = updated_columns.map(convert_decimal)
            t2=time.time()
            print(f'time taken to complete stage 1 : {t2-t1}\n')
            self.util.update_pipeline_status('Completed','1',self.status_pipeline,self.mongo_instance)
            self.util.update_pipeline_status('In Process','2',self.status_pipeline,self.mongo_instance)
            self.util.update_pipeline_status('Queued','3',self.status_pipeline,self.mongo_instance)
            time.sleep(15)
            self.InsertDataIntoCollection(df,config_label)

            self.util.update_pipeline_status('Completed','2',self.status_pipeline,self.mongo_instance)
            self.util.update_pipeline_status('In Process','3',self.status_pipeline,self.mongo_instance)
            self.util.update_pipeline_status('Queued','4',self.status_pipeline,self.mongo_instance)
            #self.BlobCSV(df)
            time.sleep(15)            
            self.util.update_pipeline_status('Completed','3',self.status_pipeline,self.mongo_instance)
            self.util.update_pipeline_status('In Process','4',self.status_pipeline,self.mongo_instance)
            self.util.update_pipeline_status('Queued','5',self.status_pipeline,self.mongo_instance)

            csv_file_path=f'{config.csvfilepath}/{config_label}.csv'
            updated_columns.to_csv(csv_file_path, index=False)
            time.sleep(15)

            self.get_csv.BlobCSV()
            time.sleep(15)
            self.util.update_pipeline_status('Completed','4',self.status_pipeline,self.mongo_instance)
            self.util.update_pipeline_status('In Process','5',self.status_pipeline,self.mongo_instance)
            self.util.update_pipeline_status('Queued','6',self.status_pipeline,self.mongo_instance)

            blob = CsvToBlob()
            blob.upload_file_chunks(f'{config.blobcsvpath}/{config_label}.csv',f'datapulse/{config_label}.csv')#datapulse/config_label.csv


        # print(f"df details :{df.shape}")
        return df

    # def InsertDataIntoCollection(self,df,config_label):
    #     mongo_collection = self.mongo_instance[config_label]
    #     t1=time.time()
    #             # Step 1: Identify unique columns
    #     for column in df.columns:
    #         if (df[column].nunique() == len(df)) and ('id' in column.lower()) :
    #             unique_column= column
    #             break
    #         else:
    #             unique_column=None

    #     # Step 2: Iterate over each row, convert to dictionary, and insert into MongoDB with duplicate check
    #     for index, row in df.iterrows():
    #         # Convert each row (Series) to a dictionary
    #         row_dict = row.to_dict()

    #         #Replace NaT values with None
    #         row_dict = {k: None if pd.isna(v) else v for k, v in row_dict.items()}
    #         # Create a query based on unique columns to check if the document already exists
    #         #query = {column: row_dict[column] for column in unique_columns}
    #         query={unique_column:row_dict[unique_column]}

    #         # Check if the document already exists in the collection
    #         existing_document = mongo_collection.find_one(query)

    #         # If the document doesn't exist, insert it into the MongoDB collection
    #         if not existing_document and unique_column:
    #             # Create a new dictionary for each record
    #             expected_output = {}

    #             for key, value in row_dict.items():
    #                 keys = key.split('.')
    #                 current_dict = expected_output
    #                 #print('keys:',keys)
    #                 for k in keys[:-1]:
    #                     if '[' in k:
    #                         k, index = k.split('[')
    #                         index = int(index.strip(']'))
    #                         current_dict = current_dict.setdefault(k, {})
    #                         current_dict = current_dict.setdefault(str(index), {})
    #                     else:
    #                         current_dict = current_dict.setdefault(k, {})

    #                 current_dict[keys[-1]] = value

    #             # Insert the current record into the MongoDB collection
    #             mongo_collection.insert_one(expected_output)
    #         else:
    #             print(f"Document already exists: {query}")
    #     t2=time.time()
    #     print(f"Data mapped and inserted Successfully! Time taken : {t2-t1}\n")

    def InsertDataIntoCollection(self, df, config_label):
        mongo_collection = self.mongo_instance[config_label]
        t1 = time.time()

        # Step 1: Identify unique column
        unique_column = None
        for column in df.columns:
            if (df[column].nunique() == len(df)) and ('id' in column.lower()):
                unique_column = column
                break

        # Step 2: Preprocess DataFrame to eliminate rows that already exist in MongoDB
        if unique_column:
            existing_ids = set(mongo_collection.distinct(unique_column))
            df = df[~df[unique_column].isin(existing_ids)]

        # Step 3: Convert DataFrame to list of dictionaries for bulk insertion
        bulk_operations = []
        for _, row in df.iterrows():
            row_dict = row.to_dict()
            row_dict = {k: None if pd.isna(v) else v for k, v in row_dict.items()}
            expected_output = self._prepare_document(row_dict)
            bulk_operations.append(expected_output)

        # Step 4: Bulk insert data into MongoDB
        if bulk_operations:
            mongo_collection.insert_many(bulk_operations)

        t2 = time.time()
        print(f"Data mapped and inserted Successfully! Time taken: {t2 - t1}\n")

    def _prepare_document(self, row_dict):
        expected_output = {}
        for key, value in row_dict.items():
            keys = key.split('.')
            current_dict = expected_output
            for k in keys[:-1]:
                if '[' in k:
                    k, index = k.split('[')
                    index = int(index.strip(']'))
                    current_dict = current_dict.setdefault(k, {}).setdefault(str(index), {})
                else:
                    current_dict = current_dict.setdefault(k, {})
            current_dict[keys[-1]] = value
        return expected_output


    def BlobCSV(self,df):
        """This function  is used to create CSV file by mapping the columns with blob config and then we can upload that data into Azure Blob Storage"""

        print("We are in BlobCSV function")

        config_folder='./Configs/Blob_Configs'

        config_labels=[i.split('.')[0] for i in os.listdir(config_folder)]

        for config_label in config_labels:   
                
            matching_count=0
            updated_columns = pd.DataFrame()
            config_data=os.path.join(config_folder,f"{config_label}.json")
            with open(config_data, 'r') as f:
                config_data = json.load(f)
                for key, aliases in config_data.items():
                    if not aliases:  # If aliases list is empty, add an empty column
                        updated_columns[key] = pd.Series(dtype=df.dtypes.get(key, 'object'))
                    else:
                        for alias in aliases:
                            if alias in df.columns:
                                matching_count+=1
                                print(f"Mathcing alias name:{alias}.. Total count : {matching_count}")
                                updated_columns[key]=df[alias]
                    if key not in updated_columns.columns:  # If key not added, add empty column
                        updated_columns[key] = pd.Series(dtype=df.dtypes.get(key, 'object'))
            print(f"Matching alias count :{matching_count}")

            df = updated_columns.map(convert_decimal)

            csv_file_path=f'./Configs/Blob_CSV/{config_label}.csv'
            updated_columns.to_csv(csv_file_path, index=False)

            #to determine the column with unique values
            # for column in updated_columns.columns:
            #     if updated_columns[column].is_unique:
            #         unique_id_column = column
            #         break  
            # else:
            #     unique_id_column=None
            
            # for record in data:
            #     if unique_id_column:
            #         id = record.get(unique_id_column)
            #         existing_record = mongo_collection.find_one({unique_id_column: id})
            #         if existing_record:
            #             mongo_collection.update_one({unique_id_column: id}, {'$set': record})
            #         else:
            #             mongo_collection.insert_one(record)
            #     else:
            #         # If no unique identifier exists, add all the data
            #         mongo_collection.insert_one(record)
            # uploadtoblob=CsvToBlob()
            # uploadtoblob.upload_file_chunks(f'./tables/{config_label}.csv',f'datapulse/{config_label}.csv')
        # print("File Updated Successfully!")
        # return 'done'
            
    # for config_label in config_labels:#config_file_path in config_files:
        #     # Extract config name from the file path
        #     config_name = config_label#os.path.splitext(os.path.basename(config_file_path))[0]

        #     # Check if config name is in the DataFrame columns
        #     if config_name in df.columns:
        #         config_file_path=os.path.join(config_folder,f"{config_name}.json")
        #         # Load config.json file
        #         with open(config_file_path, 'r') as config_file:
        #             config_data = json.load(config_file)

        #         # Update the DataFrame based on the keys in config.json
        #         # Only update columns that exist in both DataFrame and config.json
        #         valid_columns = set(df.columns) & set(config_data.keys())
        #         df_update = df[valid_columns]

        #         # Rename the DataFrame columns to match the keys in config.json
        #         df_update = df_update.rename(columns=config_data)

        #         # Save the updated DataFrame to a CSV file
        #         # The output file will have the same name as the config.json file with '.csv' extension
        #         output_csv_path = config_file_path.replace('.json', '.csv')
        #         df_update.to_csv(output_csv_path, index=False)

        #         print(f"CSV file created for config: {config_name}")
        #     else:
        #         print(f"Config name '{config_name}' not found in DataFrame columns. Skipping CSV creation.")

        # print("CSV files created successfully.")        

    # def flatten_dict(self, d, parent_key='', sep='.'):
    #     items = []
    #     for k, v in d.items():
    #         new_key = f"{parent_key}{sep}{k}" if parent_key else k
    #         if isinstance(v, dict):
    #             items.extend(flatten_dict(v, new_key, sep=sep).items())
    #         else:
    #             items.append((new_key, v))
    #     print(dict(items))
    #     return dict(items)

    # def map_fields(self,data_col, config_col):
    #     mapped_data = {}
    #     for key, value in config_col.items():
    #         if isinstance(value, list) and value:
    #             #print(value)
    #             if isinstance(value[0], str):  # Check if value is a string
    #                 print(value[0])
    #                 if value[0] in data:
    #                     mapped_data[key] = data[value[0]]
    #             elif isinstance(value[0], dict):  # Check if value is a dictionary
    #                 nested_key = list(value[0].keys())[0]
    #                 if nested_key in data:
    #                     if isinstance(data[nested_key], list):
    #                         mapped_data[key] = [map_fields(item, value[0][nested_key]) for item in data[nested_key]]
    #                     else:
    #                         mapped_data[key] = map_fields(data[nested_key], value[0][nested_key])
    #     return mapped_data
 