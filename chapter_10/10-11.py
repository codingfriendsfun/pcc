from pathlib import Path
import json
##I'm going to be a little extra with it because I want to use this kind of code
##to try some more advanced stuff
name = input('What is your name? ')
favorite = input(f'What is your favorite number {name}? ')
##favorite_number = {name:favorite} - couldn't get key value to dump, try again later when we figure out how to addendum
##since the key value was an causing an error I'm going to try a simple work
##around for now although this gets a little excessive with your buildup.
path = Path(f'{name}.json')
contents = json.dumps(favorite)
path.write_text(contents)




