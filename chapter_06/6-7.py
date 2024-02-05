# Store information about a person you know
mom  = {
    'first_name': 'deb',
    'last_name': 'walz',
    'age': 65,
    'city': 'bedford',
    }

dad = {
    'first_name': 'dan',
    'last name': 'bourquard',
    'age': 64,
    'city': 'bow',
    }

me = {
    'first_name': 'noelle',
    'last_name': 'riley',
    'age': 31,
    'city': 'perris',
    }

people = [mom, dad, me]

for person in people:
    for detail in person:
        print(f"{detail}: {person[detail]}")