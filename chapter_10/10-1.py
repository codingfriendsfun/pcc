from pathlib import Path

path = Path('./chapter_10/learning_python.txt')

# Print as entire file
print("Print contents of learning_python as an entire file:")
print(path.read_text())

# Print by storing lines as a list and looping through each line.
contents = path.read_text()
lines = contents.splitlines()
in_python = ''
for line in lines:
    in_python += line

print("\nPrint contents by looping through a list:")
print(in_python)
