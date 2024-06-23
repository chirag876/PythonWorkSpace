# ------------------------------------------------------------------ Importing Libraries 

# Pandas for data manipulation and analysis
import pandas as pd

# NumPy for numerical operations
import numpy as np

# CSV and JSON for handling data in these formats
import csv
import json

# To ignore unnecessary warnings during execution
import warnings
warnings.filterwarnings('ignore')

# ------------------------------------------------------------------  Basic EDA 

file_path = f'C:\Workspaces\CodeSpaces\Analytics\EDA_Python\Salary Data.csv'
dataset_df = pd.read_csv(file_path)

# displaying top 5 data from the dataset
dataset_df.head()

# displaying last 5 data from the dataset
dataset_df.tail()

# understanding the data type and information about data, including the number of records in each column, data having null or not null, Data type, the memory usage of the dataset
dataset_df.info()

# Generating descriptive statistics of a DataFrame, such as mean, standard deviation, minimum, and maximum values
dataset_df.describe()

# The argument 'include='all'' indicates that statistics for all types of columns, including object types, should be computed.
# This includes count, mean, std (standard deviation), min, 25%, 50%, 75%, and max.
# The '.T' transposes the result, swapping rows and columns.    
dataset_df.describe(include='all').T

# to get the number of missing records in each column
dataset_df.isna().sum()

# Counting the number of unique values in each column of the DataFrame
dataset_df.nunique()

# checking unique values for a specific feature/column
dataset_df['vehicle'].unique()

# How many entries we have for each Feature and they are shown in descending order (higest value first)
dataset_df["Feature/Column"].value_counts().sort_values(ascending = False)

# Check the data types of each column
data_types = dataset_df.dtypes

# The aggregate function calculates the mean, standard deviation, count, maximum, and minimum for each column
agre = dataset_df.aggregate(['mean', 'std', 'count', 'max', 'min'])

# Calculate the percentage of missing values in each column
percentage_missing = (dataset_df.isna().sum() / len(dataset_df)) * 100

# ------------------------------------------------------------------ Dropping Unnecessary Columns - 1 

# Extracting column names
columns_to_drop = dataset_df.columns

# Dropping the unnecessary columns from the dataset
cleaned_data = dataset_df.drop(columns=columns_to_drop, axis=1)

# Removing duplicates rows based on specified columns
cleaned_data = dataset_df.drop_duplicates(subset=columns_to_drop)

# Alternatively, you can use the following:
# cleaned_data = dataset_df.drop(columns=columns_to_drop, axis=1, inplace=True)


# ------------------------------------------------------------------ Dropping Unnecessary Columns - 2

# Null Column Removal with Threshold
# Calculate Null Percentage
null_percentage = (dataset_df.isnull().sum() / len(dataset_df)) * 100

# Set Threshold (let's say 30%)
threshold = 30

# Identify Columns Exceeding Threshold
columns_to_remove = null_percentage[null_percentage > threshold].index.tolist()

# Remove Null Columns
df_cleaned = dataset_df.drop(columns=columns_to_remove, axis=1)

# Display the cleaned DataFrame
print(df_cleaned)

# ------------------------------------------------------------------ Separating Numerical and Categorical Variables

# Using the 'select_dtypes' function to identify and select columns of specific data types
# Here, selecting columns of type 'object', which typically represent categorical variables.
cat_cols = dataset_df.select_dtypes(include=['object']).columns

# Using 'select_dtypes' again, but this time with 'np.number' as the argument
# This selects columns of numeric types, including integers and floats.
# The result is converted to a Python list for easier handling.
num_cols = dataset_df.select_dtypes(include=np.number).columns.tolist()

# Printing the list of categorical variables extracted in the previous step
print("Categorical Variables:")
print(cat_cols)

# Printing the list of numerical variables extracted in the previous step
print("Numerical Variables:")
print(num_cols)













