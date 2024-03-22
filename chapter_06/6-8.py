antares = {"name": "antares", "owner": "noelle", "job": "service dog", "age": "2"}

chekov = {"name": "chekov", "owner": "larissa", "job": "service dog", "age": "3"}

sherlock = {
    "name": "sherlock",
    "owner": "mom",
    "job": "sleep, human walker",
    "age": "6",
}


pets = [antares, chekov, sherlock]

for pet in pets:
    for key, value in pet.items():
        # value should only title sometimes so this comes out weird
        print(f"\n{key.title()}: {value.title()}")
