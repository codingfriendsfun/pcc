# User class
# for exercise 9-12

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