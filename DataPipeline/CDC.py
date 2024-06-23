import pyodbc
from pymongo import MongoClient
from datetime import datetime
import time

# Function to connect to SQL Server
def connect_to_sql_server(server, database, username=None, password=None):
    conn_str = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};'
    conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', host=server, database=database,
                      trusted_connection='yes', user=username, password=password)
    cursor = conn.cursor()
    return cursor

# Function to connect to MongoDB
def connect_to_mongodb(host='localhost', port=27017, db_name=None, collection_name=None):
    client = MongoClient(host, port)
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Function to get the latest timestamp from MongoDB
def get_latest_timestamp(collection):
    latest_record = collection.find_one(sort=[("CreatedDateTime", -1)])
    if latest_record:
        return latest_record['CreatedDateTime']
    else:
        # If collection is empty, return a default timestamp
        return datetime.min

# Function for CDC (Change Data Capture) operation with batch processing
def cdc(source_cursor, target_collection, tablename, batch_size=1000):
    # Connect to target collection
    target = connect_to_mongodb(collection_name=target_collection)
    
    # Get the latest timestamp from the target collection
    latest_timestamp = get_latest_timestamp(target)

    # Initialize variables for batching
    offset = 0
    fetch_batch = True
    
    while fetch_batch:
        # Execute SQL query to retrieve new records from SQL Server in batches
        source_cursor.execute(f"SELECT * FROM {tablename} WHERE CreatedDateTime > ? ORDER BY CreatedDateTime OFFSET ? ROWS FETCH NEXT ? ROWS ONLY", latest_timestamp, offset, batch_size)
        new_records = source_cursor.fetchall()
        
        # If no new records fetched, stop fetching batches
        if not new_records:
            fetch_batch = False
            break
        
        # Insert new records into the target collection
        for record in new_records:
            # Assuming record is a dictionary with field names as keys
            target.insert_one(record)
        
        # Update offset for the next batch
        offset += batch_size

if __name__ == "__main__":
    # Example usage:
    server = '10.130.205.31'
    database = 'IMS_Base'
    username = 'ims_kmg_dev'
    password = 'the5.Guide.jested.a.fact.fools.the1.vestibule'
    source_cursor = connect_to_sql_server(server, database, username, password)
    
    target_collection_name = "target_collection"
    tablename = "Quotes"  # Name of the table in SQL Server
    delay_seconds = 10  # Adjust the delay as needed
    
    while True:
        cdc(source_cursor, target_collection_name, tablename, batch_size=1000)  # Adjust batch_size as needed
        time.sleep(delay_seconds)
