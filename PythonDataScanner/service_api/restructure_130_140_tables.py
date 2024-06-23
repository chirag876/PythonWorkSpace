from fuzzywuzzy import fuzz

dict1 = {
        "SINKHOLE COVERAGE (Required in Florida)":
            {
                "ACCEPT COVERAGE":"",
                "REJECT COVERAGE":"",
                "LIMIT":""
            }
        }
                    
dict2 = {
        "MINE SUBSIDENCE COVERAGE (Required in IL, IN, KY and WV)":
            {
            "ACCEPT COVERAGE":"",
            "REJECT COVERAGE":"",
            "LIMIT":""
            }
        }

dict_3 = {
    "ADDITIONAL COVERAGES, OPTIONS, RESTRICTIONS, ENDORSEMENTS AND RATING INFORMATION":
    {
        "SPOILAGE COVERAGE (Y / N)":"",
        "DESCRIPTION OF PROPERTY COVERED":"",
        "LIMIT":"",
        "DEDUCTIBLE":"",
        "REFRIG MAINT AGREEMENT (Y / N)":"",
        "OPTIONS":
        {
           "BREAKDOWN OR CONTAMINATION":"",
           "POWER OUTAGE":"",
            "SELLING PRICE":""
        }

    }
}

dict_4 = {
    "ADDITIONAL INTEREST":
    {
      "INTEREST":
      {
        "LOSS PAYEE":"",
        "MORTGAGEE":""}  
    }
}


dict_5 = {
    "INTEREST IN ITEM NUMBER":
    {
        "LOCATION":"",
        "BUILDING":"",
        "ITEM CLASS":"",
        "ITEM":"",
        "ITEM DESCRIPTION":"",
    }
}

class RESTRUCTURE_130_140 :

    def identify_table_structure(self,tables):

        filtered_tables = {}
        table_count = 1
        for table_name, table_data in tables.items():
            if len(table_data) == 1:
                keys = list(table_data["row_1"].values())
                result = {key: " " for  key in keys}
                filtered_tables.update({f"table_{table_count}" : result})
                table_count += 1

            elif len(table_data) == 2:  # Check if the table has exactly 2 rows
                keys = list(table_data["row_1"].values())
                values = list(table_data["row_2"].values())
                
                if len(keys)%2 != 0 :   # If number of columns is odd then add empty space to make it
                        similarity_1 = fuzz.token_set_ratio([key for key in dict1.keys()][0], keys[0])
                        similarity_2 = fuzz.token_set_ratio([key for key in dict2.keys()][0], values[0])
                        
                        if similarity_1 >= 90 and similarity_2 >=90:
                            # print("Condition satisfied...")
                            result = {**dict1,**dict2}
                            # filtered_tables.update({table_name : result})
                            # print("filtered tables :::",filtered_tables)

  
                else:
                    result = {key:value for  key, value in zip(keys, values)}
                    filtered_tables.update({f"table_{table_count}" : result})
                    table_count += 1

            # for table_name, table_data in data.items():
            # elif len(table_data) >= 3:  # Check if the table has at least 3 rows
            #     keys = list(table_data["row_1"].values())
            #     values = [row.values() for row_key, row in table_data.items() if row_key != "row_1"]
            #     result = [dict(zip(keys, value)) for value in values]
            #     filtered_tables.update({table_name : result})

            elif len(table_data) >= 3:  # Check if the table has at least 3 rows
                row_1_values = [key for key in table_data["row_1"].values() if key]
                row_2_values = [key for key in table_data["row_2"].values() if key]

                similarity_1 = fuzz.token_set_ratio([key for key in dict_3.keys()][0], " ".join(row_1_values))    
                similarity_2 =  fuzz.token_set_ratio([key for key in dict_4.keys()][0], " ".join(row_1_values))
                similarity_3 =  fuzz.token_set_ratio([key for key in dict_5.keys()][0], " ".join(row_1_values)) 
                    
                if similarity_1 >= 90 :
                    # print("condition satisfied...")
                    pass
                    # filtered_tables.update({table_name:dict_3})

                elif similarity_2 >= 90:
                    pass
                    # filtered_tables.update({table_name :  dict_4})

                elif similarity_3 >= 90:
                    pass
                    # filtered_tables.update({table_name :  dict_5})
                
                elif len(row_1_values) < len(row_2_values):
                    keys = row_2_values
                    values = [row.values() for row_key, row in table_data.items() if row_key not in ['row_1','row_2']]
                    result = [dict(zip(keys, value)) for value in values]
                    filtered_tables.update({f"table_{table_count}" : result})
                    table_count += 1

                elif len(set(row_1_values)) < len(row_1_values):
                    unique_keys = []
                    for v in table_data["row_1"].values() :
                        if v not in unique_keys:
                            unique_keys.append(v)
                        else:
                            unique_keys.append(v+'.')
                    keys = unique_keys
                    values = [row.values() for row_key, row in table_data.items() if row_key != "row_1"]
                    result = [dict(zip(keys, value)) for value in values]
                    filtered_tables.update({f"table_{table_count}" : result})
                    table_count += 1

                # elif len(table_data.keys()) == 4:
                #     row_1_values = [key for key in table_data["row_1"].values()]
                #     row_2_values = [key for key in table_data["row_2"].values()]
                #     # print(row_1_values,row_2_values)
                #     # if len(set(row_1_values)) > len(set(row_2_values)) and (row_1_values.index('') == row_2_values.index('')):
                #     #     # Binding row_1 with row_2
                #     #     bound_row_1_2 = {table_data["row_1"][key]: table_data["row_2"][key] for key in table_data["row_1"].keys()}

                #     #     # Binding row_3 with row_4
                #     #     bound_row_3_4 = {table_data["row_3"][key]: table_data["row_4"][key] for key in table_data["row_3"].keys()}

                #     #     result = {**bound_row_1_2, **bound_row_3_4}
                #     #     filtered_tables.update({table_name: result})
                #     if len(row_1_values) == len(row_2_values) and '' in row_1_values and row_1_values.index('') == row_2_values.index(''):
                #         # Binding row_1 with row_2
                #         bound_row_1_2 = {table_data["row_1"][key]: table_data["row_2"][key] for key in table_data["row_1"].keys()}
                #         # Binding row_3 with row_4
                #         bound_row_3_4 = {table_data["row_3"][key]: table_data["row_4"][key] for key in table_data["row_3"].keys()}
                #         result = {**bound_row_1_2, **bound_row_3_4}
                #         filtered_tables.update({table_name: result})
                #         # print(result)

                #     else:
                #         keys = [key for key in table_data["row_1"].values()]
                #         values = [row.values() for row_key, row in table_data.items() if row_key != "row_1"]
                #         result = [dict(zip(keys, value)) for value in values]
                #         filtered_tables.update({table_name: result})
                
                elif len([key for key in table_data["row_1"].values()]) == len([key for key in table_data["row_2"].values()]) and '' in [key for key in table_data["row_1"].values()] and [key for key in table_data["row_1"].values()].index('') == [key for key in table_data["row_2"].values()].index(''):
                        # Binding row_1 with row_2
                        bound_row_1_2 = {table_data["row_1"][key]: table_data["row_2"][key] for key in table_data["row_1"].keys()}
                        # Binding row_3 with row_4
                        bound_row_3_4 = {table_data["row_3"][key]: table_data["row_4"][key] for key in table_data["row_3"].keys()}
                        result = {**bound_row_1_2, **bound_row_3_4}
                        result = {key:value for key,value in result.items() if key and value}
                        filtered_tables.update({f"table_{table_count}" : result})
                        table_count += 1

                elif (len(row_1_values) >= len(row_2_values)) and ('EXPLAIN ALL "YES" RESPONSES' not in row_1_values):
                    # print(table_data.items())
                    keys = [key for key in table_data["row_1"].values()]
                    values = [row.values() for row_key, row in table_data.items() if row_key!= "row_1"]
                    result = [dict(zip(keys, value)) for value in values]
                    filtered_tables.update({f"table_{table_count}" : result})
                    table_count += 1

                # print(f"{table_name}: {result}")
            
                elif (len(row_1_values) >= len(row_2_values)) and ('EXPLAIN ALL "YES" RESPONSES' in row_1_values) :
                    result = { }

                    # print("table_data ::",table_data)

                    for values in table_data.values():

                        key = values["col_1"] 
                        value = values["col_2"]

                        if key != 'EXPLAIN ALL "YES" RESPONSES':
                            result[key] = value 
                        
                    combined_result = {"EXPLAIN ALL 'Y/N' RESPONSES":result}
                    filtered_tables.update({f"table_{table_count}" : combined_result})
                    table_count += 1 
                else:
                    filtered_tables.update({f"table_{table_count}" : result})
                    table_count += 1
            
        # print("filtered_table ::",filtered_tables)

        return filtered_tables
            
        