import json
from fuzzywuzzy import fuzz

config_json = "acord126_V2014_04/schema/updated_schema.json"

with open(config_json,'r') as file: 
    config= json.load(file)  

def match_table_header(table_keys):

    tables = {
                "LOCATIONS":"LOC # HIGHES FLOOR STREET CITY COUNTY STATE ZIP CODE",
                "CONTACT INFORMATION":"TYPE NAME OFFICE PHONE MOBILE PHONE E-MAIL",
                "INDIVIDUALS INCLUDED / EXCLUDED":"STATE LOC NAME DATE OF BIRTH TITLE RELATIONSHIP OWNER SHIP DUTIES INCIEXO CLASS CODE REMUNERATION/PAYROLL",    
                "STATE RATING WORKSHEET":"LOC. CLASS CODE CODE CATEGORIES DUTIES CLASSIFICATIONS FULL TIME PART TIME SIC NAICS REMUNERATION PAYROLL RATE ANNUAL MANUAL PREMIUM",
                "PREMIUM":"STATE FACTOR FACTORED PREMIUM FACTOR FACTORED PREMIUM",
                "GENERAL INFORMATION":"EXPLAIN ALL 'YES' RESPONSES, 'Y/N'",
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



def acord126_mapper(json_data,page_count,file_name):

    # filename = file_name.split('\\')[-1].split('.')[0]

    def match(page_number,key):
        try:
            if key in json_data[page_number]['all_kvs'].keys():
                return json_data[page_number]['all_kvs'][key]
            else:
                
                for KEY in json_data[page_number]['all_kvs'].keys():
                    fuzzy_score = fuzz.token_sort_ratio(key,KEY)
                    
                    if fuzzy_score > 70:
                        # print(f"key :: {key} ACORD_KEY ::{KEY}")
                        return json_data[page_number]['all_kvs'][KEY]
                    else:
                        if key in ["AMOUNT IN WI","AMOUNT % IN WI"]:
                            # print("KEY FOUND")
        
                            return json_data[page_number]['all_kvs']["AMOUNT IN WI"] or json_data[page_number]['all_kvs']["AMOUNT % IN WI"]
        except:
            return None  

    
    for page_number,data in config.items():
        if isinstance(data,dict):
            for key,value in data.items():
                if isinstance(value,str):
                    # print("key ::",key)
                    config[page_number][key] = match(page_number,key)                
                elif  isinstance(value,dict):
                    for key_2,value_2 in value.items(): 
                        if isinstance(value_2,str):
                            # print("key ::",key_2)
                            config[page_number][key][key_2] = match(page_number,key_2)
                        elif  isinstance(value_2,dict):
                            for key_3,value_3 in value_2.items():
                                if isinstance(value_3,str):
                                    # print("key ::",key_3)
                                    config[page_number][key][key_2][key_3] = match(page_number,key_3)
                                elif  isinstance(value_3,dict):
                                    for key_4,value_4 in value_3.items():
                                        if isinstance(value_4,str):
                                            # print("key ::",key_4)
                                            config[page_number][key][key_2][key_3][key_4] = match(page_number,key_4)
                                        elif  isinstance(value_4,dict):
                                            for key_5,value_5 in value_4.items():
                                                if isinstance(value_5,str):
                                                    # print("key ::",key_5)
                                                    config[page_number][key][key_2][key_3][key_4][key_5] = match(page_number,key_5)
                            
        config[page_number]['table_data'] = json_data[page_number]['table_data']
        # final_tables = {}
        # for table_number,table in json_data[page_number]['table_data'].items():
        #     if isinstance(table,list):
        #         table_keys = " ".join([row for row in table[0]])
        #         # print("table keys ::",table_keys)
            
        #         header = match_table_header(table_keys)
        #         if header:
        #             final_tables.update({header : table})
        #         # else:
        #         #     final_tables.update({table_number : table})

        #     elif isinstance(table,dict):
        #         # print("inside dict table")
        #         keys = [key for key in table.keys()]
        #         table_keys = " ".join(keys)
        #         # print(f"table keys ::{table_keys}")
        #         header = match_table_header(table_keys)
        #         if header:
        #             final_tables.update({header : table})
        #         # else:
        #         #     final_tables.update({table_number : table})

        #     # else:
        #     #     # print(f"unknown {table}")
        #     #     final_tables.update({table_number : table})
        
        # config[page_number]['table_data'] = final_tables
    # config['File_Name'] = filename
    config['Page_Count'] = page_count

    # with open(f"acord126/output/{filename}.json",'w') as file:
    #     json.dump(config,file,indent=4)

    
    with open(f"acord126_V2014_04/output/LAMB_Petorian.json",'w') as file:
        json.dump(config,file,indent=4)

    return config
# with open("BuffetOne_schema_output.json",'w') as file: 
#     json.dump(config,file,indent=4) 
 
    