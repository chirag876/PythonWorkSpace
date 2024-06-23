# Dtale: A web-based, interactive interface for data exploration, analysis, and visualisation is offered by the Python package Dtale. It is very helpful for quickly understanding your datasets without having to write much code. Dtale is frequently used in data science and data analysis workflows and may be used with various data types, including pandas DataFrames.

import dtale
import pandas as pd
# df = pd.read_csv('C:\Workspaces\CodeSpaces\Analytics\EDA_Python\Datasets\Salary Data.csv')
d = dtale.show()
d.open_browser()
