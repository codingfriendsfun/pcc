from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
text_string = ''

for line in contents.splitlines():
    line = line.replace('python', 'C##')
    line = line.replace('snake','dog')
    text_string += line.lstrip().rstrip()

print(contents)
print(text_string)