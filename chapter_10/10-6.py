x = input('enter the 1st num: ')
y = input('enter the 2nd num: ')

try:
    sum = int(x) + int(y)
except ValueError:
    print("You didn't put two integers please try again")
else:
    print(f"the total of {x} + {y} is {sum}")
