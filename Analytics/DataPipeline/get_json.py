import pandas as pd
import json

# Read the Excel file
xlsx_file = pd.ExcelFile('stage0Tostage1.xlsx')

# Iterate over each sheet in the Excel file
for sheet_name in xlsx_file.sheet_names:
    # Read the current sheet into a pandas DataFrame
    df = pd.read_excel(xlsx_file, sheet_name,header=None)
    
    df.fillna('', inplace=True)
    df.replace('Nan','', inplace=True)
    #df = df.map(lambda x: x.replace('[0]', '') if isinstance(x, str) else x)
    # Group values by the first column and aggregate them into lists for duplicate keys
    grouped_data = df.groupby(df.columns[0])[df.columns[1]].agg(list).to_dict()

    # Write the dictionary to a JSON file
    with open(f'./{sheet_name}.json', 'w') as json_file:
        json.dump(grouped_data, json_file, indent=4)