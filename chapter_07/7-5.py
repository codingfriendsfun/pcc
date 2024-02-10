prompt = "\nHow old is the person you are buying a ticket for? "
prompt += "\nIf you are done purchasing tickets, please enter 'done'. "

while True:
    age = input(prompt)

    if age == 'done':
        print("Thank you for purchasing movie tickets!")
        break
    age = int(age)
    if age <= 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")