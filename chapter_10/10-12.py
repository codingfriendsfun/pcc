# 10-12. Favorite Number
# store and retrieve a favorite number

import json
import os
from pathlib import Path


def getRootDir():
    # deal with "What folder am I working from?"
    cwd = os.getcwd()
    index = cwd.find("chapter")
    if index > 0:
        cwd = cwd[:index]
    # else do nothing, assume we're in workspace root
    return cwd


def getNumber():
    return int(input("Please enter your favorite number: "))
    print("Favorite number cached.")


def storeNumber(jsonFile, num):
    path = Path(jsonFile)
    path.write_text(json.dumps(num))
    return


def retrieveNumber(jsonFile):
    path = Path(jsonFile)
    if path.exists():
        print("I know your favorite number! It's " + f"{json.loads(path.read_text())}.")
    else:
        print("Cached file not found, prompting for number...")
        storeNumber(jsonFile, getNumber())
    return


def main():
    rootDir = getRootDir()

    # create scratch dir
    scratchDir = Path(f"{rootDir}/scratch_files")
    if not scratchDir.exists():
        os.mkdir(scratchDir.resolve())

    # now do the thing
    retrieveNumber(f"{scratchDir.resolve()}/favNum.json")


if __name__ == "__main__":
    main()
