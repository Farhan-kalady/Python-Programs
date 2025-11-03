#Write a program that count the number of strings where string length is 2 or more and the first and last characters are same.
# Method 1: Using list of strings
def count_special_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

# Example usage
words = ["hello", "ana", "a", "world", "noon", "python", "racecar", "test"]
result = count_special_strings(words)
print(f"Count: {result}")