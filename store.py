

# Write a Python program to read a file line by line and store it in a list.

file_path = 'your_file.txt'  # Replace with the path to your file

lines = []

with open(file_path, 'r') as file:
    for line in file:
        lines.append(line.strip())  # Remove newline characters

print(lines)
