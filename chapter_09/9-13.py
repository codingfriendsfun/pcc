from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1,self.sides)

six = Die()
ten = Die(10)
twenty = Die(20)

for _ in range(10):
    print(six.roll_die())
for _ in range(10):
    print(ten.roll_die())
for _ in range(10):
    print(twenty.roll_die())
