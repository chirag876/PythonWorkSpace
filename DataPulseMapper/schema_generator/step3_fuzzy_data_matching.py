import pandas as pd
from fuzzywuzzy import fuzz
import app_level as app_level
from logzero import logger
import time

class FuzzyDataMatching:
    def __init__(self) -> None:
        pass


    # Function to match columns by content similarity using fuzzy matching
    def step3_process_fuzzy_get_data_score(self,source_df, benchmark_data, mapped_columns, mapping_scores, matching_scores):
        # Record the start time for performance measurement
        start_time = time.time()

        try:
            # Initialize dictionaries for data scores and set a similarity threshold
            data_scores = {}
            similarity_threshold = 70

            mapping_scores = {key.upper(): value for key, value in mapping_scores.items()}
            matching_scores = {key.upper(): value for key, value in matching_scores.items()}
            
            #Added columns to list for which you do not want to do data scoring
            mapped_values = []
            for mapped_key, mapped_value in mapped_columns.items():
                mapping_score = mapping_scores.get(mapped_value, 0)
                if mapping_score > 50:
                    mapped_values.append(mapped_value.upper())
                matching_score = matching_scores.get(mapped_value, 0)
                if matching_score > 80:
                    mapped_values.append(mapped_value.upper())

            
            # Iterate over source columns in the input DataFrame
            for src_col in source_df.columns:
                src_col_upper = src_col.upper()
                # Check if the source column has not been mapped yet
                if src_col_upper not in mapped_values:
                    # Find the most common non-null value in the source column
                    src_common_value = source_df[src_col].dropna().mode()

                    # Check if a common value exists in the source column
                    if not src_common_value.empty:
                        # Take the first mode value if there are multiple
                        src_common_value = src_common_value[0]
                        
                        # Initialize variables to keep track of the best matching column and score
                        best_match = None
                        best_score = 0

                        # Iterate over destination columns in the output DataFrame
                        for dest_col in benchmark_data.columns:
                            dest_col_upper = dest_col.upper()
                            # Check if the destination column has not been mapped yet
                            if dest_col_upper not in mapped_columns.keys():
                                # Find unique non-null values in the destination column
                                dest_common_values = benchmark_data[dest_col].dropna().unique()

                                # Iterate over unique destination values
                                for dest_value in dest_common_values:
                                    # Calculate the similarity score between source common value and destination value
                                    similarity_score = fuzz.partial_ratio(str(src_common_value), str(dest_value))
                                    #similarity_score = fuzz.WRatio(str(src_common_value), str(dest_value))

                                    # Update the best match and score if the current score is higher
                                    if similarity_score > best_score:
                                        best_score = similarity_score
                                        best_match = dest_col

                        # If the best score is above the similarity threshold, consider it a match
                        if best_score >= similarity_threshold:
                            best_match =best_match.upper()
                            mapped_columns[best_match] = src_col_upper
                            data_scores[src_col_upper] = best_score
                        else:
                            # If no match is found, set the data score to 0
                            data_scores[src_col_upper] = 0

            # Record the end time and print the time taken for the function
            end_time = time.time()
            logger.info(f"Time taken for step3_process_fuzzy_matching_data: {end_time - start_time} seconds")

            # Return the mapped columns and data scores
            return mapped_columns, data_scores

        except Exception as e:
            # Handle exceptions and print an error message
            end_time = time.time()
            logger.error(f"Error in step3_process_fuzzy_matching_data: {e}")
            logger.info(f"Time taken for step3_process_fuzzy_matching_data: {end_time - start_time} seconds")

            # Return empty dictionaries in case of an error
            return {}, {}