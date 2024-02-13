dobby = {
    'species': 'rabbit',
    'owner': 'kristin',
}

antares = {
    'species': 'dog',
    'owner': 'noelle',
}

princess = {
    'species': 'dog',
    'owner': 'grandma'
}

pets = [dobby, antares, princess]

for pet in pets:
    species = pet['species']
    owner = pet['owner']
    print(f"{owner.title()} owns a {species}")
