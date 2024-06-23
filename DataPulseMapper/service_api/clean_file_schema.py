from flask import request
import time
from bson import ObjectId
from database.mongoconnection2 import Mongoconnection
import time

obj_mongo = Mongoconnection()

def clean_file_Schema():
    file_schema_id = request.form['file_schema_id']
    start_time = time.time()
    
    file_status_document = obj_mongo.get_file_status_by_schema_id(file_schema_id)
    print("file status document:", file_status_document)
    
    obj_mongo.update_file_status(file_status_document.get('_id'),"UPLOADED")
    file_schema_id_ = file_status_document.get('file_schema_id')
    
    old_query = {'file_schema_id': file_schema_id}
    query = {'$set':{'file_schema_id':''}}
    obj_mongo.file_status_collection.update_one(old_query, query)
    
    old_query = {'_id': ObjectId(file_schema_id_)}
    print("old_query:", old_query)
    
    obj_mongo.file_schema_collection.delete_one(old_query)
    return ""













    