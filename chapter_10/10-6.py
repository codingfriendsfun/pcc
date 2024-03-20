print("Too lazy to add things yourself? Don't worry, I gotchu.")

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
try:
    sum = int(first_number) + int(second_number)
except ValueError:
    print("One of those is not a number :)")
    # The smile makes it a friendly error message
else:
    print(sum)
