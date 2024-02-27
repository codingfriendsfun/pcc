class User:
    """A basic class containing user profile informaiton."""

    def __init__(self, first_name, last_name):
        """Initialize first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Print a summary of the information collected about the user."""
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
    
    def greet_user(self):
        """Print a customized greeting to the user."""
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello, {full_name}.")