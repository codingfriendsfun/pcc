from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()
text_string = ''
for line in lines:
    text_string += line.lstrip().rstrip()

print(contents)
print(text_string)