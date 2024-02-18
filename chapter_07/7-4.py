# 7-4. Pizza Toppings

topping = ""

while topping != 'quit':
    topping = input("What topping would you like on your pizza? ")
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.\n")