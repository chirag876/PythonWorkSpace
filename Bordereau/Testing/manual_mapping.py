import pandas as pd
from fuzzywuzzy import fuzz, process
import json

# def manage_mapping_from_config(config_path):
#     # Load manual mappings from a CSV file
#     manual_mapping_df = pd.read_csv(config_path, encoding='cp1252')
#     manual_mappings = {}
#     for _, row in manual_mapping_df.iterrows():
#         source_columns = row['source_columns'].split(';')
#         for source_col in source_columns:
#             manual_mappings[source_col.strip()] = row['destination_column'].strip()
#     return manual_mappings

def manage_mapping_from_config(config_path):
    # Load manual mappings from a JSON file
    with open(config_path, 'r') as file:
        manual_mappings = json.load(file)
    # Reverse the mapping for easier use in the script: source -> destination
    reversed_mappings = {src_col: dest for dest, src_cols in manual_mappings.items() for src_col in src_cols}
    #print(reversed_mappings)
    return reversed_mappings

def manage_matching_column_from_fuzzy(source_df, destination_df, mapped_from_config):
    # Apply manual mappings first
    mapping = {src: dest for src, dest in mapped_from_config.items() if src in source_df.columns}

    # Automatic column mapping for unmapped columns
    for src_col in source_df.columns:
        if src_col not in mapping:
            best_match, score = process.extractOne(src_col, destination_df.columns, scorer=fuzz.token_sort_ratio)
            if score >= 80:  # Threshold for a good match
                mapping[src_col] = best_match

    # combine all the mapped columns and return
    # merged_columns = mapping + mapped_from_config
    # return merged_columns       
    return mapping

def manage_matching_column_from_data_fuzzy(source_df, destination_df, mapped_columns):
    similarity_threshold = 70
    for src_col in source_df.columns:
        if src_col not in mapped_columns:
            # Check if there's any non-null data in the source column
            if not source_df[src_col].dropna().empty:
                src_common_value = source_df[src_col].dropna().mode()
                if not src_common_value.empty:
                    src_common_value = src_common_value[0]
                    best_match = None
                    best_score = 0
                    for dest_col in destination_df.columns:
                        if dest_col not in mapped_columns.values():
                            dest_common_values = destination_df[dest_col].dropna().unique()
                            for dest_value in dest_common_values:
                                similarity_score = fuzz.partial_ratio(str(src_common_value), str(dest_value))
                                if similarity_score > best_score:
                                    best_score = similarity_score
                                    best_match = dest_col
                    if best_score >= similarity_threshold:
                        mapped_columns[src_col] = best_match
    return mapped_columns

def fill_unmapped_columns(destination_df, mapped_columns):
    # Filling unmapped columns
    for dest_col in destination_df.columns:
        if dest_col not in mapped_columns.values():
            # Check if the column in destination is of integer type
            if pd.api.types.is_integer_dtype(destination_df[dest_col]):
                destination_df[dest_col].fillna(0, inplace=True)
            else:
                destination_df[dest_col].fillna('N/A', inplace=True)


def export_data_from_input_to_output(source_df, destination_df, mapped_columns):
    fill_unmapped_columns(destination_df, mapped_columns)
    output_df = pd.DataFrame(index=source_df.index)
    schema_data = []

    for src_col, dest_col in mapped_columns.items():
        if dest_col and dest_col in destination_df.columns:
            output_df[dest_col] = source_df[src_col]
            schema_data.append({'Input Column Name': src_col, 'Output Column Name': dest_col})
        else:
            schema_data.append({'Input Column Name': src_col, 'Output Column Name': 'N/A'})

    for dest_col in destination_df.columns:
        if dest_col not in output_df.columns:
            output_df[dest_col] = destination_df[dest_col]

    schema_df = pd.DataFrame(schema_data)
    return output_df, schema_df

def main(source_path, benchmark_path, output_path, schema_path, config_path):
    # Load the CSV files
    source_df = pd.read_csv(source_path, encoding='cp1252')
    benchmark_df = pd.read_csv(benchmark_path, encoding='cp1252')

    manual_mappings = manage_mapping_from_config(config_path)
    mapped_columns = manage_matching_column_from_fuzzy(source_df, benchmark_df, manual_mappings)
    mapped_columns = manage_matching_column_from_data_fuzzy(source_df, benchmark_df, mapped_columns)

    output_df, schema_df = export_data_from_input_to_output(source_df, benchmark_df, mapped_columns)

    schema_df.to_csv(schema_path, index=False)
    output_df.to_csv(output_path, index=False)

    return output_df, schema_df

# Define file paths
source_path = '/content/data_2__input.csv'
benchmark_path = '/content/benchmark.csv'
output_path = '/content/data_2__output.csv'
schema_path = '/content/data_2__schema.csv'
config_path = '/content/config.json'
#config_path = '/content/config.csv'

# Replace the above paths with the actual paths of your files and then run this function in your local environment
output_df = main(source_path, benchmark_path, output_path, schema_path, config_path)