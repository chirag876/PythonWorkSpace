
from database.mongoDB_collection import MongoDBHandler

obj_mongo = MongoDBHandler()
def read_acord_schema(read_acord_form_name):
    
    stai_json_schema = obj_mongo.get_stai_json_schema_by_form_name(read_acord_form_name)
    return stai_json_schema



    