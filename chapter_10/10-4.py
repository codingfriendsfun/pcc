from pathlib import Path

path = Path('guests.txt')
guest = input('What is your name? ')

path.write_text(guest)
