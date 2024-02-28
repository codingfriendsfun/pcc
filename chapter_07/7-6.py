# using 7-4 code
order_message = "\nEnter the topping you would like:"
order_message += "\n(Type 'quit' when you are finished.)\n"

active = True
while active:
    topping = input(order_message)

    if topping == 'quit':
        break
        active = False
    else:
        print(f"Adding {topping}!")