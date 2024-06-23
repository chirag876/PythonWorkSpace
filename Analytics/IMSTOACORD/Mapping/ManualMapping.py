# import os, json
# import pandas as pd
# import re,csv
# import numpy as np
# from UploadCsvToBlob import CsvToBlob
# from bson.decimal128 import Decimal128
# import decimal

# class ManualMapping:
#     def __init__(self,column_names, rows, mongo_instance) -> None:
#         self.column_names = column_names
#         self.mongo_instance=mongo_instancev
#         self.rows=rows

#     def read_config(self,filename):
#         with open(filename, 'r') as file:
#             config_data = json.load(file)
#         return config_data

#     def mapandcreatecsvs(self):
#         #mongo_data = data
#         config_folder='./Configs'
#         print(config_folder)
#         config_labels=[i.split('.')[0] for i in os.listdir(config_folder)]
#         print(self.column_names)
#         rows=np.array(self.rows)
#         #print(self.rows[0],self.column_names[1])
#         df=pd.DataFrame(rows,columns=self.column_names)
#         #print("input df:",df['InsuredCity'])
#         for config_label in config_labels:   
        
#             matching_count=0
#             updated_columns = pd.DataFrame()
#             config_data=os.path.join(config_folder,f"{config_label}.json")
#             with open(config_data, 'r') as f:
#                 config_data = json.load(f)
#                 for key, aliases in config_data.items():
#                     if not aliases:  # If aliases list is empty, add an empty column
#                         updated_columns[key] = pd.Series(dtype=df.dtypes.get(key, 'object'))
#                     else:
#                         for alias in aliases:
#                             if alias in df.columns:
#                                 matching_count+=1
#                                 print(f"Mathcing alias name:{alias}.. Total count : {matching_count}")
#                                 updated_columns[key]=df[alias]
#                     if key not in updated_columns.columns:  # If key not added, add empty column
#                         updated_columns[key] = pd.Series(dtype=df.dtypes.get(key, 'object'))
#             #print('updated df:\n',updated_columns.head())
#             json_data = updated_columns.to_json(orient='records')
#             data = json.loads(json_data)
#             csv_file_path=f'./tables/{config_label}.csv'
#             updated_columns.to_csv(csv_file_path, index=False)

#             mongo_collection = self.mongo_instance[config_label]

#             # Convert Decimal objects to Decimal128
#             def convert_decimal(value):
#                 if isinstance(value, decimal.Decimal):
#                     return Decimal128(str(value))
#                 return value

#             df = updated_columns.map(convert_decimal)

#             for index, row in df.iterrows():
#                 # Convert each row to a dictionary with the specified orientation ('list')
#                 row_dict = row.to_dict()

#                 # Create a new dictionary for each record
#                 expected_output = {}

#                 for key, value in row_dict.items():
#                     keys = key.split('.')
#                     current_dict = expected_output

#                     for k in keys[:-1]:
#                         current_dict = current_dict.setdefault(k, {})

#                     current_dict[keys[-1]] = value

#                 # Insert the current record into the MongoDB collection
#                 mongo_collection.insert_one(expected_output)
#             #to determine the column with unique values
#             # for column in updated_columns.columns:
#             #     if updated_columns[column].is_unique:
#             #         unique_id_column = column
#             #         break  
#             # else:
#             #     unique_id_column=None
            
#             # for record in data:
#             #     if unique_id_column:
#             #         id = record.get(unique_id_column)
#             #         existing_record = mongo_collection.find_one({unique_id_column: id})
#             #         if existing_record:
#             #             mongo_collection.update_one({unique_id_column: id}, {'$set': record})
#             #         else:
#             #             mongo_collection.insert_one(record)
#             #     else:
#             #         # If no unique identifier exists, add all the data
#             #         mongo_collection.insert_one(record)
#             # uploadtoblob=CsvToBlob()
#             # uploadtoblob.upload_file_chunks(f'./tables/{config_label}.csv',f'datapulse/{config_label}.csv')
#             print("File Updated Successfully!")
#         return 'done'
            
#     # for config_label in config_labels:#config_file_path in config_files:
#         #     # Extract config name from the file path
#         #     config_name = config_label#os.path.splitext(os.path.basename(config_file_path))[0]

#         #     # Check if config name is in the DataFrame columns
#         #     if config_name in df.columns:
#         #         config_file_path=os.path.join(config_folder,f"{config_name}.json")
#         #         # Load config.json file
#         #         with open(config_file_path, 'r') as config_file:
#         #             config_data = json.load(config_file)

#         #         # Update the DataFrame based on the keys in config.json
#         #         # Only update columns that exist in both DataFrame and config.json
#         #         valid_columns = set(df.columns) & set(config_data.keys())
#         #         df_update = df[valid_columns]

#         #         # Rename the DataFrame columns to match the keys in config.json
#         #         df_update = df_update.rename(columns=config_data)

#         #         # Save the updated DataFrame to a CSV file
#         #         # The output file will have the same name as the config.json file with '.csv' extension
#         #         output_csv_path = config_file_path.replace('.json', '.csv')
#         #         df_update.to_csv(output_csv_path, index=False)

#         #         print(f"CSV file created for config: {config_name}")
#         #     else:
#         #         print(f"Config name '{config_name}' not found in DataFrame columns. Skipping CSV creation.")

#         # print("CSV files created successfully.")        

#     # def flatten_dict(self, d, parent_key='', sep='.'):
#     #     items = []
#     #     for k, v in d.items():
#     #         new_key = f"{parent_key}{sep}{k}" if parent_key else k
#     #         if isinstance(v, dict):
#     #             items.extend(flatten_dict(v, new_key, sep=sep).items())
#     #         else:
#     #             items.append((new_key, v))
#     #     print(dict(items))
#     #     return dict(items)

#     # def map_fields(self,data_col, config_col):
#     #     mapped_data = {}
#     #     for key, value in config_col.items():
#     #         if isinstance(value, list) and value:
#     #             #print(value)
#     #             if isinstance(value[0], str):  # Check if value is a string
#     #                 print(value[0])
#     #                 if value[0] in data:
#     #                     mapped_data[key] = data[value[0]]
#     #             elif isinstance(value[0], dict):  # Check if value is a dictionary
#     #                 nested_key = list(value[0].keys())[0]
#     #                 if nested_key in data:
#     #                     if isinstance(data[nested_key], list):
#     #                         mapped_data[key] = [map_fields(item, value[0][nested_key]) for item in data[nested_key]]
#     #                     else:
#     #                         mapped_data[key] = map_fields(data[nested_key], value[0][nested_key])
#     #     return mapped_data
