# 10-5. Guest Book

from pathlib import Path

# deal with "What folder am I working from?"
import os
cwd = os.getcwd()
index = cwd.find("chapter")
if index > 0:
    cwd = cwd[:index]
# else do nothing, assume we're in workspace root

path = Path(f'{cwd}scratch_files/guest_book.txt')

guests = ""
name = input("\nQ to quit. Else, enter name of guest: ")

while name != "Q":
    guests += f"{name}\n"
    name = input("\nQ to quit. Else, enter name of guest: ")

path.write_text(guests[:-1]) # -1 to remove the last \n