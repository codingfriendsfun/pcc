class User:
    """A basic class containing user profile informaiton."""

    def __init__(self, first_name, last_name):
        """Initialize first and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the information collected about the user."""
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
    
    def greet_user(self):
        """Print a customized greeting to the user."""
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello, {full_name}.")

    def increment_login_attempts(self):
        """Increase the value of login attempts by 1"""
        self.login_attempts =+ 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0

# Create instance
user_0 = User('obi wan', 'kenobi')

# Ensure value for login attempts is 0
print(f"Current login attempts: {user_0.login_attempts}")

# Verify that increment_login_attempts() method works
user_0.increment_login_attempts()
print(f"Current login attempts: {user_0.login_attempts}")

# Verify that reset_login_attempts() method works
user_0.reset_login_attempts()
print(f"Current login attempts: {user_0.login_attempts}")