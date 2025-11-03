# Method 1: Simple and direct
with open('filename.txt', 'r') as file:
    lines = file.readlines()
    longest_line = max(lines, key=len)
    
print(f"Longest line: {longest_line.strip()}")
print(f"Length: {len(longest_line)} characters")