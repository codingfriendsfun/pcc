class Employee:
    def __init__(self, firstN, lastN, msalary):
        self.first = firstN
        self.last =  lastN
        self.salary = msalary
    def give_raise(self, increase=5000):
        self.salary += increase

##testing code to see if it works. I should probably set this to that one Alexa used     
##Ravi = Employee('Ravi', 'Ghotra', 38000)

##print(f'{Ravi.first} makes {Ravi.salary}')
##Ravi.give_raise()
##print(f'{Ravi.first} makes {Ravi.salary}')

    
