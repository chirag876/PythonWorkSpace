# import pandas as pd

# def get_top_rows_with_max_non_empty_cells(excel_file, top_n=5):
#     # Read the Excel file into a pandas DataFrame
#     df = pd.read_excel(excel_file)

#     # Exclude the header and count the non-empty and empty cells in each row
#     df['non_empty_count'] = df.apply(lambda row: row.count(), axis=1)
#     df['empty_count'] = df.apply(lambda row: row.isna().sum(), axis=1)

#     # Find the top rows with the maximum number of non-empty cells
#     top_rows = df.nlargest(top_n, 'non_empty_count')

#     return top_rows.index, top_rows['non_empty_count'], top_rows['empty_count']

# # Example usage with your specific file path and top 5 rows: excel_file_path =
# 'C:/Workspaces/CodeSpaces/CSV/BDX_Data_Input_Files/main_benchmark.xlsx' top_result_indices,
# top_result_non_empty_count, top_result_empty_count = get_top_rows_with_max_non_empty_cells(excel_file_path)

# # Display the result in the specified format for the top 5 rows for index, non_empty_count, empty_count in zip(
# top_result_indices, top_result_non_empty_count, top_result_empty_count): print(f"Row {index} has data in {
# non_empty_count} non-empty columns and {empty_count} empty columns.")

import pandas as pd


def get_top_rows_with_max_non_empty_cells(excel_file, top_n=5):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)

    # Exclude the header and count the non-empty and empty cells in each row
    df['non_empty_count'] = df.apply(lambda row: row.count(), axis=1)
    df['empty_count'] = df.apply(lambda row: row.isna().sum(), axis=1)

    # Find the top rows with the maximum number of non-empty cells
    top_rows = df.nlargest(top_n, 'non_empty_count')

    # Drop additional columns from the result
    columns_to_drop = ['non_empty_count', 'empty_count']
    top_rows = top_rows.drop(columns=columns_to_drop)

    return top_rows


# Example usage with your specific file path and top 5 rows:
excel_file_path = 'C:/Workspaces/CodeSpaces/CSV/BDX_Data_Input_Files/main_benchmark.xlsx'
top_result_rows = get_top_rows_with_max_non_empty_cells(excel_file_path)

# Display the result in the specified format for the top rows
print(top_result_rows)
