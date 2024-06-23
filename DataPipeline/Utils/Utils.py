import pymongo, pyodbc
import json,decimal
from bson.decimal128 import Decimal128

class Util:
    def __init__(self) -> None:
        pass

    def update_pipeline_status(self, status, stage, collection_name, mongo_db_instance):
        progress_collection = mongo_db_instance[collection_name]
        update = {"$set": {f"Stages.{stage}.Status": status}}
        progress_collection.update_one({}, update, upsert=True)
        if status=='Completed':
            print(f"Status for stage :{stage} is updated!\n")
        
def read_config(filename):
    with open(filename, 'r') as file:
        config_data = json.load(file)
    return config_data

def convert_decimal(value):
    if isinstance(value, decimal.Decimal):
        return Decimal128(str(value))
    return value
