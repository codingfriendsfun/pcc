sandwich_orders = [
    "Pastrami", 
    "Monte Cristo", 
    "Pastrami", 
    "Tuna Melt", 
    "Pastrami", 
    "Meatball Sub"
    ]

finished_sandwiches = []

print("Notice: shop is out of pastrami.\n")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == "Pastrami":
        continue
    print(f"{sandwich} order, ready to go!")
    finished_sandwiches.append(sandwich)

print(f"\nList of finished sandwiches: {finished_sandwiches}")