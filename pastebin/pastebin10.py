# Write lambda functions, each to find area of square, rectangle and triangle.
area_square = lambda s: s * s
area_rectangle = lambda l, w: l * w
area_triangle = lambda b, h: 0.5 * b * h

# Testing all functions
print("Area Calculations:")
print("Square (5):", area_square(5))
print("Rectangle (4x6):", area_rectangle(4, 6))
print("Triangle (6x4):", area_triangle(6, 4))