class User:
    def __init__(self, first, last, email, phone, soooup = True):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.phone = phone
        self.soooup = soooup
        self.login_attempts = 0
    
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
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_logins(self):
        self.login_attempts = 0
    def print_login_attempts(self):
        print(f"Attempts at login: {self.login_attempts}")
    
    


ravi = User('Ravi', 'Ghotra', 'therawv@gmail.com', '5622902248')
ravi.describe_user()
ravi.soup()
ravi.greet_user()
ravi.increment_login_attempts()
ravi.increment_login_attempts()
ravi.increment_login_attempts()
ravi.print_login_attempts()
ravi.reset_logins()
ravi.print_login_attempts()



bobby = User('George', 'Ghotra', 'thebobv@gmail.com', '5622902248')
bobby.describe_user()
bobby.soup()
bobby.greet_user()