unprinted_designs = ['phone case', 'robot pendant', 'dodechohedron']
completed_models = []

while unprinted_designs:
    current_design=unprinted_designs.pop()
    print(f"printing model: {current_design}")
    completed_models.append(current_design)

print ("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_models)