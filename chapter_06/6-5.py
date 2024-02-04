rivers = {
    'brazil': 'amazon',
    'united states': 'mississippi',
    'iraq': 'euphrates',
    }

# Use a loop to print a sentence about each river
for country, river in rivers.items():
    print(f"The {river.title()} River flows through {country.title()}.")

# Use a loop to print the name of each river.
print("\nThe following rivers are included:")
for river in rivers.values():
    print(f"The {river.title()} River")

# Use a loop to print each country.
print("\nThe rivers run through the following countries:")
for country in rivers.keys():
    print(country.title())