import pandas as pd

# Define manual mappings
manual_mappings = {
    'source_columns': ['Agent;MGA', 'Program Name;Admitted'],
    'destination_column': ['MGA', 'Program Name']
}

# Create a DataFrame
config_df = pd.DataFrame(manual_mappings)

# Define the file path
config_file_path = 'config.csv'

# Save the DataFrame to a CSV file
config_df.to_csv(config_file_path, index=False)
