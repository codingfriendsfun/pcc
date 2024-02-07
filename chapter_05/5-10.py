current_users = ['uSeR', 'ReSu', 'admin', 'name', 'eman']
new_users = ['Kero', 'hens', 'AdMiN', 'nAMe', 'idfk']
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, {user} is taken. Please choose a new user")
    else: 
        print(f"Welcome, {user}!")
