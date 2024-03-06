class User:
    """Creating a user profile."""
    def __init__(self, first_name, last_name, location, hobby):
        """Initializing attributes of a users information."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.hobby = hobby
        self.login_attempts = 0


    def describe_user(self):
        """Describes a user"""
        print(f"\n{self.first_name.title()} {self.last_name.title()} was born in "
              f"{self.location.title()} and enjoys {self.hobby}.")
        
    def greet_user(self):
        """Greets a user."""
        print(f"Good morning, {self.first_name.title()}"
              f" {self.last_name.title()}!")
    
    def read_login_attempts(self):
        """Reads login attempts by a user."""
        print(f"You have failed to login {self.login_attempts} times.")

    def increment_login_attempts(self):
        """Updates login attempts by one."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Sets the number of login attempts to zero."""
        self.login_attempts = 0

#creating instances of User()
user_1 = User('gandalf', 'the grey', 'the undying lands of valinor', 'wizardry')
user_2 = User('kristin', 'lastname', 'arkansas', 'coding')
user_3 = User('rami', 'malek', 'california', 'hacking')
user_4 = User('dobby', 'bunbun', 'texas', 'food')

#Changing and reading the login attempts by a user
user_1.read_login_attempts()
user_1.increment_login_attempts()
user_1.read_login_attempts()
user_1.increment_login_attempts()
user_1.read_login_attempts()
user_1.increment_login_attempts()
user_1.read_login_attempts()
user_1.increment_login_attempts() 
user_1.reset_login_attempts()
user_1.read_login_attempts()