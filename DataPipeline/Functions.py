from pymongo import MongoClient
from Preprocessing.Preprocess import Preprocess
import pandas as pd
from SourceToAccords import SqlConnect
import config
import os,time
import traceback, schedule, logging 

#logging.basicConfig(filename='logger.txt', level=logging.ERROR)


# def connect_to_mongodb(database_name, collection_name,connection_string):
#     client = MongoClient(connection_string) 
#     db = client[database_name]
#     collection = db[collection_name]
#     return collection   

# def fetch_data(collection):
#     cursor = collection.find()
#     data = list(cursor)
#     return data

# def store_preprocessed_data(preprocessed_data, database_name, collection_name,connection_string):
#     client = MongoClient(connection_string)
#     db = client[database_name]
#     collection = db[collection_name]
#     #collection.insert_many(preprocessed_data.to_dict('records'))
#     for record in preprocessed_data.to_dict('records'):
#         # Define the filter criteria (e.g., based on unique identifiers)
#         filter_criteria = {'_id': record['_id']}  # Assuming '_id' is a unique identifier

#         # Update the document if it already exists, otherwise insert a new one
#         collection.update_one(filter_criteria, {'$set': record}, upsert=True)

def preprocess_data(data):
    df=pd.DataFrame(data)
    #preprocess= Preprocess(data)
    print(df.head())
    return df #preprocess.Preprocessed()


def fetch_data_and_store():

    #connect to SQL server
    obj = SqlConnect(
        server='10.130.205.31',
        database='IMS_Base',
        username='ims_kmg_dev',
        password='the5.Guide.jested.a.fact.fools.the1.vestibule'        
        )   
    
    try:
        
        # Provide a list of table names you want to fetch and insert into MongoDB
        obj.run_query(table_names=['dbo.tblQuotes'])#, 'dbo.tblQuoteDetails'])
    except Exception as e:
        print(f"Exception while calling function : {e}")
        #finally:
            #obj.close_connections()

    # source_database_name = 'camico' #credentials['name']
    # source_collection_name = 'Insurance_Policy' #credentials['collection']
    # connection_string='mongodb://localhost:27017/'#credentials['connectionstring']
    # source_collection = connect_to_mongodb(source_database_name, source_collection_name,connection_string)

    # data = fetch_data(source_collection)    
    
    #data=Map_json(data)
    
    #preprocessed_data = preprocess_data(data)
    # table_path="./tables/"
    # try:
    #     for table in table_path:
    #         print("data is saved")
    #         return 'Data is Saved!'
    
    # except Exception as e:
    #     print(f'Process could not be completed. Exception : \n {e} . Traceback: {traceback.print_exc()}')
    #     return f'Process could not be completed. Exception : \n {e}'
    #return "Saved Successfully"
            
def schedule_pipeline():
    try:
        fetch_data_and_store()
        
        print('Scheduler started...')
        # Schedule the data pipeline to run hourly
        schedule.every().second.do(fetch_data_and_store)

        # Infinite loop to keep the script running
        while True:
            schedule.run_pending()
            time.sleep(10)  # Sleep for 1 second to avoid high CPU usage
    except Exception as e:
        #logging.error(f"An error occurred in the scheduler: {str(e)}")
        print(f"An error occurred in the scheduler: {e}")
