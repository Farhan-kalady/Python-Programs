# Write recursive functions for the following:
# (a) Factorial
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# (b) Fibonacci
def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

# (c) Sum of list
def list_sum(lst):
    return 0 if not lst else lst[0] + list_sum(lst[1:])

# (d) Sum of first N numbers
def sum_n_numbers(n):
    return 0 if n == 0 else n + sum_n_numbers(n - 1)

# (e) Reverse string
def reverse_string(s):
    return s if len(s) <= 1 else reverse_string(s[1:]) + s[0]

# Testing all functions
print("Recursive Functions:")
print(f"Factorial of 5: {factorial(5)}")
print(f"8th Fibonacci: {fibonacci(8)}")
print(f"Sum of [1,2,3,4,5]: {list_sum([1,2,3,4,5])}")
print(f"Sum of first 5 numbers: {sum_n_numbers(5)}")
print(f"Reverse of 'hello': {reverse_string('hello')}")