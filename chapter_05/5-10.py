#list 5+ current_users
current_users = ['kerowyn', 'suntanna', 'scriptless', 'kristin', 'eclipse']
#list 5 new_users
new_users = ['Suntanna', 'cmpsr2000', 'dt777', 'caileigh', 'xorphix']

for user in new_users:
    user = user.lower()
    if user in current_users:
        print(f"The username {user} is taken. Please try a different username.")
    else:
        print("That username is available!")