sandwich_orders = ['tuna', 'pastrami','pastrami', 'reuben', 'italian', 'dogfish', 'pastrami']
finished_sandwiches = []

#solution that was asked for, but I prefer the if/else solution
#print("Sorry, we have run out of pastrami.")
#while 'pastrami' in sandwich_orders:
#    sandwich_orders.remove('pastrami')
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