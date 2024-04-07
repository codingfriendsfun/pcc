while True:

    x = input('enter the 1st num, type "q" at any time to quit: ')
    if x == 'q':
        break
    y = input('enter the 2nd num: ')
    if y =='q':
        break

    try:
        sum = int(x) + int(y)
    except ValueError:
        print("You didn't put two integers please try again")
    else:
        print(f"the total of {x} + {y} is {sum}")