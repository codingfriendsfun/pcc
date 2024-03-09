from admin import User, Admin

#creating instances of Admin() and User() from admin.py
user_1 = Admin('gandalf', 'the grey', 
              'the undying lands of valinor', 
              'wizardry')

user_2 = User('kristin', 'lastname', 'arkansas', 'coding')
user_3 = User('rami', 'malek', 'california', 'hacking')
user_4 = Admin('dobby', 'bunbun', 'texas', 'food')

# List of admins
admin_users = [user_1, user_4]

#calling the method that prints priveleges
for user in admin_users:
    print(f"\n{user.first_name.title()} {user.last_name.title()} can:")
    user.priveleges.privelege_list()
