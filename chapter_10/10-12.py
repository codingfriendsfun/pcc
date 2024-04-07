from pathlib import Path
import json
## does everything the same but uses the name to find the correct file so you can
## store multiple people
name = input('What is your name? ')
path = Path(f'{name}.json')
if path.exists():
    contents = path.read_text()
    favorite = json.loads(contents)
    print(f'Welcome back {name}')
    print(f"The favorite number you selected is {favorite}")
else:
    favorite = input(f'What is your favorite number {name}? ')
    contents = json.dumps(favorite)
    path.write_text(contents)
    print('I will remember your favorite number!')