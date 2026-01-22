import numpy as np
import matplotlib.pyplot as plt

data = np.array([10, 20, 30])
plt.bar(data, data)
plt.barh(data, data)
plt.pie(data)
plt.show()
