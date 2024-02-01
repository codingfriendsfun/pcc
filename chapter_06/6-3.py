# Make a dictionary dictionary.
glossary = {
    'traceback': 'an error report Python displays when a program contains a significant error',
    # What should I do formatting wise with the above line? It's technically too long
    'interpreter': 'reads through the program and determines what each word means',
    'syntax highlighting': 'editor highlights different parts of programs in different ways',
    'string': 'a series of characters, anything in single or double quotes',
    'method': 'an action Python can perform on a piece of data',
    }

# Print each word and definition
for word in glossary:
    print(f"{word}: {glossary[word]}\n")