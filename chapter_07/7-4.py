prompt = "\nType what toppings you would like on your pizza:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")