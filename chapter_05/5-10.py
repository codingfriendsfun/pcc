# website username simulation

current_users = ["name1", "name2", "namE3", "admin", "name4"]
new_users = ["name5", "NAME2", "name6", "Name3", "name7"]

#make lowercase for comparison
current_users = [user.lower() for user in current_users]

for new in new_users:
    if new.lower() in current_users:
        print(f"Username {new} taken, please choose another.")
    else:
        print(f"Username {new} available.")