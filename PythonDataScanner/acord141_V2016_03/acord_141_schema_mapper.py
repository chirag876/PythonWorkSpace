import json
from fuzzywuzzy import fuzz

def match_table_header(table_keys):

    tables = {
                "MONEY - SECURITIES":"TYPE MONEY CHECKS FOR DEPOSIT CHECKS FOR ACCOUNTSPAYABLE PAYROLL CHECKS MONEY OVERNIGHT SECURITIES ON BANK SAFE DEPOSIT",
                "EMPLOYEE SCHEDULE (Complete if required)":"NAME OF EMPLOYEES TO BE COVERED TITLE LIMIT DEDUCTIBLE",
                "COVERAGE TABLE 2":"COVERAGE LIMIT DEDUCTIBLE",
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
  
def calculate_similarity(string, string_list):
    max_match = max(string_list, key=lambda s: fuzz.ratio(string, s))
    # print(f" max match :{max_match}, string : {string}, probab:{fuzz.ratio(string, max_match)}\n")
    return max_match if fuzz.ratio(string, max_match) >= 88 else None

#data is data from textract, schema is schema json created for FORM 125
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
                return value
        else:
            KEYs = json_data[page_number]['all_kvs'].keys()
            match = calculate_similarity(key,KEYs)
            if match:
                value = json_data[page_number]['all_kvs'][match]
                if isinstance(value, list):
                    # If value is a list, take the first item and remove it from the list
                    if value:
                        json_data[page_number]['all_kvs'][match] = value[1:]  # Remove the first item
                        return value[0]
                    else:
                        return None
                else:
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

            if table_number == "COVERAGE TABLE 1":
                final_tables.update({table_number:table})

            elif isinstance(table,list):
                table_keys = " ".join([row for row in table[0]])
            
                header = match_table_header(table_keys)
                if header:
                    final_tables.update({header : table})
              

            elif isinstance(table,dict):
                # print("inside dict table")
                keys = [key for key in table.keys()]
                table_keys = " ".join(keys)
                # print(f"table keys ::{table_keys}")
                header = match_table_header(table_keys)
                if header:
                    final_tables.update({header : table})
                
        data['table_data'] = final_tables
    # print(config)
    except Exception as e:
        print(f"Error occured :: {e}")


def acord141_mapper(config,json_data,page_count,file_name):
    for page_number, data in config.items():
        update_config(data, json_data, page_number)
        append_table_data(data, json_data, page_number)

    file_name = file_name.split("/")[1].replace(' ', '')
    
    config['File_Name'] = file_name
    config['Page_Count'] = page_count

    # with open(f"acord141_V2016_03/output/{file_name.split('.')[0]}.json",'w') as file:
    #     json.dump(config,file,indent=4)

    return config

 
    