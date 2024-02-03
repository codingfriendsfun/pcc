# login greeting, with special greeting for admins

usernames = []

if usernames:
    for name in usernames:
        if name == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {name}, thanks for logging in.")
else: # no users
    print("We need users.")