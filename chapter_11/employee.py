
class Employee:


    def __init__(self, first_name, last_name, salary):
        """Initialize the attributes for Employee"""

        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


    def give_raise(self, salary_raise=5000):
        """Give an employee a raise."""
        
        return self.salary + salary_raise
