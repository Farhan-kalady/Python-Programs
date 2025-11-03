#List Comprehension:(a) Generate positive list of numbers from a given list of numbers.
numbers = list(map(int, input("Enter a list of numbers (separated by spaces): ").split()))
positive_numbers = [num for num in numbers if num > 0]
print("Positive numbers:", positive_numbers)

# (b) Generate a list with square of numbers from a given list.
squared_numbers = [num**2 for num in positive_numbers]
print("Squared numbers:", squared_numbers)

# (c) Form a list containing vowels from a given word.
word = input("Enter a word: ")
vowels = [char for char in word if char.lower() in 'aeiou'] 
print("Vowels in the word:", vowels)

# (d) Generate a list of numbers by removing even numbers from a given list.
numbers = list(map(int, input("Enter a list of numbers (separated by spaces): ").split()))
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)

# (f) Display leap years from current year to a future year entered by user.
current_year = int(input("Enter the current year: "))
future_year = int(input("Enter a future year: "))
leap_years = [year for year in range(current_year, future_year + 1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
print("Leap years from", current_year, "to", future_year, ":", leap_years)