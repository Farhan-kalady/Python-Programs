import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the function to minimize
def f(x):
    return x**2 + 10*np.sin(x)

# Initial guess
x0 = 2

# Perform optimization
result = minimize(f, x0)

# Extract minimum point
x_min = result.x[0]
y_min = result.fun

# Generate values for plotting
x = np.linspace(-10, 10, 400)
y = f(x)

# Plot the function
plt.plot(x, y, label="f(x) = x² + 10sin(x)")

# Plot initial point
plt.scatter(x0, f(x0), color="red", label="Initial Point")

# Plot minimum point
plt.scatter(x_min, y_min, color="green", label="Minimum Point")

# Labels and legend
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Numerical Optimization using SciPy")
plt.legend()
plt.grid(True)

plt.show()
