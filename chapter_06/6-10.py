favorite_numbers = {
    'kris': [13],
    'eli': [3, 5, 6, 7],
    'dobs': [3, 12],
    'blake': [11],
    'zack': [8, 88],
    }

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"\n{name.title()}'s favorite numbers are:")
        for num in numbers:
            print(f"\t{num}")
    else:
        print(f"\n{name.title()}'s favorite number is:")
        for num in numbers:
            print(f"\t{num}")