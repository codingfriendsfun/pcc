index = {
    'list': 'An array.',
    'title()': 'Capitalizes the first letters of each word.',
    'upper()': 'Converts all letters to uppercase.',
    'lower()': 'Converts all letters to lowercase.',
    'strip()': 'Removes beginning and trailing whitespace.',
    'dictionary': 'Stores key-value pairs.',
    'key()': 'Pulls the keys in a dictionary.',
    'value()': 'Pulls the values in a dictionary.',
    'camelCase': 'firstLowerCase restUpperCase',
    'snake_case': 'under_scores_represent_spaces'
    }

for term, definition in index.items():
    print(f"{term}: \n\t {definition}\n")