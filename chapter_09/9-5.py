# 9-5. Login Attempts
# based off of 9-3. Users

class User:
    """ Class model of a User."""

    def __init__(self, f_name, l_name):
        """Initialize user"""
        self.first_name = f_name
        self.last_name = l_name
        self.login_attempts = 0
        self.attributes = {}

    def describe_user(self):
        """Print attributes"""
        print(f"{self.first_name} {self.last_name} has the following attributes: ")
        for attribute in self.attributes:
            print(f"    {attribute}: {self.attributes[attribute]}")

    def greet_user(self):
        """Greet user by name"""
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

myUser = User("Alexa", "Adams")

for i in range(5):
    myUser.increment_login_attempts()

print(myUser.login_attempts)

myUser.reset_login_attempts()
print(myUser.login_attempts)
