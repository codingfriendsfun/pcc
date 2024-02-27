from random import choice

# List ten numbers and five letters
random_things = [4, 8, 15, 16, 23, 42, 77, 82, 19, 28, 'l', 'a', 'd', 'f',]


# Pick the numbers for my ticket.
my_ticket = [77, 4, 'a', 19]

# Set attempts to 0
attempts = 0
max_attempts = 1_000_000

while True:
    # Keep pulling numbers until my_ticket wins.
    if attempts == max_attempts:
        break
    selection = f"{choice(random_things)} {choice(random_things)} "
    selection += f"{choice(random_things)} {choice(random_things)}"
    print(selection)
    if selection == my_ticket:
        break
    # Count the number of tries it takes to match my ticket
    else:
        attempts += 1

if attempts == 1_000_000:
    print(f"{my_ticket} wasn't drawn even after 1,000,000 attempts.")
else:
    print(f"It took {attempts} attempts to match my lottery ticket of {my_ticket}")