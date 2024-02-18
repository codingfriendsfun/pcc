# 7-6 Three Exits

### conditional

topping = ""

while topping != 'quit':
    topping = input("What topping would you like on your pizza? ")
    if topping == 'quit':
        continue
    else:
        print(f"I'll add {topping} to your pizza.\n")


### active

active = True

while active:
    topping = input("What topping would you like on your pizza? ")
    if topping == 'quit':
        active = False
        continue
    else:
        print(f"I'll add {topping} to your pizza.\n")


### break

while True:
    topping = input("What topping would you like on your pizza? ")
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.\n")