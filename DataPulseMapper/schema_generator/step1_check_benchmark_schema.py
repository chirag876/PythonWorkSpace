import app_level as app_level
from logzero import logger
import time

class CheckBenchmarkSchema:
    def __init__(self) -> None:
       pass

    # Function to load mapping configurations from a JSON file
    def step1_check_benchmark_schema(self,source_df, benchmark_schema):
      # Record the start time for performance measurement
      start_time = time.time()

      try:
        # Initialize dictionaries to store reversed mappings and mapping scores
        mappings = {}
        mapping_scores = {}


        for bm_key, bm_values in benchmark_schema.items():
          bm_key_upper = bm_key.upper()
          bm_values_upper= list(map(str.upper, bm_values))
          for src_col in source_df.columns:
              if src_col.upper() in bm_values_upper:
                mappings[bm_key_upper] = src_col.upper()
                mapping_scores[src_col] = 100  # Score of 100 for manual mappings

        # Record the end time and print the time taken for the function        
        end_time = time.time()
        logger.info(f"Time taken for step1_check_benchmark_schema: {end_time - start_time} seconds")

        # Return the reversed mappings and mapping scores
        return mappings, mapping_scores
      
      except Exception as e:
          # Handle exceptions, print an error message, and return empty dictionaries in case of an error
          end_time = time.time()
          logger.info(f"Error in step1_check_benchmark_schema: {e}")
          logger.info(f"Time taken for step1_check_benchmark_schema: {end_time - start_time} seconds")
          # Return empty dictionaries in case of an error
          return {}, {}