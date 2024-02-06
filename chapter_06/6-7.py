# Store information about a person you know
mom  = {
    'first_name': 'deb',
    'last_name': 'walz',
    'age': 65,
    'city': 'bedford',
    }

dad = {
    'first_name': 'dan',
    'last_name': 'bourquard',
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
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nName: {full_name.title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")