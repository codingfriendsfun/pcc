# 10-1. Learning Python

from pathlib import Path

file = Path('./chapter_10/learning_python.txt')
filedump = file.read_text()

print(filedump)

lines = filedump.splitlines()
for line in lines:
    print(line)