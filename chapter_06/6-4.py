# Make a dictionary dictionary.
glossary = {
    'traceback': 'an error report Python displays when a program contains a significant error',
    # What should I do formatting wise with the above line? It's technically too long
    'interpreter': 'reads through the program and determines what each word means',
    'syntax highlighting': 'editor highlights different parts of programs in different ways',
    'string': 'a series of characters, anything in single or double quotes',
    'method': 'an action Python can perform on a piece of data',
    'f-string': 'Python formats the string by replacing the name of any variable in braces with its value',
    'whitespace': 'any nonprinting characters like spaces, tabs, end-of-line symbols',
    'syntax error': "error occurring when Python doesn't recognize a section of program as valid Python code",
    'float': 'any number with a decimal point',
    'constant': 'a variable whose value stays the same throughout the life of a program'
    }

# Print each word and definition. Joke's on 6-4, I'd already made it a loop in 6-3.
for word in glossary:
    print(f"{word}: {glossary[word]}\n")