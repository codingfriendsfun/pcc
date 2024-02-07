cities = {
    'boston': {
        'population': '655k',
        'state': 'massachusetts',
        'fact': "The children's book 'Make Way for Ducklings' took place in Boston."
        },
    'new york city': {
        'population': '8.4 million',
        'state': 'new york',
        'fact': 'Broadway is here, making it almost as awesome as Boston.'
        },
    'san diego': {
        'population': '1.4 million',
        'state': 'california',
        'fact': 'Pretty cool, but not as cool as NYC or Boston. Quite literally warmer.'
        },
    }

for city, details in cities.items():
    print(f"\n{city.title()} is a city in {details['state'].title()} of about "
          f"{details['population']}. {details['fact']}")