# Method 1: Simple and direct
with open('filename.txt', 'r') as file:
    words = file.read().split()
    longest_word = max(words, key=len)

print(f"Longest word: '{longest_word}'")
print(f"Length: {len(longest_word)} characters")