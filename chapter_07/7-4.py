order_message = "\nEnter the topping you would like:"
order_message += "\n(Type 'quit' when you are finished.)\n"

while True:
    topping = input(order_message)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping}!")