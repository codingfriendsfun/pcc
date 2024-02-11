antares = {
    'owner': 'noelle',
    'job':'make sure she does the right things',
    'age': 2
}

chekov = {
    'owner': 'larissa',
    'job':'make sure she does not break herself',
    'age': 3
}

sherlock = {
    'owner': 'mom',
    'job':'sleep and walk his humans',
    'age': '6'
}


pets = [antares, chekov, sherlock]

for pet in pets:
   for key, value in pet.items():
      print (f"\n{key.title()}: {value}") ##value won't accept title. How would I only do certain values? If statement?...