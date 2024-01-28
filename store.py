

# Write a Python program to read a file line by line and store it in a list.

file_path = 'your_file.txt'  # Replace with the path to your file

# Initialize an empty list to store lines
lines = []

# Read file line by line and store in the list
with open(file_path, 'r') as file:
    for line in file:
        lines.append(line.strip())  # Remove newline characters

# Print the list of lines
print(lines)
