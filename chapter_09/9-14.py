from random import choice

# List ten numbers and five letters
random_things = [4, 8, 15, 16, 23, 42, 77, 82, 19, 28, 'l', 'a', 'd', 'f',]

# Randomly select 4 letters or numbers to be fake lotto numbers.
selection = f"{choice(random_things)} {choice(random_things)} "
selection += f"{choice(random_things)} {choice(random_things)}"

# This would probably make more sense if I'd played the lottery more than once.
print(f"If your ticket matches any of the following, you have one our grand prize!")
print(selection)