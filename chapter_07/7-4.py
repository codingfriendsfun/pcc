done = False
while not done:
    topping = input("What topping would you like?")

    if topping == "quit":
        done = True
    else:
        print (f"I will add {topping} to the pizza")


##write a loop that prompts the user to enter a series of pizza toppings until
## they enter a 'quit' value. As they enter each topping, print a message saying
## you will add that topping to the pizza