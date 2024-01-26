#List three favorite pizzas
pizzas = ['pepperoni', 'spinach and feta', 'cheese']
#Make a copy of the list and call it friend_pizzas
friend_pizzas = pizzas [:]
#Add a new pizza t othe original list
pizzas.append('bacon')
#Add a different pizza to friend_pizzas
friend_pizzas.append('hawaiian')
#Prove that there are two separate lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)