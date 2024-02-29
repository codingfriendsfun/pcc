from pathlib import Path

path = Path('./chapter_10/learning_python.txt')

# Print as entire file
print("Print contents of learning_python as an entire file:")
print(path.read_text())

# Print by storing lines as a list and looping through each line.
contents = path.read_text()
# Removed below line per 10-3
# lines = contents.splitlines()
in_python = ''
for line in contents.splitlines():
    in_python += line

print("\nPrint contents by looping through a list:")
print(in_python)
