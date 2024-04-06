from pathlib import Path
import json

def get_favorite_number(path):
    """Get stored favorite number."""
    path = Path(path)
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)

        print(f"Your favorite number is {favorite_number}!")
    
    else:
        print("You have no favorite number!")
    
get_favorite_number('favorite_number.json')
