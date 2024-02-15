def get_formatted_place(city_name, country_name):
    """Neatly format a city and country."""
    formatted_place = f"{city_name}, {country_name}"
    return formatted_place.title()

places = {
    'boston': 'united states',
    'sydney': 'australia',
    'edinburgh': 'scotland',
    'london': 'england',
    }

for city, country in places.items():
    place = get_formatted_place(city, country)
    print(place)