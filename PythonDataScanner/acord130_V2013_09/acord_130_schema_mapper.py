import json
from fuzzywuzzy import fuzz
from logzero import logger


# with open("acord130_V2013_09/schema/config.json",'r') as file: 
#     config= json.load(file)  

def match_table_header(table_keys):

    tables = {
                "LOCATIONS":"LOC # HIGHES FLOOR STREET CITY COUNTY STATE ZIP CODE",
                "CONTACT INFORMATION":"TYPE NAME OFFICE PHONE MOBILE PHONE E-MAIL",
                "INDIVIDUALS INCLUDED / EXCLUDED":"STATE LOC NAME DATE OF BIRTH TITLE RELATIONSHIP OWNER SHIP DUTIES INCIEXO CLASS CODE REMUNERATION/PAYROLL",    
                "STATE RATING WORKSHEET":"LOC. CLASS CODE CODE CATEGORIES DUTIES CLASSIFICATIONS FULL TIME PART TIME SIC NAICS REMUNERATION PAYROLL RATE ANNUAL MANUAL PREMIUM",
                "PREMIUM":"STATE FACTOR FACTORED PREMIUM FACTOR FACTORED PREMIUM",
                "GENERAL INFORMATION":"EXPLAIN ALL 'Y/N' RESPONSES",
                "PRIOR CARRIER INFORMATION / LOSS HISTORY":"YEAR CARRIER & POLICY NUMBER ANNUAL PREMIUM MCD CLAIMS AMOUNT PAID RESERVE"
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



# def acord130_mapper(json_data,page_count,file_name):

#     # filename = file_name.split('\\')[-1].split('.')[0]

#     def match(page_number,key):
#         try:
#             if key in json_data[page_number]['all_kvs'].keys():
#                 return json_data[page_number]['all_kvs'][key]
#             else:
                
#                 for KEY in json_data[page_number]['all_kvs'].keys():
#                     fuzzy_score = fuzz.token_sort_ratio(key,KEY)
                    
#                     if fuzzy_score > 70:
#                         # print(f"key :: {key} ACORD_KEY ::{KEY}")
#                         return json_data[page_number]['all_kvs'][KEY]
#                     else:
#                         if key in ["AMOUNT IN WI","AMOUNT % IN WI"]:
#                             # print("KEY FOUND")
        
#                             return json_data[page_number]['all_kvs']["AMOUNT IN WI"] or json_data[page_number]['all_kvs']["AMOUNT % IN WI"]
#         except:
#             return None  

#     logger.info("ACORD 130 (2013/09) mapping started ...")
#     for page_number,data in config.items():
#         if isinstance(data,dict):
#             for key,value in data.items():
#                 if isinstance(value,str):
#                     # print("key ::",key)
#                     config[page_number][key] = match(page_number,key)                
#                 elif  isinstance(value,dict):
#                     for key_2,value_2 in value.items(): 
#                         if isinstance(value_2,str):
#                             # print("key ::",key_2)
#                             config[page_number][key][key_2] = match(page_number,key_2)
#                         elif  isinstance(value_2,dict):
#                             for key_3,value_3 in value_2.items():
#                                 if isinstance(value_3,str):
#                                     # print("key ::",key_3)
#                                     config[page_number][key][key_2][key_3] = match(page_number,key_3)
#                                 elif  isinstance(value_3,dict):
#                                     for key_4,value_4 in value_3.items():
#                                         if isinstance(value_4,str):
#                                             # print("key ::",key_4)
#                                             config[page_number][key][key_2][key_3][key_4] = match(page_number,key_4)
#                                         elif  isinstance(value_4,dict):
#                                             for key_5,value_5 in value_4.items():
#                                                 if isinstance(value_5,str):
#                                                     # print("key ::",key_5)
#                                                     config[page_number][key][key_2][key_3][key_4][key_5] = match(page_number,key_5)

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
                        return value
                elif key in ["AMOUNT IN WI", "AMOUNT % IN WI"]:
                    value = json_data[page_number]['all_kvs'].get("AMOUNT IN WI") or json_data[page_number]['all_kvs'].get("AMOUNT % IN WI")
                    if isinstance(value, list):
                        # If value is a list, take the first item and remove it from the list
                        if value:
                            if "AMOUNT IN WI" in json_data[page_number]['all_kvs']:
                                json_data[page_number]['all_kvs']["AMOUNT IN WI"] = value[1:]  # Remove the first item
                            else:
                                json_data[page_number]['all_kvs']["AMOUNT % IN WI"] = value[1:]  # Remove the first item
                            return value[0]
                        else:
                            return None
                    else:
                        return value
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
    
    final_tables = {}
    try:
        for table_number,table in json_data[page_number]['table_data'].items():
            if isinstance(table,list):
                table_keys = " ".join([row for row in table[0]])
                # print("table keys ::",table_keys)
            
                header = match_table_header(table_keys)
                if header:
                    final_tables.update({header : table})
                # else:
                #     final_tables.update({table_number : table})

            elif isinstance(table,dict):
                # print("inside dict table")
                keys = [key for key in table.keys()]
                table_keys = " ".join(keys)
                # print(f"table keys ::{table_keys}")
                header = match_table_header(table_keys)
                if header:
                    final_tables.update({header : table})
                # else:
                #     final_tables.update({table_number : table})

            # else:
            #     # print(f"unknown {table}")
            #     final_tables.update({table_number : table})
        
        data['table_data'] = final_tables
    # print(config)
    except Exception as e:
        print(f"Error occured :: {e}")


def acord130_mapper(config,json_data,page_count,file_name):
    for page_number, data in config.items():
        update_config(data, json_data, page_number)
        append_table_data(data, json_data, page_number)
    
    file_name = file_name.split("/")[1].replace(' ', '')
    config['File_Name'] = file_name
    config['Page_Count'] = page_count

    # with open(f"acord130_V2013_09/output/{file_name.split('.')[0]}.json",'w') as file:
    #     json.dump(config,file,indent=4)

    return config
# with open("BuffetOne_schema_output.json",'w') as file: 
#     json.dump(config,file,indent=4) 
 
    