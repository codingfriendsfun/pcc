current_users = ["ravi", "chris", "rob", "larissa", "Noelle"]
new_users = ["Chris", "noelle", "lauren", "dan", "george"]

current_users = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users:
        print("Sorry that name already exists, please enter a new name")
    else:
        print(f"That username is available. welcome " + user.title()) ##{user} may be needed here
