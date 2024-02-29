# Admin classes
# for exercise 9-12

from User import User

class Privileges:
    """Class that stores info about user privileges"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_priveleges(self):
        print("User has the following priveleges: ")
        for privelege in self.privileges:
            print(f"    {privelege}")


class Admin(User):
    """User class with elevated priveleges"""

    def __init__(self, f_name, l_name, privileges=[]):
        """Initialize Admin"""
        super().__init__(f_name, l_name)
        self.privileges = Privileges(privileges)

