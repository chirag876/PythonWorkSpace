import json
from fuzzywuzzy import fuzz

# with open("acord140_V2014_12/schema/config.json",'r') as file: 
#     config= json.load(file)  

def match_table_header(table_keys):

    tables = {
        "DRIVER INFORMATION" : "DRIVER # NAME (include address if required MAR STAT SEX DATE OF BIRTH YRS EXP YEAR LIC DRIVERS LICENSE NUMBER SOCIAL SECURITY NUMBER STATE LIC DATE HIRE BROADEN NO-FAULT DOC USE VEH # % USE"
                }
    try:
        
        for header,value in tables.items():
            fuzzy_score = fuzz.token_sort_ratio(value,table_keys)
            # print(f"table keys ::{key} table_header :: {header}  score :: {fuzzy_score}")
            if fuzzy_score > 70:
                # print(f"header :: {header}  table_keys ::{table_keys}")
                return header
        else:
            return None
    except:
        return None
      
    
def match_key(json_data, page_number, key):
    try:
        if key in json_data[page_number]['all_kvs'].keys():
            value = json_data[page_number]['all_kvs'][key]
            if isinstance(value, list):
                # If value is a list, take the first item and remove it from the list
                if value:
                    json_data[page_number]['all_kvs'][key] = value[1:]  # Remove the first item
                    return value[0]
                else:
                    return None
            else:
                json_data[page_number]['all_kvs'].pop(key,None)
                return value
        else:
            for KEY in json_data[page_number]['all_kvs'].keys():
                fuzzy_score = fuzz.token_sort_ratio(key, KEY)
                if fuzzy_score > 70:
                    value = json_data[page_number]['all_kvs'][KEY]
                    if isinstance(value, list):
                        # If value is a list, take the first item and remove it from the list
                        if value:
                            json_data[page_number]['all_kvs'][KEY] = value[1:]  # Remove the first item
                            return value[0]
                        else:
                            return None
                    else:
                        json_data[page_number]['all_kvs'].pop(KEY,None)
                        return value
                else:
                    return None
    except KeyError:
        pass
    return None
    


def update_config(config, json_data, page_number):
    for key, value in config.items():
        if isinstance(value, str):
            config[key] = match_key(json_data, page_number, key)
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                if isinstance(item, dict):
                    update_config(item, json_data, page_number)
        elif isinstance(value, dict):
            update_config(value, json_data, page_number)


def append_table_data(data, json_data, page_number):
    # data['table_data'] = json_data[page_number]['table_data']       
    # if page_number != "Page_3" :

    #         config[page_number]['table_data'] = json_data[page_number]['table_data']
    final_tables = {}
    try:
        for table_number,table in json_data[page_number]['table_data'].items():
            if isinstance(table,list):
                table_keys = " ".join([row for row in table[0]])
                header = match_table_header(table_keys)
                if header:
                    final_tables.update({header:table})
                    
            elif isinstance(table,dict):
                # print("inside dict table")
                keys = [key for key in table.keys()]
                table_keys = " ".join(keys)
                # print(f"table keys ::{table_keys}")
                header = match_table_header(table_keys)
                if header:
                    final_tables.update({header : table})   
        data['table_data'] = final_tables

    except Exception as e:
        print(f"Error occured :: {e}")


def acord127_mapper(config,json_data,page_count,file_name):
    for page_number, data in config.items():
        update_config(data, json_data, page_number)
        append_table_data(data, json_data, page_number)

    file_name = file_name.split("/")[1].replace(' ', '')

    config['File_Name'] = file_name
    config['Page_Count'] = page_count
    
    # with open(f"acord127_V2010_05/output/{file_name.split('.')[0]}.json",'w') as file:
    #     json.dump(config,file,indent=4)

    return config
# with open("BuffetOne_schema_output.json",'w') as file: 
#     json.dump(config,file,indent=4) 
 
    