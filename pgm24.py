#Check whether a given positive integer is power of 2. Raise exception for negative input.

def is_power_of_two(n):
    if n <= 0:
        raise ValueError("This is not a positive integer.")
    
    return (n & (n - 1)) == 0

try:
    num = int(input("Enter a positive integer: "))
    if is_power_of_two(num):
        print(f"{num} is a power of 2.")
    else:
        print(f"{num} is not a power of 2.")
except ValueError as e:
    print(e)