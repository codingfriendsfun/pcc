#10-3. Simpler Code

from pathlib import Path

# deal with "What folder am I working from?"
import os
cwd = os.getcwd()
index = cwd.find("chapter")
if index > 0:
    cwd = cwd[:index]
# else do nothing, assume we're in workspace root

file = Path(f'{cwd}/chapter_10/learning_python.txt')
filedump = file.read_text()

print(filedump)

#10-1

for line in filedump.splitlines():
    print(line)


#10-2

for line in filedump.splitlines():
    print(line.replace('I', 'you'))