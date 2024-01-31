#list five or more usernames, including admin
users = ['kerowyn', 'admin', 'scriptless', 'kristin', 'eclipse']

#print greeting for each user, with special greeting for admin.
for user in users:
    if user == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")