from pathlib import Path
import json

def set_favorite_number(path):
    """Prompt for a new favorite number."""

    path = Path(path)

    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)

    print(f"Your favorite number {favorite_number} has been saved!")
    
set_favorite_number('favorite_number.json')
