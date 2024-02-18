# 7-4. Pizza Toppings

topping = ""

while topping != 'quit':
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.\n")
        topping = input("What topping would you like on your pizza? ")