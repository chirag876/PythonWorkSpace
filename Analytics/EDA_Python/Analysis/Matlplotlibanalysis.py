import pandas as pd
import matplotlib.pyplot as plt 
dataset_df = pd.read_csv('C:\Workspaces\CodeSpaces\Analytics\EDA_Python\Datasets\Salary Data.csv')
# ------------------------------------------------------------------ Creating word cloud for most and least occuring values of each feature
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# Iterate through each column in the dataset
for column in dataset_df.columns:
    # Check if the column contains non-text data
    if dataset_df[column].dtype == 'O':  # 'O' represents object type (usually used for strings)
        # Generate word clouds for most and least occurring words in the column
        wordcloud_most = WordCloud().generate_from_frequencies(dataset_df[column].value_counts())
        wordcloud_least = WordCloud().generate_from_frequencies(dataset_df[column].value_counts(ascending=True))

        # Plotting the word clouds side by side
        plt.figure(figsize=(12, 6))

        # Plot for most occurring words
        plt.subplot(1, 2, 1)
        plt.imshow(wordcloud_most, interpolation='bilinear')
        plt.title(f'Most Occurring Words in {column}')
        plt.axis('off')

        # Plot for least occurring words
        plt.subplot(1, 2, 2)
        plt.imshow(wordcloud_least, interpolation='bilinear')
        plt.title(f'Least Occurring Words in {column}')
        plt.axis('off')

        # Display the plots
        plt.show()
    else:
        # Skip columns that contain non-text data
        print(f"Skipping '{column}' as it contains non-text data.")