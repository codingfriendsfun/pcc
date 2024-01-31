#list 5+ current_users
current_users = ['kerowyn', 'suntanna', 'scriptless', 'kristin', 'eclipse']
#list 5 new_users
new_users = ['Suntanna', 'cmpsr2000', 'dt777', 'caileigh', 'xorphix']

for user in current_users:
    current_users.append(user)
for user in new_users:
    new_users.append(user)
#loop through new_users to see if username has already been used
for new_user in new_users:
    if new_user in current_users:
        print(f"The username {new_user} is taken. Please try a different username.")
    #if I try to put the above line on two lines, it gives an "unterminated f-string literal" error
    else:
        print("That username is available!")