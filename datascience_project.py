# Data Science Project
# Author: Léo

# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data.csv')

# Exploratory data analysis
print("First 5 rows of the dataset:")
print(data.head())

# Data visualization
plt.plot(data['X'], data['Y'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Data Visualization')
plt.show()
