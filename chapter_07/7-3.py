# a script to determine if a number is a multiple of 10.

num = int(input("Provide an integer: "))

if num % 10: # remainder > 0
    print(f"{num} is not a multiple of 10.")
else: # remainder = 0
    print(f"{num} is a multiple of 10.")