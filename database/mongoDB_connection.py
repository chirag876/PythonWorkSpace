import json
from pymongo import MongoClient

class MongoDBHandler:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.database = self.client["Test"]
        self.collection = self.database["pdf_records"]

    def document_exists(self, serff_tracking_number):
        # Check if a document with the given SERFF Tracking # exists in the collection
        return self.collection.count_documents({"SERFF Tracking #": serff_tracking_number}) > 0
    
    def insert_json_data(self, json_data):
        
        print("JSON data :",json_data)
        # Extract SERFF Tracking # from the JSON data
        serff_tracking_number = json_data.get("SERFF Tracking #")
        print("SERFF Tracking #:", serff_tracking_number)
        # Check if a document with the same SERFF Tracking # already exists
        if not self.document_exists(serff_tracking_number):
            # Insert JSON data into MongoDB collection
            result = self.collection.insert_one(json_data)
            return (f"Document inserted with SERFF Tracking #: {serff_tracking_number}, ObjectId: {result.inserted_id}")
        else:
            return (f"Document with SERFF Tracking # {serff_tracking_number} already exists. Skipping insertion.")



