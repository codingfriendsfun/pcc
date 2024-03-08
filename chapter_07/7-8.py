# Create a list of sandwich orders
sandwich_orders = ["BLT", "Turkey Club", "Veggie Delight", "Pastrami", "Grilled Cheese"]

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