favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

population = ['phil', 'noelle', 'eli', 'kristin', 'sarah']

for name in population:
    if name.lower() in [polled.lower() for polled in favorite_languages]:
        print("Thanks for responding")
    else:
        print(f"Would you like to respond to the poll, {name.title()}?")



