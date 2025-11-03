#Wrtie a program to (a) determine frequency of alphabets in a word

word = input("Enter a word: ")
freq = {}

for char in word:
    if char.isalpha():  # Check if the character is an alphabet
        char = char.lower()  # Convert to lowercase for uniformity
        if char in freq:
            freq[char] += 1  # Increment count if character already exists
        else:
            freq[char] = 1  # Initialize count if character is encountered for the first time

print("Frequency of alphabets in the word:", freq)

#(b) create a list of first-names. Count the number of names that starts with 'a'.
names = input("Enter a list of names (separated by spaces): ").split()
name_a = [name for name in names if name.lower().startswith('a')]
count = len(name_a)
print(f"Names starting with 'A': {name_a}, Count: {count}")

#(c) each word in a line of text
line = input("Enter a line of text: ")
words = line.split()    # Split the line into words based on whitespace characters
print("Words in the line of text:", words)
