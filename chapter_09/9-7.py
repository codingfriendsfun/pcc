# 9-7. Admin

class User:
    """ Class model of a User."""

    def __init__(self, f_name, l_name):
        """Initialize user"""
        self.first_name = f_name
        self.last_name = l_name
        self.attributes = {}
        self.privileges = []

    def describe_user(self):
        """Print attributes"""
        print(f"{self.first_name} {self.last_name} has the following attributes: ")
        for attribute in self.attributes:
            print(f"    {attribute}: {self.attributes[attribute]}")

    def greet_user(self):
        """Greet user by name"""
        print(f"Hello, {self.first_name} {self.last_name}!")

class Admin(User):
    """User class with elevated priveleges"""

    def __init__(self, f_name, l_name, privileges=[]):
        """Initialize Admin"""
        super().__init__(f_name, l_name)
        self.privileges = privileges

    def show_priveleges(self):
        print(f"{self.first_name} {self.last_name} " +
            "has the following priveleges: ")
        for privelege in self.privileges:
            print(f"    {privelege}")


myAdmin = Admin("Ruthe", "Ginsburg", ["Notorious", "Can write laws", 
                                        "Takes no shit"])

myAdmin.show_priveleges()



