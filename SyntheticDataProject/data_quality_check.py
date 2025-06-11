import pandas as pd
import matplotlib.pyplot as plt

# Load real and synthetic data
real = pd.read_csv('flat-training.csv')
synthetic = pd.read_csv('synthetic_data.csv')

# Compare distributions for a few columns
columns_to_check = real.columns[:5]  # Check first 5 columns as an example

for col in columns_to_check:
    plt.figure(figsize=(8, 4))
    plt.hist(real[col], bins=30, alpha=0.5, label='Real', density=True)
    plt.hist(synthetic[col], bins=30, alpha=0.5, label='Synthetic', density=True)
    plt.title(f'Distribution of {col}')
    plt.legend()
    plt.show()