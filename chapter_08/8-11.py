##write a function that accepts a list of items a person wants on a sandwich
toppings = []

while toppings != 'q':
    topping = input("What topping would you like on your sandwich? 'q' to quit ")
    if topping == 'q':
        break
    else:
        toppings.append(topping)

def make_sandwich(*ingredients):
    print ("making a sandwhich: ")
    for ingredient in ingredients:
        print(f"\nAdding topping - {ingredient}")

make_sandwich(toppings)

