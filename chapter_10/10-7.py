print("Too lazy to add things yourself? Don't worry, I gotchu.")
print("(Enter 'q' to quit.)")

while True:
    first_number = input("Enter the first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter the second number: ")
    if second_number == 'q':
        break
    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        print("That is neither the number nor the way to quit. Try again :)")
        # The smile makes it a friendly error message
    else:
        print(sum)