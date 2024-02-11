# Make a list of sandwich orders and finished sandwiches.
sandwich_orders = ['grilled cheese', 'pastrami', 'tuna melt', 'pastrami', 'blt', 'pastrami', 'ham and cheese']
finished_sandwiches = []

# No pastrami allowed.
print("We have 'run out' of pastrami.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through sandwiches as you make them.
while sandwich_orders:
    fresh_sandwich = sandwich_orders.pop()
    print(f"Making a {fresh_sandwich}.")
    finished_sandwiches.append(fresh_sandwich)

print('\nWe made the following sandwiches:')
for sandwich in finished_sandwiches:
    print(f"{sandwich}")