import os
import json
from pymongo import MongoClient

def insert_json_files_into_mongo(folder_path, collection):
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as json_file:
                json_data = json.load(json_file)
                collection.insert_one(json_data)
                print(f"Inserted {filename} into MongoDB")

def connect_to_mongo():
    client = MongoClient("mongodb://localhost:27017")
    db = client.Stage0ims
    collection = db.Insurance_Policy_Data
    # collection = db.Insurance_Quote_Data
    return collection

if __name__ == "__main__":
    folder_path = "C:/Workspaces/CodeSpaces/Analytics/EDA_Python/fakedatageneration/generated_policy_json"
    # folder_path = "C:/Workspaces/CodeSpaces/Analytics/EDA_Python/fakedatageneration/generated_quote_json"
    mongo_collection = connect_to_mongo()
    insert_json_files_into_mongo(folder_path, mongo_collection)

