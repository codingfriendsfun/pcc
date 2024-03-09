"""Building user profiles."""

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
        