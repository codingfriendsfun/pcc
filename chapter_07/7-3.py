number = input("Gimme a number: ")
number = int(number)

if number % 10 == 0:
    print(f"\n{number} is divisible by ten! Good job!")
else:
    print(f"\nWhy did you pick {number} when it isn't divisible by ten?")