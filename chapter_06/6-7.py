# originally 6-1
# using dictionaries to store info about a person

person1 = {
    'first_name' : 'Alexa',
    'last_name' : 'Adams',
    'age' : 31,
    'city' : 'San Diego'
}

person1 = {
    'first_name' : 'Alexa',
    'last_name' : 'Adams',
    'age' : 31,
    'city' : 'San Diego'
}

person2 = {
    'first_name' : 'Blexa',
    'last_name' : 'Adams',
    'age' : 31,
    'city' : 'San Diego'
}

person3 = {
    'first_name' : 'Clexa',
    'last_name' : 'Adams',
    'age' : 31,
    'city' : 'San Diego'
}

people = [person1, person2, person3]

for person in people:
    for key in person:
        print(f"{key} : {person[key]}")