
import numpy as np
import matplotlib.pyplot as plt

# Sample data using NumPy ndarray
data = np.array([25, 15, 30, 10, 20])
labels = np.array(["A", "B", "C", "D", "E"])

# 1. Bar Chart
plt.figure()
plt.bar(labels, data)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# 2. Horizontal Bar Chart
plt.figure()
plt.barh(labels, data)
plt.title("Horizontal Bar Chart")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()

# 3. Pie Chart
plt.figure()
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
