from random import randint

# Representing a 6 sided die with a method to roll the die
class Dice:
    """Modeling a die."""

    def __init__(self, sides=6):
        """Initializing dice attributes."""

        self.sides = sides


    def roll_dice(self):
        """Roll a 6 sided die."""

        number_of_rolls = 10
        while number_of_rolls:
            roll_number = randint(1, self.sides)
            print(f"You rolled a {roll_number}!")
            number_of_rolls -= 1

# Instances of Dice() with varying numbers of sides.
die_1 = Dice()
die_2 = Dice(10)
die_3 = Dice(20)

# List of all dice to be rolled
dice = [die_1, die_2, die_3]

# Loop through our list of dice calling the roll_dice() method.
for die in dice:
    die.roll_dice()
