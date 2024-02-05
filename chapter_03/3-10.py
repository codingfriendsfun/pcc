#simulating a horse game
user_name = "User 1"
horse_names = []
horse_breeds = []
sold_horse_names = []
sold_horse_breeds = []


print(f"Hello, {user_name}! You currently have {len(horse_breeds)} horses, would you like to purchase one?")

#player chooses yes
print("\nYes.")
horse_names.append('Dolly')
horse_breeds.append('Arabian')
print(f"\nCongratulations, {user_name}! You now have an {horse_breeds[0]} horse named {horse_names[0]}.")
print(f"\nWould you like to buy another horse, {user_name}?")

#player picks yes
print("\nYes.")
horse_names.append('Chase')
horse_breeds.append('Thoroughbred')
print(f"\nCongratulations, {user_name}! You now have a {horse_breeds[1]} horse named {horse_names[1]}.")
print(f"\n{user_name}, you now have {len(horse_names)} horses. Would you like to sell any?")

#player picks yes
print(f"\nYes.")
print(f"\nWould you like to sell {horse_names[0]} or {horse_names[1]}?")

#player picks Dolly
print(f"\n{horse_names[0]}.")
sold_horse_name = horse_names.pop(0)
sold_horse_breed = horse_breeds.pop(0)
print(f"\nYou have sold an {sold_horse_breed} named {sold_horse_name}.")

#horse dies
print(f"\nOh no! It looks like {horse_names[0]} has died!")
del horse_names[0]
del horse_breeds[0]
print(f"You now have {len(horse_names)} horses! Would you like to buy any?")

#player picks yes
print("\nYes.")

#player buys 4 horses
horse_names.insert(0, 'Feather') 
horse_names.insert(1, 'Zeus')
horse_names.insert(2, 'Apple')
horse_names.insert(3, 'Egg')
print(f"\nCongratulations, {user_name}! You have purchased {horse_names[0]}, {horse_names[1]}, {horse_names[2]}, and {horse_names[3]}!")

#players page defaults to sort by alphabetical
horse_names.sort()
print(f"\nWelcome to your barn, here you can view your horses: {horse_names[0]}, {horse_names[1]}, {horse_names[2]}, and {horse_names[3]}.")

#player sets it to sort by name descending
horse_names.sort(reverse=True)
print(f"\nWelcome to your barn, here you can view your horses: {horse_names[0]}, {horse_names[1]}, {horse_names[2]}, and {horse_names[3]}.")
