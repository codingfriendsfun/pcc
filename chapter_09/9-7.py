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


class Admin(User):
    """Represent specific traits of the admin type of user."""

    def __init__(self, first_name, last_name):
        """
        Initialize attributes of parent class (user).
        Initialize attributes of admin.
        """
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        """Show the privileges an admin has."""
        print("A user of your rank can do the following:")
        for privilege in self.privileges:
            print(f"{privilege}")

admin_0 = Admin('yoda', 'adoy')

admin_0.privileges = [
    'can grant rank of master',
    'can grant seat on council',
    'can declare sith lord'
]

admin_0.describe_user()
admin_0.show_privileges()