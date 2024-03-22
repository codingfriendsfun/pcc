glossary = {
    'print': 'outputs the things in () can use f to allow more complex outputs',
    'if': 'checks conditions and outputs true or false',
    'elif': 'if the first condition fails it checks for another condition',
    'else': 'if the other conditions fail it runs this',
    'loop': 'repeating code usually until a condition is met (unless your a maniac)',
    'variable': 'changeable value',
    'Pop': 'removing an item from a list and storing it elsewhere',
    'tupple': 'unchangeable value',
    'dictionary': 'a series of key value pairs',
    'for': 'does something for a time'

}

for key, value in glossary.items():
    print(f"\nTaught Item: {key.title()}, function: {value}")
