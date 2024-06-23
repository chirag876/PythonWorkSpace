import copy
import json
import pandas as pd
import app_level as app_level
from logzero import logger
import uuid
from pandas import json_normalize
from rules.rule_field_map import Rule_field_map
from database.mongoconnection2 import Mongoconnection
from rules.rule_merge import Rule_merge
from rules.rule_split import Rule_split
import traceback

obj_mongo = Mongoconnection()

def excute_file_mapping(input_file_path_n_name, file_schema_id, exclude_id):
    logger.info("excute file mapping....")
    
    rule_type_list = ["field_map","MERGE", "SPLIT"]

    if input_file_path_n_name == None or file_schema_id == None:
        return

    
    # Read the input CSV file into a pandas DataFrame
    input_df = pd.read_csv(input_file_path_n_name)
    unique_id = list(input_df.apply(lambda _: str(uuid.uuid4()), axis=1))    
    # input_df change  in json 
    input_df['unique_id'] = unique_id
    # Convert DataFrame to JSON and save it to a file
    app_level.input_json = input_df.to_dict(orient='records')  

     #create output schema 
    benchmark_fields_df = pd.read_csv('uploads/benchmark_fields.csv')  
    logger.info("read Benchmark field file")
    benchmark_fields_df['unique_id']= ''
    #benchmark_fields_df = {col: None for col in benchmark_fields_df.columns}
    
    # benchmark_fields_df = pd.Series(benchmark_fields_df)
    # get all the column from benchmark_df   
    # benchmark_df.to_json (benchmark_df.columns)   
    app_level.benchmark_fields_json = benchmark_fields_df.to_json()    
    
    
    #create empty output_json an dcopy unique id for each record of input_json
    for r in app_level.input_json:        
        input_record = r         
        base = copy.deepcopy(app_level.benchmark_fields_json)
        base = json_normalize(json.loads(base))
        base['unique_id'] = input_record['unique_id']
        # base = base.to_dict() 
        if app_level.output_json is None:
            app_level.output_json = []
        app_level.output_json.append(base) 
    logger.info("Create Empty output.json")
     
    
    # keys_to_exclude = ['_id', 'file_id', 'MERGE', 'SPLIT']
    # file mapping rule is json object
    errors = []
    error_records = []
    app_level.error_records_csv = pd.DataFrame(columns= input_df.columns)
    
    file_mapping_rules = obj_mongo.get_file_schema_rules(file_schema_id) 
     
    
    if file_mapping_rules != None:
        
        schema_data_list = []

        file_mapping_rules  = sorted(file_mapping_rules, key=lambda k: (int(k['rule_section']), float(k['rule_sequence'])), reverse=False)
        for rule in file_mapping_rules:
            if rule['output_column'] != "" and rule['input_column'] != "":
                schema_data_list.append({'output_column':rule['output_column'], 'input_column':rule['input_column']})
        for input_record, output_record in zip(app_level.input_json, app_level.output_json):
                input_record = {key.upper(): value for key, value in input_record.items()}
                # output_record = {key.upper(): value for key, value in output_record.items()}
                for rule in file_mapping_rules:
                    try:
                        # if rule['output_column'] != "" and rule['input_column'] != "":
                        #     continue
                        if rule['rule_type'] in rule_type_list and rule['is_active'] == True and (rule['output_column'] != "" and rule['input_column'] != ""):
                            execute_rule(input_record, output_record, rule)
                    except Exception as e:
                        print(f"Error executing rule: {e}")
                        logger.error(f"Error in processing input record: {input_record.get('UNIQUE_ID')}")
                        logger.error(f"Error in processing rule:  {rule['rule_key'], rule['rule_type'], rule['input_column']}")
                        logger.error( f"Unexpected error: {str(e)}\n{traceback.format_exc()}")
                        # Log any unexpected errors
                        f"Unexpected error: {str(e)}\n{traceback.format_exc()}"
                        add_error_records(input_record.get('UNIQUE_ID'), input_df)

        app_level.error_records_csv.to_csv("error_record_csv.csv")

        concatenated_df = pd.concat(app_level.output_json, axis=0, ignore_index=True)
        concatenated_df.to_csv("outputs/output.csv", index=False)
        output_file_path = "outputs/output.csv"
        schema_path = 'outputs/schema_test.json'
        
        with open(schema_path, 'w') as json_file:
            json.dump(schema_data_list, json_file, indent=2)
        logger.info("Schema file Created")
    return schema_path, output_file_path
            # cleanUp and Write the data buffer back to file after all rules are exceuted




def execute_rule(input_record, output_record, rule):
    if rule['rule_type'] == "field_map":
        obj_rule_field_map =Rule_field_map()
        obj_rule_field_map.execute_rule(input_record, output_record, rule)
            # print("pp_level.schema_json",app_level.schema_json)
            
            # obj_rule_field_map = None
    elif rule['rule_type'] == "SPLIT" : 
        obj_rule_field_map = Rule_split()
        obj_rule_field_map.execute_rule(input_record, output_record, rule)  
    elif rule['rule_type'] == "MERGE": 
        obj_rule_field_map = Rule_merge()
        obj_rule_field_map.execute_rule(input_record, output_record, rule)  

def add_error_records(unique_id, input_df):
        app_level.error_records_csv.append(input_df[unique_id],ignore_index=True)
        
    

      