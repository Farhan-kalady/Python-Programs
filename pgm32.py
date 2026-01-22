#Write a program to generate 1000 random samples from a normal distribution with mean 10 and standard deviation 3, then plot a histogram of these values.

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate 1000 random samples
data = np.random.normal(loc=10, scale=3, size=1000)

# Step 2: Plot histogram
plt.hist(data, bins=10)

# Step 3: Add labels and title
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normal Distribution (Mean=10, Std Dev=3)")

# Step 4: Display the plot
plt.show()
