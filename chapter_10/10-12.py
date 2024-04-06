from pathlib import Path
import json

def get_favorite_number(path):
    """Get stored favorite number."""

    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)

        return favorite_number
    
    else:
        return None
    

def set_favorite_number(path):
    """Prompt for a new favorite number."""

    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)

    return favorite_number
    

def your_favorite_number():
    """
    Display stored favorite number or prompt user for their favorite number.
    """
    path = Path('favorite_number.json')
    fav_number = get_favorite_number(path)

    if fav_number:
        print(f"Your favorite number is {fav_number}!")
    
    else:
        fav_number = set_favorite_number(path)
        print(f"Your favorite number is {fav_number}! "
              "We'll remember this for next time!")

your_favorite_number()