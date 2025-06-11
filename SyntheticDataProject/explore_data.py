import pandas as pd

def explore_data(file_path='flat-training.csv'):
    """
    Function to explore a dataset and print key information about it.

    Parameters:
    file_path (str): Path to the CSV file. Default is 'flat-training.csv'.

    Returns:
    pandas.DataFrame: The loaded DataFrame.
    """
    try:
        # Load the training data
        df = pd.read_csv(file_path)
        print(f"\n📂 Successfully loaded dataset from {file_path}")

        # Optional preprocessing: Impute missing values for numeric columns
        # df = df.fillna(df.mean(numeric_only=True))

        # Optional preprocessing: Ensure object columns are treated as strings
        # for col in df.select_dtypes(include=['object']).columns:
        #     df[col] = df[col].astype(str)

        # Show the shape of the data
        print("\n📐 Shape (rows, columns):", df.shape)

        # Show the first few rows
        print("\n👀 First 5 rows of the dataset:")
        print(df.head())

        # Show column types and memory usage
        print("\nℹ️ Column types and memory usage:")
        df.info()

        # Show the first few rows of the 'text' column if it exists
        if 'text' in df.columns:
            print("\n📝 First 5 rows of 'text' column:")
            print(df['text'].head())
        else:
            print("\n⚠️ 'text' column not found in the dataset.")

        # Check missing values
        print("\n🧯 Missing values in each column:")
        print(df.isnull().sum())

        # Describe numeric columns
        print("\n📊 Summary statistics for numeric columns:")
        print(df.describe())

        # Show unique values for first 5 columns (or all if fewer than 5)
        print("\n🔢 Unique values in first 5 columns (up to 5 values shown):")
        for col in df.columns[:5]:
            unique_vals = df[col].unique()[:5]
            print(f"{col} → {unique_vals}")

        # Identify categorical columns based on low unique values (<20)
        categorical_columns = [col for col in df.columns if df[col].nunique() < 20]
        print("\n🧵 Categorical columns (less than 20 unique values):", categorical_columns)

        # Show unique values for categorical columns
        if categorical_columns:
            print("\n🔡 Unique values in categorical columns (up to 5 values shown):")
            for col in categorical_columns:
                unique_vals = df[col].unique()[:5]
                print(f"{col} → {unique_vals}")
        else:
            print("\n⚠️ No categorical columns found (based on <20 unique values).")

        return df

    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print(f"❌ Error: File '{file_path}' is empty or invalid.")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    df = explore_data()