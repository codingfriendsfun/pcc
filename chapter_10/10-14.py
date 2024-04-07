from pathlib import Path
import json

def get_stored_user(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None
def get_new_user(path):
    """Prompt for new username."""
    username = input("What is your name? ")
    hobby = input("What is your favorite hobby? ")
    age = input("How old are you? ")
    user = {
        'name' : username,
        'hobby' : hobby,
        'age' : age
    }
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet user by name"""
    path = Path('username.json')
    user = get_stored_user(path)
    if user:
        for key, value in user.items():
            print(f"{key.title()}: {value}")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user}")

user = input('Type "N" to enter a new user otherwise any key to continue: ')
if user == "N":
    path = Path('username.json')
    newUser = get_new_user(path)
    print(f"We'll remember you when you come back, {newUser['name']}")
else:
    greet_user()
