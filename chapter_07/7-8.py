sandwich_orders = ['tuna', 'meatball', 'reuben', 'italian', 'dogfish']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:\n")
for sandwich in finished_sandwiches:
    print(sandwich.title())
