from pathlib import Path

pet_names = ['./chapter_10/cats.txt', './chapter_10/dogs.txt']

for pet_name in pet_names:
    try:
        path = Path(pet_name)
        pet_name = path.read_text()
    
        print("Some good pet names are:")
        print(pet_name)
    except FileNotFoundError:
        pass