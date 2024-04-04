#10-3. Simpler Code

from pathlib import Path

file = Path('./chapter_10/learning_python.txt')
filedump = file.read_text()

print(filedump)

#10-1

for line in filedump.splitlines():
    print(line)


#10-2

for line in filedump.splitlines():
    print(line.replace('I', 'you'))