#3-4
guest_list = ['Mom', 'Ellie', 'Elijah']
print(f"You're invited to dinner, {guest_list[0]}!")
print(f"Come on, {guest_list[1]}, you don't get a choice to join dinner!")
print(f"{guest_list[2]}, yes you're invited and yes, you must eat the food.")

#new line

print('\n')

#3-5
print(f"Oh no, {guest_list[0]} can't make it!(rip)")

#new line

print('\n')

del guest_list[0]
guest_list.insert(0, 'Grandma')
print(f"You're invited to dinner, {guest_list[0]}!")
print(f"Come on, {guest_list[1]}, you don't get a choice to join dinner!")
print(f"{guest_list[2]}, yes you're invited and yes, you must eat the food.")

#new line
#start of 3-6
print('\n')

print("Good news, we found a bigger table! (Sorry, Mom)")
#new line
print('\n')

guest_list.insert(0, 'Irma')
guest_list.insert(2, 'Noelle')
guest_list.append('Blake')

print(f"Bring the food, {guest_list[0]}!")
print(f"You're invited to dinner, {guest_list[1]}!")
print(f"{guest_list[2]}, I just needed to fill seats, thanks!")
print(f"Come on, {guest_list[3]}, you don't get a choice to join dinner!")
print(f"{guest_list[4]}, yes you're invited and yes, you must eat the food.")
print(f"{guest_list[5]}, you're invited as long as you leave when we're done.")
