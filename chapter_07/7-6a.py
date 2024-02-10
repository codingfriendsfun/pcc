# See 7-4 for a quit value triggering a break statement. 
prompt = "\nType what toppings you would like on your pizza:"
prompt += "\nEnter 'quit' when you are finished. "

# Version of 7-4 using an active variable to control the loop:
active = True
while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")