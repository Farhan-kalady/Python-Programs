# Write a function to get a new string from a given string by adding ‘Is’ to the beginning of the input string. If the given string already begins with ‘Is’, return the input string unchanged.
def add_is_prefix(text):
    return text if text.startswith('Is') else 'Is ' + text

# Example usage
print(add_is_prefix("Hello"))      
print(add_is_prefix("Is Python"))  