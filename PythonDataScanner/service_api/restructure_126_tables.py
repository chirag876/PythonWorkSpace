class RESTRUCTURE_126 :

    def identify_table_structure(self,tables):

        filtered_tables = {}
        for table_name, table_data in tables.items():
            if len(table_data) == 2:  # Check if the table has exactly 2 rows
                keys = list(table_data["row_1"].values())
                values = list(table_data["row_2"].values())
                result = {key:value for  key, value in zip(keys, values)}
                filtered_tables.update({table_name : result})


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
                else:
                    keys = row_1_values
                    values = [row.values() for row_key, row in table_data.items() if row_key != "row_1"]

                result = [dict(zip(keys, value)) for value in values]
                filtered_tables.update({table_name: result})


                # print(f"{table_name}: {result}")
            
            elif all((len(values)==2 for values in table_data.values()) and ('Y' or 'N' in values)) :
                result = {}
                for values in table_data.values():
                    # print(values)        
                    key = values["col_1"]
                    value = values["col_2"]
                    result[key] = value 
                    
                filtered_tables.update({table_name : result}) 
            else:
                filtered_tables.update({table_name :  table_data})
        
        # print("filtered_table ::",filtered_tables)

        return filtered_tables