from random import randint

# Create the die class, with the ability to roll the die
class Die():
    """Simulate a die (the rolling kind)"""

    def __init__(self, sides=6):
        """Initialize attributes to describe the die."""
        self.sides = sides

    def roll_die(self):
        """Simulate rolling a die."""
        print(randint(1, self.sides))

    def roll_ten(self):
        """Simulate rolling the die ten times."""
        roll_times = 0
        while roll_times < 10:
            self.roll_die()
            roll_times += 1

# Create a six-sided die and roll it 10 times
standard_die = Die()
print(f"Rolling a {standard_die.sides}-sided die ten times:")
standard_die.roll_ten()

# Make a d10 and roll it 10 times
d10 = Die()
d10.sides = 10
print(f"Rolling a {d10.sides}-sided die ten times:")
d10.roll_ten()

# Make a d20 and roll it 10 times
d20 = Die()
d20.sides = 20
print(f"Rolling a {d20.sides}-sided die ten times:")
d20.roll_ten()