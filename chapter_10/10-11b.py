from pathlib import Path
import json

##uses the name to search the filename and pull your favorite number from before
name = input('What is your name? ')
path = Path(f'{name}.json')
contents = path.read_text()
favorite = json.loads(contents)
print(f"I know your favorite number it's {favorite}")