#10-11a. Favorite Number
# store a favorite number

from pathlib import Path
import json, os

def getNumber():
    return int(input("Please enter your favorite number: "))


def storeNumber(jsonFile, num):
    path = Path(jsonFile)
    path.write_text(json.dumps(num))
    return 

# deal with "What folder am I working from?"
cwd = os.getcwd()
index = cwd.find("chapter")
if index > 0:
    cwd = cwd[:index]
# else do nothing, assume we're in workspace root

storeNumber(f"{cwd}/chapter_10/favNum.json", getNumber())
