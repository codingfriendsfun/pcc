class User:
    def __init__(self, first, last, email, phone, soooup = True):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.phone = phone
        self.soooup = soooup
    
    def soup(self):
        if self.first_name == 'George':
            print("NO SOUP FOR YOU!!")
        elif self.soooup == True:
            print("soup for you")
        else:
            print("NO SOUP FOR YOU!!")
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.email}, {self.phone}")
    
    def greet_user(self):
        print(f"Hello {self.first_name}")


ravi = User('Ravi', 'Ghotra', 'therawv@gmail.com', '5622902248', soooup=False)
ravi.describe_user()
ravi.soup()
ravi.greet_user()
