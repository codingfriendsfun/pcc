person_1 = {"first": "Ravi", "last": "Ghotra", "age": 36, "city": "Long Beach"}

person_2 = {"first": "Dan", "last": "Bautista", "age": 35, "city": "Anaheim"}

person_3 = {
    "first": "Chris",
    "last": "Richardson",
    "age": "classified",
    "city": "classified",
}

people = [person_1, person_2, person_3]

for person in people:
    for key, value in person.items():
        print(f"\nKey: {key.title()}")
        print(f"Value: {value}")
