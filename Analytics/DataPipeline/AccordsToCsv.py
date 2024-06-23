import os ,json, pymongo
import pandas as pd
import config
from Utils.Utils import read_config, convert_decimal

class AccordsToCSV:
    def __init__(self,mongo_instance) -> None:
        self.mongo_instance=mongo_instance

    def get_df(self,table):
        collection = self.mongo_instance[table]
        cursor = list(collection.find())
        # Create DataFrame
        df = pd.DataFrame(cursor)
        nested_columns = ['insured','address','location','producer']
        #df = pd.concat([df.drop(nested_columns, axis=1), df[nested_columns].apply(pd.Series)], axis=1)

        for column in nested_columns:
            #df = pd.concat([df.drop(column, axis=1), json_normalize(df[column], max_level=1, record_prefix=f'{column}.')], axis=1)
            df = pd.concat([df.drop(column, axis=1), 
                    pd.json_normalize(df[column], max_level=1).add_prefix(f'{column}.')], axis=1)
        print(df.columns)
        return df

    def BlobCSV(self):
        """This function  is used to create CSV file by mapping the columns with blob config and then we can upload that data into Azure Blob Storage"""

        print("We are in BlobCSV function")


        config_folder=config.stage0toazureconfigs#'./Blob_Configs'

        config_labels=[i.split('.')[0] for i in os.listdir(config_folder)]

        for config_label in config_labels:   
            df=self.get_df(config_label)        
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

            csv_file_path=f'{config.blobcsvpath}/{config_label}.csv'
            print(csv_file_path)
            updated_columns.to_csv(csv_file_path, index=False)


# mongo_client = pymongo.MongoClient(config.mongodb_uri)
# mongo_db_instance = mongo_client[config.db]

# get_csv=Stage0ToCSV(mongo_instance=mongo_db_instance)
# get_csv.BlobCSV()