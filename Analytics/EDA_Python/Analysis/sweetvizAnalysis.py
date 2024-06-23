# SweetViz: With just two lines of code, this open-source Python library can launch the EDA (Exploratory Data Analysis) procedure and produce stunning, high-density visualisations. The result is an independent HTML application.The system's goal is to swiftly compare datasets and visualise target values. It seeks to facilitate quick analyses of data target properties, training vs. testing, and other related data characterisation activities.

# SweetViz 2.0: Sweetviz's basic OS module, making the reports it produces incompatible with environments built specifically for them, such as Google Colab. Second, because the reports are in HTML format, inline plotting of the graphs is not possible.However, in version 2.0, these problems have been resolved by a new feature called show_notebook() that uses an iframe to embed the visualisations in the notebooks. Additionally, you will be able to store a report in HTML format for later use.

# Another feature included in version 2.0, show_notebook(), places the report inside the notebook environment as opposed to any external environment based on a browser by use of an IFRAME HTML element.

import sweetviz as sw

import pandas as pd

# Generating a sample report using sweetviz
file_path1 = f'C:/Workspaces/CodeSpaces/Analytics/EDA_Python/Salary Data.csv'
dataset_df = pd.read_csv(file_path1)
analyze_report = sw.analyze(dataset_df)
analyze_report.show_html('analyze_updated.html')

# Creating a comparison report using sweetviz 
from sklearn.model_selection import train_test_split
X = dataset_df[['Education Level', 'Years of Experience', 'Job Title', 'Gender']]
# Target variable (y)
y = dataset_df[['Salary']]

# Split the dataset into training and testing sets, 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Generate a comparison report using Sweetviz. This report will compare the training and testing datasets
compare_report = sw.compare([X_train, 'Train'], [X_test, 'Test'])
compare_report.show_html('compare.html', layout='vertical/widescreen', scale=None, open_browser=True)
compare_report.show_notebook(w="100%", h="Full", layout='widescreen/vertical', scale=None)