from pathlib import Path

files = [Path("cats.txt"), Path("dogs.txt")]

for file in files:
    try:
        filedump = f"{file} names: \n"
        filedump += file.read_text()
        print(filedump)
    except FileNotFoundError:
        print(f"Error {file} not found")
