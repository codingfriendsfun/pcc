# login greeting, with special greeting for admins

usernames = ["name1", "name2", "name3", "admin", "name4"]

for name in usernames:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thanks for logging in.")