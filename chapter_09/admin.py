from user import User

class Privileges:
    """Represents the different privileges an account"""

    def __init__(self, privileges=[]):
        """Initialize attributes"""
        self.privileges = privileges

    def show_privileges(self):
        """Show the privileges an admin has."""
        print("A user of your rank can do the following:")
        for privilege in self.privileges:
            print(f"{privilege}")

class Admin(User):
    """Represent specific traits of the admin type of user."""

    def __init__(self, first_name, last_name):
        """
        Initialize attributes of parent class (user).
        Initialize attributes of admin.
        """
        super().__init__(first_name, last_name)
        self.privileges = Privileges()