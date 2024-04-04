from pathlib import Path

path = Path('text_files/learning_python.txt')

contents = path.read_text()
py_string = ''

for line in contents.splitlines():
    py_string += f"{line} \n"

print(contents)
print("\n")
print(py_string)
