class User:
    """Creating a user profile."""
    def __init__(self, first_name, last_name, location, hobby):
        """Initializing attributes of a users information."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.hobby = hobby

    def describe_user(self):
        """Describes a user"""
        print(f"\n{self.first_name.title()} {self.last_name.title()} was born in "
              f"{self.location.title()} and enjoys {self.hobby}.")
        
    def greet_user(self):
        """Greets a user."""
        print(f"Good morning, {self.first_name.title()}"
              f" {self.last_name.title()}!")
        
#creating instances of User()
user_1 = User('gandalf', 'the grey', 'the undying lands of valinor', 'wizardry')
user_2 = User('kristin', 'lastname', 'arkansas', 'coding')
user_3 = User('rami', 'malek', 'california', 'hacking')
user_4 = User('dobby', 'bunbun', 'texas', 'food')

#storing users in a list and looping through the list calling User() methods.
users = [user_1, user_2, user_3, user_4]
for user in users:
    user.describe_user()
    user.greet_user()