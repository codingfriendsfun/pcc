from pathlib import Path

path = Path('./chapter_10/learning_python.txt')
learning = path.read_text()

lines = learning.splitlines()
in_python = ''
for line in lines:
    line = line.replace('Python', 'Godot')
    in_python += line

print(in_python)