from fuzzywuzzy import process
import app_level as app_level
from logzero import logger
import time


class FuzzyMatchingColumns:
    def __init__(self) -> None:
        pass

# Function to match column names using fuzzy matching
    def step2_process_fuzzy_matching_columns(self, source_df, mapped_columns, benchmark_schema):
        # Record the start time for performance measurement
        start_time = time.time()

        try:
            logger.info("column matching start...")

            # Initialize dictionaries to store mappings and matching scores
            # mapping = {src: dest for src, dest in mapped_columns.items() if src in source_df.columns}
           
            matching_scores = {}
            mapped_values = []
            for mapped_key, mapped_value in mapped_columns.items():
                mapped_values.append(mapped_value.upper())
            
            for bm_key, bm_values in benchmark_schema.items():
                if bm_key in mapped_columns: 
                    continue
                bm_key_upper = bm_key.upper()
                bm_values_upper= list(map(str.upper, bm_values))
                for src_col in source_df.columns:
                    if src_col.upper() in mapped_values:     
                            continue        
                              
                    src_col_upper = src_col.upper()

                    # Use fuzzy matching to find the best match among potential source columns
                    scores = process.extract(src_col_upper, benchmark_schema)

                    # Check if scores is not empty before finding the maximum score
                    if scores:
                        best_match, best_score,best_key = max(scores, key=lambda x: x[1])

                        # Check if the best score is above the threshold (80)
                        if best_score >= 80:
                            # Map the source column to the destination column
                            best_key = best_key.upper()
                            mapped_columns[best_key] = src_col_upper
                            matching_scores[src_col_upper] = best_score
                            mapped_values.append(src_col_upper)
                            # Uncomment the following line if you want to print the matched columns and scores
                            # print(f"Matched {src_col_upper} to {dest_col.upper()} with score {best_score}")
                            break  # Break the loop if a match is found
                    else:
                        # If scores is empty, set default values
                        best_match, best_score = None, 0
                        matching_scores[src_col_upper] = 0                       

            end_time = time.time()
            logger.info(f"Time taken for step2_process_fuzzy_matching_columns: {end_time - start_time} seconds")
            return mapped_columns, matching_scores

        except Exception as e:
            # Handle exceptions and log the error
            logger.error(f"Error in step2_process_fuzzy_matching_columns: {str(e)}")
            raise e  # Re-raise the exception if needed