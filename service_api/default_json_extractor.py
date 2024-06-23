import re
from logzero import logger
import json

def refined_output(json_data):
    table_values = set()

    def collect_table_values(data):
        if isinstance(data, dict):
            for value in data.values():
                if isinstance(value, dict):
                    collect_table_values(value)
                elif isinstance(value, str):
                    table_values.add(value)
        elif isinstance(data, list):
            for item in data:
                collect_table_values(item)
        print("table_values ::",table_values)

    collect_table_values(json_data['table_data'])

    def process_value(value):
        if value in ["X Yes No", "X Yes"]:
            return "YES SELECTED"
        elif value in ["X No", "Yes X No"]:
            return "NO SELECTED"
        elif value in ["Yes", "No", "Yes No", "No No", "Yes Yes"]:
            return "NOT_SELECTED"
        else:
            return value

    def refine_data(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict):
                    refine_data(value)
                elif isinstance(value, str):
                    data[key] = process_value(value)
                elif isinstance(value, list):
                    for i, item in enumerate(value):
                        if isinstance(item, str):
                            value[i] = process_value(item)
                        elif isinstance(item, dict) or isinstance(item, list):
                            refine_data(item)

    refine_data(json_data['table_data'])
    refine_data(json_data['all_kvs'])

    keys_to_remove = []

    for key, value in json_data['all_kvs'].items():
        if key not in table_values:
            if value == "X " or value == "X":
                json_data['all_kvs'][key] = "SELECTED"
            elif value == "":
                json_data['all_kvs'][key] = None
            elif isinstance(value, list):
                v = [v.strip() for v in value if v]
                if len(v) == 1:
                    if v[0] in ["X","X "]:
                        json_data['all_kvs'][key] = "SELECTED"
                    elif v[0] == "":
                        json_data['all_kvs'][key] = None    
                    else:
                        json_data['all_kvs'][key] = v[0]
                else:
                    json_data['all_kvs'][key] = ",".join(v)
        else:
            keys_to_remove.append(key)


    for key in keys_to_remove:
        del json_data['all_kvs'][key]
    
    return json_data


def get_formatted_json(kvs):
    for key,value in kvs.items():
        if isinstance(value,dict):
            for  subkey,subval in value.items():
                if isinstance(subval,list) and len(subval)==1:
                    kvs[key][subkey]= subval[0]
                elif isinstance(subval,list) and len(subval)>1:
                    kvs[key][subkey]= list(set(subval))
        else:
            pass
    return kvs

def default_json(kvs,page_count,file_name):

    filename = file_name.split('.')[0]
    kvs["File name"] = filename
    kvs["Page count"] = page_count

    for key,value in kvs.items():
        if isinstance(value,dict):
            formatted_value = get_formatted_json(value)
            print("formatted_value ::",formatted_value,type(formatted_value))
            kvs[key] = refined_output(formatted_value)

    with open(f"custom_page_extractor/output/{filename}.json",'w') as file:
        json.dump(kvs,file,indent=4)

    return kvs

def search_value(kvs, search_key):
    for key, value in kvs.items():
        if re.search(search_key, key, re.IGNORECASE):
            return value