sandwich_orders = ['tuna', 'pastrami','pastrami', 'reuben', 'italian', 'dogfish', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        print("Sorry, we have run out of pastrami.")

    else:
        print(f"I made your {current_sandwich.title()} sandwich.")
        finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:\n")
for sandwich in finished_sandwiches:
    print(sandwich.title())