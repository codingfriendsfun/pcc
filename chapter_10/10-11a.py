from pathlib import Path
import json

fav_num = input("What is your favorite number? ")
path = Path('./chapter_10/fav_num.json')
contents = json.dumps(fav_num)
path.write_text(contents)
