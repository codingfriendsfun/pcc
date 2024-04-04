from pathlib import Path

path = Path('text_files/learning_python.txt')

contents = path.read_text()
lines = contents.splitlines()
py_string = ''

for line in lines:
    py_string += f"{line} \n"

print(contents)
print("\n")
print(lines)
print("\n")
print(py_string)
