import pandas as pd

mapping_df = pd.read_excel("D:/snowpark/tesed csv/New folder/Arrowhead_GL_Mapping v1.0.xlsx")

# Step 2: Read the source CSV file
source_df = pd.read_csv("D:/snowpark/tesed csv/New folder/input1.csv", encoding='latin1')

# Step 3: Create a new DataFrame with target column names
new_df = pd.DataFrame(columns=mapping_df['Target'].tolist())

# Step 4: Map the source data to the new DataFrame based on the mapping
for index, row in mapping_df.iterrows():
    target_col = row['Target']
    source_col = row['Source']

    # Check if the source column exists in the source DataFrame
    if source_col in source_df.columns:
        new_df[target_col] = source_df[source_col]

# Step 5: Save the new DataFrame as a CSV file
new_df.to_csv('D:/snowpark/tesed csv/New folder/mapped_data.csv', index=False)