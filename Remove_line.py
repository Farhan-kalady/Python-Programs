# Remove line at specific position (0-based index)
def remove_line(filename, line_number):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    if 0 <= line_number < len(lines):
        lines.pop(line_number)
        
        with open(filename, 'w') as file:
            file.writelines(lines)
        print(f"Line {line_number} removed successfully!")
    else:
        print("Invalid line number!")

# Usage example
remove_line('filename.txt', 1)  # Removes the 3rd line (index 2)