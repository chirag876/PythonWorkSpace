# ------------------------------------------------------------------ Autoviz  
# AutoViz for automatic visualization of the dataset
from autoviz.AutoViz_Class import AutoViz_Class
import pandas as pd
file_path = 'Salary Data.csv'
df = pd.read_csv(file_path)

# Initialize the AutoViz class
AV = AutoViz_Class()

# Visualize the dataset without a specific target variable
AV.AutoViz(
    filename=file_path,
    sep=',',
    depVar='',  # Leave this empty for exploratory data analysis without a target variable
    dfte=df,
    header=0,
    verbose=2,
    lowess=False,
    chart_format='png',
    max_rows_analyzed=150000,
    max_cols_analyzed=30,
)