#Store 5 basic foods in a tuple
menu = ('stir fry', 'quesadillas', 'omlettes', 'fried rice', 'pizza')
#Use a for loop to print the five foods
print("Restaurant menu:")
for food in menu:
    print(food)

#Modify tuple to create error; in comment to run rest of program
#menu[0] = 'schwarma'
#Rewrite the tuple
menu = ('salad', 'quesadillas', 'omlettes', 'fried rice', 'ice cream')
#Use a for loop to print the new foods
print("\nNew restaurant menu:")
for food in menu:
    print(food)