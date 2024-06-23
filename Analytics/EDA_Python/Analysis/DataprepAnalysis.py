# Dataprep: DataPrep lets you prepare your data using a single library with a few lines of code. One can use DataPrep to:

# DataPrep.Connector: provides an intuitive, open-source API wrapper that speeds up development by standardizing calls to multiple APIs as a simple workflow. Streamline calls to multiple APIs through one intuitive library. It also supports loading data from databases through SQL queries. With one line of code, you can speed up pandas.read_sql by 10X with 3X less memory usage!

#  DataPrep.EDA: is the fastest and the easiest EDA tool in Python. It allows data scientists to understand a Pandas/Dask DataFrame with a few lines of code in seconds.

#  DataPrep.Clean:  aims to provide a large number of functions with a unified interface for cleaning and standardizing data of various semantic types in a Pandas or Dask DataFrame.

# ----------------------------------------------------------- Dataprep library 
import pandas as pd
# Dataprep library for generating EDA reports
from dataprep.eda import create_report, plot, plot_correlation, plot_missing

# List Available Datasets
from dataprep.datasets import get_dataset_names
get_dataset_names()
# Load Dataset
from dataprep.datasets import load_dataset
df = load_dataset("DatasetName")

# Analyze Dataset
dataset_df = pd.read_csv("DatasetName")
report_df = create_report(dataset_df)
report_df.save("EDA.html")
# report.save(filename='report_01', to='~/Desktop')
report_df.show_browser()

# Get an overview of the dataset using plot
file_path1 = f'C:/Workspaces/CodeSpaces/Analytics/EDA_Python/Salary Data.csv'
dataset_df = pd.read_csv(file_path1)
plot(dataset_df).show_browser()
# Understand a column with plot(df, column name)
plot(dataset_df, 'col1').show_browser()
# Understanding the relationship between two features
plot(dataset_df, 'col1', 'col2').show_browser()


# Get an overview of the correlations with plot_correlation(df)
plot_correlation(dataset_df)
# Get an overview of the correlations with plot_correlation(df)
plot_correlation(dataset_df, "col1")
# Find the columns that are most correlated to column col1 with plot_correlation(df, col1)
plot_correlation(dataset_df, 'Col1', 'Col2')


# Get an overview of the missing values with plot_missing(df)
plot_missing(dataset_df).show_browser()
# Understand the impact of the missing values in column x with plot_missing(df, col1)
plot_missing(dataset_df, 'Col1').show_browser()
# Understand the impact of the missing values in column col1 on column col2 with plot_missing(df, col1, col2)
plot_missing(dataset_df, 'Col1', 'Col2').show_browser()

# --------------------------------------------------------------------- Output customization ---------------------------------------------
# display is a list of names which controls the Tabs, Sections and Sessions you want to show
# Example 1 Choose the Tabs, Sections and Sessions you want
plot(dataset_df, 'Education Level', display=['Stats', 'Bar Chart', 'Pie Chart']).show_browser()
report_df = create_report(dataset_df, display=["Overview","Interactions"]).show_browser()

# 1. Local Parameters:
# These parameters are specific to individual plots, and their names are separated by dots (..).
# The part before the first dot represents the plot name, and the part after the dot is the parameter name.
# For example, in "bar.bars," "bar" is the plot name, and "bars" is the specific parameter for that plot.

# 2. Global Parameters:
# These parameters apply to all plots that have that specific parameter. They are single-word parameters.
# An example is "ngroups." This parameter will have a uniform effect on all plots that support the "ngroups" parameter.

# 3. Interaction between Global and Local Parameters:
# If both global and local parameters are provided, the local parameters for a specific plot will overwrite the global parameter for that plot.
# In simple terms, if a plot has its own specific setting for a parameter (local), it takes precedence over the general setting for that parameter (global).

# config is a dictionary that contains the customizable parameters and designated values.
# Example 2 Customize your plot
plot(dataset_df, 'Age', config={'bar.bars': 10, 'bar.sort_descending': True, 'bar.yscale': 'linear', 'height': 400, 'width': 450, }).show_browser()

# Example 3 customize your insights
plot(dataset_df, config={'insight.missing.threshold':20, 'insight.duplicates.threshold':20}).show_browser()
