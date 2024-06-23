# Import necessary libraries
from pymongo import MongoClient  # MongoDB client library
import csv  # Library for reading and writing CSV files
import json  # Library for working with JSON data

# Function to insert data from CSV and JSON files into MongoDB
def datainsert(benchmark_csv, schema_json):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')  # Connect to MongoDB server running on localhost
    mydatabase = client['sample']  # Access or create a database named 'sample'
    benchmark_collection = mydatabase['benchmark2']  # Access or create a collection named 'benchmark2'
    json_collection = mydatabase['main_schema_config']  # Access or create a collection named 'main_schema_config'
    # schema_json_collection = mydatabase['schema_config']
    
    # Read CSV file and insert non-empty rows into MongoDB
    with open(benchmark_csv, 'r') as csv_file:  # Open CSV file for reading
        csv_reader = csv.DictReader(csv_file)  # Create a CSV reader object
        for row in csv_reader:  # Iterate through each row in the CSV file
            # Check if the row is not empty before inserting
            if any(row.values()):  # If any values in the row are present
                benchmark_collection.insert_one(row)  # Insert the row as a document in the 'benchmark2' collection
                
    # Read JSON file and append values to the array in MongoDB
    # Read JSON file and update arrays in MongoDB
    with open(schema_json, 'r') as json_file:  # Open JSON file for reading
        json_data = json.load(json_file)  # Load JSON data from the file
        for document in json_collection.find():  # Iterate through documents in the 'main_schema_config' collection
            for key, values in json_data.items():  # Iterate through keys and values in the JSON data
                # If the key is present in the document, append values to the array
                if key in document:  # If the key is already present in the document
                    existing_values = document[key]  # Get the existing values for the key
                    if not isinstance(existing_values, list):  # If existing values is not a list, convert it to a list
                        existing_values = [existing_values]
                    for value in values:  # Iterate through values in the JSON data
                        if value not in existing_values:  # If the value is not already in the existing values
                            existing_values.append(value)  # Append the value to the existing values
                    # Update the document in MongoDB with the modified array for the key
                    json_collection.update_one(
                        {'_id': document['_id']},
                        {'$set': {key: existing_values}}
                    )
                else:
                    # If the key is not present, add a new array with the values
                    # Update the document in MongoDB with a new array for the key
                    json_collection.update_one(
                        {'_id': document['_id']},
                        {'$set': {key: values}}
                    )
                    
# Example usage
if __name__ == "__main__":
    benchmark_csv = 'benchmark.csv'  # Path to the CSV file
    schema_json = 'config.json'  # Path to the JSON file
    datainsert(benchmark_csv, schema_json)  # Call the datainsert function with the file paths
