# 10-2. Learning C

from pathlib import Path
# deal with "What folder am I working from?"
import os
cwd = os.getcwd()
index = cwd.find("chapter")
if index > 0:
    cwd = cwd[:index]
# else do nothing, assume we're in workspace root

file = Path(f'{cwd}/chapter_10/learning_python.txt')
lines = file.read_text().splitlines()

print(lines)

for line in lines:
    print(line.replace('I', 'you'))