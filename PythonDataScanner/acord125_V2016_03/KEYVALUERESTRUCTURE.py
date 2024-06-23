import json
from acord125_V2016_03.Rstructure import RESTRUCTURE
from fuzzywuzzy import fuzz

# f=open('config.json')
# schema_json=json.load(f)

# f=open("ACORD125_LAMBIS_InsuranceExample_Medicinzy1_05232022_more_keys.json")
# data_json=json.load(f)
# result_json={}

def calculate_similarity(string, string_list):
    max_match = max(string_list, key=lambda s: fuzz.ratio(string, s))
    # print(f" max match :{max_match}, string : {string}, probab:{fuzz.ratio(string, max_match)}\n")
    return max_match if fuzz.ratio(string, max_match) >= 88 else None

#data is data from textract, schema is schema json created for FORM 125
def map_keys(data, schema):
    result = {}
    for key_schema in schema:
        if isinstance(schema[key_schema], dict):
            result[key_schema] = map_keys(data, schema[key_schema])
        else:
            #print(key_schema)
            if key_schema in data:
                if ',' in data[key_schema]:
                    value_list=data[key_schema].split(',')
                    value=value_list[0]
                    data[key_schema]=' '.join(value_list[1:])
                else:
                    value=data[key_schema]
                    data.pop(key_schema)
                result[key_schema] = value

            else:
                found=0
                KEYS=list(data.keys())
                #print("keys : \n",KEYS)
                key_match_found=calculate_similarity(key_schema, KEYS)
                if key_match_found:
                    #print(key_match_found,key_schema)
                    if ',' in data[key_match_found]:
                        value_list=data[key_match_found].split(',')
                        value=value_list[0]
                        data[key_match_found]=' '.join(value_list[1:])
                    else:
                        value=data[key_match_found]
                        data.pop(key_match_found)
                        result[key_schema] = value
                else: result[key_schema] = ""
    return result

def acord125_mapper(schema_json,data_json,filename):
    # f=open("acord125_V2016_03/schema/config.json")
    # schema_json=json.load(f)    
    r=RESTRUCTURE()
    result_json={}
    for page, page_data in data_json.items():
        if "Page_" in page and page!= "Page_Count": 
            result_json[page] = map_keys(page_data["all_kvs"], schema_json.get(page, {}))
            if page in ["Page_3","Page_4"]:
                result_json[page]["table_data"] = page_data["table_data"]#r.identify_table_structure(page_data["table_data"])

    # file_name = filename.split("/")[1].replace(' ', '')
    # with open(f"acord125_V2016_03/output/{file_name}.json",'w') as file:
    #     json.dump(result_json,file,indent=4)

    return result_json
