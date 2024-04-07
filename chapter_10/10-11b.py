#10-11b. Favorite Number
# retrieve a favorite number

from pathlib import Path
import json, os

def retrieveNumber(jsonFile):
    path = Path(jsonFile)
    if path.exists():
        print("I know your favorite number! It's " + 
            f"{json.loads(path.read_text())}.")
    else:
        print("File not found, try again.")
    return 


# deal with "What folder am I working from?"
cwd = os.getcwd()
index = cwd.find("chapter")
if index > 0:
    cwd = cwd[:index]
# else do nothing, assume we're in workspace root

retrieveNumber(f"{cwd}/chapter_10/favNum.json")