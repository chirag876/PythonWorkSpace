# Import necessary libraries and modules
from utils import Model  # Assuming there is a Model class in the utils module
import streamlit as st
import re
import pandas as pd

# Define the target columns for the output
target_columns = ['Attachment Point', 'Broker/Agent', 'Broker/Agent Address', 'Broker/Agent City', 'Broker/Agent State',
                  'CM/Occ Indicator', 'Exposure Type', 'Full policy number', 'Gross Vehicle Weight', 'Insured Address',
                  'Insured City', 'Insured Name', 'Insured State', 'MGA', 'Policy Type', 'Primary/Excess Indicator',
                  'Risk/Location Address', 'Transaction Type', 'Vehicle Make', 'Vehicle Model', 'Vehicle Number',
                  'Vehicle Type']

# Create an empty dictionary with target columns as keys
dict1 = {i: [] for i in target_columns}

# Print the initial state of the dictionary
print("dict1:", dict1)

# Instantiate the Model class from the utils module
model = Model()

# Define a function to check and clean strings
def check_string(input_user):
    # Remove non-alphanumeric characters and convert to lowercase
    str1 = "".join(re.sub("[^a-zA-Z0-9.+,() ]", '', input_user)).lower()
    flag = False
    # Check if the string contains any alphabetic characters
    for i in str1:
        for j in range(97, 123):
            if ord(i) == j:
                flag = True
    if flag:
        return input_user
    else:
        return False

# Set the title of the Streamlit application
st.title("Schema Mapping Classification Model (Naive-Bayes)")

# Display a message about the classification algorithm
st.write("This is an application based on a classification algorithm.")

# Create a file uploader for CSV files
input_csv = st.file_uploader('Upload CSV file')

# Display a success message if a file is uploaded
if input_csv:
    st.success('File uploaded')

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(input_csv, encoding='utf-8', encoding_errors='ignore')
df = df.astype(str)

# Iterate over rows in the DataFrame
for i in range(df.shape[0]):
    # Extract the input array and list for the current row
    input_array = df.iloc[:i + 1, :].values
    input_list = list(input_array[0])

    # Remove 'nan' values from the input list
    new_input_list = [data for data in input_list if data != 'nan']

    # Clean and filter the input list using the check_string function
    input_list = [check_string(i) for i in new_input_list if check_string(i)]

    # If the input list is not empty, make a prediction using the model
    if input_list:
        result = model.prediction(input_list)

        # Update the dictionary with the results
        for key in dict1.keys():
            if key in result:
                value = dict1[key]
                value.append(input_list[result.index(key)])
                dict1[key] = value

# Find the maximum length of lists in dict1
max_len = max(len(value) for value in dict1.values())

# Pad lists with None if necessary to create a DataFrame
for key in dict1.keys():
    dict1[key] += [None] * (max_len - len(dict1[key]))

# Create a DataFrame from the dictionary
df = pd.DataFrame(dict1)

# Define a function to convert the DataFrame to a CSV file
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

# Convert the DataFrame to CSV format
csv = convert_df(df)

# Create a download button for the CSV file
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='output_file.csv',
    mime='text/csv',
)
