# using dictionaries to store info about a person

person = {
    'first_name' : 'Alexa',
    'last_name' : 'Adams',
    'age' : 31,
    'city' : 'San Diego'
}

for key in person:
    print(f"{key} : {person[key]}")