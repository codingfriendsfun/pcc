mypizzas = ["pepperoni", "cheese", "pepperoni with honey!"]
friendsPizza = mypizzas[:]
friendsPizza.append("Pinneapple")
mypizzas.append("green onion and garlic")
for pizza in mypizzas:
    print(f"I like {pizza.title()} pizza")
print ("I'm not the most diverse person haha. I fucking love me some pizza")

for pizza in friendsPizza:
    print(f"They like {pizza.title()} pizza")
print ("We like a lot of the same but they like pineapple..gross")