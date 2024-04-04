# 10-4. Guest

from pathlib import Path

# deal with "What folder am I working from?"
import os
cwd = os.getcwd()
index = cwd.find("chapter")
if index > 0:
    cwd = cwd[:index]
# else do nothing, assume we're in workspace root

path = Path(f'{cwd}scratch_files/guest.txt')
name = input("\nName of guest: ")
path.write_text(name)