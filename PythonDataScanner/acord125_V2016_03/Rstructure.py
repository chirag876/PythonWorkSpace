import json 

class RESTRUCTURE :

#check if alternate tables are blank/X/SELECTED or not
    def check_alternate_columns(self, table_data):
        for row_names, row_values in table_data.items():
            # Check if the value is 'X' or 'SELECTED'
            if 'X' in list(row_values.keys()) or 'X' in list(row_values.values()):
                return True
        return False


#When col[i] and col[i+1] are supposed to be key and value. Transform attachments table
    def transform_rows_attachments(self, table_data,reverse=False):
        new_table_data = {}
        if table_data['row_1']['col_1'] not in ['','X','SELECTED']:# and table_data['row_1']['col_3'] not in ['','X','SELECTED']:
            reverse=True
        for row_key, row_data in table_data.items():
            new_row_data = {}
            for i in range(1, len(row_data), 2):
                #print(i,table_data)
                if i + 1 <= len(row_data):
                    if reverse:
                        new_row_data[row_data[f'col_{i}']] = row_data[f'col_{i+1}']
                    else:   
                        new_row_data[row_data[f'col_{i+1}']] = row_data[f'col_{i}']
            new_table_data[row_key] = new_row_data
        return new_table_data

    def identify_table_structure(self,tables):

        filtered_tables = {}
        for table_name, table_data in tables.items():
            if self.check_alternate_columns(table_data):
                result=self.transform_rows_attachments(table_data)
                filtered_tables.update({table_name : result})
                print('new logic results :\n',result)

            elif len(table_data) == 2:  # Check if the table has exactly 2 rows
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
        
        #print("filtered_table ::",filtered_tables)

        return filtered_tables