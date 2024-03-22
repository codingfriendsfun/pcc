sandwich_orders = ["BLT", "Turkey Club", "Veggie Delight",
                   "Pastrami", "Grilled Cheese", "Pastrami", "Pastrami", "Pastrami"]

# Check if there's enough pastrami
if sandwich_orders.count("Pastrami") >= 3:
    print("Apologies, the deli has run out of pastrami.")
    while "Pastrami" in sandwich_orders:
        # Remove all occurrences of pastrami from sandwich orders
        sandwich_orders.remove("Pastrami")
else:
    print("Pastrami is available! Let's make some sandwiches.")

# Initialize an empty list for finished sandwiches
finished_sandwiches = []


# Loop through each sandwich order
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Get the first sandwich order
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each finished sandwich
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
