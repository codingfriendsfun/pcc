# 10-8. Cats and Dogs

from pathlib import Path

# deal with "What folder am I working from?"
import os

cwd = os.getcwd()
index = cwd.find("chapter")
if index > 0:
    cwd = cwd[:index]
# else do nothing, assume we're in workspace root


def readCatFile(catFile="cats.txt", animal="cats"):
    file = Path(f"{cwd}/chapter_10/{catFile}")
    try:
        fileDump = file.read_text()
    except FileNotFoundError:
        print(f"Note: {catFile} does not exist in chapter_10 directory.\n")
        return
    print(f"Printing list of {animal}: ")
    print(f"{fileDump}\n")


def readDogFile(dogFile="dogs.txt", animal="dogs"):
    readCatFile(dogFile, animal)


catFile = input("Enter cat file name, or enter nothing to use default cats.txt: ")
dogFile = input("Enter dog file name, or enter nothing to use default dogs.txt: ")
print()  # output a blank line for readability

if not catFile:
    readCatFile()
else:
    readCatFile(catFile)

if not dogFile:
    readDogFile()
else:
    readDogFile(dogFile)
