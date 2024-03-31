from User import User

class Admin(User):
    def __init__(self, first, last, email, phone, privlidges =[]):
        super().__init__(first, last, email, phone)
        self.userPrivlidge = Privlidges(privlidges)

class Privlidges:
    def __init__(self, privlidges =[]):
        self.my_privlidge = privlidges

    def show_privlidge(self):
        for privli in self.my_privlidge:
            print(f"Has the ability to: {privli}")