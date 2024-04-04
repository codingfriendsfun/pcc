# 10-8. Cats and Dogs

# deal with "What folder am I working from?"
import os
from pathlib import Path

cwd = os.getcwd()
index = cwd.find("chapter")
if index > 0:
    cwd = cwd[:index]
# else do nothing, assume we're in workspace root


def readCatFile(catFile="cats.txt", animal="cats"):
    """

    :param catFile:  (Default value = "cats.txt")
    :param animal:  (Default value = "cats")

    """
    try:
        file = Path(f"{cwd}/chapter_10/{catFile}")
    except FileNotFound:
        print(f"{cwd}/{catFile} does not exist in chapter_10 directory.")
    print(f"Printing list of {animal}: ")
    print(f"{file.read_text()}\n")


def readDogFile(dogFile="dogs.txt", animal="dogs"):
    """

    :param dogFile:  (Default value = "dogs.txt")
    :param animal:  (Default value = "dogs")

    """
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
