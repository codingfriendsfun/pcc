# rivers, looping through dictionaries

rivers = {
    'nile' : 'Egypt',
    'mississippi' : 'US',
    'thames' : 'England'
}

for river in rivers:
    print(f"The {river.title()} river is in {rivers[river]}.")

for river in rivers:
    print(river.title())

for river in rivers:
    print(rivers[river])