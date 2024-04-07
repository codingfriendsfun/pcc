# 10-14. Verify User

from pathlib import Path
import json, os

def getRootDir():
    # deal with "What folder am I working from?"
    cwd = os.getcwd()
    index = cwd.find("chapter")
    if index > 0:
       cwd = cwd[:index]
    # else do nothing, assume we're in workspace root
    return cwd


def get_stored_userInfo(path):
    """Get stored userInfo if available."""
    if path.exists():
        contents = path.read_text()
        userInfo = json.loads(contents)
        return userInfo
    else:
        return None

def get_new_userInfo(path):
    """Prompt for a new userInfo."""
    userInfo = {}
    userInfo["username"] = input("What is your name? ")
    userInfo["favColor"] = input("What is your favorite color? ")
    userInfo["city"] = input("What city do you live in? ")
    
    contents = json.dumps(userInfo)
    path.write_text(contents)
    return userInfo


def isCorrectUser(userInfo):
    if input(f"Are you {userInfo['username']}? Type yes/no. ").lower() == 'yes':
        return True
    return False


def greet_user(jsonFile):
    """Greet the user by name."""
    path = Path(jsonFile)
    if path.exists():
        userInfo = get_stored_userInfo(path)
        if len(userInfo) == 3:
            if isCorrectUser(userInfo):
                print(f"Welcome back, {userInfo['username']}!")
                print(f"Your favorite color is {userInfo['favColor']}.")
                print(f"You live in {userInfo['city']}.")
            else: # not correct user
                userInfo = get_new_userInfo(path)
                print(f"We'll remember you when you come back, {userInfo['username']}!")
        # else fall back and create new, as we don't have a valid file.
    else:
        userInfo = get_new_userInfo(path)
        print(f"We'll remember you when you come back, {userInfo['username']}!")


def main():
    rootDir = getRootDir()

    # create scratch dir
    scratchDir = Path(f"{rootDir}/scratch_files")
    if not scratchDir.exists():
        os.mkdir(scratchDir.resolve())

    #now do the thing
    greet_user(f'{scratchDir}/userInfo.json')


if __name__ == "__main__":
    main()