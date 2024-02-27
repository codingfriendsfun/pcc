# 9-3. Users

class User:
    """ Class model of a User."""

    def __init__(self, f_name, l_name):
        """Initialize user"""
        self.first_name = f_name
        self.last_name = l_name
        self.attributes = {}

    def describe_user(self):
        """Print attributes"""
        print(f"{self.first_name} {self.last_name} has the following attributes: ")
        for attribute in self.attributes:
            print(f"    {attribute}: {self.attributes[attribute]}")

    def greet_user(self):
        """Greet user by name"""
        print(f"Hello, {self.first_name} {self.last_name}!")

alexa = User("Alexa", "Adams")
alexa.attributes = {"birthday": "1/7/93", "Dog's name": "Prise"}
alexa.greet_user()
alexa.describe_user()

noelle = User("Noelle", "Riley")
noelle.attributes = {"birthday": "7/24/92", "Dog's name": "Antares", "Cat's name": "Rey"}
noelle.greet_user()
noelle.describe_user()