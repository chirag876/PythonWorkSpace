import json
from fuzzywuzzy import fuzz

# with open("acord140_V2014_12/schema/config.json",'r') as file: 
#     config= json.load(file)  

def match_table_header(table_keys):

    tables = {
                "INFORMATION":"AGENCY NAME CARRIER NAIC CODE EFFECTIVE DATE NAMED INSURED(S)",
                "BLANKET SUMMARY":"BLKT . AMOUNT TYPE BLKT I AMOUNT.TYPE.",
                "PREMISES INFORMATION":"SUBJECT OF INSURANCE AMOUNT COINS % VALUE ATION CAUSES OF LOSS INFL ATION GUARD'S DED DED TYPE BLAC . FORMS AND CONDITIONS TO APPLY",
                "ADDITIONAL COVERAGES, OPTIONS, RESTRICTIONS, ENDORSEMENTS AND RATING INFORMATION":"CONSTRUCTION TYPE Frame DIST ANCE HYDRANT TO FIRE STAT FIRE DISTRICT CODE NUMBER PROT CL # STORIES BASM'TS YR BUILT TOTAL AREA",
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






    # def match(page_number,key):
    #     try:
    #         if key in json_data[page_number]['all_kvs'].keys():
    #             output = json_data[page_number]['all_kvs'][key]
    #             json_data[page_number]['all_kvs'].pop(key)
    #             return output
    #         else:
                
    #             for KEY in json_data[page_number]['all_kvs'].keys():
    #                 fuzzy_score = fuzz.token_sort_ratio(key,KEY)
                    
    #                 if fuzzy_score > 70:
    #                     # print(f"key :: {key} ACORD_KEY ::{KEY}")
    #                     output = json_data[page_number]['all_kvs'][KEY]
    #                     json_data[page_number]['all_kvs'].pop(KEY)
    #                     return output
    #             else:
    #                 if key in ["AMOUNT IN WI","AMOUNT % IN WI"]:
    #                     # print("KEY FOUND")
    #                     return json_data[page_number]['all_kvs']["AMOUNT IN WI"] or json_data[page_number]['all_kvs']["AMOUNT % IN WI"]
    #                 else:
    #                     return None
    #     except:
    #         return None  
        

    
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
    # config['table_data'] = json_data[page_number]['table_data']       
    # if page_number != "Page_3" :

    #         config[page_number]['table_data'] = json_data[page_number]['table_data']
    final_tables = {}
    try:
        for table_number,table in json_data[page_number]['table_data'].items():
            if isinstance(table,list):
                table_keys = " ".join([row for row in table[0]])
                header = match_table_header(table_keys)
                if header:
                    if header == "BLANKET SUMMARY":
                        column_names = ["BLTK #","AMOUNT","TYPE"]
                        final_list = []
                        for subdict in table:
                            values = [v for v in subdict.values()]
                            dict_1 = {new_key:val for new_key,val in zip(column_names,values[:3])}
                            final_list.append(dict_1)        
                            dict_2 = {new_key:val for new_key,val in zip(column_names,values[3:])}
                            final_list.append(dict_2)
                        final_tables.update({header:final_list})
                    else:
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


def acord140_mapper(config,json_data,page_count,file_name):
    for page_number, data in config.items():
        update_config(data, json_data, page_number)
        append_table_data(data, json_data, page_number)

    file_name = file_name.split("/")[1].replace(' ', '')

    
    config['File_Name'] = file_name
    config['Page_Count'] = page_count
    


    # with open(f"acord140_V2014_12/output/{file_name.split('.')[0]}.json",'w') as file:
    #     json.dump(config,file,indent=4)

    return config
# with open("BuffetOne_schema_output.json",'w') as file: 
#     json.dump(config,file,indent=4) 
 
    