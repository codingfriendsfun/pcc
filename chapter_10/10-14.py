from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user info if available."""

    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    
    else:
        return None
    

def collect_user_info(path):
    """Collect data from new users."""

    user = {}
    user['username'] = input("What is your name? ")
    user['location'] = input("Where do you live? ")
    user['occupation'] = input("What is your job title? ")

    contents = json.dumps(user)
    path.write_text(contents)

    return user


def describe_user(path, user={}):
    """Display a description of the user."""

    if user:
        print("User info:")
        for cat, data in user.items():
            print(f"{cat.title()}: {data.title()}")
          
    else:
        user  = collect_user_info(path)
        print("\nYou've successfully submitted the following info: ")
        for cat, data in user.items():
            print(f"{cat.title()}: {data.title()}")


def authenticate_user():
    """Confirm if the correct user is accessing the program."""

    path = Path('user.json')
    user = get_stored_user_info(path)

    if user:
        ver_user = input(f"Is your username {user['username'].title()}? (Y/N) ")

        if ver_user.lower() == 'y':
            describe_user(path, user)

        else:
            describe_user(path)

    else:
        describe_user(path)
            

authenticate_user()
