# using dictionaries to store info about pets

pet1 = {
    'name' : 'Oliver',
    'human' : 'Alexa',
    'age' : 10
}

pet2 = {
    'name' : 'Matrim',
    'human' : 'Caileigh',
    'age' : 8
}

pet3 = {
    'name' : 'Wednesday',
    'human' : 'Alexa',
    'age' : 7
}



pets = [pet1, pet2, pet3]

for pet in pets:
    for key in pet:
        print(f"{key} : {pet[key]}")