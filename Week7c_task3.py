import matplotlib.pyplot as plt

# Sample data for the examples
import pandas as pd
data = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'sales': [100, 120, 130, 150, 140, 170, 160, 200, 210, 220],
    'species': ['Peace', 'Ikeoluwa', 'Adegbite'] * 3 + ['Peace'],
    'petal_length': [1.5, 4.2, 5.3, 1.3, 4.0, 5.1, 1.6, 4.1, 5.4, 1.8],
    'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.8, 5.2, 5.5, 5.3]
})

# 1. Line Chart: Trends Over Time
plt.figure(figsize=(8, 5))
plt.plot(data['date'], data['sales'], marker='o', linestyle='-', color='blue')
plt.title('Sales Trend Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.grid(True)
plt.show()

# 2. Bar Chart: Comparison Across Categories
category_means = data.groupby('species')['petal_length'].mean()
plt.figure(figsize=(8, 5))
plt.bar(category_means.index, category_means.values, color=['skyblue', 'orange', 'green'])
plt.title('Average Petal Length Per Species', fontsize=16)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Average Petal Length', fontsize=12)
plt.grid(axis='y')
plt.show()

# 3. Histogram: Distribution of a Numerical Column
plt.figure(figsize=(8, 5))
plt.hist(data['sepal_length'], bins=5, color='purple', edgecolor='black')
plt.title('Distribution of Sepal Length', fontsize=16)
plt.xlabel('Sepal Length', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True)
plt.show()

# 4. Scatter Plot: Relationship Between Two Numerical Columns
plt.figure(figsize=(8, 5))
for species in data['species'].unique():
    subset = data[data['species'] == species]
    plt.scatter(subset['sepal_length'], subset['petal_length'], label=species, s=50)

plt.title('Sepal Length vs Petal Length', fontsize=16)
plt.xlabel('Sepal Length', fontsize=12)
plt.ylabel('Petal Length', fontsize=12)
plt.legend(title='Species')
plt.grid(True)
plt.show()
