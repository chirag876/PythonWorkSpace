import pandas as pd
import json
import app_level as app_level
import copy
from logzero import logger
import time

class CreateRules:
    def __init__(self) -> None:
        pass

    def create_rules_for_file_schema(self, benchmark_schema_id, source_df, benchmark_schema, mapped_columns, mapping_scores, matching_scores, data_scores):
        start_time = time.time()
        errors = []
        error_records = []
        source_column = source_df.columns
        source_column= list(map(str.upper, source_column))
        columns_df = pd.DataFrame(columns=source_column)
        columns_df.to_csv('error_record_csv.csv', index=False)
        source_df.columns = source_df.columns.str.upper()
        mapping_scores = {key.upper(): value for key, value in mapping_scores.items()}
        matching_scores = {key.upper(): value for key, value in matching_scores.items()}
        data_scores = {key.upper(): value for key, value in data_scores.items()}        
        

        try:
            logger.info("Creating rules for schema file..")
           
            file_schema = copy.deepcopy(app_level.file_schema_template)
            file_schema['benchmark_schema_id'] =  benchmark_schema_id
            file_schema['fields'] = list(source_df.columns)

            for bm_key, bm_values in benchmark_schema.items():
                if bm_key not in mapped_columns:
                    mapped_columns[bm_key] = ""
                
            
            # Append the mapping to the schema data list along with confidence score
            for mp_key, mp_value in mapped_columns.items():
                # Get mapping, matching, and data scores for the source column
                mapping_score = mapping_scores.get(mp_value, 0)
                matching_score = matching_scores.get(mp_value, 0)
                data_score = data_scores.get(mp_value, 0)

                # Check if mapping_score is 100, if so, set confidence score to 100
                if mapping_score == 100:
                    confidence_score = 100
                    matching_score = 0
                    data_score = 0
                else:
                    # Calculate confidence score as the average of matching and data scores
                    if data_score > 70:
                        data_score = 60

                    confidence_score = (matching_score + data_score) / 2
                file_schema['rules'].append({
                    "rule_key": "",
                    "rule_type": "field_map",
                    "output_column": mp_key,
                    "input_column": mp_value,
                    "confidence_score": confidence_score, # avgrage of mapping, matching, data and model score
                    "mapping_score": mapping_score,   #from config score
                    "matching_score": matching_score, #fuzzy column score
                    "data_score": data_score, # data score
                    "model_score": 0, #Ai score
                    "default_value": "",
                    "error_override_with_default_value": True,
                    "rule_section": 1,
                    "rule_sequence": 1,
                    "is_active": True,
                    "description": ""                      
                })

            logger.info("Creating fields in schema file")
            # Convert the Index object to a list before serializing
            file_schema['fields'] = list(file_schema['fields'])

            # Serialize the schema data to JSON
            schema_json = json.dumps(file_schema, indent=4)
            end_time = time.time()
            logger.info(f"Time taken for create_rules_for_file_schema: {end_time - start_time} seconds")
            return schema_json


        except Exception as e:
            end_time = time.time()
            logger.info(f"Error in create_rules_for_file_schema: {e}")
            logger.info(f"Time taken for create_rules_for_file_schema: {end_time - start_time} seconds")
            return {}, {}