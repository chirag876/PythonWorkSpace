import pandas as pd

# Load the Excel file
excel_file_path = 'C:\Workspaces\CodeSpaces\ChatGpt_AzureAI\Sample\InspectionResponse_VYRD FNOL Inspection_638257809345214699 1.xls'
xls = pd.ExcelFile(excel_file_path)

# Create a list to store DataFrames from each sheet
dfs = []

# Loop through each sheet and append data to the list
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name)
    dfs.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
combined_data = pd.concat(dfs, ignore_index=True)

# Save the combined data to a new Excel file in XLSX format using openpyxl engine
output_excel_file = 'C:\Workspaces\CodeSpaces\ChatGpt_AzureAI\Sample\data_merge.xlsx'
combined_data.to_excel(output_excel_file, index=False, engine='openpyxl')

print("Sheets combined and saved to", output_excel_file)
