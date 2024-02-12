river_data = {
    'nile': 'egypt',
    'arkansas': 'united states',
    'yukon': 'canada',
    }

for river, country in river_data.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers:")
for river in river_data.keys():
    print(f"\t{river.title()}")

print("\nCountries:")
for country in river_data.values():
    print(f"\t{country.title()}")