# #make a class called mapping
# #all the functions inside the class
# #main should __main__
# import pandas as pd
# from fuzzywuzzy import fuzz, process
# import json

# #------------------------------------------------------------------------------#
# class mapping():
#     def __init__(self, source_path, benchmark_path, output_path, schema_path, config_path):
#         self.source_path = source_path
#         self.benchmark_path = benchmark_path
#         self.output_path = output_path
#         self.schema_path = schema_path
#         self.config_path = config_path
    
# #------------------------------------------------------------------------------#
#     def manage_mapping_from_config(self):
#     # Open and read the JSON configuration file
#         with open(self.config_path, 'r') as file:
#             manual_mappings = json.load(file)
#     # Reverse the mapping to be source_column -> destination_column for ease of access
#         reversed_mappings = {src_col: dest for dest, src_cols in manual_mappings.items() for src_col in src_cols}
#         return reversed_mappings
    
# #------------------------------------------------------------------------------#
#     def manage_matching_column_from_fuzzy(self, source_df, destination_df, mapped_from_config):
#     # Start with manually mapped columns
#         mapping = {src: dest for src, dest in mapped_from_config.items() if src in source_df.columns}
#     # Find the best fuzzy match for each unmapped source column in the destination columns
#         for src_col in source_df.columns:
#             if src_col not in mapping:
#                 best_match, score = process.extractOne(src_col, destination_df.columns, scorer=fuzz.token_sort_ratio)
#             # Accept the match if the score is 80 or higher
#                 if score >= 80:
#                     mapping[src_col] = best_match
#         return mapping
    
# #------------------------------------------------------------------------------#
#     def manage_matching_column_from_data_fuzzy(self, source_df, destination_df, mapped_columns):
#     # Set a similarity threshold for renaming columns
#         similarity_threshold = 70
#     # Iterate over each column in the source DataFrame
#         for src_col in source_df.columns:
#         # Only proceed with source columns that haven't been mapped yet
#             if src_col not in mapped_columns:
#             # Drop null values and check if the source column has any non-null data
#                 if not source_df[src_col].dropna().empty:
#                 # Calculate the mode (most common value) of the source column
#                     src_common_value = source_df[src_col].dropna().mode()
#                 # If the mode calculation returns at least one value, proceed
#                     if not src_common_value.empty:
#                     # Take the first mode value if there are multiple
#                         src_common_value = src_common_value[0]
#                     # Initialize variables to keep track of the best matching column and score
#                         best_match = None
#                         best_score = 0
#                     # Iterate over each column in the destination DataFrame
#                         for dest_col in destination_df.columns:
#                         # Only consider destination columns that haven't been mapped yet
#                             if dest_col not in mapped_columns.values():
#                             # Get unique non-null values from the destination column
#                                 dest_common_values = destination_df[dest_col].dropna().unique()
#                             # Iterate over each unique value in the destination column
#                                 for dest_value in dest_common_values:
#                                 # Calculate the similarity score between the source and destination values
#                                     similarity_score = fuzz.partial_ratio(str(src_common_value), str(dest_value))
#                                 # If this score is the highest so far, update the best match and score
#                                     if similarity_score > best_score:
#                                         best_score = similarity_score
#                                         best_match = dest_col
#                     # If the best score is above the threshold, add the mapping to the mapped_columns dictionary
#                         if best_score >= similarity_threshold:
#                             mapped_columns[src_col] = best_match

#     # Return the updated mapping dictionary
#         return mapped_columns

# #------------------------------------------------------------------------------# 
    
#     def fill_unmapped_columns(self, destination_df, mapped_columns):
#     # Loop through destination columns and fill unmapped columns with defaults
#         for dest_col in destination_df.columns:
#         # Check if the current destination column is not in the mapped columns
#             if dest_col not in mapped_columns.values():
#             # Check the data type of the column
#                 if pd.api.types.is_integer_dtype(destination_df[dest_col]):
#                 # If the column is of integer type, fill NaN values with 0
#                     destination_df[dest_col].fillna(0, inplace=True)
#                 else:
#                 # If the column is of any other type, fill NaN values with 'N/A'
#                     destination_df[dest_col].fillna('N/A', inplace=True)

#  #------------------------------------------------------------------------------#
    
#     def export_data_from_input_to_output(self, source_df, destination_df, mapped_columns):
#         # Fill unmapped columns in the destination dataframe
#         self.fill_unmapped_columns(destination_df, mapped_columns)
#         # Create an empty dataframe with the same index as the source dataframe
#         output_df = pd.DataFrame(index=source_df.index)
#         # List to store schema information for each column
#         schema_data = []
#         # Iterate over columns in the destination dataframe
#         for dest_col in destination_df.columns:
#             # Find the corresponding source column based on the mapped columns
#             src_col = next((k for k, v in mapped_columns.items() if v == dest_col), None)
#             # Check if a source column was found
#             if src_col:
#                 # If source column exists, copy data from source dataframe to output dataframe
#                 output_df[dest_col] = source_df[src_col]
#             else:
#                 # If no source column found, use the data from the destination dataframe
#                 output_df[dest_col] = destination_df[dest_col]
#             # Store schema information for the current column
#             schema_data.append({
#                 'Output Column Name': dest_col,
#                 'Input Column Name': src_col if src_col else 'N/A'
#             })
#         # Create a dataframe with schema information
#         schema_df = pd.DataFrame(schema_data)
#         # Return the output dataframe and schema dataframe
#         return output_df, schema_df
    
# #------------------------------------------------------------------------------#


# def execute_the_functions(self):
#     # Reading data from source and benchmark files using pandas
#     source_df = pd.read_csv(self.source_path, encoding='cp1252')
#     benchmark_df = pd.read_csv(self.benchmark_path, encoding='cp1252')
#     # Managing manual mappings based on configuration
#     manual_mappings = self.manage_mapping_from_config()
#     # Performing initial column matching using fuzzy logic
#     mapped_columns = self.manage_matching_column_from_fuzzy(source_df, benchmark_df, manual_mappings)
#     # Refining column matching further using data-specific fuzzy logic
#     mapped_columns = self.manage_matching_column_from_data_fuzzy(source_df, benchmark_df, mapped_columns)
#     # Exporting data from source to output based on mapped columns
#     output_df, schema_df = self.export_data_from_input_to_output(source_df, benchmark_df, mapped_columns)
#     # Returning the resulting dataframes
#     return output_df, schema_df

# #------------------------------------------------------------------------------#

# # Define the main function with input parameters
# def main(source_path, benchmark_path, output_path, schema_path, config_path):
#     # Call the 'mapping' function with specified parameters and store the result in 'True_mapping'
#     True_mapping = mapping(source_path, benchmark_path, output_path, schema_path, config_path)
#     # Execute the functions inside the 'True_mapping' object and store the DataFrames in 'output_df' and 'schema_df'
#     output_df, schema_df = True_mapping.execute_the_functions()
#     # Save the 'schema_df' DataFrame to a CSV file at the specified 'schema_path' without including the index
#     # For example, you might want to save the DataFrames to files
#     schema_df.to_csv(schema_path, index=False)
#     # Save the 'output_df' DataFrame to a CSV file at the specified 'output_path' without including the index
#     output_df.to_csv(output_path, index=False)

# #------------------------------------------------------------------------------#
# if __name__ == "__main__":
#     # Set your file paths or other configuration parameters here
#     source_path = "C:/Workspaces/CodeSpaces/Python_Work/Bordereau/Main/Documents/data_2__input.csv"
#     benchmark_path = "C:/Workspaces/CodeSpaces/Python_Work/Bordereau/Main/Documents/benchmark.csv"
#     output_path = "C:/Workspaces/CodeSpaces/Python_Work/Bordereau/Main/Documents/data_5_output.csv"
#     schema_path = "C:/Workspaces/CodeSpaces/Python_Work/Bordereau/Main/Documents/data_5_schema.csv"
#     config_path = "C:/Workspaces/CodeSpaces/Python_Work/Bordereau/Main/Documents/config.json"

#     # Call the main function with the specified parameters
#     main(source_path, benchmark_path, output_path, schema_path, config_path)

#make a class called mapping
#all the functions inside the class
#main should __main__
import pandas as pd
from fuzzywuzzy import fuzz, process
import json

#------------------------------------------------------------------------------#
class mapping():
    def __init__(self, source_path, benchmark_path, output_path, schema_path, config_path):
        self.source_path = source_path
        self.benchmark_path = benchmark_path
        self.output_path = output_path
        self.schema_path = schema_path
        self.config_path = config_path
    
#------------------------------------------------------------------------------#
    def manage_mapping_from_config(self):
    # Open and read the JSON configuration file
        with open(self.config_path, 'r') as file:
            manual_mappings = json.load(file)
    # Reverse the mapping to be source_column -> destination_column for ease of access
        reversed_mappings = {src_col: dest for dest, src_cols in manual_mappings.items() for src_col in src_cols}
        return reversed_mappings
    
#------------------------------------------------------------------------------#
    def manage_matching_column_from_fuzzy(self, source_df, destination_df, mapped_from_config):
    # Start with manually mapped columns
        mapping = {src: dest for src, dest in mapped_from_config.items() if src in source_df.columns}
    # Find the best fuzzy match for each unmapped source column in the destination columns
        for src_col in source_df.columns:
            if src_col not in mapping:
                best_match, score = process.extractOne(src_col, destination_df.columns, scorer=fuzz.token_sort_ratio)
            # Accept the match if the score is 80 or higher
                if score >= 80:
                    mapping[src_col] = best_match
        return mapping
    
#------------------------------------------------------------------------------#
    def manage_matching_column_from_data_fuzzy(self, source_df, destination_df, mapped_columns):
    # Set a similarity threshold for renaming columns
        similarity_threshold = 70
    # Iterate over each column in the source DataFrame
        for src_col in source_df.columns:
        # Only proceed with source columns that haven't been mapped yet
            if src_col not in mapped_columns:
            # Drop null values and check if the source column has any non-null data
                if not source_df[src_col].dropna().empty:
                # Calculate the mode (most common value) of the source column
                    src_common_value = source_df[src_col].dropna().mode()
                # If the mode calculation returns at least one value, proceed
                    if not src_common_value.empty:
                    # Take the first mode value if there are multiple
                        src_common_value = src_common_value[0]
                    # Initialize variables to keep track of the best matching column and score
                        best_match = None
                        best_score = 0
                    # Iterate over each column in the destination DataFrame
                        for dest_col in destination_df.columns:
                        # Only consider destination columns that haven't been mapped yet
                            if dest_col not in mapped_columns.values():
                            # Get unique non-null values from the destination column
                                dest_common_values = destination_df[dest_col].dropna().unique()
                            # Iterate over each unique value in the destination column
                                for dest_value in dest_common_values:
                                # Calculate the similarity score between the source and destination values
                                    similarity_score = fuzz.partial_ratio(str(src_common_value), str(dest_value))
                                # If this score is the highest so far, update the best match and score
                                    if similarity_score > best_score:
                                        best_score = similarity_score
                                        best_match = dest_col
                    # If the best score is above the threshold, add the mapping to the mapped_columns dictionary
                        if best_score >= similarity_threshold:
                            mapped_columns[src_col] = best_match

    # Return the updated mapping dictionary
        return mapped_columns

#------------------------------------------------------------------------------#

    def fill_unmapped_columns(self, destination_df, mapped_columns):
    # Loop through destination columns and fill unmapped columns with defaults
        for dest_col in destination_df.columns:
            if dest_col not in mapped_columns.values():
            # Fill integer columns with 0 and other types with 'N/A'
                if pd.api.types.is_integer_dtype(destination_df[dest_col]):
                    destination_df[dest_col].fillna(0, inplace=True)
                else:
                    destination_df[dest_col].fillna('N/A', inplace=True)

 #------------------------------------------------------------------------------#
    
    def export_data_from_input_to_output(self, source_df, destination_df, mapped_columns):
        self.fill_unmapped_columns(destination_df, mapped_columns)

        output_df = pd.DataFrame(index=source_df.index)
        schema_data = []

        for dest_col in destination_df.columns:
            src_col = next((k for k, v in mapped_columns.items() if v == dest_col), None)

            if src_col:
                output_df[dest_col] = source_df[src_col]
            else:
                output_df[dest_col] = destination_df[dest_col]

            schema_data.append({
                'Output Column Name': dest_col,
                'Input Column Name': src_col if src_col else 'N/A'
            })

        schema_df = pd.DataFrame(schema_data)
        return output_df, schema_df
    
#------------------------------------------------------------------------------#

    def execute_the_functions(self):
        source_df = pd.read_csv(self.source_path, encoding='cp1252')
        benchmark_df = pd.read_csv(self.benchmark_path, encoding='cp1252')

        manual_mappings = self.manage_mapping_from_config()
        mapped_columns = self.manage_matching_column_from_fuzzy(source_df, benchmark_df, manual_mappings)
        mapped_columns = self.manage_matching_column_from_data_fuzzy(source_df, benchmark_df, mapped_columns)

        output_df, schema_df = self.export_data_from_input_to_output(source_df, benchmark_df, mapped_columns)
        return output_df, schema_df

#------------------------------------------------------------------------------#
def main(source_path, benchmark_path, output_path, schema_path, config_path):
    True_mapping = mapping(source_path, benchmark_path, output_path, schema_path, config_path)
    output_df, schema_df = True_mapping.execute_the_functions()

    
    # For example, you might want to save the DataFrames to files
    schema_df.to_csv(schema_path, index=False)
    output_df.to_csv(output_path, index=False)

#------------------------------------------------------------------------------#
if __name__ == "__main__":
    # Set your file paths or other configuration parameters here
    # Set your file paths or other configuration parameters here
    source_path = "C:/Workspaces/CodeSpaces/Python_Work/Bordereau/Main/Documents/data_2__input.csv"
    benchmark_path = "C:/Workspaces/CodeSpaces/Python_Work/Bordereau/Main/Documents/benchmark.csv"
    output_path = "C:/Workspaces/CodeSpaces/Python_Work/Bordereau/Main/Documents/data_5_output.csv"
    schema_path = "C:/Workspaces/CodeSpaces/Python_Work/Bordereau/Main/Documents/data_5_schema.csv"
    config_path = "C:/Workspaces/CodeSpaces/Python_Work/Bordereau/Main/Documents/config.json"

    # Call the main function with the specified parameters
    main(source_path, benchmark_path, output_path, schema_path, config_path)
