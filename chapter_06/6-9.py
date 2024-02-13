favorite_places = {
    'kristin': ['colorado', 'montana'],
    'grandma': ['chicago'],
    'chris': ['texas', 'florida', 'california'],
}

for person, locations in favorite_places.items():
    if len(locations) > 1:
        print(f"\n{person.title()}'s favorite locations are:")
        for location in locations:
            print(f"\t{location.title()}")
    else:
        print(f"\n{person.title()}'s favorite location is {location.title()}")