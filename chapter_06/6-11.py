sharn ={
    'name':'Sharn',
    'world':'Eberron',
    'setting':'d&d',
    'description':'fantasy futuristic world like a new york or some other major multi level city.',
}

coruscant ={
    'name':'Coruscant',
    'world':'Coruscant',
    'setting':'star wars',
    'description':'City World at the heart of the Star Wars Universe.',
}
thecitadel ={
    'name':'The Citadel',
    'world':'Mass Relay Space Station',
    'setting':'Mass Effect',
    'description':'Space station at the center of the alliance of alien species in the Mass Effect Universe.',
}

cities = [sharn, coruscant, thecitadel]

for city in cities:
    for key, value in city.items():
        print (f"{key.title()}:{value}\n")