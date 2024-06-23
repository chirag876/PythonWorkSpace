
from utils import Model
import streamlit as st
import re
import pandas as pd

model = Model()

def check_string(input_user):
  str1 = "".join(re.sub("[^a-zA-Z0-9.+,() ]",'',input_user)).lower()
  # print(str1)
  flag = False
  for i in str1:
    for j in range(97,123):
      if ord(i) == j:
        flag = True
  if flag:
    return input_user
  else:
    return False


st.title("Schema Mapping Classification Model (Naive-Bayes)")

st.write("This is an application which is based on classification algorithm.")


input_csv = st.file_uploader('upload csv file')

if input_csv:
  st.success('file uploaded')

df = pd.read_csv(input_csv,encoding='utf-8',encoding_errors='ignore')

df = df.astype(str)

input_array = df.iloc[:1,:].values

# print("input_array::",input_array)

input_list = list(input_array[0])

# print("input list:",list(input_array[0]))

new_input_list = []
for data in input_list:
  if data == 'nan':
    pass
  else:
    new_input_list.append(data)

# print(new_input_list)


input_list = []

for i in new_input_list:
  
  if check_string(i):
    input_list.append(check_string(i))



print("input_list: ",input_list)


if input_list:

    # print("input:",input)



    result = model.prediction(input_list)

    st.write(list(zip(input_list,result)))