# Make a list of sandwich orders and finished sandwiches.
sandwich_orders = ['grilled cheese', 'tuna melt', 'blt', 'ham and cheese']
finished_sandwiches = []

# Loop through sandwiches as you make them.
while sandwich_orders:
    fresh_sandwich = sandwich_orders.pop()
    print(f"Making a {fresh_sandwich}.")
    finished_sandwiches.append(fresh_sandwich)

print('\nWe made the following sandwiches:')
for sandwich in finished_sandwiches:
    print(f"{sandwich}")