import pandas as pd

# Step 1: Load the dataset
# Replace the file path with the actual location of your file
dataset_path = r"wdbc.data"
data = pd.read_csv(dataset_path)
# Basic Statistics for Numerical Columns
print("Basic Statistics of Numerical Columns:")
print(data.describe())  # Computes mean, median, standard deviation, etc.

# Perform Grouping: Replace 'categorical_column' and 'numerical_column' with actual column names
categorical_column = 'category_column'  # Example: 'species', 'region', or 'department'
numerical_column = 'numerical_column'  # Example: 'sales', 'age', or 'income'

# Grouping and Calculating Mean
grouped_mean = data.groupby(categorical_column)[numerical_column].mean()

print(f"\nMean of {numerical_column} for each {categorical_column}:")
print(grouped_mean)

# Identifying Patterns
print("\nInteresting Findings or Patterns:")
for group, value in grouped_mean.items():
    print(f"The average {numerical_column} for {categorical_column} '{group}' is {value:.2f}.")