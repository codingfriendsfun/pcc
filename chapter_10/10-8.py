from pathlib import Path

def cat_dog_reading(file_name):
    """
    Read the names in cat or dog text files.
    """
    path = Path(f'text_files/{file_name}')

    try:
        contents = path.read_text(encoding='utf-8')

    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist")

    else:
        print(contents)

cat_dog_reading('cats.txt')
# Exception message
cat_dog_reading('dogs.txt')
