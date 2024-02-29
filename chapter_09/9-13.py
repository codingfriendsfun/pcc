# 9-13. Dice
from random import randint


class Die:
    """Class for modeling dice with a given number of sides"""

    def __init__(self, no_sides=6):
        """Initialize Die with given number of sides"""
        self.sides = no_sides

    def roll_die(self):
        """Simulate rolling a die"""
        print(randint(1, self.sides))


ten = Die(10)
twenty = Die(20)

for i in range(10):
    print(f"\n*** Roll {i+1} ***")
    print("Ten sided die rolled: ")
    ten.roll_die()
    print("Twenty sided die rolled: ")
    twenty.roll_die()
