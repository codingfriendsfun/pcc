from pathlib import Path

name = input("What is your name? ")

path = Path('./chapter_10/guest.txt')
path.write_text(name)