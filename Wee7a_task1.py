import pandas as pd

# Step 1: Load the dataset
# Replace the file path with the actual location of your file
dataset_path = r"todays_data.csv"
data = pd.read_csv(dataset_path)

# Step 2: Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Step 3: Explore the dataset's structure
print("\nDataset Information:")
print(data.info())

print("\nChecking for Missing Values:")
print(data.isnull().sum())

# Step 4: Clean the dataset
# Fill missing values (if any) with 0 (or an appropriate value based on context)
data_filled = data.fillna(0)