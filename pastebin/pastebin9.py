#e Write a lambda function 
# (a) Largest of 2 numbers
max_of_two = lambda a, b: a if a > b else b

# (b) Check divisible by 5
divisible_by_5 = lambda x: x % 5 == 0

# (c) Remove strings with length < 5
filter_long_strings = lambda strings: list(filter(lambda s: len(s) >= 5, strings))

# (d) Increment numbers by percentage
increment_numbers = lambda numbers: list(map(lambda x: x * 1.10 if x > 1000 else x * 1.05, numbers))

# Testing all functions
print("(a) Largest of 10 and 20:", max_of_two(10, 20))
print("(b) Is 25 divisible by 5:", divisible_by_5(25))
print("(c) Filtered strings:", filter_long_strings(["hi", "hello", "a", "world"]))
print("(d) Incremented numbers:", increment_numbers([500, 1200, 800]))