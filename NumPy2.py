
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("\n2D Array:")
print(arr)

print("\nSum along axis 0 (columns):", arr.sum(axis=0))
print("Sum along axis 1 (rows):", arr.sum(axis=1))

print("\nCumulative sum along axis 0:")
print(np.cumsum(arr, axis=0))
print("\nCumulative sum along axis 1:")
print(np.cumsum(arr, axis=1))

print("\nMax along axis 0:", arr.max(axis=0))
print("Min along axis 0:", arr.min(axis=0))
print("Max along axis 1:", arr.max(axis=1))
print("Min along axis 1:", arr.min(axis=1))