# a script for collecting sandwich orders

sandwich_orders = ["Monte Cristo", "Tuna Melt", "Meatball Sub"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"{sandwich} order, ready to go!")
    finished_sandwiches.append(sandwich)

print(f"\nList of finished sandwiches: {finished_sandwiches}")

