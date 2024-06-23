# ----------------------------------------------------------- Feature Engineering 
import pandas as pd
import numpy as np
file_path = f'C:\Workspaces\CodeSpaces\Analytics\EDA_Python\Salary Data.csv'
dataset_df = pd.read_csv(file_path)
# A. Creating New Feature by combining Columns to Create a New Feature

dataset_df['new_feature'] = dataset_df['your_column'] + dataset_df['new_column']
# Printing the updated dataset
print(dataset_df)

# -----------------------------------------------------------------------------------------------------------------------------------------

# B. Splitting a Feature to Create a New Feature by extracting Information from an Existing Feature

# Using the 'str.split()' method to split the values based on whitespace.
# Extracting the first part of the split and assigning it to a new column.
# Extracting the second part of the split and assigning it to another new column.
# Splitting and creating a new column with the first part of the split
dataset_df['new_feature_part1'] = dataset_df['your_column/new_column'].str.split().str[0]
# Splitting and creating another new column with the second part of the split
dataset_df['new_feature_part2'] = dataset_df['your_column/new_column'].str.split().str[1]
# Printing the updated dataset
print(dataset_df)

# -----------------------------------------------------------------------------------------------------------------------------------------

# C. Using NumPy for Calculations 

# Step 1: Calculate the maximum value in the 'your_column/new_column'
dataset_df['max_value'] = np.max(dataset_df['your_column/new_column'])
# Step 2: Calculate the minimum value in the 'your_column/new_column'
dataset_df['min_value'] = np.min(dataset_df['your_column/new_column'])
# Step 3: Check if values in 'your_column/new_column' are equal to a specific value ('value')
column_filter = dataset_df['your_column/new_column'] == 'value'
# Step 4: Replace 'value' with 1 and other values with 0 in 'your_column/new_column'
dataset_df['binary_column'] = np.where(dataset_df['your_column/new_column'] == 'value', 1, 0)
# Step 5: Create a binary column based on a set of specific values ('value1' and 'value2')
dataset_df['binary_column_set'] = np.where(dataset_df['your_column/new_column'].isin(['value1', 'value2']), 1, 0)
# You can print the updated dataset
print(dataset_df)

# ----------------------------------------------------------------------------------------------------------------------------------------

# D. Handling Missing Values

# Filling with the Most Frequent Value
# Extract the most frequent value in the 'your_column/new_column'
most_frequent_value = dataset_df['your_column/new_column'].mode()[0]
# imputing categorical variable with most frequent value
dataset_df['your_column/new_column'] = dataset_df['your_column/new_column'].fillna(dataset_df['your_column/new_column'].mode()[0])
# Fill missing values with the most frequent value
dataset_df['your_column/new_column'] = dataset_df['your_column/new_column'].fillna(most_frequent_value)
# Imputing Numerical Features
# Impute missing values in 'your_column/new_column' with the mean U=unknown
dataset_df['new_column'] = dataset_df['new_column'].fillna('U')
dataset_df['your_column/new_column'].fillna(dataset_df['your_column/new_column'].mean(), inplace=True)
# Impute missing values in another numerical feature with the median
dataset_df['your_column/new_column'].fillna(dataset_df['your_column/new_column'].median(), inplace=True)
# Alternatively, impute missing values in 'your_column/new_column' with the mean
dataset_df['your_column/new_column'] = dataset_df['your_column/new_column'].fillna(dataset_df['your_column/new_column'].mean())

# -----------------------------------------------------------------------------------------------------------------------------------------

# E. Identifying missing values percentage

# Identify Missing Data and then calculate the sum of missing values for each column, sort in descending order
missing_data = dataset_df.isnull().sum().sort_values(ascending=False)
# Calculate the percentage of missing values for each column
percentage_missing = (missing_data / len(dataset_df)) * 100
# Create a DataFrame to store the missing values and their percentages
missing_info = pd.DataFrame({
    'Missing Values': missing_data,
    'Percentage': percentage_missing
})
print("Missing Data Information:", missing_info)

# Filling with a specific value
specific_value = 3433 # Replace this with the value you want to use
# Fill the missing values in 'Salary 2' column with the specific value
dataset_df['Salary'].fillna(specific_value, inplace=True)
dataset_df.to_csv('S.csv')

# Creating a new column then filling it will a specific value
dataset_df['Filling'] = None
dataset_df['Filling'].fillna('Chirag', inplace=True)  # Fill a specific column
dataset_df.to_csv('filename.csv')

# filling with prev/next value
dataset_df['vehicle'].fillna(method='ffill')
dataset_df['naming'].fillna(method='bfill')

# dropping rows/cols with any missing values
dataset_df.dropna(axis=0) 
dataset_df.dropna(axis=1) 

# dropping the null columns using fixed threshold
threshold = 0.8
dataset = dataset_df[dataset_df.columns[dataset_df.isnull().mean() < threshold]]
print(dataset)


# ------------------------------------------------------------------ Encoding the categorical value
# for working with categorical values we have to convert them into numbers for proper handling
# Label Encoding in Python


