cities = {
    'arlington': {
        'state': 'texas',
        'population': 150000,
        'idk': 'stuff',
    },
    'jacksonville': {
        'state': 'arkansas',
        'population': 2,
        'idk': 'oompa',
    },
    'ovilla': {
        'state': 'texas',
        'population': 20,
        'idk': 'loompa',
    },
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    state = info['state']
    population = info['population']
    idk = info['idk']

    print(f"\tState: {state.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tIdk: {idk.title()}")