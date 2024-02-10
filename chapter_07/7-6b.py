# See 7-4 for a quit value triggering a break statement. 
prompt = "\nType what toppings you would like on your pizza:"
prompt += "\nEnter 'quit' when you are finished. "

# Version of 7-4 using while statment to control the loop:
topping = " "
while topping != 'quit':
    topping = input(prompt)    
    
    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")