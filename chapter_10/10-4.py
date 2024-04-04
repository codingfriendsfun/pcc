from pathlib import Path

contents = input("Enter your first and last name: ")

# Store users name
path = Path('text_files/guest.txt')
path.write_text(contents)
