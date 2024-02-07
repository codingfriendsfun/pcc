# Make dictionaries for pets
antares = {
    'name': 'antares',
    'species': 'dog',
    'human': 'noelle',
    }

rey = {
    'name': 'rey',
    'species': 'cat',
    'human': 'noelle',
    }

chekov = {
    'name': 'chonk',
    'species': 'dog',
    'human': 'larissa',
    }

kanan = {
    'name': 'kanan',
    'species': 'orange',
    'human': 'rob',
    }

oliver = {
    'name': 'mr. teefies',
    'species': 'perfection',
    'human': '.....noelle',
    }

pets = [antares, rey, chekov, kanan, oliver]

for pet in pets: 
    print(f"\nName: {pet['name'].title()}")
    print(f"Species: {pet['species']}")
    print(f"Owner: {pet['human'].title()}")