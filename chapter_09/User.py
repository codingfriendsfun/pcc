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