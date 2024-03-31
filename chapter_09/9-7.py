class User:
    def __init__(self, first, last, email, phone):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.phone = phone
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.email}, {self.phone}")
    
    def greet_user(self):
        print(f"Hello {self.first_name}")

class Admin(User):
    def __init__(self, first, last, email, phone, privlidges =[]):
        super().__init__(first, last, email, phone)
        self.myPrivlidge = privlidges

    def show_privlidge(self):
        for privli in self.myPrivlidge:
            print(f"{self.first_name} has the ability to: {privli}")

adminPower = ['Ban Users', 'Refund Orders', 'Make Schedules', 'Talk Back']
Ravi = Admin('Ravi', 'Ghotra', 'therawv@gmail.com','5622902248', adminPower)

Ravi.show_privlidge()