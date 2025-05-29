#Script to unify the 2 files of SECOM dataset into a single .csv
import pandas as pd
from pathlib import Path

# Define the dataset folder path (the files are in a subfolder called dataset)
dataset_folder = Path('dataset')

# Define file paths
features_file = dataset_folder / 'secom.data'
labels_file = dataset_folder / 'secom_labels.data'


# Load the features (handles multiple spaces or tabs in the file)
features_df = pd.read_csv(features_file, sep=r'\s+', header=None, engine='python')

# Name the features as feature_0, feature_1, ...
features_df.columns = [f'feature_{i}' for i in range(features_df.shape[1])]

# Load the labels and timestamps
#labels_df = pd.read_csv(labels_file, sep=' ', header=None, names=['label', 'timestamp'])

# Load only the labels (first column) and skip the timestamp
labels_df = pd.read_csv(labels_file, sep=' ', header=None, usecols=[0], names=['label'])


# Basic check: Ensure both files have the same number of rows
if features_df.shape[0] != labels_df.shape[0]:
    raise ValueError(f"Row count mismatch: features have {features_df.shape[0]} rows, labels have {labels_df.shape[0]} rows.")

# Combine features with labels and timestamp
full_df = pd.concat([features_df, labels_df], axis=1)

# Display info and first few rows
print(full_df.info())
print(full_df.head())

# Save to CSV
output_file = dataset_folder / 'SECOM_combined_dataset.csv'
full_df.to_csv(output_file, index=False)
