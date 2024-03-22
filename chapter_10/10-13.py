from pathlib import Path
import json

def get_stored_userdata(path):
    """Get stored userdata if available."""
    if path.exists():
        contents = path.read_text()
        userdata = json.loads(contents)
        return userdata
    else:
        return None
    
def get_new_userdata(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    pet = input("What kind of pet would you like to own? ")
    book_rec = input("What is the name of a book you recommend? ")

    # Create dictionary to store info in
    userdata = {
        'name': username,
        'pet': pet,
        'book_rec': book_rec,
        }
    
    contents = json.dumps(userdata)
    path.write_text(contents)
    return userdata

def greet_user():
    """Greet the user by name."""
    path = Path('userdata.json')
    userdata = get_stored_userdata(path)
    if userdata:
        print(f"Welcome back, {userdata['name']}!")
        print(f"You would like to own a pet {userdata['pet']}.")
        print(f"You recommend the book {userdata['book_rec']}.")
    else:
        userdata = get_new_userdata(path)
        print(f"We'll remember you when you come back, {userdata['name']}!")

greet_user()