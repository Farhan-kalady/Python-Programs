
with open('filename.txt', 'r') as file:
    line_count = len(file.readlines())
print(f"Number of lines: {line_count}")