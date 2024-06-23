import pandas as pd
from fuzzywuzzy import fuzz

def read_csv(file_path):
    return pd.read_csv(file_path, encoding='latin1')

def find_best_name_match(orig_col, new_data, similarity_threshold=70):
    best_match = None
    best_score = 0

    for new_col in new_data.columns:
        if orig_col == new_col:  
            best_match = new_col
            best_score = 100  
            break  

        max_similarity_score = 0

        for new_row, orig_row in zip(new_data[new_col].dropna(), existing_data[orig_col].dropna()):
            similarity_score = fuzz.ratio(str(new_row), str(orig_row))

            if similarity_score > max_similarity_score:
                max_similarity_score = similarity_score

        if max_similarity_score > best_score:
            best_score = max_similarity_score
            best_match = new_col

    return best_match if best_score >= similarity_threshold else None

def automate_column_mapping(existing_data, new_data, similarity_threshold=70):
    column_mapping = {}

    for orig_col in existing_data.columns:
        best_match = find_best_name_match(orig_col, new_data, similarity_threshold)
        column_mapping[orig_col] = best_match if best_match else "N/A"

    return column_mapping

def create_updated_data(existing_data, new_data, column_mapping):
    updated_data = pd.DataFrame()

    for orig_col, new_col in column_mapping.items():
        if new_col != "N/A":
            updated_data[orig_col] = new_data[new_col]
        else:
            updated_data[orig_col] = "N/A"

    return updated_data

def save_updated_data(updated_data, output_file_path):
    updated_data.to_csv(output_file_path, index=False)

def create_schema_data(column_mapping):
    schema_data = []

    for orig_col, new_col in column_mapping.items():
        schema_data.append({
            'output column name': orig_col,
            'input column name': new_col if new_col != "N/A" else 'N/A'
        })

    return pd.DataFrame(schema_data)

def save_schema_data(schema_df, schema_file_path):
    schema_df.to_csv(schema_file_path, index=False)

if __name__ == "__main__":
    existing_data = read_csv('D:/snowpark/tesed csv/New folder/benchmark.csv')
    new_data = read_csv("D:/snowpark/tesed csv/New folder/Aditya/Aditya/data_2__input.csv")

    similarity_threshold = 70

    column_mapping = automate_column_mapping(existing_data, new_data, similarity_threshold)
    updated_data = create_updated_data(existing_data, new_data, column_mapping)

    save_updated_data(updated_data, 'D:/snowpark/tesed csv/New folder/data_2__output.csv')

    schema_df = create_schema_data(column_mapping)
    save_schema_data(schema_df, 'D:/snowpark/tesed csv/New folder/data_2__schema.csv')