# this was originally exercise 4-1
# a script that lists pizzas

pizzas = ["Everest", "Hawaiian", "Chicken Artichoke"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("But I'm open to trying any pizza once.")

print() # for readability

friend_pizzas = pizzas[0:4]
pizzas.append("Pepperoni")
friend_pizzas.append("Cheese")

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print() # for readability

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)