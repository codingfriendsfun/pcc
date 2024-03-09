"""Special priveleges for admins."""

from user import User

class Priveleges(User):
    """Administrator priveleges."""

    def __init__(self, priveleges=['add posts', 'delete posts', 
                             'edit posts', 'ban users']):
                                                        
        """Initializing Priveleges attributes."""
        self.priveleges = priveleges


    def privelege_list(self):
        """Describe the priveleges admins have."""

        for privelege in self.priveleges:
            print(privelege.title())

class Admin(User):
    """Administrator attributes."""

    def __init__(self, first_name, last_name, location, hobby):
        """Initialize parent and Admin attributes."""

        super().__init__(first_name, last_name, location, hobby)
        self.priveleges = Priveleges()
