import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Sales data
sales = [10, 12, 14, 15, 18, 19, 21, 23, 25, 28, 35, 50, 100]

# Create a Pandas Series
data_series = pd.Series(sales)

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = data_series.quantile(0.25)  # First quartile
Q3 = data_series.quantile(0.75)  # Third quartile

# Calculate IQR
IQR = Q3 - Q1
factor = 2.5  # Outlier detection factor

# Calculate lower and upper limits
lower_limit = Q1 - IQR * factor
upper_limit = Q3 + IQR * factor

# Create boolean masks for outliers
islower = data_series < lower_limit
isupper = data_series > upper_limit

# Find outliers
outliers = data_series[islower | isupper]

# Print results
print("Number of outliers:", len(outliers))
print("Outliers:", outliers.tolist())


# Box Plots 
#default whisker length alia factor is 1.5 in matplotlib
plt.boxplot(sales, whis=2.5)
plt.show()