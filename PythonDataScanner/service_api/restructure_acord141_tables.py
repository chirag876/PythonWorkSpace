from fuzzywuzzy import fuzz


class RESTRUCTURE_141:

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

                
                if len(row_1_values) < len(row_2_values):
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
                
                elif (len(row_1_values) >= len(row_2_values)) and ('NO EXPLANATION REQUIRED' not in row_1_values):
                    # print(table_data.items())

                    if ("COVERGAE" or "LIMIT" in row_1_values) and (len(table_data['row_1']) == 6):
                        # print("table row_1 ::",table['row_1'].values())
                        key_1 = " ".join([k for k in table_data['row_1'].values()][:4]).strip()
                        key_2 = [k for k in table_data['row_1'].values()][4]
                        key_3 = [k for k in table_data['row_1'].values()][5]
                        print(key_1,key_2,key_3)

                        v1 = [[" ".join([k for k in table_data[row].values()][:4]).strip()] for row in table_data.keys() if row != 'row_1']
                        v2 = [[k for k in table_data[row].values()][4] for row in table_data.keys() if row != 'row_1']
                        v3 = [[k for k in table_data[row].values()][5] for row in table_data.keys() if row != 'row_1']

                        result = dict(zip((key_1,key_2,key_3),(v1,v2,v3)))
                        final_result = []

                        print(len(result[list(result.keys())[0]]))
                        for i in range(len(result[list(result.keys())[0]])):
                            final_result.append({"COVERAGE":result["COVERAGE"][i][0],
                                                "LIMIT":result["LIMIT"][i],
                                                "DEDUCTIBLE":result["DEDUCTIBLE"][i]})
                            
                        filtered_tables.update({f"COVERAGE TABLE 1" : final_result})
                        

                    elif ("COVERGAE" or "LIMIT" in row_1_values) and (len(table_data['row_1']) == 4):
                    
                        def combine_col1_col2(data):
                            combined_data=[]
                            h1,h2,h3='','',''
                            flag=False
                            for key,values in data.items():
                                if not flag:
                                    if len(data)>3:
                                        combined_data.append({'col_1':f"{values['col_1']}{values['col_2']}",'col_2':values['col_3'],'col_3':values['col_4']})
                                        h1,h2,h3=f"{values['col_1']}{values['col_2']}",values['col_3'],values['col_4']
                                    else:
                                        combined_data.append({'col_1':f"{values['col_1']}{values['col_2']}",'col_2':values['col_3'],'col_3':values['col_4']})
                                        h1,h2,h3=f"{values['col_1']}{values['col_2']}",values['col_3'],values['col_4']
                                    flag=True
                                else:
                                    combined_data.append({h1:f"{values['col_1']}{values['col_2']}",h2:values['col_3'],h3:values['col_4']})
                            del combined_data[0]
                            return combined_data
                        result = combine_col1_col2(table_data)

                        filtered_tables.update({table_name : result})

                    else:
                        keys = [key for key in table_data["row_1"].values()]
                        values = [row.values() for row_key, row in table_data.items() if row_key!= "row_1"]
                        result = [dict(zip(keys, value)) for value in values]
                        filtered_tables.update({f"table_{table_count}" : result})
                        table_count += 1

                # print(f"{table_name}: {result}")
            
                elif (len(row_1_values) >= len(row_2_values)) and ('NO EXPLANATION REQUIRED' in row_1_values) :
                    result = { }

                    # print("table_data ::",table_data)

                    for values in table_data.values():

                        key = values["col_1"] 
                        value = values["col_2"]

                        if key != 'NO EXPLANATION REQUIRED':
                            result[key] = value 
                        
                    combined_result = {"NO EXPLANATION REQUIRED":result}
                    filtered_tables.update({f"table_{table_count}" : combined_result})
                    table_count += 1 
                else:
                    filtered_tables.update({f"table_{table_count}" : result})
                    table_count += 1
            
        # print("filtered_table ::",filtered_tables)

        return filtered_tables