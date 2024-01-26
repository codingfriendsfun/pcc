#Use an example from the textbook and write two for loops to print each list of foods.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
#This is where I will differ from the book, adding for loops
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)