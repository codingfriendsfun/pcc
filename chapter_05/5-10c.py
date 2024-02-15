current_users = ["ravi", "chris", "rob", "larissa", "Noelle"]
new_users = ["Chris", "noelle", "lauren", "dan", "george"]

for user in new_users:
    if user.lower() in [user.lower() for user in current_users]:
        print("Sorry that name already exists, please enter a new name")
    else:
        print(f"That username is available. welcome " + user.title()) 
