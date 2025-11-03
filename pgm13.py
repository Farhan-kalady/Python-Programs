#Accept a string and return the length of longest word.
#If the result has more than one word, then print "BINGO"
string = input("Enter a string: ")
words = string.split()  # Split the string into words based on whitespace characters
max_length = max(len(word) for word in words)  # Find the length of the longest word
print("Length of the longest word:", max_length)
longest_words = [word for word in words if len(word) == max_length]
print("Longest word(s):", longest_words)
if len(longest_words) > 1:
    print("BINGO")