import pandas as pd
from fuzzywuzzy import fuzz, process

def map_columns_by_name(source_df, destination_df):
    # Automatic column mapping based on column name similarity
    mapping = {}
    for src_col in source_df.columns:
        # Use extractOne to find the best match above a score threshold
        best_match, score = process.extractOne(src_col, destination_df.columns, scorer=fuzz.token_sort_ratio)
        if score >= 80:  # Threshold for a good match
            mapping[src_col] = best_match
    return mapping

def map_columns_by_data(source_df, destination_df, mapped_columns):
    # Additional mapping based on data similarity
    # For unmapped columns, we check if the most common value in the source
    # column appears in the destination column
    unmapped_source_columns = [col for col in source_df.columns if col not in mapped_columns]
    unmapped_destination_columns = [col for col in destination_df.columns if col not in mapped_columns.values()]

    for src_col in unmapped_source_columns:
        # Ignore empty source columns
        if source_df[src_col].dropna().empty:
            continue
        
        # Get the most common value in the source column
        most_common_value = source_df[src_col].value_counts().idxmax()

        # Check for the presence of this common value in each unmapped destination column
        for dest_col in unmapped_destination_columns:
            # If the value is found in the destination column, we consider it a match
            if most_common_value in destination_df[dest_col].values:
                mapped_columns[src_col] = dest_col
                unmapped_destination_columns.remove(dest_col)  # Remove the matched column from further consideration
                break  # Move on to the next source column once a match is found

    return mapped_columns


def fill_unmapped_columns(destination_df, source_df, mapped_columns):
    # Filling unmapped columns
    for col in destination_df.columns:
        if col not in mapped_columns.values():
            # Check if the column in destination is of integer type
            if pd.api.types.is_integer_dtype(destination_df[col]):
                destination_df[col].fillna(0, inplace=True)
            else:
                destination_df[col].fillna('N/A', inplace=True)

def generate_schema_file(source_df, output_df, mapped_columns):
    schema_df = pd.DataFrame({
        'Input Column Names': source_df.columns,
        'Output Column Names': [mapped_columns.get(col, 'N/A') for col in source_df.columns]
    })

    # Apply conditional formatting to highlight mismatches in Excel
    # TODO: This part cannot be done directly in pandas. You would need a library like openpyxl to create Excel files with formatting

    return schema_df

def map_and_merge_data(source_path, benchmark_path, output_path, schema_path):
    # Load the CSV files
    source_df = pd.read_csv(source_path)
    benchmark_df = pd.read_csv(benchmark_path)

    # Map the columns
    mapped_columns = map_columns_by_name(source_df, benchmark_df)
    map_columns_by_data(source_df, benchmark_df, mapped_columns)

    # Combine the dataframes based on the mapping
    for src_col, dest_col in mapped_columns.items():
        benchmark_df[dest_col] = source_df[src_col]

    fill_unmapped_columns(benchmark_df, source_df, mapped_columns)

    # Save the output CSV
    benchmark_df.to_csv(output_path, index=False)

    # Generate and save the schema CSV
    schema_df = generate_schema_file(source_df, benchmark_df, mapped_columns)
    schema_df.to_csv(schema_path, index=False)

# Define file paths
source_path = 'path_to_input_file.csv'
benchmark_path = 'path_to_benchmark_file.csv'
output_path = 'path_to_output_file.csv'
schema_path = 'path_to_schema_file.csv'

# Execute the function
map_and_merge_data(source_path, benchmark_path, output_path, schema_path)
