# Write a program to perform element-wise trigonometric functions (sin, cos, tan) on an array

import numpy as np

arr = np.array([0, 30, 45, 60])

arr = np.radians(arr)

print("sin values:", np.sin(arr))
print("cos values:", np.cos(arr))
print("tan values:", np.tan(arr))