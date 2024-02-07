user_names = ['uSeR', 'ReSu', 'admin', 'name', 'eman']

for user in user_names:
    if user == 'admin':
        print(f"Hello, {user}! Would you like a status report?")
    else:
        print(f"Hello, {user}!")
