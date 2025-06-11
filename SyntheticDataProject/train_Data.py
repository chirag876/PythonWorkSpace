from explore_data import explore_data
from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer
import pandas as pd
import os

def train_sdv_model(df, metadata_file='metadata.json', model_file='ctgan_model.pkl'):
    """
    Function to train a CTGAN model using the provided DataFrame and save metadata/model.

    Parameters:
    df (pandas.DataFrame): The input DataFrame to train the model on.
    metadata_file (str): Path to save the metadata JSON file.
    model_file (str): Path to save the trained CTGAN model.

    Returns:
    CTGANSynthesizer: The trained CTGAN model, or None if training fails.
    """
    if df is None:
        print("❌ Error: No DataFrame provided. Cannot train model.")
        return None

    try:
        # Preprocess: Impute missing values for numeric columns
        df = df.fillna(df.mean(numeric_only=True))

        # Preprocess: Ensure object columns are treated as strings
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str)

        # Initialize metadata for a single-table dataset
        metadata = SingleTableMetadata()
        metadata.detect_from_dataframe(data=df)
        print("\n📋 Metadata detected successfully:")
        print(metadata)

        # Validate metadata
        metadata.validate()
        print("\n✅ Metadata validated successfully.")

        # Save metadata to JSON file
        metadata.save_to_json(metadata_file)
        print(f"\n💾 Metadata saved to {metadata_file}")

        # Initialize and train the CTGAN model
        model = CTGANSynthesizer(metadata=metadata, epochs=10, verbose=True)
        model.fit(df)
        print("\n✅ Model training complete.")

        # Save the trained model
        model.save(model_file)
        print(f"\n💾 Model saved to {model_file}")

        # Generate a small sample of synthetic data for verification
        synthetic_data = model.sample(num_rows=len(df))
        print("\n📈 Sample of synthetic data (len(df)):")
        print(synthetic_data.head())

        # Save synthetic data to CSV
        synthetic_data.to_csv('synthetic_data.csv', index=False)
        print("\n💾 Synthetic data saved to synthetic_data.csv")

        return model

    except Exception as e:
        print(f"❌ Error during SDV processing: {str(e)}")
        return None

# Main execution
if __name__ == "__main__":
    # Load and explore the dataset
    df = explore_data('flat-training.csv')

    # Train the SDV model and save metadata/model
    model = train_sdv_model(df, metadata_file='metadata.json', model_file='ctgan_model.pkl')