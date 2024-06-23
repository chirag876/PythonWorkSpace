import pandas as pd
import app_level as app_level
from logzero import logger
from database.mongoconnection2 import Mongoconnection
from schema_generator.step1_check_benchmark_schema import CheckBenchmarkSchema
from schema_generator.step2_fuzzy_matching_columns import FuzzyMatchingColumns
from schema_generator.step3_fuzzy_data_matching import FuzzyDataMatching
from schema_generator.step4_ai_model import AiModel
from schema_generator.create_rules import CreateRules


class AiSchemaGenerator:
    def __init__(self) -> None:
        self.obj_mongo = Mongoconnection()
        self.obj_step1 = CheckBenchmarkSchema()
        self.obj_step2 = FuzzyMatchingColumns()
        self.obj_step3 = FuzzyDataMatching()
        self.obj_step4 = AiModel()
        self.obj_create_rule = CreateRules()


    # Main function to orchestrate the mapping and data merging process
    def generate_schema(self,input_file_path, benchmark_schema_id = None): 
        logger.info("generate_schema started")

        if benchmark_schema_id is None:
            return      

        # Setup main config and benchmark
        # Get benchmark_data and benchmark_schema form mongodb
        benchmark_data, benchmark_schema = self.obj_mongo.get_benchmark_schema_and_benchmark_data(benchmark_schema_id) 
        benchmark_schema = benchmark_schema.get('schema')

        # Load the source and benchmark data from the provided CSV files
        source_df = pd.read_csv(input_file_path, encoding='cp1252')
        
        # Step 1: Load manual mappings from the configuration file
        mapped_columns, mapping_scores = self.obj_step1.step1_check_benchmark_schema(source_df, benchmark_schema)
        # Step 2: Perform fuzzy matching on column names
        mapped_columns, matching_scores = self.obj_step2.step2_process_fuzzy_matching_columns(source_df, mapped_columns, benchmark_schema)

        # Step 3: Perform fuzzy matching on column data content
        
        mapped_columns, data_scores = self.obj_step3.step3_process_fuzzy_get_data_score(source_df, benchmark_data, mapped_columns,mapping_scores, matching_scores)
        
        # Step 4: Perform fuzzy matching on column data content
        # model_score = self.obj_step4.step4_process_ai_models(source_df, benchmark_data, mapped_columns)
        
        # Step 5: Perform fuzzy matching on column data content
        # Export the mapped schema to json file
        # Load manual mappings from the configuration file
        schema_df = self.obj_create_rule.create_rules_for_file_schema(benchmark_schema_id, source_df, benchmark_schema, mapped_columns, mapping_scores, matching_scores, data_scores)        

        logger.info("generate_schema completed")
        
        return schema_df