# Store people's favorite numbers, using their names as keys.
favorite_numbers = {
    'Noelle': 7,
    'Kristin': 5,
    'Alexa': 7,
    'Ravi': 4,
    'Larissa': 6
    }

# Print each person's favorite number.
for person in favorite_numbers:
    print(f"{person}'s favorite number is {favorite_numbers[person]}")