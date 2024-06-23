import pandas as pd
from fuzzywuzzy import fuzz

def map_and_append_data(source_path, destination_path, output_path):
    # Load the source and destination data
    source_df = pd.read_csv(source_path, encoding='cp1252')
    destination_df = pd.read_csv(destination_path, encoding='cp1252')

    # Automatically mapping columns based on column name similarity
    mapping = {}
    for src_col in source_df.columns:
        max_ratio = 0
        mapped_col = None
        for dest_col in destination_df.columns:
            # Calculate similarity ratio between column names
            ratio = fuzz.token_sort_ratio(src_col, dest_col)
            if ratio > max_ratio:
                max_ratio = ratio
                mapped_col = dest_col
        if max_ratio > 70:  # A threshold to consider the column names as similar
            mapping[src_col] = mapped_col
        else:
            # Display unmapped columns and unique values for manual inspection
            print(f"Unmapped column: {src_col}")
            print("Unique values:")
            print(source_df[src_col].unique())
            user_input = input(f"Enter the destination column name to map to {src_col}, or press enter to skip: ")
            if user_input:
                mapping[src_col] = user_input

    # Apply the mapping and append the data
    mapped_data_df = pd.DataFrame()
    for src_col, dest_col in mapping.items():
        mapped_data_df[dest_col] = source_df[src_col]

    # Fill missing values
    for col in mapped_data_df.columns:
        if pd.api.types.is_numeric_dtype(mapped_data_df[col]):
            mapped_data_df[col].fillna(0, inplace=True)
        else:
            mapped_data_df[col].fillna('N/A', inplace=True)

    # Append the mapped data to the destination dataframe
    destination_df = destination_df.append(mapped_data_df, ignore_index=True)

    # Save the appended data to a new CSV file
    destination_df.to_csv(output_path, index=False, encoding='cp1252')

# You can call this function with the paths of your source and destination CSV files, and an output path:
# map_and_append_data('path_to_source.csv', 'path_to_destination.csv', 'path_to_output.csv')
