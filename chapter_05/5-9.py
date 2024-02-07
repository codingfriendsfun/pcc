user_names = []

if user_names:
    for user in user_names:
        if user == 'admin':
            print(f"Hello, {user}! Would you like a status report?")
        else:
            print(f"Hello, {user}!")
else:
    print("No users!")
