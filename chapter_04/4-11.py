pizzas = ['pepperoni', 'black olives', 'cheese']
friend_pizzas = pizzas[:]

pizzas.append('mushroom')
friend_pizzas.append('supreme')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
    
print("\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())