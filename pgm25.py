# Find the sum of even valued terms in a Fibonacci series

num = int(input("Enter a number:"))
a, b = 0, 1
even_sum = 0

for i in range(num):
    if a % 2 == 0:
        even_sum += a
    a, b = b, a + b

print(f"The sum of even valued terms in the Fibonacci series up to {num} is {even_sum}.")    