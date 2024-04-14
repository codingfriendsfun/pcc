# Create a class for an employee that takes first/last name, salary, and raise

class Employee:
    """A representation of an employee"""

    def __init__(self, first_name, last_name, salary):
        """Initialize employee attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amt = 5000):
        """Give the employee a raise"""
        self.salary += raise_amt