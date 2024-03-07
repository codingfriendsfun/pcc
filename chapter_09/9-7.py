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
        
    def greet_user(self, user):
        """Greets a user."""
        print(f"Good morning, {self.first_name.title()}"
              f" {self.last_name.title()}!")

class Admin(User):
    """Administrator attributes."""

    def __init__(self, first_name, last_name, location, hobby):
        """Initialize parent and Admin attributes."""

        super().__init__(first_name, last_name, location, hobby)

        self.priveleges =['add posts', 'delete posts', 
                             'edit posts', 'ban users']
       

    def privelege_list(self):
        """Describe the priveleges admins have."""

        print(f"\n{self.first_name.title()} {self.last_name.title()} can:")
        for privelege in self.priveleges:
            print(privelege.title())



#creating instances of Admin() and User()
user_1 = Admin('gandalf', 'the grey', 
              'the undying lands of valinor', 
              'wizardry')

user_2 = User('kristin', 'lastname', 'arkansas', 'coding')
user_3 = User('rami', 'malek', 'california', 'hacking')
user_4 = Admin('dobby', 'bunbun', 'texas', 'food')

#calling the method that prints priveleges
user_1.privelege_list()
user_4.privelege_list()