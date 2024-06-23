from utils import Model
import streamlit as st
import re
import pandas as pd

target_columns = ['Attachment Point', 'Broker/Agent', 'Broker/Agent Address', 'Broker/Agent City', 'Broker/Agent State', 'CM/Occ Indicator', 'Exposure Type', 'Full policy number', 'Gross Vehicle Weight', 'Insured Address', 'Insured City', 'Insured Name', 'Insured State', 'MGA', 'Policy Type', 'Primary/Excess Indicator', 'Risk/Location Address', 'Transaction Type', 'Vehicle Make', 'Vehicle Model', 'Vehicle Number', 'Vehicle Type']

dict1 = {i: [] for i in target_columns}

print("dict1:", dict1)

model = Model()

def check_string(input_user):
    str1 = "".join(re.sub("[^a-zA-Z0-9.+,() ]", '', input_user)).lower()
    flag = False
    for i in str1:
        for j in range(97, 123):
            if ord(i) == j:
                flag = True
    if flag:
        return input_user
    else:
        return False

st.title("Schema Mapping Classification Model (Naive-Bayes)")

st.write("This is an application based on a classification algorithm.")

input_csv = st.file_uploader('Upload CSV file')

if input_csv:
    st.success('File uploaded')

    df = pd.read_csv(input_csv, encoding='utf-8', encoding_errors='ignore')
    df = df.astype(str)

    for i in range(df.shape[0]):
        input_array = df.iloc[:i + 1, :].values
        input_list = list(input_array[0])

        new_input_list = [data for data in input_list if data != 'nan']

        input_list = [check_string(i) for i in new_input_list if check_string(i)]

        if input_list:
            result = model.prediction(input_list)

            for key in dict1.keys():
                if key in result:
                    value = dict1[key]
                    value.append(input_list[result.index(key)])
                    dict1[key] = value

    # Find the maximum length of lists in dict1
    max_len = max(len(value) for value in dict1.values())

    # Pad lists with None if necessary
    for key in dict1.keys():
        dict1[key] += [None] * (max_len - len(dict1[key]))

    # Create a DataFrame with selected columns
    selected_columns = st.multiselect('Select columns to include in the output file', target_columns, default=target_columns)
    selected_df = pd.DataFrame({key: dict1[key] for key in selected_columns})

    # Display the DataFrame
    st.write(selected_df)

    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(selected_df)

    # Download button
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='output_file.csv',
        mime='text/csv',
    )


