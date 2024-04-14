# 11-3. Employee

class Employee:
    """A class to represent an employee"""

    def __init__(self, fname, lname, salary):
        """Initialize Employee"""

        self.fname = fname
        self.lname = lname
        self.salary = int(salary)

    def give_raise(self, praise=5000):
        """Give a raise, default 5000"""
        self.salary += praise
