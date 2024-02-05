guest_list = ['Mom', 'Ellie', 'Elijah']
print(f"You're invited to dinner, {guest_list[0]}!")
print(f"Come on, {guest_list[1]}, you don't get a choice to join dinner!")
print(f"{guest_list[2]}, yes you're invited and yes, you must eat the food.")

#new line

print('\n')

print(f"Oh no, {guest_list[0]} can't make it!(rip)")

#new line

print('\n')

del guest_list[0]
guest_list.insert(0, 'Grandma')
print(f"You're invited to dinner, {guest_list[0]}!")
print(f"Come on, {guest_list[1]}, you don't get a choice to join dinner!")
print(f"{guest_list[2]}, yes you're invited and yes, you must eat the food.")