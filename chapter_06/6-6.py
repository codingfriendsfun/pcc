favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

# Make a list of people who should take the poll. Include names that are and are not in the dictionary.
poll_takers = ('jen', 'larissa', 'alexa', 'caileigh', 'sarah', 'phil')

# Loop through the list. If they've taken the poll, thank them. If not, invite them.
for person in poll_takers: 
    if person in favorite_languages.keys():
        print(f"Thank you, {person.title()}, for taking the poll.\n")
    else:
        print(f"{person.title()}, please take the poll.\n")