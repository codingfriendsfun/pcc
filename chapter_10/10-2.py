# 10-2. Learning C

from pathlib import Path

file = Path('./chapter_10/learning_python.txt')
lines = file.read_text().splitlines()

print(lines)

for line in lines:
    print(line.replace('I', 'you'))