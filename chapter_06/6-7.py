#6-1
ellie = {
    'first': 'ellie',
    'last': 'garcia',
    'age': 0,
    'town': 'grand prairie',
    }
#new
elijah = {
    'first': 'elijah',
    'last': 'garcia',
    'age': 7,
    'town': 'grand prairie',
}

kristin = {
    'first': 'kristin',
    'last': 'hensley',
    'age': 27,
    'town': 'jacksonville',
}

people = [ellie, elijah, kristin]

for person in people:
    first = person['first']
    last = person['last']
    age = person['age']
    town = person['town']
    print(f"{first.title()} {last.title()} is {age} years old and from {town.title()}.")