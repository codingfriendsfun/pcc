from pathlib import Path
import json

path = Path('./chapter_10/fav_num.json')
if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"I know your favorite number! It's {fav_num}.")
else:
    fav_num = input("What is your favorite number? ")
    contents = json.dumps(fav_num)
    path.write_text(contents)
